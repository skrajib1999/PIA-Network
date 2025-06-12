import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, ContextTypes,
    CommandHandler, CallbackQueryHandler
)
import requests
from datetime import datetime, timedelta

from app.core.config import settings

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Constants
API_BASE_URL = settings.API_URL  # e.g. "https://your-api.com"
MINING_INTERVAL_HOURS = 12


# --- /start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_id = user.id
    ref_code = context.args[0] if context.args else None

    # Register user via backend API
    payload = {"telegram_id": telegram_id, "ref_code": ref_code}
    try:
        response = requests.post(f"{API_BASE_URL}/bot/register", json=payload)
        data = response.json()
    except Exception as e:
        await update.message.reply_text("❌ Failed to connect to server.")
        return

    # Send welcome message
    kb = [
        [InlineKeyboardButton("🚀 Mine Now", callback_data="mine")],
        [InlineKeyboardButton("💰 Balance", callback_data="balance")],
        [InlineKeyboardButton("🎯 Refer", callback_data="refer")],
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")],
    ]
    await update.message.reply_text(
        f"👋 Welcome {user.first_name or 'miner'}!\nStart mining and earn tokens every {MINING_INTERVAL_HOURS} hours.",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# --- Mining Callback ---
async def handle_mine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    try:
        res = requests.post(f"{API_BASE_URL}/mining/mine", headers={"X-Telegram-ID": str(user_id)})
        data = res.json()
    except Exception as e:
        await query.edit_message_text("⚠️ Server error. Please try later.")
        return

    if res.status_code != 200:
        await query.edit_message_text(f"⛏️ {data.get('detail', 'Error occurred')}")
    else:
        await query.edit_message_text(f"✅ Mining Successful!\n💸 You earned {data['reward']} coins.")


# --- Balance Callback ---
async def handle_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    try:
        res = requests.get(f"{API_BASE_URL}/user/balance", headers={"X-Telegram-ID": str(user_id)})
        data = res.json()
    except Exception:
        await query.edit_message_text("❌ Failed to fetch balance.")
        return

    await query.edit_message_text(f"💰 Your current balance: {data.get('balance', 0)} coins")


# --- Referral Callback ---
async def handle_refer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    ref_link = f"https://t.me/{settings.BOT_USERNAME}?start={user_id}"
    await query.edit_message_text(f"🔗 Your referral link:\n{ref_link}")


# --- Leaderboard Callback ---
async def handle_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        res = requests.get(f"{API_BASE_URL}/leaderboard")
        data = res.json()
    except:
        await query.edit_message_text("❌ Couldn't fetch leaderboard.")
        return

    text = "🏆 Top Miners:\n"
    for i, user in enumerate(data[:10], 1):
        text += f"{i}. {user['username']} - {user['balance']}💰\n"

    await query.edit_message_text(text)


# --- Main Bot Launcher ---
def launch_bot():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_mine, pattern="mine"))
    app.add_handler(CallbackQueryHandler(handle_balance, pattern="balance"))
    app.add_handler(CallbackQueryHandler(handle_refer, pattern="refer"))
    app.add_handler(CallbackQueryHandler(handle_leaderboard, pattern="leaderboard"))

    logging.info("🤖 Telegram Bot Running...")
    app.run_polling()
