from helper.utils import progress_for_pyrogram, convert
from pyrogram import Client, filters
from pyrogram.types import (  InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import find
import os 
import humanize
from PIL import Image
import time

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
           await update.message.delete()
	except:
           return
@Client.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("<b>💌 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙽𝙴𝚆 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴 💌</b>",	
	reply_to_message_id=update.message.reply_to_message.id,  
	reply_markup=ForceReply(True))
	
@Client.on_callback_query(filters.regex("upload"))
async def doc(bot,update):
     type = update.data.split('_')[1]
     new_name = update.message.text
     new_filename = new_name.split(":-")[1]
     if not "." in new_filename:
         new_filename = new_filename + ".mkv"
     else:
         new_filename = new_filename + ".mkv"
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("<b>📥 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 📥</b>")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "<b>📥 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 📥</b>",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return 
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
     except:
        pass
     user_id = int(update.message.chat.id) 
     ph_path = None
     data = find(user_id) 
     media = getattr(file, file.media.value)
     c_caption = data[1] 
     c_thumb = data[0]
     if c_caption:
         caption = c_caption.format(filename=new_filename, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
     else:
         caption = f"**{new_name}**"
     if (media.thumbs or c_thumb):
         if c_thumb:
            ph_path = await bot.download_media(c_thumb) 
         else:
            ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")
     await ms.edit("<b>📤 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳 📤</b>")
     c_time = time.time() 
     try:
        if type == "document":
           await bot.send_document(
		    update.message.chat.id,
                    document=file_path,
                    thumb=ph_path, 
                    caption=caption, 
                    progress=progress_for_pyrogram,
                    progress_args=( "<b>📤 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳 📤</b>",  ms, c_time   ))
        elif type == "video": 
            await bot.send_video(
		    update.message.chat.id,
		    video=file_path,
		    caption=caption,
		    thumb=ph_path,
		    duration=duration,
		    progress=progress_for_pyrogram,
		    progress_args=( "<b>📤 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳 📤</b>",  ms, c_time))
        elif type == "audio": 
            await bot.send_audio(
		    update.message.chat.id,
		    audio=file_path,
		    caption=caption,
		    thumb=ph_path,
		    duration=duration,
		    progress=progress_for_pyrogram,
		    progress_args=( "<b>📤 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳 📤</b>",  ms, c_time   )) 
     except Exception as e: 
         await ms.edit(e) 
         os.remove(file_path)
         if ph_path:
           os.remove(ph_path)
     await ms.delete() 
     os.remove(file_path) 
     if ph_path:
        os.remove(ph_path) 
