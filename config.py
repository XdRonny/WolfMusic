from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "BQBEWk1Mek1Xynjpo1mBg0rZXD2uD5xbcPvlDv0-yKzwMLNoMH8ol4Y5LDrj8kPqg13nymyUORddEo92VfxTcM1ZqkDQECrGnjhR0fWve6DHXl565U-gneg3Yn-lWwMlpSMSDcTQz7wnZHquzsTm-5TC766yYNlvL6vQ6jrnoEr2mYr0wjMaE_mOEmZiJfhv4xLSSUsSMIKbamLfACqc0VW-p1hget-l9Opbo8pPlYAgTm7_ED3ldd6Wa2UeWlwo_1beja5vSGf8CPm-am4PUIkxwQ-d7iVKYD90g4fpZZilLavyqtf4rZSp3T8UmjEpR6I2bzbLpBKa0TprwjL-MTrDeJyNsQA")
BOT_TOKEN = getenv("BOT_TOKEN" , "1607821276:AAGuamsqQ2pe9yHz1fn9kWuI268o_vO9Yuc")
API_ID = int(getenv("API_ID", "16043274"))
API_HASH = getenv("API_HASH", "314d816924009b7eb70f0d372520b12b")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "15"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI" , "mongodb+srv://Aman:Aman@cluster0.x5zhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1920507972").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1920507972").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001216286774"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Yuriko")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/0c2151459a4b37c51cc9c.jpg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "Shubhanshutya")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "RaichuOfficial")
