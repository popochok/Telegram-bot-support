from aiogram import types

from ..config.initialize import bot, dp
from ..config.const import TEXT_FOR_START

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
	await bot.send_message(msg.from_user.id, f"Hello, <b>{msg.from_user.full_name}!</b> \n\n{TEXT_FOR_START}")