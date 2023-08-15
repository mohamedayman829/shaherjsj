from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/Shaher-08-15")
START_IMG = getenv("START_IMG", "https://graph.org/Photo-07-29-20")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/hsbjndk")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SHaHeRrrrrrr")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5134002906").split()))


FAILED = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
