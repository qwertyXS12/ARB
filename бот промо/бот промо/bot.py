import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile

TOKEN = os.getenv("BOT_TOKEN")
if TOKEN is None:
    raise ValueError("❗ Переменная окружения BOT_TOKEN не найдена.")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎁 Промокоды")],
        [KeyboardButton(text="🔗 Актуальная ссылка на 1win")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот с промокодами и актуальными ссылками на 1win.\n"
        "Выберите действие:",
        reply_markup=main_keyboard
    )

@dp.message(lambda message: message.text == "🎁 Промокоды")
async def send_promocodes(message: types.Message):
    text = (
        "🎯 *Актуальная ссылка 1win:*\n"
        "https://r1wxdpc.life/casino/list?open=register&p=x0fg\n\n"
        "📜 *Список промокодов:*\n"
        "• `1win2026win`\n"
        "• `1win5004win`\n"
        "• `WIN1WIN21`\n"
        "• `Bigwwin1`\n"
        "• `stars202611`\n"
        "• `HSKC50KKW`\n"
        "• `HSKC34KKW`\n\n"
        "🎁 *Бонусы новым игрокам по ссылке + промокоду:*\n"
        "➕ +500% на первые 4 депозита\n"
        "⚡ Бонус на экспресс\n"
        "💰 Кэшбэк до 30% (слоты)\n"
        "🎰 70 фриспинов за первый депозит"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(lambda message: message.text == "🔗 Актуальная ссылка на 1win")
async def send_actual_links(message: types.Message):
    links_text = (
        "🔗 *Актуальные ссылки на 1win:*\n"
        "1️⃣ https://r1wxdpc.life/casino/list?open=register&p=x0fg\n"
        "2️⃣ https://r1wabgx.life/casino/list?open=register&p=7k6q"
    )
    await message.answer(links_text, parse_mode="Markdown")

    # --- ФИКС: правильное имя файла (без пробелов и скобок) ---
    photo_path = "qr.png"
    # Доп. отладка: напечатаем в лог путь и проверим существование
    logging.info(f"Ищем файл: {photo_path}, текущая папка: {os.getcwd()}, файлы в папке: {os.listdir('.')}")
    
    if os.path.exists(photo_path):
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo, caption="📱 QR-код для быстрого перехода")
    else:
        await message.answer("⚠️ Фото с QR-кодом не найдено. Убедитесь, что файл 'qr.png' лежит в папке с ботом.")

async def main():
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())