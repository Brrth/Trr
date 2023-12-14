import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    print("تم توقف التنصيب | API_ID ماموجود")
    raise SystemExit
if not API_HASH:
    print("تم توقف التنصيب | API_HASH مموجود")
    raise SystemExit
if not BOT_TOKEN:
    print("تم توقف التنصيب | توكن البوت مموجود")
    raise SystemExit
if not DATABASE_URL:
    print("تم توقف التنصيب | رابط قاعده البيانات مموجود")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("تم توقف التنصيب | API_ID غير صحيح")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
