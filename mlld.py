from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
import asyncio

TOKEN = "8706406639:AAGfpy5X0X2L_MenJevBiMgssEf09_06HNg"

bot = Bot(
    TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()

WELCOME_TEXT = """
<b>╔═══ ⛩️ ДОБРО ПОЖАЛОВАТЬ ⛩️ ═══╗</b>

🌸 <b>{mention}</b>

✨ <b>Мы рады приветствовать тебя в <u>{chat}</u>!</b>

🍃 <b>Устраивайся поудобнее и чувствуй себя как дома.</b>

📖 <b>Обязательно ознакомься с правилами сообщества.</b>

💬 <b>Общайся, знакомься и наслаждайся атмосферой!</b>

🎐 <b>Желаем приятного общения и отличного настроения!</b>

<code>━━━━━━━━━━━━━━━━━━━━</code>

🌺 <b>ようこそ • ДОБРО ПОЖАЛОВАТЬ • WELCOME</b> 🌺

<b>╚════════════════════╝</b>
"""


@dp.message(F.new_chat_members)
async def welcome_new_users(message: Message):

    for user in message.new_chat_members:

        text = (
            WELCOME_TEXT
            .replace(
                "{mention}",
                f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
            )
            .replace(
                "{chat}",
                message.chat.title
            )
        )

        await message.answer(text)


async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())