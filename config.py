from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AQAUwbEkwzBfJoPydOq8xBvnnHNkOIdDQwz6u7CT90J5sXVdHAv1mxq24LZ7R_vB3f0-C_TU4XfhsZ_w7Y1OWxTistEbKAoQJDFPjlRBuEJUNSEXBeuBimA3wCnzd53_IiqoLLy5oav6RhwDtbD-WH46RKlQOBnNGK5h278zjeObAjDSOA1argyaaJ9xQeJ-f51VdeBegBCqXLX4mpHy-xkB9RXJAXWxWj7NnMv_x3yo87PJQtt9NAcK5tH8M1CGbkrrp7wSGx1Dk6sej6bOX8HEzFwlHBNoPA8VAEUTf8SmLTrlGRVFnXYgdRhZyzLuD68xA8UVDIEfc2X1zElDAP92AAAAAS4fyOgA")
BOT_TOKEN = getenv("BOT_TOKEN" , "2100234484:AAEb0S-CWC4h2Xr1rOUft9PvbqPKszSnCxQ")
API_ID = int(getenv("API_ID", "14486017"))
API_HASH = getenv("API_HASH", "e303f55d6a548e29ca7e91cadbd80182")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI" , "mongodb+srv://xd:xd@cluster0.wb93b.mongodb.net/xd?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1920507972").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5032100535").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001781944400"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Florenza_Musix")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/732363bb2cafd8281aadd.jpg")
if str(getenv("SUPPORT_CHANNEL", "STARZ_BOTS")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "STARZ_BOTS"))
if str(getenv("SUPPORT_GROUP", "Starz_Support")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "Starz_Support"))
