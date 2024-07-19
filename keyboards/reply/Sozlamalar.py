from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

uzru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇷🇺|🇺🇿🇧 Tilni o'zgartirish", callback_data='🇷🇺|🇺🇿🇧 Tilni o\'zgartirish')   
        ],
         [
            KeyboardButton("🔖 Shaxsiy ma'lumotlarni o'zgartirish", callback_data='🔖 Shaxsiy ma\'lumotlarni o\'zgartirish')   
        ],
         [
            KeyboardButton("⬅️ Орқага", callback_data='⬅️ Орқага')   
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

Malumot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔖 Shaxsiy ma'lumotlarni o'zgartirish")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
