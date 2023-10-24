from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

storage = MemoryStorage()

bot = Bot(token = '6792719026:AAEnwk-mvIXkymnORF8r7E8zyu0RQ_nVgIU')
dp = Dispatcher(bot, storage = storage)
dp.middleware.setup(LoggingMiddleware())

async def echo(message: types.Message):
    await message.answer(text=f'Не {message.text}, а с ДР Санечка')

def register_handlers():
    dp.register_message_handler(echo)