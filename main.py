from pyrogram import Client, filters

api_id = 27161064
api_hash = "cd938033ba1289337b03297075a9e135"
bot_token = "8183222598:AAGqEVdNUMp4gqpHxpHmfhzM-lXDuogDbfw"
app = Client("video_enhancer_bot", api_id=27161064, api_hash=cd938033ba1289337b03297075a9e135, bot_token=8183222598:AAGqEVdNUMp4gqpHxpHmfhzM-lXDuogDbfw)
from pyrogram import Client, filters

# /start command
@Client.on_message(filters.command("start"))
def start_handler(client, message):
    message.reply_text("👋 Hey! Send me a video and I’ll enhance it for you.")

# /enhancevideo command
@Client.on_message(filters.command("enhancevideo"))
def enhancevideo_handler(client, message):
    message.reply_text("📤 Please upload the video you'd like to enhance.")

# /help command
@Client.on_message(filters.command("help"))
def help_handler(client, message):
    message.reply_text(
        "/start - Start the bot\n"
        "/enhancevideo - Upload a video\n"
        "/help - Show help info"
    )
    app.run()
