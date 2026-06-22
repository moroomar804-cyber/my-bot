import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# التوكن الخاص بك
API_TOKEN = '8418407948:AAH-PVZvJohPcey3JY1f075fQ9XzsrKgwhA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("🚀 البوت يعمل الآن على Render بنجاح!")

async def main():
    print("البوت بدأ في العمل...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
