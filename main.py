import create_bot
from create_bot import dp
from aiogram.utils import executor

async def on_startup(_):
	print('Бот вышел в онлайн')

create_bot.register_handlers()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)