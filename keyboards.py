from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


keyboard_hotel = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➡️ ПРОДОЛЖИТЬ ОПЕРАЦИЮ",
                callback_data="hotel"
            )
        ]
    ]
)
