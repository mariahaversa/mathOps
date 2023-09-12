from telegram import Bot
import asyncio


bot_token = '6643809195:AAHdpcv9NyY1CeB_2BPtMEgHJqjZHiCFoG8'

async def enviar_alerta():
    bot = Bot(token=bot_token)

    chat_id = '6657974100'

    message = 'Foram feitas modificações no repositório.'

    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(enviar_alerta())
