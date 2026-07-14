from telegram import InlineKeyboardButton, InlineKeyboardMarkup


keyboard_start = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "✅ ПОДТВЕРДИТЬ ПОЛУЧЕНИЕ",
                callback_data="confirm"
            )
        ]
    ]
)


keyboard_wait = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🛰 ОЖИДАЮ ДАЛЬНЕЙШИХ ИНСТРУКЦИЙ",
                callback_data="wait"
            )
        ]
    ]
)


keyboard_hotel = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🏨 ПОДТВЕРДИТЬ ОТЕЛЬ",
                callback_data="hotel"
            )
        ]
    ]
)


keyboard_location = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "📍 ПОЛУЧИТЬ ЛОКАЦИЮ",
                callback_data="location"
            )
        ]
    ]
)


keyboard_tube = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🌪 НАЧАТЬ АЭРОТРУБУ",
                callback_data="tube"
            )
        ]
    ]
)


keyboard_football = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "⚽ НАЧАТЬ СПОРТИВНОЕ ИСПЫТАНИЕ",
                callback_data="football"
            )
        ]
    ]
)
