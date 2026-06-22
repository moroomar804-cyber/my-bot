hereimport os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web

# التوكن الخاص بك
TOKEN = '8808428811:AAFiLKSL6G-JbL6E1prOyb1L5A0hIzTIiqk'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# القائمة الخاصة بالدفع
@dp.message(Command("pay"))
async def show_payment_methods(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 ادفع باستخدام نجوم تليجرام (Stars)", callback_data="pay_stars")]
    ])
    await message.answer("اضغط على الزر أدناه لإتمام عملية الدفع:", reply_markup=keyboard)

# الرد عند الضغط على الزر
@dp.callback_query(F.data == "pay_stars")
async def pay_stars_info(callback: types.CallbackQuery):
    await callback.message.answer(
        "✨ **الدفع عبر نجوم تليجرام (Stars):**\n\n"
        "يرجى إرسال لقطة شاشة (Screenshot) لعملية التحويل هنا لنقوم بتفعيل خدمتك فوراً!"
    )
    await callback.answer()

# خادم وهمي لمنع الـ Crash في Railway
async def web_server(request):
    return web.Response(text="Bot is running!")

async def main():
    # إعداد الخادم
    app = web.Application()
    app.router.add_get('/', web_server)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    # حل مشكلة التعارض (طرد أي اتصال قديم)
    await bot.delete_webhook(drop_pending_updates=True)
    
    print(f"البوت يعمل الآن على المنفذ {port}...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
