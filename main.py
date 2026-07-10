import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

OPERATOR_TOKEN = os.getenv("OPERATOR_TOKEN")
SYSTEM_TOKEN = os.getenv("SYSTEM_TOKEN")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")


messages = {
    "road": """
🔐 LEVEL 21 SYSTEM

ПРОТОКОЛ 03

🚗 ДОРОГА

Агент.

Маршрут активирован.

Следующая точка операции подтверждена.

Ожидайте дальнейших инструкций.

STATUS:
🟢 ACTIVE
""",

    "hotel": """
🔐 LEVEL 21 SYSTEM

ПРОТОКОЛ 04

🏨 ОТЕЛЬ

Локация подтверждена.

Получен новый этап операции.

Следуйте инструкциям на месте.

STATUS:
🟢 ACTIVE
""",

    "final": """
🔐 LEVEL 21 SYSTEM

ФИНАЛЬНЫЙ ПРОТОКОЛ

🏕 БАЗА

Агент.

Все испытания завершены.

Операция LEVEL 21 выполнена.

STATUS:
🟢 COMPLETE
"""
}


async def send_stage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.replace("/", "")

    if command in messages:
        await context.bot.send_message(
            chat_id=TARGET_CHAT_ID,
            text=messages[command]
        )

        await update.message.reply_text(
            "✅ Протокол отправлен агенту."
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 LEVEL CONTROL CENTER\n\nКоманды:\n/road\n/hotel\n/final"
    )


app = Application.builder().token(OPERATOR_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler(["road", "hotel", "final"], send_stage))

app.run_polling()
