import os

class Config(object):
    BOT_TOKEN = os.environ.get("8334590640:AAFqlvUVCsdiK153ZzfOULYLzmnp3zbeMB0")
    API_ID = int(os.environ.get("28227907"))
    API_HASH = os.environ.get("bc3acb5bd0282fe4fd076cec1f24df62")
    AUTH_USER = os.environ.get('AUTH_USERS', '919335654').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
