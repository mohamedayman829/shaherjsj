from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/8fa109bec9bb4dcf64e74.mp4")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2514530559cc173845e3f.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SORS0C")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/UIU_II")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6300938349").split()))


FAILED = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
