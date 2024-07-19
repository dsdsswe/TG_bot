
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share phone number", request_contact=True)]
    ],
    resize_keyboard=True
)
