import os
import json
import threading
from telegram import Bot
from flask import Flask, request


app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "6643809195:AAHdpcv9NyY1CeB_2BPtMEgHJqjZHiCFoG8"
TELEGRAM_CHAT_ID = "6657974100"

bot = Bot(token=TELEGRAM_BOT_TOKEN)

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    data = json.loads(request.data)
    if data['action'] == 'push':
        repo_name = data['repository']['full_name']
        sender_name = data['sender']['login']
        message = f"Alterações no projeto {repo_name} feitas por {sender_name}!"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    return '', 200

def run_flask():
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

if flask_thread.is_alive():
    flask_thread.join()  
