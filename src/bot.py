from aiogram import Bot, Dispatcher, Router
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from config import API_TOKEN_BOT
from src import keyboards as kb

data = {"date": None,
        "category": None,
        "price": None,
        "comment": None}

router = Router()


class Incase(StatesGroup):
    date = State()
    category = State()
    price = State()
    comment = State()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f'Добрый вечер', reply_markup=kb.first)


@router.message(F.text == 'Доход')
async def add_item_date(message: Message, state: FSMContext):
    await message.answer(f'Введите дату')
    await state.set_state(Incase.date)


@router.message(Incase.date)
async def set_date(message: Message, state: FSMContext):
    data['date'] = message.text
    await message.answer('Выберите категорию')
    await state.set_state(Incase.category)


@router.message(Incase.category)
async def set_date(message: Message, state: FSMContext):
    data['category'] = message.text
    await message.answer('Напишите стоимость')
    await state.set_state(Incase.price)


@router.message(Incase.price)
async def set_date(message: Message, state: FSMContext):
    data['price'] = message.text
    await message.answer('Напишите комментарий')
    await state.set_state(Incase.comment)


@router.message(Incase.comment)
async def set_date(message: Message, state: FSMContext):
    data['comment'] = message.text
    await message.answer('Спасибо!')
    for i in data:
        print(data[i])
    await state.clear()


async def start_bot():
    bot = Bot(token=API_TOKEN_BOT)
    storage = MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_router(router)
    await dp.start_polling(bot)
