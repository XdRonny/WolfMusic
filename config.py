from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AQChKll4pT0GVgeBvJup9bez3tsdsj7pgjIfdzS7oQBnS5fmFPze-sE8rBqohlwjGVBwDfsQfXXEfDAaipUOjemBKv6ZTgHd7b_-dQAYzuMJKHhX4plxEfQKxDAHiu7RAwoDh--vqmJCDfzDTH0HA9uuv3179I3o-P1E5-jh_Bo77zo3G7dUweSy52zUyJgAO8cp1leImoMx79XDiypT0H4ASH6ygvN3f2FCFkPi5tPo8ZBBK4B9z0UCdqyhZXfseCHNrgd8WBMJlPy7jdEbpFM0vujzF_ZCnO_LJowJmoJE59dBN4tN1oYY0zR1DT0YBISdLDUeTuEc7X-2LtplwJiJeSrSXAA")
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
if str(getenv("SUPPORT_CHANNEL", "international_chatting_hub")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "Shubhanshutya")
if str(getenv("SUPPORT_GROUP", "BrayDenXD")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "RaichuOfficial"))
