from telegram import InlineKeyboardButton, InlineKeyboardMarkup


keyboard_start = InlineKeyboardMarkup(
    [[InlineKeyboardButton("✅ ПОДТВЕРДИТЬ ПОЛУЧЕНИЕ", callback_data="confirm")]]
)


keyboard_wait = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🛰 ОЖИДАЮ ДАЛЬНЕЙШИХ ИНСТРУКЦИЙ", callback_data="wait")]]
)


keyboard_hotel = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🏨 ПОДТВЕРДИТЬ ОТЕЛЬ", callback_data="hotel")]]
)


keyboard_tube = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🌪 ЗАПУСТИТЬ ИСПЫТАНИЕ", callback_data="tube")]]
)


keyboard_football = InlineKeyboardMarkup(
    [[InlineKeyboardButton("⚽ ПРИНЯТЬ ВЫЗОВ", callback_data="football")]]
)

keyboard_lounge = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🛋 ОТКРЫТЬ LOUNGE", callback_data="lounge")]]
)

keyboard_detailing = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🚗 ПЕРЕДАТЬ ОБЪЕКТ", callback_data="detailing")]]
)


keyboard_midnight = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🌙 НАЧАТЬ НОЧНОЙ ЭТАП", callback_data="midnight")]]
)

keyboard_morning = InlineKeyboardMarkup(
    [[InlineKeyboardButton("☀️ НАЧАТЬ НОВЫЙ ДЕНЬ", callback_data="morning")]]
)

keyboard_elabuga = InlineKeyboardMarkup(
    [[InlineKeyboardButton("📍 ПОДТВЕРДИТЬ ПРИБЫТИЕ", callback_data="elabuga")]]
)

keyboard_questionnaire = InlineKeyboardMarkup(
    [[InlineKeyboardButton("📋 ОТКРЫТЬ ПРОТОКОЛ", callback_data="questionnaire")]]
)

keyboard_return = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 ПОДТВЕРДИТЬ ВОЗВРАЩЕНИЕ", callback_data="return")]]
)
