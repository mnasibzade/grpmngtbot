import sys
import os
from telegram.ext import Application, CommandHandler
from modules.start import start
from modules.poll import createpoll

def read_token():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        token_path = os.path.join(base_dir, 'token.txt')
        with open(token_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Token file (token.txt) not found.", file=sys.stderr)
        return None

TOKEN = read_token()

if not TOKEN:
    print("Bot token is missing. Please make sure the token.txt file exists.", file=sys.stderr)
    sys.exit(1)

def main():
    app = Application.builder().token(TOKEN).job_queue(None).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("poll", poll))

    app.run_polling()

if __name__ == '__main__':
    main()
