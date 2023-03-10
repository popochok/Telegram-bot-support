from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from ..config.initialize import bot, dp
from ..config.const import ADMIN_ID

class Question(StatesGroup):
    question_msg = State()

@dp.message_handler(commands=["sms"])
async def send_question(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        await bot.send_message(msg.from_user.id, "Ask a question:")
        await Question.question_msg.set()
        

@dp.message_handler(state=Question.question_msg)
async def question_to_admin(msg: types.Message, state: FSMContext):
    await bot.send_message(msg.from_user.id, "Thank you! your question will be considered")
    await bot.send_message(ADMIN_ID, f"{msg.from_user.full_name}({msg.from_user.id}): {msg.text}")    