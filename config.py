from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "23999542"))
API_HASH = getenv("API_HASH", "f7026a559d4e1924604c31927435aa05")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "5000000"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", "!").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "951454060").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001836099748"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹ҡʏɴλɴ ꝛσʙσᴛ˼༗")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = "https://github.com/Onlymeriz/Mus"
UPSTREAM_BRANCH = "main"

SUPPORT_CHANNEL = "https://t.me/kontenfilm"
SUPPORT_GROUP = "https://t.me/kynansupport"

THUMBNAIL = getenv("THUMB_LINK") 

botusername = str(getenv("BOT_USERNAME", "KynanUserbot"))

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))

if str(getenv("LIMIT")).strip().upper() == "TRUE":
    PL_LIMIT = "FALSE"
else:
    PL_LIMIT = "TRUE"

if str(getenv("PM_PERMIT")).strip().upper() == "TRUE":
    PM_PERMIT = "FALSE"
else:
    PM_PERMIT = "TRUE"
