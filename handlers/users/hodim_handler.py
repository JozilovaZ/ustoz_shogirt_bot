
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import  confirm_state
from data.config import ADMINS
from loader import dp,bot
from states.anketa import hodimkkState


@dp.message_handler(text="Hodim kerak")
async def Ish_joyi_hadler(message:types.Message):
    text="""
        Xodim topish uchun ariza berish
        Hozir sizga birnecha savollar beriladi. 
        Har biriga javob bering. 
        Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.     
    """
    await message.answer(text)
    await message.answer("🎓 Idora nomi?")
    await hodimkkState.idora.set()

@dp.message_handler(state=hodimkkState.idora)
async def idora(message:types.Message,state:FSMContext):
    idora=message.text
    await state.update_data(
        {
            "idora": idora
        }
    )
    await hodimkkState.texno.set()
    await message.answer("📚 Texnologiya:\n\n Talab qilinadigan texnologiyalarni kiriting?\n Masalan,Java, C++, C#")


@dp.message_handler(state=hodimkkState.texno)
async def texno(message:types.Message,state:FSMContext):
    texno=message.text
    await state.update_data(
        {
            "texno": texno
        }
    )
    await hodimkkState.aloqa.set()
    await message.answer("📞 Aloqa: \n\n Bog`lanish uchun raqamingizni kiriting?\n Masalan, +998 90 123 45 67 ")

@dp.message_handler(state=hodimkkState.aloqa)
async def aloqa(message:types.Message,state:FSMContext):
    aloqa=message.text
    await state.update_data(
        {
            "aloqa": aloqa
        }
    )
    await hodimkkState.hudud.set()
    await message.answer("🌐 Hudud: \n\nQaysi hududdansiz?\n Viloyat nomi, Toshkent shahar yoki Respublikani kiriting")


@dp.message_handler(state=hodimkkState.hudud)
async def hudud(message:types.Message,state:FSMContext):
    hudud=message.text
    await state.update_data(
        {
            "hudud": hudud
        }
    )
    await hodimkkState.full_name.set()
    await message.answer("✍️Mas'ul ism sharifi?")


@dp.message_handler(state=hodimkkState.full_name)
async def full_name(message:types.Message,state:FSMContext):
    fullname=message.text
    await state.update_data(
        {
            "fullname":fullname
        }
    )
    await hodimkkState.murojat.set()
    await message.answer("🕰 Murojaat qilish vaqti: \n\n Qaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")

@dp.message_handler(state=hodimkkState.murojat)
async def murojat(message: types.Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {
            "murojat": murojat
        }
    )
    await hodimkkState.ish_vaqti.set()
    await message.answer("🕰 Ish vaqtini kiriting")

@dp.message_handler(state=hodimkkState.ish_vaqti)
async def ish_vaqti(message: types.Message, state: FSMContext):
    ish_vaqti = message.text
    await state.update_data(
        {
              "ish_vaqti": ish_vaqti
        }
    )
    await hodimkkState.maosh.set()
    await message.answer("💰 Maoshni kiriting?")


@dp.message_handler(state=hodimkkState.maosh)
async def maosh(message: types.Message, state: FSMContext):
    maosh = message.text
    await state.update_data(
        {
              "maosh": maosh
        }
    )
    await hodimkkState.qoshimcha_malumot.set()
    await message.answer("‼️ Qo`shimcha ma`lumotlar?")


@dp.message_handler(state=hodimkkState.qoshimcha_malumot)
async def qoshimcha_malumot(message: types.Message, state: FSMContext):
    qoshimcha_malumot = message.text
    await state.update_data(
        {
              "qoshimcha_malumot": qoshimcha_malumot
        }
    )

    # Ma'lumotlarni o'qiymiz
    data = await state.get_data()
    idora = data.get('idora')
    texno = data.get('texno')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    fullname=data.get('fullname')
    murojat = data.get('murojat')
    ish_vaqti=data.get('ish_vaqti')
    maosh=data.get('maosh')
    qoshimcha_malumot = data.get('qoshimcha_malumot')


    # xabar chiqaramiz
    text = f"<b>Hodim kirak:</b> \n\n"
    text += f"🏢 Idora:{idora}\n"
    text += f"📚 Texnologiya{texno}"
    text += f"Telegram:{aloqa}\n"
    text += f"📞 Aloqa:{aloqa}\n"
    text += f"🌐 Hudud:{hudud}\n"
    text+=f"✍️ Mas'ul:{fullname}\n"
    text += f"🕰 Murojaat vaqti:{murojat}\n"
    text+=f"🕰 Ish vaqti:{ish_vaqti}\n"
    text+=f"💰 Maosh:{maosh}\n"
    text += f"‼️ Qo`shimcha:{qoshimcha_malumot}\n"


    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=confirm_state)
    await hodimkkState.confirm.set()


@dp.message_handler(state=hodimkkState.confirm)
async def confirm(message: types.Message, state: FSMContext):
    javob = message.text.lower()

    if javob == "ha":
        data = await state.get_data()
        idora = data.get('idora')
        texno = data.get('texno')
        aloqa = data.get('aloqa')
        hudud = data.get('hudud')
        fullname = data.get('fullname')
        murojat = data.get('murojat')
        ish_vaqti = data.get('ish_vaqti')
        maosh = data.get('maosh')
        qoshimcha_malumot = data.get('qoshimcha_malumot')

        # xabar chiqaramiz
        text = f"<b>Hodim kirak:</b> \n\n"
        text += f"🏢 Idora:{idora}\n"
        text += f"📚 Texnologiya{texno}"
        text += f"Telegram:{aloqa}\n"
        text += f"📞 Aloqa:{aloqa}\n"
        text += f"🌐 Hudud:{hudud}\n"
        text += f"✍️ Mas'ul:{fullname}\n"
        text += f"🕰 Murojaat vaqti:{murojat}\n"
        text += f"🕰 Ish vaqti:{ish_vaqti}\n"
        text += f"💰 Maosh:{maosh}\n"
        text += f"‼️ Qo`shimcha:{qoshimcha_malumot}\n"

        await bot.send_message(ADMINS[0], text)
        await message.answer("Adminga yuborildi")
        await state.finish()

    elif javob == "yo`q":
        await message.answer("Qabul qilinmadi")
        await state.finish()
    else:
        await message.answer("Ha yoki Yo`q deb javob bering")




