from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AQCLqEWij6zFxp99grjrtASN8wne39L_mhDE3OFXU9MLoiYn5G2UEZ0vi8Pp87BzIw4rlonEn_QlDP73AFLg3i8arm36Lpv56jklOr9NdkYfKzCBsebBPVqL9SrVcl1bel5Vh0vqPslTIElp8dyi-xq7cUbzP73BbarpNuMf_Qs1mSPplPMs42hnHNJLmIsdgI-lfUriKoALPP9SWN-dYQdCmh0rUAiBP6ItLhVtGMstXscoRFjOkUpaCoQ6SMyLkdgMxlseyPEyv4XLowuRSY1TIIZLI7O8I_HOpRWiskl7n3dat0ZYpoldQK_Jd_j-6TWbw3CQVovaMK7_dIFKojYmAAAAAS4fyOgA")
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
