from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def createpoll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("Usage: /poll <question> | <variant1> | <variant2> | ...")
        return

    text = " ".join(context.args)
    parts = text.split("|")
    question = parts[0].strip()
    options = [opt.strip() for opt in parts[1:]]

    keyboard = [
    [
        InlineKeyboardButton("Anonymous", callback_data=f"anon|{question}|{'|'.join(options)}"),
        InlineKeyboardButton("Open", callback_data=f"open|{question}|{'|'.join(options)}")
    ]
]   
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Should this poll be anonymous?", reply_markup=reply_markup)
    
    question = parts[0].strip()
    options = [p.strip() for p in parts[1:]]
    if len(options) < 2:
        await update.message.reply_text("Min 2 variant!")
        return

    await context.bot.send.poll(
        chat_id = update.effective_chat.id,
        question=question,
        options=options,
        is 
    )

