import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# ضع التوكن الخاص بك هنا
API_TOKEN = '8418407948:AAH-PVZvJohPcey3JY1f075fQ9XzsrKgwhA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# دالة إنشاء الأزرار
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="الزر الأول 1️⃣", callback_data="btn1")],
        [InlineKeyboardButton(text="الزر الثاني 2️⃣", callback_data="btn2")]
    ])
    return keyboard

# أمر البدء
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("🚀 البوت يعمل الآن على Railway بنجاح!\nاختر زراً من الأسفل:", reply_markup=get_main_keyboard())

# معالجة ضغطات الأزرار
@dp.callback_query(F.data == "btn1")
async def process_btn1(callback: types.CallbackQuery):
    await callback.message.answer("لقد اخترت الزر الأول بنجاح! ✅")
    await callback.answer()

@dp.callback_query(F.data == "btn2")
async def process_btn2(callback: types.CallbackQuery):
    await callback.message.answer("لقد اخترت الزر الثاني بنجاح! ✅")
    await callback.answer()

async def main():
    print("البوت بدأ في العمل...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
