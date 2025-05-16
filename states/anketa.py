from aiogram.dispatcher.filters.state import State,StatesGroup


class SherikState(StatesGroup):
    full_name=State()
    texno=State()
    aloqa=State()
    hudud=State()
    narx=State()
    kasb=State()
    murojat=State()
    maqsad=State()
    confirm=State()


class Ishjoyikerak(StatesGroup):
    full_name=State()
    yosh=State()
    texno=State()
    aloqa=State()
    hudud=State()
    narx=State()
    kasb=State()
    vaqt=State()
    maqsad=State()
    confirm = State()

class hodimkkState(StatesGroup):
    idora=State()
    texno=State()
    aloqa=State()
    hudud = State()
    full_name=State()
    murojat=State()
    ish_vaqti=State()
    maosh=State()
    qoshimcha_malumot=State()
    confirm=State()

class ustozState(StatesGroup):
    confirm = State()
    fullname=State()
    yosh=State()
    texno=State()
    aloqa = State()
    hudud = State()
    aloqa = State()
    hudud = State()
    narx= State()
    kasb = State()
    vaqt = State()
    maqsad=State()


class shogirtkkState(StatesGroup):
    confirm = State()
    fullname = State()
    yosh = State()
    texno = State()
    aloqa = State()
    hudud = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()


