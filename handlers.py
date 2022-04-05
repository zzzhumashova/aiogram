from main import bot, dp

from aiogram.types import Message

from config import id

async def send_to_admin(dp):
    await bot.send_message(chat_id=id, text="Salem, balakai")

@dp.message_handler()
async def echo(message: Message):
    text = f"Salem, ty tochno immel v vidu: {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)