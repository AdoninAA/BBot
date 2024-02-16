from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter

from config import API_TOKEN_BOT
from excel_handler import clear_directory, process_excels


router = Router()


@router.message(Command('load_sku'))
async def load(message: Message, state: FSMContext):
    await message.answer('Пришлите файлы отчетов по <b>sku</b> в формате .xls или .xlxs\n'
                         'По завершению напишите мне слово:\n<code>Стоп</code>', parse_mode='html')
    user_id = message.from_user.id
    creat_directories(user_id)
    clear_directory(f'reports/{user_id}/reports_sku')
    clear_directory(f'reports/{user_id}/ready_reports_sku')
    await state.set_state(FileReportsSku.files)





async def start_bot():
    bot = Bot(token=API_TOKEN_BOT)
    storage = MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_router(router)
    await dp.start_polling(bot)