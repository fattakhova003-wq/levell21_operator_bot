```python
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
    [[InlineKeyboardButton("⚽ ПРИНЯТЬ ВЫЗОВ", callback_data="
```
```python
keyboard_lounge = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🛋 ОТКРЫТЬ LOUNGE", callback_data="lounge")]]
)

keyboard_midnight = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🌙 НАЧАТЬ НОЧНОЙ ПРОТОКОЛ", callback_data="midnight")]]
)
```
