from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


tillar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("O'zbek tili🇺🇿", callback_data='uz'),
            InlineKeyboardButton("Русский язык🇷🇺", callback_data='ru')
        ]
    ]
)