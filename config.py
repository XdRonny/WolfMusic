from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "")
BOT_TOKEN = getenv("BOT_TOKEN" , "1607821276:AAGuamsqQ2pe9yHz1fn9kWuI268o_vO9Yuc")
API_ID = int(getenv("API_ID", "15816197"))
API_HASH = getenv("API_HASH", "42a79ffac6e037eb1a2671298c34d5de")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "15"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI" , "mongodb+srv://Aman:Aman@cluster0.kigqe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1668305941").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1668305941").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001654637381"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Innexiabot")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/732363bb2cafd8281aadd.jpg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "Shubhanshutya")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "RaichuOfficial")
