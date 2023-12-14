import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("يتم بدء التنصيب للبوت ..")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("المتطلبات ( APP_ID , APP_HASH ) خطأ")
    except AccessTokenInvalid:
        raise Exception("المتطلبات ( BOT_TOKEN ) خطأ")
    uname = app.get_me().username
    print(f"@{uname} تم بدأ البوت")
    idle()
    app.stop()
    print("- - - - - ")
