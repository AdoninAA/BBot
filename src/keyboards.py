from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

first = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Доход"),
                    KeyboardButton(text="Расход"),
                ]
            ],
            resize_keyboard=True,
        )
