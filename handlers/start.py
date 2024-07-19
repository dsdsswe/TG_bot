from aiogram import types
from loader import dp
from states.manu import Example
from aiogram.dispatcher import FSMContext
from keyboards.reply.button import phone_number
from keyboards.reply.asosiy import jinsi
from datetime import datetime

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}. Botimizga xush kelibsiz.")
    await Example.name.set()
    await message.answer("Iltimos, ismingizni kiriting:")

@dp.message_handler(state=Example.name, content_types=types.ContentType.TEXT)
async def name_handler(message: types.Message, state=FSMContext):
    ism = message.text
    if not ism.isalpha():
        await message.answer("Ism faqat harflardan iborat bo'lishi kerak. Iltimos, qayta kiriting:")
        return
    await state.update_data(name=ism)
    await Example.age.set()
    await message.answer("Iltimos, yoshingizni kiriting:")

@dp.message_handler(lambda message: message.text.isdigit(), state=Example.age)
async def age_handler(message: types.Message, state=FSMContext):
    age = int(message.text)
    if age <= 14:
        await message.answer("Yoshingiz 14 yoshdan katta bo'lishi kerak. Iltimos, qayta kiriting:")
        return
    await state.update_data(age=age)
    await Example.phone_number.set()
    await message.answer("Iltimos, telefon raqamingizni yuboring:", reply_markup=phone_number)

@dp.message_handler(state=Example.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_handler(message: types.Message, state=FSMContext):
    phone_number = message.contact
    await state.update_data(phone_number=phone_number)
    await Example.birthdate.set()
    await message.answer("Iltimos, tug'ilgan kuningizni quyidagi ko'rinishda kiriting (12.01.1991):")

@dp.message_handler(state=Example.birthdate, content_types=types.ContentType.TEXT)
async def birthdate_handler(message: types.Message, state=FSMContext):
    birthdate = message.text
    try:
        birthdate_obj = datetime.strptime(birthdate, "%d.%m.%Y")
        current_date = datetime.now()
        age = (current_date - birthdate_obj).days // 365
        if age <= 14:
            await message.answer("Yoshingiz 14 yoshdan katta bo'lishi kerak. Iltimos, qayta kiriting:")
            return
    except ValueError:
        await message.answer("Noto'g'ri format. Iltimos, tug'ilgan kuningizni quyidagi ko'rinishda kiriting (12.01.1991):")
        return

    await state.update_data(birthdate=birthdate)

    data = await state.get_data()

    ism = data.get('name')
    telefon_raqam = data.get('phone_number')['phone_number']
    tugilgan_yil = data.get('birthdate')
    age = data.get('age')

    text = "Sizdan quyidagi ma'lumotlar qabul qilindi:\n"
    text += f"Ismingiz: {ism}\n"
    text += f"Telefon raqamingiz: {telefon_raqam}\n"
    text += f"Tug'ilgan yilingiz: {tugilgan_yil}\n"
    text += f"Yoshingiz: {age}"

    await message.answer(text)
    await message.answer("Asosiyga o'tdingiz", reply_markup=jinsi)
    await state.finish()

@dp.message_handler(lambda message: not message.text.isdigit(), state=Example.age)
async def invalid_age_handler(message: types.Message):
    await message.answer("Yosh faqat raqamlardan iborat bo'lishi kerak. Iltimos, qayta kiriting:")
