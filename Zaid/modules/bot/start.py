from Lovely import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("Hey Lovely Userbot Assistant here")
