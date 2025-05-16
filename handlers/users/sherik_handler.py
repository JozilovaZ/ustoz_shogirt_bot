from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp,bot
from states.anketa import SherikState
from keyboards.default.menu import confirm_state,menu_start

@dp.message_handler(text="Sherik kerak")
async def sherik_hadler(message:types.Message):
    text="""
        Sherik topish uchun ariza berish
        Hozir sizga birnecha savollar beriladi. 
        Har biriga javob bering. 
        Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
    """
    await message.answer(text)
    await message.answer("<b>Isn familiyangizni kiriting </b>")
    await SherikState.full_name.set()


@dp.message_handler(state=SherikState.full_name)
async def full_name(message:types.Message,state:FSMContext):
    fullname=message.text
    await state.update_data(
        {
            "fullname":fullname
        }
    )
    await SherikState.texno.set()
    await message.answer("📚 Texnologiya:\n\n Talab qilinadigan texnologiyalarni kiriting?\n Texnologiya nomlarini vergul bilan ajrating. Masalan\nJava, C++, C#")



@dp.message_handler(state=SherikState.texno)
async def texnologiya(message:types.Message,state:FSMContext):
    texnologiya=message.text
    await state.update_data(
        {
            "texnologiya":texnologiya
        }
    )
    await SherikState.aloqa.set()
    await message.answer("📞 Aloqa: \n\n  Bog`lanish uchun raqamingizni kiriting?\n Masalan, +998 90 123 45 67\n")

@dp.message_handler(state=SherikState.aloqa)
async def aloqa(message:types.Message,state:FSMContext):
    aloqa=message.text
    await state.update_data(
        {
            "aloqa":aloqa
        }
    )
    await SherikState.hudud.set()
    await message.answer("🌐 Hudud:\n\n Qaysi hududdansiz?\n Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")

@dp.message_handler(state=SherikState.hudud)
async def hudud(message:types.Message,state:FSMContext):
    hudud=message.text
    await state.update_data(
        {
            "hudud":hudud
        }
    )
    await SherikState.narx.set()
    await message.answer("💰 Narxi:\n\n Tolov qilasizmi yoki Tekinmi?\n Kerak bo`lsa, Summani kiriting?")




@dp.message_handler(state=SherikState.narx)
async def narx(message:types.Message,state:FSMContext):
    narx=message.text
    await state.update_data(
        {
            "narx":narx
        }
    )
    await SherikState.kasb.set()
    await message.answer("👨🏻‍💻 Kasbi:\n\n Ishlaysizmi yoki o`qiysizmi?\n Masalan, Talaba")



@dp.message_handler(state=SherikState.kasb)
async def kasb(message:types.Message,state:FSMContext):
    kasb=message.text
    await state.update_data(
        {
            "kasb":kasb
        }
    )
    await SherikState.murojat.set()
    await message.answer("🕰 Murojaat qilish vaqti:\n\n Qaysi vaqtda murojaat qilish mumkin?\n Masalan, 9:00 - 18:0")




@dp.message_handler(state=SherikState.murojat)
async def murajat(message:types.Message,state:FSMContext):
    murajat=message.text
    await state.update_data(
        {
            "murajat":murajat
        }
    )
    await SherikState.maqsad.set()
    await message.answer("🔎 Maqsad:\n\n Maqsadingizni qisqacha yozib bering.")


@dp.message_handler(state=SherikState.maqsad)
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
    await SherikState.confirm.set()




@dp.message_handler(state=SherikState.confirm)
async def confirm(message:types.Message,state:FSMContext):
    javob=message.text.lower()

    if javob=="ha":
        data=await state.get_data()

        fullname = data.get('fullname')
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
        text += f"📚 Texnologiya:{texnologiya}\n"
        text += f"🇺🇿 Telegram:{aloqa}\n"
        text += f"📞 Aloqa:{aloqa}\n"
        text += f"🌐 Hudud:{hudud}\n"
        text += f"💰 Narxi:{narx}\n"
        text += f"🏻‍💻 Kasbi:{kasb}\n"
        text += f"🕰 Murojaat qilish vaqti:{murajat}\n"
        text += f"🔎 Maqsad:{maqsad}\n"

        await bot.send_message(ADMINS[0],text)
        await message.answer("Adminga yuborildi")
        await state.finish()

    elif javob=="yo`q":
        await message.answer("Qabul qilinmadi")
        await state.finish()
    else:
        await message.answer("Ha yoki Yo`q deb javob bering")











