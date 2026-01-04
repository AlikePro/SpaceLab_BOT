from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
import asyncio

BOT_TOKEN = "8545772004:AAFSxxHOJ8saXcuZHaehrZCvD4XsWPQ_j68"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="🚀 Открыть Mini App",
                    web_app=WebAppInfo(
                        url="https://alikepro.github.io/SpaceLab_BOT/"
                    )
                )
            ]
        ]
    )

    await message.answer(
        "Нажми кнопку ниже:",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
