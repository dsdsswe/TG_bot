from aiogram import Bot,Dispatcher
from data.config import API_TOKEN
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# logging qismi
logging.basicConfig(level=logging.INFO)

# frontend va backend qismni ulash 
bot = Bot(API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

