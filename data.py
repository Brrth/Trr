from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("بـدء الاسـتخراج ∆", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("B𝖾𝗋𝗈T𝗁𝗈𝗇 C𝗁𝖺𝗇𝗇𝖾𝗅 𓍰", url="https://t.me/Sero_Bots"),
        ],
    ]

    START = """
- مرحبـاً  بك .

- فـي بـوت استخـراج كـود تيرمكـس
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه 🏂
- للحصـول على كـود تيرمكـس بـدون بـانـد🎗
» قم بالضغط علي بدء الاستخراج لرؤيه اوامر الاستخراج ⭐
» لـ الحصـول على كـود بيروثـون اضغـط الزر (ᴛᴇʟᴇᴛʜᴏɴ)
    """
