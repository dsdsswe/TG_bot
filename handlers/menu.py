from aiogram import types
from loader import dp
from keyboards.inline.languages import tillar
from keyboards.reply.asosiy import jinsi
from keyboards.reply.asosiy import main_menu
from keyboards.inline.menu import website_button
from keyboards.reply.Sozlamalar import uzru
from keyboards.reply.manzil import hudud
from keyboards.reply.manzil import Toshkent
from keyboards.reply.asosiy import bosh_menuga_qaytish

@dp.callback_query_handler(text="uz")
async def menu_handler(call: types.CallbackQuery):
    await call.message.answer(text="Siz o'zbek tilini tanladingiz.", reply_markup=jinsi)

@dp.message_handler(text="jinsi")
async def start_handler(message: types.Message):
    await message.answer(f"Jinsingizni yozing:", reply_markup=jinsi)

@dp.message_handler(text="Erkak")
async def start_handler(message: types.Message):
    text = """
🙋‍♂️🙋‍♀️ Мы рады видеть вас в числе наших покупателей.  помощью этого бота вы можете:

💳🛍 Пользоваться накопительной картой, проверить баланс и историю карты, использовать e при следующей покупки, показав штрих-код кассиру.
💬 Оставлять отзыв или обратную связь
🚚👕 Заказать доставку одежды не выходя из телеграма
🛒💰 Быть в курсе новых поступлений и эксклюзивных акций.
📍📞 Узнать адреса и контакты наших магазинов.
💼👔 Получить информацию по актуальным вакансиям в нашей компании.
"""
    await message.answer(text, reply_markup=main_menu)

@dp.message_handler(text="💳 Mening imtiyoz kartam")
async def card_handler(message: types.Message):  
    await message.answer_photo(
        photo="https://idum.uz/wp-content/uploads/2016/11/Kak_proverit_shtrih-kod.jpg",
        caption="""Balans: 15599.0\nBir oyda sarflangan: 0.0\nBir yilga sarflangan: 0.0\nBor davr mobaynida sarflangan: 0.0"""
    )

@dp.message_handler(text="🛍 Saytdan buyurtma qilish")
async def order_handler(message: types.Message):
    await message.answer("Buyutma uchun quyidagi <a href='https://terrapro.uz/uz/'>link</a> ni ustiga bosing👇️: ",
                    reply_markup=website_button, parse_mode='HTML')    

@dp.message_handler(text="⚙️ Sozlamalar")
async def start_handler(message: types.Message):
    text = "Sozlamalar"
    await message.answer(text, reply_markup=uzru)

@dp.message_handler(text="🇷🇺|🇺🇿🇧 Tilni o'zgartirish")
async def start_handler(message: types.Message):
    text = """
Здравствуйте! 🌟 Давайте для начала выберем язык обслуживания! 🌐

Assalomu aleykum! 🌟 Keling, avvaliga xizmat korsatish tilini tanlab olaylik. 🌐

Choose a language, please
"""
    await message.answer(text, reply_markup=tillar)

@dp.message_handler(text="🔖 Shaxsiy ma'lumotlarni o'zgartirish")
async def start_handler(message: types.Message):
    text = """
Diqqat! Telefon raqamingiz o'zgartirilgach, sizning Akkauntingizga eski raqamdan kirish imkoniyati boshqa mavjud bo'lmaydi.
"""
    await message.answer(text, reply_markup=main_menu)

@dp.message_handler(text="⬅️ Орқага")
async def back_handler(message: types.Message):
    text = "Ortga qaytdingiz"
    await message.answer(text, reply_markup=main_menu)

@dp.message_handler(text="☎️ Biz bilan bog'lanish")
async def back_handler(message: types.Message):
    text = """Написать в телеграм: @Terraprocommunity_bot

           Позвонить в офис: +998 71 250 93 91 📞"""
    await message.answer(text, reply_markup=main_menu)

@dp.message_handler(text='✍️ Izoh qoldirish')
async def order_handler(message: types.Message):
    await message.answer("Agar biror muammoga duch kelgan bo'lsangiz, iltimos, uni imkon qadar batafsilroq yoriting", reply_markup=bosh_menuga_qaytish)
    

@dp.message_handler(text='↩️ Bosh menuga')
async def order_handler(message: types.Message):
    await message.answer("ortaga otdingiz",reply_markup=main_menu)

@dp.message_handler(text='📍 Dokonlarimiz')
async def manzil_handler(message:types.Message):
    await message.answer("hududni tanlang",reply_markup=hudud)   

@dp.message_handler(text='Toshkent')
async def manzil_handler(message:types.Message):
    text=""" Самарканд Дарвоза
Адрес: г.Ташкент ул. Караташ 5 "а" ТРЦ "Самарканд Дарваза" 3-этаж (https://maps.google.com/maps?q=41.316586,69.230498&ll=41.316586,69.230498&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 - 23:00
Телефон: +998 71 205 10 23

2. Некст
Адрес: г. Ташкент ул Бабура ТРЦ  "Некст" 1 этаж (https://maps.google.com/maps?q=41.298280,69.249421&ll=41.298280,69.249421&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 - 23:00
Телефон: +998 71 230 77 50

3. Атлас
Адрес: г. Ташкент ул катартал 28, ТРЦ " Атлас" 2 этаж (https://maps.google.com/maps?q=41.281444,69.201246&ll=41.281444,69.201246&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 22:00
Телефон: +998 99 875 99 29

4. Парус
Адрес:  г. Ташкент ул Катартал 60  ТРЦ "Парус" 1 этаж (https://maps.google.com/maps?q=41.292024,69.210617&ll=41.292024,69.210617&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 22:00
Телефон: +998 78 150 67 14

5. Максим Горький
Адрес: г. Ташкет Буюк Ипак Йули 59 (метро) (https://maps.google.com/maps?q=41.325978,69.329539&ll=41.325978,69.329539&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 22:00
Телефон: +998 95 142 32 30

6. Мега
Адрес:  г.Ташкент Юнусобод 11 кв ТРЦ " Мега Планет " 3 этаж (https://maps.google.com/maps?q=41.367178,69.291145&ll=41.367178,69.291145&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 22:00
Телефон:  +998 71 205 06 46

7. Компасс
Адрес:  г.Ташкент Бектемирский Район ТКАД ул Фаргона йули 17 ТРЦ "Компасс"
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 - 22:00
Телефон: +998 71 205 06 50

8. Вега
Адрес:  г.Ташкент ТРЦ "Вега Центре" ул Шота Руставели 150
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 22:00
Телефон: +998 95 199 09 39

9. Пойтахт
Адрес:  г. Ташкент ул Матбуотчилар ТРЦ "Пойтахт"  2 этаж (https://maps.google.com/maps?q=41.311339,69.275473&ll=41.311339,69.275473&z=16)
График работы:
Будние дни: 10:00 – 20:00
Выходные: 10:00 – 20:00
Телефон: +998 78 113 24 03

10.  GoldenLife
Адрес: г. Ташкент Сергелийский район, пересечение улиц Мирзо турсунзода и мехригие, Ориентир 3- станция метро 
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 23:00

11. Чимган Плаза
Адрес:  г. Ташкент Мирзо-Улугбек район ТРЦ "Чимган Атлас" ориентир Эко базар (https://maps.google.com/maps?q=41.353506,69.353464&ll=41.353506,69.353464&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 23:00
Телефон: +998  99 796 89 15

12. Magic City
Адрес:  Г.Ташкент ул Бобура 174 (https://maps.google.com/maps?q=41.304011,69.245788&ll=41.304011,69.245788&z=16)
График работы:
Будние дни: 10:00 – 22:00
Выходные: 10:00 – 22:00
Телефон: +998  99 890 19 02

41°18'59.7"N 69°13'49.8"E (https://maps.google.com/maps?q=41.316586,69.230498&ll=41.316586,69.230498&z=16)
Find local businesses, view maps and get driving directions in Google Maps."""
    await message.answer(text,reply_markup=Toshkent)  
    await message.answer(".",reply_markup=main_menu)
