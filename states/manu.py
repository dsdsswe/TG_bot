from aiogram.dispatcher.filters.state import State, StatesGroup


class Example(StatesGroup):
    name = State()
    phone_number = State()
    age = State()
    birthdate = State()


