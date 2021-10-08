from pywhatkit import text_to_handwriting
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor




bot = Bot(token='There goes token')
dp = Dispatcher(bot)





@dp.message_handler()
async def ascii_art_func(message : types.Message):
    user_id = message.from_user.id
    text_to_handwriting(message.text)
    await bot.send_photo(user_id, photo=open('pywhatkit.png', 'rb'))
    
    
    
    executor.start_polling(dp, skip_updates=True)
