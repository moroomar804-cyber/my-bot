@dp.callback_query(F.data == "payment")
async def show_payment(callback: types.CallbackQuery):
    text = (
        "💳 **مركز شحن الرصيد الرسمي**\n\n"
        "يرجى التحويل إلى إحدى الحسابات التالية:\n\n"
        "💎 **سي واليت (C-Wallet):**\n"
        "ID: `91552675`\n\n"
        "💸 **فوست باي (FaucetPay):**\n"
        "اسم الحساب: `Flashnumber`\n\n"
        "🏦 **باي بت (Bybit):**\n"
        "ID: `493857145`\n\n"
        "🔗 **عناوين USDT:**\n"
        "• **BEP20:**\n`0xcc17cd115159942cbe18cc7d6ec2285d063cff23`\n\n"
        "• **Polygon:**\n`0xcc17cd115159942cbe18cc7d6ec2285d063cff23`\n\n"
        "⚠️ **ملاحظة:** بعد التحويل أرسل صورة الإيصال للدعم الفني ليتم شحن رصيدك."
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 تواصل مع الدعم", url="https://t.me/Flashnumbersupport2")],
        [InlineKeyboardButton(text="⬅️ رجوع", callback_data="back_main")]
    ])
    
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

