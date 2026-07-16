import os
import logging
import httpx

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
    keyboard_morning,
    keyboard_elabuga,
    keyboard_detailing,
    keyboard_questionnaire,
    keyboard_return,
    keyboard_final,
)

from messages import MESSAGES


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)


BOT_TOKEN = os.getenv("BOT_TOKEN")
AGENT_BOT_TOKEN = os.getenv("AGENT_BOT_TOKEN")
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


async def send_agent_message(text):

    url = f"https://api.telegram.org/bot{AGENT_BOT_TOKEN}/sendMessage"

    async with httpx.AsyncClient() as client:

        await client.post(
            url,
            json={
                "chat_id": AGENT_ID,
                "text": text
            }
        )


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

        await send_agent_message(
            MESSAGES["hotel"]
        )


    elif query.data == "tube":

        await query.message.reply_text(
            MESSAGES["tube"],
            reply_markup=keyboard_football
        )

        await send_agent_message(
            MESSAGES["tube"]
        )


    elif query.data == "football":

        await query.message.reply_text(
            MESSAGES["football"],
            reply_markup=keyboard_lounge
        )

        await send_agent_message(
            MESSAGES["football"]
        )


    elif query.data == "lounge":

        await query.message.reply_text(
            MESSAGES["lounge"],
            reply_markup=keyboard_midnight
        )

        await send_agent_message(
            MESSAGES["lounge"]
        )


    elif query.data == "midnight":

        await query.message.reply_text(
            MESSAGES["midnight"],
            reply_markup=keyboard_morning
        )

        await send_agent_message(
            MESSAGES["midnight"]
        )


    elif query.data == "morning":

        await query.message.reply_text(
            MESSAGES["morning"],
            reply_markup=keyboard_elabuga
        )

        await send_agent_message(
            MESSAGES["morning"]
        )


    elif query.data == "elabuga":

        await query.message.reply_text(
            MESSAGES["elabuga"],
            reply_markup=keyboard_detailing
        )

        await send_agent_message(
            MESSAGES["elabuga"]
        )


    elif query.data == "detailing":

        await query.message.reply_text(
            MESSAGES["detailing"],
            reply_markup=keyboard_questionnaire
        )

        await send_agent_message(
            MESSAGES["detailing"]
        )


    elif query.data == "questionnaire":

        await query.message.reply_text(
            MESSAGES["questionnaire"],
            reply_markup=keyboard_return
        )

        await send_agent_message(
            MESSAGES["questionnaire"]
        )


    elif query.data == "return":

        await query.message.reply_text(
            MESSAGES["return"],
            reply_markup=keyboard_final
        )

        await send_agent_message(
            MESSAGES["return"]
        )


    elif query.data == "final":

        await query.message.reply_text(
            MESSAGES["final"]
        )

        await send_agent_message(
            MESSAGES["final"]
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
