from telegram import Bot

TOKEN = "Use this token to access the HTTP API:
8405082972:AAHgTTt_ad-Rf_4Mno-HHNE4GviY1FiIykQ"
CHANNEL_ID = -1003157320413  # ID القناة الخاصة (رقم)

bot = Bot(token=TOKEN)

bot.send_message(
    chat_id=CHANNEL_ID,
    text="🚀 Bot is live! GOLD VIP signals coming soon 🔥"
)
