import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Lovely"])

async def join(client):
    try:
        await client.join_chat("NehalG143")
    except BaseException:
        pass
