from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import  confirm_state
from data.config import ADMINS
from loader import dp,bot
from states.anketa import Ishjoyikerak


@dp.message_handler(text="Ish joyi kerak")
async def Ish_joyi_hadler(message:types.Message):
    text="""
        Ish joyi topish uchun ariza berish
        Hozir sizga birnecha savollar beriladi. 
        Har biriga javob bering. 
        Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.     
    """
    await message.answer(text)
    await message.answer("<b>Isn familiyangizni kiriting </b>")
    await Ishjoyikerak.full_name.set()

@dp.message_handler(state=Ishjoyikerak.full_name)
async def full_name(message:types.Message,state:FSMContext):
    fullname=message.text
    await state.update_data(
        {
            "fullname":fullname
        }
    )
    await Ishjoyikerak.yosh.set()
    await message.answer("🕑 Yosh:\n\n Yoshingizni kiriting?\n Masalan, 19")



@dp.message_handler(state=Ishjoyikerak.yosh)
async def yosh(message:types.Message,state:FSMContext):
    yosh=message.text
    await state.update_data(
        {
            "yosh":yosh
        }
    )
    await Ishjoyikerak.texno.set()
    await message.answer("📚 Texnologiya:\n\n Talab qilinadigan texnologiyalarni kiriting?\n Texnologiya nomlarini vergul bilan ajrating. Masalan\nJava, C++, C#")


@dp.message_handler(state=Ishjoyikerak.texno)
async def texnologiya(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
            {
                "texnologiya": texnologiya
            }
        )
    await Ishjoyikerak.aloqa.set()
    await message.answer("📞 Aloqa: \n\n  Bog`lanish uchun raqamingizni kiriting?\n Masalan, +998 90 123 45 67\n")


@dp.message_handler(state=Ishjoyikerak.aloqa)
async def aloqa(message:types.Message,state:FSMContext):
    aloqa=message.text
    await state.update_data(
        {
            "aloqa":aloqa
        }
    )
    await Ishjoyikerak.hudud.set()
    await message.answer("🌐 Hudud:\n\n Qaysi hududdansiz?\n Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")

@dp.message_handler(state=Ishjoyikerak.hudud)
async def hudud(message:types.Message,state:FSMContext):
    hudud=message.text
    await state.update_data(
        {
            "hudud":hudud
        }
    )
    await Ishjoyikerak.narx.set()
    await message.answer("💰 Narxi:\n\n Tolov qilasizmi yoki Tekinmi?\n Kerak bo`lsa, Summani kiriting?")


@dp.message_handler(state=Ishjoyikerak.narx)
async def narx(message:types.Message,state:FSMContext):
    narx=message.text
    await state.update_data(
        {
            "narx":narx
        }
    )
    await Ishjoyikerak.kasb.set()
    await message.answer("👨🏻‍💻 Kasbi:\n\n Ishlaysizmi yoki o`qiysizmi?\n Masalan, Talaba")


@dp.message_handler(state=Ishjoyikerak.kasb)
async def kasb(message:types.Message,state:FSMContext):
    kasb=message.text
    await state.update_data(
        {
            "kasb":kasb
        }
    )
    await Ishjoyikerak.vaqt.set()
    await message.answer("🕰 Murojaat qilish vaqti:\n\n Qaysi vaqtda murojaat qilish mumkin?\n Masalan, 9:00 - 18:0")

@dp.message_handler(state=Ishjoyikerak.vaqt)
async def murajat(message:types.Message,state:FSMContext):
    murajat=message.text
    await state.update_data(
        {
            "murajat":murajat
        }
    )
    await Ishjoyikerak.maqsad.set()
    await message.answer("🔎 Maqsad:\n\n Maqsadingizni qisqacha yozib bering.")

@dp.message_handler(state=Ishjoyikerak.maqsad)
async def maqsad(message:types.Message,state:FSMContext):
    maqsad=message.text
    await state.update_data(
        {
            "maqsad":maqsad
        }
    )

    # Ma'lumotlarni o'qiymiz
    data = await state.get_data()
    fullname = data.get('fullname')
    yosh=data.get('yosh')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narx = data.get('narx')
    kasb = data.get('kasb')
    murajat = data.get('murajat')
    maqsad = data.get('maqsad')

    # xabar chiqaramiz
    text = f"<b>Sherik kerak:</b> \n\n"
    text += f"🏅 Sherik:{fullname}\n"
    text+=f"🕑 Yosh{yosh}"
    text += f"📚 Texnologiya:{texnologiya}\n"
    text += f"🇺🇿 Telegram:{aloqa}\n"
    text += f"📞 Aloqa:{aloqa}\n"
    text += f"🌐 Hudud:{hudud}\n"
    text += f"💰 Narxi:{narx}\n"
    text += f"🏻‍💻 Kasbi:{kasb}\n"
    text += f"🕰 Murojaat qilish vaqti:{murajat}\n"
    text += f"🔎 Maqsad:{maqsad}\n"

    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=confirm_state)
    await Ishjoyikerak.confirm.set()

@dp.message_handler(state=Ishjoyikerak.confirm)
async def confirm(message: types.Message, state: FSMContext):
        javob = message.text.lower()

        if javob == "ha":
            data = await state.get_data()

            fullname = data.get('fullname')
            yosh=data.get('yosh')
            texnologiya = data.get('texnologiya')
            aloqa = data.get('aloqa')
            hudud = data.get('hudud')
            narx = data.get('narx')
            kasb = data.get('kasb')
            murajat = data.get('murajat')
            maqsad = data.get('maqsad')

            # xabar chiqaramiz
            text = f"<b>Sherik kerak:</b> \n\n"
            text += f"🏅 Sherik:{fullname}\n"
            text+=f"🕑 Yosh:{yosh}"
            text += f"📚 Texnologiya:{texnologiya}\n"
            text += f"🇺🇿 Telegram:{aloqa}\n"
            text += f"📞 Aloqa:{aloqa}\n"
            text += f"🌐 Hudud:{hudud}\n"
            text += f"💰 Narxi:{narx}\n"
            text += f"🏻‍💻 Kasbi:{kasb}\n"
            text += f"🕰 Murojaat qilish vaqti:{murajat}\n"
            text += f"🔎 Maqsad:{maqsad}\n"

            await bot.send_message(ADMINS[0], text)
            await message.answer("Adminga yuborildi")
            await state.finish()

        elif javob == "yo`q":
            await message.answer("Qabul qilinmadi")
            await state.finish()
        else:
            await message.answer("Ha yoki Yo`q deb javob bering")



