import asyncio 
import logging 
from aiogram import Bot, Dispatcher, F, types  
from aiogram.filters.command import Command
from config_reader import config  
from kurs import perevod,  procent
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
    await message.answer("Добро пожаловать в N-бота, он поможет вам узнать акутальные курсы валют")  
    await message.answer("Вы можете написать название валюты самостоятельно или воспользоваться командой /fast, чтобы выбрать из списка самых популярных валют")  
    

@dp.message(Command("fast"))
async def cmd_fast(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="usd",
        callback_data="usd_fast"
    ))
    builder.add(types.InlineKeyboardButton(
        text="euro",
        callback_data="euro_fast"
    ))
    builder.add(types.InlineKeyboardButton(
        text="bitcoin",
        callback_data="bitcoin_fast"
    ))
    builder.add(types.InlineKeyboardButton(
        text="ton",
        callback_data="ton_fast"
    ))
    await message.answer(
        "курс какой валюты вы хотите узнать ",
        reply_markup=builder.as_markup()
    
    )

@dp.callback_query(F.data == "usd_fast")
async def usd(callback: types.CallbackQuery):
    await callback.message.answer(perevod("usd"))
    await callback.message.answer(procent("usd"))

@dp.callback_query(F.data == "euro_fast")
async def euro(callback: types.CallbackQuery):
    await callback.message.answer(perevod("euro"))
    await callback.message.answer(procent("euro"))

@dp.callback_query(F.data == "bitcoin_fast")
async def btc(callback: types.CallbackQuery):
    await callback.message.answer(perevod("bitcoin"))
    await callback.message.answer(procent("bitcoin"))

@dp.callback_query(F.data == "ton_fast")
async def ton(callback: types.CallbackQuery):
    await callback.message.answer(perevod("toncoin"))
    await callback.message.answer(procent("toncoin"))

@dp.message(F.text) 
async def any_message(message: types.Message): 
        await message.answer(perevod(message.text))
        if (perevod(message.text) != "попробуйте написать по другому"):
            await message.answer(procent(message.text))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
