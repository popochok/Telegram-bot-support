from aiogram import executor

from app.commands.start import dp
from app.commands.sms import dp
from app.commands.answer import dp

def main():
	executor.start_polling(dp)

if __name__ == "__main__":
	main()	