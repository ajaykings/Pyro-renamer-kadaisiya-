from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
    thumb = find(int(message.chat.id))[0]
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("**𝚈𝙾𝚄 𝙳𝙾𝙽𝚃 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 🫗**") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
    delthumb(int(message.chat.id))
    await message.reply_text("**𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 🗑️**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id , file_id)
    await message.reply_text("**𝚈𝙾𝚄𝚁 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚂𝙰𝚅𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈** ✅")
	
