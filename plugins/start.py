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

from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

START_PIC = environ.get("START_PIC", "https://telegra.ph/file/27e9ed6b222498bd1c177.jpg")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢 <b>𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 </b>📢", url=client.invitelink) ]]
    text = "**😔 𝚂𝙾𝚁𝚁𝚈 𝙵𝚁𝙸𝙴𝙽𝙳 𝚈𝙾𝚄 𝚆𝙴𝚁𝙴 𝙽𝙾𝚃 𝙹𝙾𝙸𝙽𝙴𝙳 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻...𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙵𝚁𝙸𝙴𝙽𝙳 😎**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""👋 <b>𝙷𝙰𝙸</b> {message.from_user.mention} \n\n<b>𝙸 𝙰𝙼 𝙰 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻𝙻 𝚁𝙴𝙽𝙰𝙼𝙴𝚁 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 & 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚂𝚄𝙿𝙿𝙾𝚁𝚃...🧑‍💻</b>\n\n😎<b>𝙼𝚈 𝙾𝚆𝙽𝙴𝚁  :</b> <b><a href=https://t.me/ajay_king_x>♚ᴀᴊᴀʏ♚</a></b>""",
       reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", callback_data='dev')                
                ],[
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 📢', url='https://t.me/Tamil_movie_studio'),
                InlineKeyboardButton('🍿 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🍿', url='https://t.me/+nDC4f5uCcN9lZmNl')
                ],[
                InlineKeyboardButton('🍻 𝙰𝙱𝙾𝚄𝚃 🍻', callback_data='about'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿 ℹ️', callback_data='help')
                ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"""**𝚆𝙷𝙰𝚃 𝙳𝙾 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙼𝙴 𝚃𝙾 𝙳𝙾 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙵𝙸𝙻𝙴.?**\n\n**𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴** :- `{filename}`\n\n**𝙵𝙸𝙻𝙴 𝚂𝙸𝚉𝙴 :-** `{filesize}`""",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📚 𝚁𝙴𝙽𝙰𝙼𝙴 📚",callback_data = "rename")],
        [InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 <b>𝙷𝙰𝙸</b> {message.from_user.mention} \n\n<b>𝙸 𝙰𝙼 𝙰 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻𝙻 𝚁𝙴𝙽𝙰𝙼𝙴𝚁 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 & 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚂𝚄𝙿𝙿𝙾𝚁𝚃...🧑‍💻</b>\n\n😎<b>𝙼𝚈 𝙾𝚆𝙽𝙴𝚁  :</b> <b><a href=https://t.me/ajay_king_x>♚ᴀᴊᴀʏ♚</a></b>""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", callback_data='dev')                
                ],[
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 📢', url='https://t.me/Tamil_movie_studio'),
                InlineKeyboardButton('🍿 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🍿', url='https://t.me/+8LCFCFGUy_JlNDhl')
                ],[
                InlineKeyboardButton('🍻 𝙰𝙱𝙾𝚄𝚃 🍻', callback_data='about'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿 ℹ️', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴 ❣️", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴 🔒", callback_data = "close")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴 ❣️", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴 🖥️", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴 🔒", callback_data = "close")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴 ❣️", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴 🖥️", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴 🔒", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()




