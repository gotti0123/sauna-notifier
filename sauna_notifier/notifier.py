from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from sauna_notifier.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID, LINE_GROUP_ID

def send_notification(message_text):
    """
    指定されたメッセージをLINE Messaging APIで送信する
    """
    # 宛先の決定：グループIDがあればグループ優先、なければユーザーID
    target_id = LINE_GROUP_ID if LINE_GROUP_ID else LINE_USER_ID

    if not LINE_CHANNEL_ACCESS_TOKEN or not target_id:
        print("Error: Notification configuration missing (Token or Target ID).")
        return False

    line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

    try:
        line_bot_api.push_message(
            target_id,
            TextSendMessage(text=message_text)
        )
        print("Notification sent successfully!")
        return True
    except LineBotApiError as e:
        print(f"Failed to send notification: {e}")
        return False
