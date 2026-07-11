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
)


from messages import MESSAGES


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)


BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID"))

AGENT_ID = int(os.getenv("AGENT_ID"))


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

    if query.data == "wait":
        await query.edit_message_text(
            WAIT_TEXT
        )

        await query.message.reply_text(
            MESSAGES["road"],
            reply_markup=keyboard_hotel
        )

    if query.data == "hotel":
        await query.message.reply_text(
            MESSAGES["hotel"]
        )if query.data == "hotel":
    await query.edit_message_text(
        MESSAGES["hotel"],
        reply_markup=keyboard_location
    )


if query.data == "location":
    await query.message.reply_text(
        MESSAGES["location"]
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



if __name__ == "__main__":

    main()
from keyboards import (
    keyboard_start,
    keyboard_wait,
    keyboard_hotel,
    keyboard_location,
)
