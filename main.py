import os
import logging
from telegram import Update
from telegram.ext import (
Application,
CommandHandler,
CallbackQueryHandler,
ContextTypes,
)
from keyboards import (
keyboard_start,
keyboard_wait,
keyboard_hotel,
keyboard_tube,
keyboard_football,
keyboard_lounge,
keyboard_midnight,
)
from messages import MESSAGES
logging.basicConfig(
format="%(asctime)s | %(levelname)s | %(message)s",
level=logging.INFO
)
BOT_TOKEN = os.getenv("BOT_TOKEN")
START_TEXT = """
🔐 <b>LEVEL 21 SYSTEM</b>
━━━━━━━━━━━━━━━━━━
Статус соединения
🟢 ONLINE
━━━━━━━━━━━━━━━━━━
Для начала операции подтвердите получение инструкции.
"""
CONFIRM_TEXT = """
Инструкция получена.
Ожидайте дальнейших указаний штаба.
"""
WAIT_TEXT = """
📡 LEVEL 21 SYSTEM
Соединение установлено.
Операция LEVEL 21 активирована.
Дальнейшие сообщения будут поступать автоматически.
"""
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    START_TEXT,
    parse_mode="HTML",
    reply_markup=keyboard_start
    )
   async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
       query = update.callback_query
await query.answer()

if query.data == "confirm":

    await query.edit_message_text(
        CONFIRM_TEXT,
        reply_markup=keyboard_wait
    )

elif query.data == "wait":

    await query.edit_message_text(
        WAIT_TEXT
    )

    await query.message.reply_text(
        MESSAGES["road"],
        reply_markup=keyboard_hotel
    )

elif query.data == "hotel":

    await query.message.reply_text(
        MESSAGES["hotel"],
        reply_markup=keyboard_tube
    )

elif query.data == "tube":

    await query.message.reply_text(
        MESSAGES["tube"],
        reply_markup=keyboard_football
    )

elif query.data == "football":

    await query.message.reply_text(
        MESSAGES["football"],
        reply_markup=keyboard_lounge
    )

elif query.data == "lounge":

    await query.message.reply_text(
        MESSAGES["lounge"],
        reply_markup=keyboard_midnight
    )

elif query.data == "midnight":

    await query.message.reply_text(
        MESSAGES["midnight"]
    )
    def main():
app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CallbackQueryHandler(
        button_handler
    )
)

print("LEVEL21 BOT STARTED")

app.run_polling()
if name == "main":
main()
