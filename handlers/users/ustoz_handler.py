from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import  confirm_state
from data.config import ADMINS
from loader import dp,bot
from states.anketa import ustozState


@dp.message_handler(text="Shogird kerak")
async def Ustoz_handler(message:types.Message):
    text="""
            Ustoz topish uchun ariza berish
            Hozir sizga birnecha savollar beriladi. 
            Har biriga javob bering. 
            Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.     
        """
    await message.answer(text)
    await message.answer("<b>Isn familiyangizni kiriting </b>")
    await ustozState.fullname.set()

@dp.message_handler(state=ustozState.fullname)
async def full_name(message:types.Message,state:FSMContext):
    fullname=message.text
    await state.update_data(
        {
            "fullname":fullname
        }
    )
    await ustozState.yosh.set()
    await message.answer("🕑 Yosh:\n\n Yoshingizni kiriting?\n Masalan, 19")

@dp.message_handler(state=ustozState.yosh)
async def yosh(message:types.Message,state:FSMContext):
    yosh=message.text
    await state.update_data(
        {
            "yosh":yosh
        }
    )
    await ustozState.texno.set()
    await message.answer("📚 Texnologiya:\n\n Talab qilinadigan \ntexnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\n Masalan,Java, C++, C#")

@dp.message_handler(state=ustozState.texno)
async def texno(message:types.Message,state:FSMContext):
    texno=message.text
    await state.update_data(
        {
            "texno":texno
        }
    )
    await ustozState.aloqa.set()
    await message.answer("📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67")

@dp.message_handler(state=ustozState.aloqa)
async def aloqa(message:types.Message,state:FSMContext):
    aloqa=message.text
    await state.update_data(
        {
            "aloqa":aloqa
        }
    )
    await ustozState.hudud.set()
    await message.answer("🌐 Hudud:\n\n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting")

@dp.message_handler(state=ustozState.hudud)
async def hudud(message:types.Message,state:FSMContext):
    hudud=message.text
    await state.update_data(
        {
            "hudud":hudud
        }
    )
    await ustozState.narx.set()
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")


@dp.message_handler(state=ustozState.narx)
async def narx(message: types.Message, state: FSMContext):
    narx = message.text
    await state.update_data(
        {
            "narx": narx
        }
    )
    await ustozState.kasb.set()
    await message.answer("👨🏻‍💻 Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba")


@dp.message_handler(state=ustozState.kasb)
async def kasb(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data(
        {
            "kasb": kasb
        }
    )
    await ustozState.vaqt.set()
    await message.answer("🕰 Murojaat qilish vaqti: \n\n Qaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")

@dp.message_handler(state=ustozState.vaqt)
async def vaqt(message: types.Message, state: FSMContext):
    vaqt = message.text
    await state.update_data(
        {
            "vaqt": vaqt
        }
    )
    await ustozState.maqsad.set()
    await message.answer("🔎 Maqsad: \n\n Maqsadingizni qisqacha yozib bering")

@dp.message_handler(state=ustozState.maqsad)
async def maqsad(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {
            "maqsad": maqsad
        }
    )

    # Ma'lumotlarni o'qiymiz
    data = await state.get_data()
    full_name = data.get('full_name')
    yosh = data.get('yosh')
    texno = data.get('texno')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narx = data.get('narx')
    kasb = data.get('kasb')
    vaqt = data.get('vaqt')
    maqsad = data.get('kamaqsadsb')

    # xabar chiqaramiz
    text = f"<b>Ustoz kerak:</b> \n\n"
    text += f"🎓 Shogird::{full_name}\n"
    text += f"🌐 Yosh:{yosh}\n"
    text += f"📚 Texnologiya::{texno}\n"
    text += f"🇺🇿 Telegram:{aloqa}\n"
    text += f"📞 Aloqa:{aloqa}\n"
    text += f"🌐 Hudud:{hudud}\n"
    text += f"💰 Narxi:{narx}\n"
    text += f"🏻‍💻 Kasbi:{kasb}\n"
    text += f"🕰 Murojaat qilish vaqti:{vaqt}\n"
    text += f"🔎 Maqsad:{maqsad}\n"


    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=confirm_state)
    await ustozState.confirm.set()

    @dp.message_handler(state=ustozState.confirm)
    async def confirm(message: types.Message, state: FSMContext):
        javob = message.text.lower()

        if javob == "ha":
            data = await state.get_data()
            full_name = data.get('full_name')
            yosh = data.get('yosh')
            texno = data.get('texno')
            aloqa = data.get('aloqa')
            hudud = data.get('hudud')
            narx = data.get('narx')
            kasb = data.get('kasb')
            vaqt = data.get('vaqt')
            maqsad = data.get('kamaqsadsb')

            # xabar chiqaramiz
            text = f"<b>Ustoz kerak:</b> \n\n"
            text += f"🎓 Shogird::{full_name}\n"
            text += f"🌐 Yosh:{yosh}\n"
            text += f"📚 Texnologiya::{texno}\n"
            text += f"🇺🇿 Telegram:{aloqa}\n"
            text += f"📞 Aloqa:{aloqa}\n"
            text += f"🌐 Hudud:{hudud}\n"
            text += f"💰 Narxi:{narx}\n"
            text += f"🏻‍💻 Kasbi:{kasb}\n"
            text += f"🕰 Murojaat qilish vaqti:{vaqt}\n"
            text += f"🔎 Maqsad:{maqsad}\n"

            await bot.send_message(ADMINS[0], text)
            await message.answer("Adminga yuborildi")
            await state.finish()

        elif javob == "yo`q":
            await message.answer("Qabul qilinmadi")
            await state.finish()
        else:
            await message.answer("Ha yoki Yo`q deb javob bering")
