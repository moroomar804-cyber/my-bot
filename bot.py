import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكين الخاص بك
API_TOKEN = '8418407948:AAH-PVZvJohPcey3JY1f075fQ9XzsrKgwhA'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- قاعدة البيانات ---
def init_db():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (user_id INTEGER PRIMARY KEY, balance REAL, points INTEGER)''')
    conn.commit()
    conn.close()

def get_user_data(user_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (user_id, 0.0, 0))
        conn.commit()
        user = (user_id, 0.0, 0)
    conn.close()
    return user

# --- الأزرار والقوائم ---
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛍 شراء حساب تليجرام", callback_data="buy_acc")],
        [InlineKeyboardButton(text="💳 طرق الدفع", callback_data="payment")],
        [InlineKeyboardButton(text="👤 ملفي الشخصي", callback_data="profile")]
    ])

# --- معالجة الأوامر ---
@dp.message(Command("start"))
async def start(message: types.Message):
    user = get_user_data(message.from_user.id)
    text = (
        "👑 **أهلاً بك في متجر خدمات تليجرام الرسمي** 👑\n\n"
        f"🆔 معرفك: `{message.from_user.id}`\n"
        f"💰 رصيدك: {user[1]}$\n"
        f"🌟 نجومك: {user[2]}\n"
        "____________________\n"
        "اختر من القائمة أدناه:"
    )
    await message.answer(text, reply_markup=main_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    await start(callback.message)
    await callback.answer()

@dp.callback_query(F.data == "buy_acc")
async def buy_account(callback: types.CallbackQuery):
    text = (
        "🛒 **قائمة الأسعار (بالنجوم):**\n\n"
        "🇺🇸 أمريكا: 0.3$ | 30 نجمة\n"
        "🇨🇦 كندا: 0.35$ | 35 نجمة\n"
        "🇳🇬 نيجيريا: 0.25$ | 25 نجمة\n"
        "🇸🇾 سوريا: 0.5$ | 50 نجمة\n"
        "🇲🇲 ماينمار: 0.3$ | 30 نجمة\n"
        "🇹🇯 طاجكستان (واتساب): 0.25$ | 25 نجمة\n"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ رجوع", callback_data="back_main")]
    ])
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")

@dp.callback_query(F.data == "payment")
async def show_payment(callback: types.CallbackQuery):
    text = (
        "💳 **طرق الدفع المتاحة للشحن:**\n\n"
        "💎 **سي واليت (C-Wallet):**\n"
        "ID: `91552675` (Flashnumber)\n\n"
        "💸 **فوست باي (FaucetPay):**\n"
        "ID: `493857145`\n\n"
        "🏦 **باي بت (Bybit):**\n"
        "• **USDT BEP20:**\n`0xcc17cd115159942cbe18cc7d6ec2285d063cff23`\n\n"
        "• **USDT Polygon:**\n`0xcc17cd115159942cbe18cc7d6ec2285d063cff23`"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ رجوع", callback_data="back_main")]
    ])
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")

# --- تشغيل البوت ---
async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
