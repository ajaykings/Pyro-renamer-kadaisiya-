"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re
import os
from pyrogram.types import Message
from pyrogram import Client ,filters
from helper.database import getid

id_pattern = re.compile(r'^.\d+$')

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("<b>🔎...𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝙰𝙻𝙻 𝙸𝙳𝚂 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴...🔎</b>")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"<b>🌟 𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃...</b> \n <b>𝚂𝙴𝙽𝙳𝙸𝙽𝙶 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝚃𝙾</b> {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="<b>𝚆𝙰𝙸𝚃....</b>")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"<b>𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂</b> = {tot}")
