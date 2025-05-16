from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_start
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text=f"""
        <b>Assalom alaykum {message.from_user.full_name}
        UstozShogird kanalining rasmiy botiga xush kelibsiz!</b>
        
        /help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!
"""
    await message.answer(text,reply_markup=menu_start)