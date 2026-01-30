import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")
LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")

if not LINE_CHANNEL_ACCESS_TOKEN:
    print("Warning: LINE_CHANNEL_ACCESS_TOKEN is not set.")

if not LINE_USER_ID:
    print("Warning: LINE_USER_ID is not set.")
