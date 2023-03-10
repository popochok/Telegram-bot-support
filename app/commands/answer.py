from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from ..config.initialize import bot, dp
from ..config.const import ADMIN_ID

class Answer(StatesGroup):
    answer_msg = State()

@dp.message_handler(commands=["answer"])
async def answer(msg: types.Message):
    if msg.from_user.id == ADMIN_ID:
        await bot.send_message(msg.from_user.id, "Give answer:")
        await Answer.answer_msg.set()

@dp.message_handler(state=Answer.answer_msg) 
async def aswer_to_user(msg: types.Message, state: FSMContext):
    s = msg.text
    await bot.send_message(int(s[s.find("(") + 1:s.find(")")]), msg.text[12:])       