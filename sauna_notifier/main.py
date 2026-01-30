import google.generativeai as genai
from sauna_notifier.notifier import send_notification
from sauna_notifier.config import GEMINI_API_KEY
import datetime
def get_ladies_day_info():
    """
    Geminiの検索機能を使ってレディースデー情報を取得する
    """
    if not GEMINI_API_KEY:
        print("Gemini API Key is not set. Skipping search.")
        return ""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        # 検索機能ツール設定
        tools = [
            {"google_search": {}}
        ]
        
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            tools=tools
        )
        today = datetime.date.today()
        # 除外施設の定義
        excluded_facilities = [
            "なにわ健康ランド 湯～トピア",
            "サウナクッカ (Sauna Kukka)",
            "スパワールド",
            "入船温泉",
            "大阪サウナ DESSE",
            "さらさのゆ",
            "大東洋",
            "水春 松井山手"
        ]
        # プロンプト作成
        prompt = f"""
        今日は{today}です。今週（今日から次の月曜日まで）開催される、
        以下のエリアの「男性専用サウナ施設のレディースデー」情報を検索してください。
        
        対象エリア: 愛知（名古屋含む）、岐阜、三重、大阪、京都、兵庫、奈良、滋賀、和歌山
        【除外施設】（以下の施設は検索結果に含めないでください）
        {", ".join(excluded_facilities)}
        見つかった場合は以下の形式で出力してください：
        ・日付: [開催日]
        ・施設名: [施設名] ([都道府県])
        ・詳細URL: [URL]
        見つからなかった場合は「今週の新しいレディースデー情報は見つかりませんでした」とのみ出力してください。
        余計な前置きや挨拶は不要です。
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error fetching ladies day info: {e}")
        return f"（情報の取得中にエラーが発生しました: {str(e)}）"
def main():
    print("=== Sauna Notifier Started ===")
    
    # 1. 固定のメッセージ
    base_message = (
        "サウナの時間です！\n整いに行きましょう♨️\n\n"
        "▼チェックしておきたい情報\n"
        "1. なにわ健康ランド\nhttps://naniwa-utopia.com/\n\n"
        "2. sauna kukka\nhttps://sauna-kukka.jp/news/\n\n"
        "3. SPAWORLD\nhttps://www.spaworld.co.jp/event/aufguss-calender/\n\n"
        "4. 入船温泉\nhttps://irihune.co.jp/\n\n"
        "5. DESSE\nhttps://www.instagram.com/desse.osaka/\n\n"
        "6. さらさのゆ\nhttps://www.sarasanoyu.com/\n\n"
        "7. 大東洋(Ladies)\nhttps://www.daitoyo.co.jp/spa/ladies/recommended/\n\n"
        "8. 水春 松井山手\nhttps://suisyun.jp/matsuiyamate/category/events/ofuro-event/"
    )
    
    # 2. Geminiによる追加情報
    print("Fetching ladies day info from Gemini...")
    ladies_day_info = get_ladies_day_info()
    
    if ladies_day_info:
        final_message = f"{base_message}\n\n🌸 【今週のレディースデー注目情報】\n{ladies_day_info}"
    else:
        final_message = base_message
    
    # 3. 送信
    success = send_notification(final_message)
    
    if success:
        print("=== Completed Successfully ===")
    else:
        print("=== Completed with Errors ===")
if __name__ == "__main__":
    main()
