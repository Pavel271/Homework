from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = '7850022438:AAHTiWhNltW39eYkj41UUslFTLRg10ckeu4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
kp = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kp.insert(button)
kp.insert(button2)
kp.insert(button3)

kb = InlineKeyboardMarkup(resize_keyboard=True)
button_1 = InlineKeyboardButton(text='1). Комплекс витаминов B', callback_data='product_buying')
button_2 = InlineKeyboardButton(text='2). Omega-3', callback_data='product_buying')
button_3 = InlineKeyboardButton(text='3). Комплекс витаминов C', callback_data='product_buying')
button_4 = InlineKeyboardButton(text='4). Витамины D-3', callback_data='product_buying')
kb.insert(button_1)
kb.insert(button_2)
kb.insert(button_3)
kb.insert(button_4)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1,5):
        with open(f'Product{i}.jpg', "rb") as jpg:
            await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
            await message.answer_photo(jpg)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
#
kl = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
kl.add(button)
kl.add(button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kl)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формулы расчета: (10 x вес(кг) + 6,25 x рост(см) – 5 x возраст(г) - 161)')
    await call.answer()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!', reply_markup=kp)
#
@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
   await state.update_data(growth=int(message.text))
   await message.answer('Введите свой вес:')
   await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша дневная норма калорий: {calories} ккал")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)