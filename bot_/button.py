from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Eng ➡️ Uz'), KeyboardButton(text='Uz ➡️ Eng')]
    ], resize_keyboard=True
)

back_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🔙back🔙')]
    ],resize_keyboard=True
)

