import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Bot Configuration
BOT_TOKEN = "8027556019:AAHym61NRjiSZLD_4Y6-AhWWhEQP_NlxSg8"
CHANNEL_LINK = "https://t.me/yourchannel"  # Replace with your channel link
GROUP_LINK = "https://t.me/yourgroup"      # Replace with your group link
TWITTER_LINK = "https://twitter.com/yourtwitter"  # Replace with your Twitter

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with participation instructions"""
    user = update.effective_user
    welcome_msg = f"""
🌟 *Welcome {user.first_name}!* 🌟

🚀 *Solana Airdrop Bot* 🚀

Complete these simple steps to qualify for 10 SOL:

1️⃣ Join our Telegram Channel
2️⃣ Join our Telegram Group
3️⃣ Follow our Twitter
4️⃣ Submit your Solana Wallet

*This is a TEST bot - no real SOL will be sent*
"""
    
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("👥 Join Group", url=GROUP_LINK)],
        [InlineKeyboardButton("🐦 Follow Twitter", url=TWITTER_LINK)],
        [InlineKeyboardButton("✅ Done All Steps", callback_data="completed")]
    ]
    
    await update.message.reply_text(
        welcome_msg,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "completed":
        await query.edit_message_text(
            "🎉 Great! Now send me your Solana wallet address:\n\n"
            "Example: `D8w6YjXz7hW5J6Z1XvL9eRtTnJkKmL3PqH2bN4sVfG7h`\n\n"
            "*Remember:* This is just a test - no real SOL will be sent!",
            parse_mode="Markdown"
        )

async def handle_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Process wallet address submission"""
    wallet = update.message.text.strip()
    response = f"""
💰 *Airdrop Successful!* 💰

10 SOL has been sent to:
`{wallet}`

🔗 TX Hash: `5n9JKc3VXvU7Rj8Kq2WbN1mL4pXz6T8Y`

⏳ *Note:* This is a test transaction. No actual SOL was sent.
"""
    await update.message.reply_text(response, parse_mode="Markdown")

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    # Start polling
    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
