import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28362850")) #optional
API_HASH = getenv("API_HASH", "34f9cb93364db16fc45d003e4c81d97a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "6896043885"))
MONGO_URL = getenv("MONGO_URL", ""mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "7793852739:AAFU9wgE9iGSYVJhxpMz2RPhGiYLwhurHtg")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GDNBharat/Xerox-userbot-")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGwyGIAFMCZ6X7ED31hvJDTZN9n49TvY1_3Pq2FcXv2viVWUIC0YqqY-bQFfvK7yzrPJ8aoiHLZEnKEPqlwihGVkKCML6wxrckHHz4lSZM1k7fp4xMXFo6zD4fO9Lal5YIPUfm3ut0346AYku7ck4jfMvmn_nCU9KyQD4DB0ETfhYdM4gQPhvHFq1YoW_o_2OuBOfK7r6MLqUCrr7vQKzioxv69OuZ0zX5oIEvKrF9ue2QX0dDwia6B_jBCgdZnz2tUdpfTfw3L0ey-3TBLYTurs7Ubp_YBrapyeWBFuPz0gwJNlaoEIFz1df2Ln0-G57Vr-BmP_Q0qMvt-3iScD6259XL2PgAAAAHETnMdAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
