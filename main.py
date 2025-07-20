from pyrogram import Client, filters

api_id = 27161064
api_hash = "cd938033ba1289337b03297075a9e135"
bot_token = "8183222598:AAGqEVdNUMp4gqpHxpHmfhzM-lXDuogDbfw"

app = Client("video_enhancer_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hey! I'm alive and ready to enhance your videos. 🚀")

app.run()



