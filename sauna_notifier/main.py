from sauna_notifier.notifier import send_notification

def main():
    print("=== Sauna Notifier Started ===")
    
    # メッセージ内容は後ほどカスタマイズ可能です
    message = (
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
    
    success = send_notification(message)
    
    if success:
        print("=== Completed Successfully ===")
    else:
        print("=== Completed with Errors ===")

if __name__ == "__main__":
    main()
