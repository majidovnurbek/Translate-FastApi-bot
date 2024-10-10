from requests import get
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters.command import Command
from config import Token
from button import language, back_button
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

logging.basicConfig(level=logging.INFO)
bot = Bot(token=Token)
dp = Dispatcher()


class choose_lang(StatesGroup):
    which_language = State()
    finish = State()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"hello welcome to translate bot {message.from_user.full_name}", reply_markup=language)


while 1:
    @dp.message(F.text == 'Eng ➡️ Uz')
    async def english_uz(message: Message, state: FSMContext):
        await state.set_state(choose_lang.which_language)
        await message.answer('enter english words or sentence!!')


    @dp.message(choose_lang.which_language)
    async def finish(message: Message, state: FSMContext):
        await state.update_data(which_language=message.text)
        await state.set_state(choose_lang.finish)
        data = await state.get_data()
        await state.clear()
        name = data.get('which_language', 'hech')
        en = f'http://127.0.0.1:8000/en_uz/{name}'
        resp = get(en)
        a = resp.json()['uz']
        await message.answer(f'{a}', reply_markup=back_button)


    @dp.message(F.text == '🔙back🔙')
    async def back(mes: Message):
        await mes.answer('stopped', reply_markup=language)


    class uzbek_language(StatesGroup):
        choose_uzbek = State()
        finish = State()


    @dp.message(F.text == 'Uz ➡️ Eng')
    async def uzbek_english(message: Message, state: FSMContext):
        await state.set_state(uzbek_language.choose_uzbek)
        await message.answer('enter uzbek words or sentence!!')


    @dp.message(uzbek_language.choose_uzbek)
    async def finishs(message: Message, state: FSMContext):
        await state.update_data(choose_uzbek=message.text)
        await state.set_state(uzbek_language.finish)
        datas = await state.get_data()
        await state.clear()
        names = datas.get('choose_uzbek', 'hech')
        en = f'http://127.0.0.1:8000/uz_en/{names}'
        resps = get(en)
        aa = resps.json()['en']
        await message.answer(f'{aa}', reply_markup=back_button)


    break


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
