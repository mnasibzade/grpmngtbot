from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


async def createpoll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("Usage: /poll <question> | <option1> | <option2> | ...")
        return

    text = " ".join(context.args)
    parts = text.split("|")
    question = parts[0].strip()
    options = [p.strip() for p in parts[1:]]

    if len(options) < 2:
        await update.message.reply_text("Minimum 2 variant!")
        return

    keyboard = [
        [
            InlineKeyboardButton("Anonymous", callback_data=f"anon|{question}|{'|'.join(options)}"),
            InlineKeyboardButton("Open", callback_data=f"open|{question}|{'|'.join(options)}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Should this poll be anonymous?", reply_markup=reply_markup)

async def poll_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data.split("|")
    poll_type = data[0]
    question = data[1]
    options = data[2:]
    is_anonymous = True if poll_type == "anon" else False

    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=question,
        options=options,
        is_anonymous=is_anonymous
    )
