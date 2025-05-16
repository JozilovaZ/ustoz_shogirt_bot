from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu_start=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joyi kerak"),

        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak"),
        ],
        [
            KeyboardButton(text="Shogird kerak"),
        ],
    ],
    resize_keyboard=True
)

confirm_state=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="yo`q"),

        ],
],
    resize_keyboard=True
)