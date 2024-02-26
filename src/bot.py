from aiogram import Bot, Dispatcher, Router
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from config import API_TOKEN_BOT
from src import keyboards as kb
from docs import add_incase, add_expenses

import datetime

data = {"podcategory": None,
        "date": None,
        "category": None,
        "price": None,
        "comment": None}

router = Router()


class Incase(StatesGroup):
    podcategory = State()
    date = State()
    category = State()
    price = State()
    comment = State()


class Expenses(StatesGroup):
    podcategory = State()
    date = State()
    category = State()
    price = State()
    comment = State()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    for i in data:
        data[i] = None
    await state.clear()
    await message.answer(f'Добрый вечер', reply_markup=kb.first)


@router.message(F.text == 'Доход')
async def add_item_date(message: Message, state: FSMContext):
    data['podcategory'] = message.text
    await message.answer(f'Введите дату', reply_markup=kb.date)
    await state.set_state(Incase.date)


@router.message(Incase.date)
async def set_date(message: Message, state: FSMContext):
    data['date'] = message.text
    await message.answer('Выберите категорию', reply_markup=kb.incase_keyboard)
    await state.set_state(Incase.category)


@router.message(Incase.category)
async def set_date(message: Message, state: FSMContext):
    data['category'] = message.text
    await message.answer('Напишите стоимость', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Incase.price)


@router.message(Incase.price)
async def set_date(message: Message, state: FSMContext):
    data['price'] = message.text
    await message.answer('Напишите комментарий')
    await state.set_state(Incase.comment)


@router.message(Incase.comment)
async def set_date(message: Message, state: FSMContext):
    data['comment'] = message.text
    await message.answer('Спасибо!', reply_markup=kb.first)
    for i in data:
        print(data[i])
    await add_incase(data['date'], data['category'], data['price'], data['comment'])
    await state.clear()


@router.message(F.text == 'Расход')
async def add_item_date(message: Message, state: FSMContext):
    await message.answer(f'Введите категорию', reply_markup=kb.expenses_keyboard)
    await state.set_state(Expenses.podcategory)


@router.message(Expenses.podcategory)
async def add_item_date(message: Message, state: FSMContext):
    data['podcategory'] = message.text
    await message.answer(f'Введите дату', reply_markup=kb.date)
    await state.set_state(Expenses.date)


@router.message(Expenses.date)
async def set_date(message: Message, state: FSMContext):
    data['date'] = message.text
    if data['podcategory'] == 'Повседневные':
        await message.answer('Выберите категорию', reply_markup=kb.expenses_category1_keyboard)
    elif data['podcategory'] == 'Крупные':
        await message.answer('Выберите категорию', reply_markup=kb.expenses_category2_keyboard)
    elif data['podcategory'] == 'Хозяйство':
        await message.answer('Выберите категорию', reply_markup=kb.expenses_category3_keyboard)
    await state.set_state(Expenses.category)


@router.message(Expenses.category)
async def set_date(message: Message, state: FSMContext):
    data['category'] = message.text
    await message.answer('Напишите стоимость', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Expenses.price)


@router.message(Expenses.price)
async def set_date(message: Message, state: FSMContext):
    data['price'] = message.text
    await message.answer('Напишите комментарий')
    await state.set_state(Expenses.comment)


@router.message(Expenses.comment)
async def set_date(message: Message, state: FSMContext):
    data['comment'] = message.text
    await message.answer('Спасибо!', reply_markup=kb.first)
    for i in data:
        print(data[i])
    await add_expenses(data['podcategory'], data['date'], data['category'], data['price'], data['comment'])
    await state.clear()


async def start_bot():
    bot = Bot(token=API_TOKEN_BOT)
    storage = MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_router(router)
    await dp.start_polling(bot)
