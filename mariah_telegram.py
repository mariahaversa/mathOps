from telegram import Bot
import asyncio


bot_token = ${{ secrets.TELEGRAM_TOKEN }}

async def enviar_alerta():
    bot = Bot(token=bot_token)

    chat_id = ${{ secrets.TELEGRAM_CHAT_ID }}

    message = 'Foram feitas modificações no repositório.'

    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(enviar_alerta())
