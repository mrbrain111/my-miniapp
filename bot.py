import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor

# Токен, который ты получил от BotFather
TOKEN = "7588071415:AAGGvexsp2DZKRzbbOzfQY5w5J027Pbn24k"
# Ссылка на твой Mini App (будет в дальнейшем на GitHub Pages)
WEB_APP_URL = "https://mymini_mrbrain111.github.io/my-mini-app/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Открыть Mini App", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)
    
    await message.answer("Нажмите кнопку ниже, чтобы открыть Mini App:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
