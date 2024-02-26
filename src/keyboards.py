import datetime

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

date = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"{datetime.date.today()}"),
        ]
    ],
    resize_keyboard=True,
)

incase_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cтипендия"),
            KeyboardButton(text="Именная стипендия"),
            KeyboardButton(text="Прочее"),
        ]
    ],
    resize_keyboard=True,
)

expenses_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Повседневные"),
            KeyboardButton(text="Крупные"),
            KeyboardButton(text="Хозяйство")
        ]
    ],
    resize_keyboard=True,
)

expenses_category1_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Еда вне дома")],
        [KeyboardButton(text="Продукты")],
        [KeyboardButton(text="Бары и рестораны")],
        [KeyboardButton(text="Транспорт")],
        [KeyboardButton(text="Алкоголь")],
        [KeyboardButton(text="Подарки")],
        [KeyboardButton(text="Здоровье")],
        [KeyboardButton(text="Одежда")],
        [KeyboardButton(text="Развлечения")],
        [KeyboardButton(text="Регулярные")],
        [KeyboardButton(text="Прочее")],
    ],
    resize_keyboard=True,
)

expenses_category3_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Комната")],
        [KeyboardButton(text="Расходники")],
    ],
    resize_keyboard=True,
)
expenses_category2_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Путешествия")],
        [KeyboardButton(text="Одежда")],
        [KeyboardButton(text="Гаджеты")],
        [KeyboardButton(text="Праздики")],
        [KeyboardButton(text="Крастота и здоровье")],
        [KeyboardButton(text="Образование")],
    ],
    resize_keyboard=True,
)

