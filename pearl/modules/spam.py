import asyncio, os
from asyncio import wait, sleep
from pearl import BOTLOG, BOTLOG_CHATID, CMD_HELP
from pearl.utils import pearl_on_cmd


@pearl.on(pearl_on_cmd(pattern=f"(?:scam|ssc)\s(.*)"))
async def scam(rider):
    if not rider.is_private:
              chat = await rider.get_chat() ; admin = chat.admin_rights ; creator = chat.creator
              if not admin and not creator and chat.id == -1001191765261:
                     	return
    try:
       await rider.delete()
    except:
    	pass
    options = ('typing', 'game' , 'voice', 'round', 'video' , 'photo', 'document')
    input_str = rider.pattern_match.group(1)
    args = input_str.split()  
    if len(args) == 2:  
        scam_action = str(args[1]).lower()
        if not scam_action in options:
           return await rider.reply(f"Failed \n\n •**Error:** Invalid Action\n\n You can use one of this \n{options}")
        try:
            scam_time = int(args[0])
        except:      
             return await rider.reply("Failed \n\n •**Error:** Invalid Time.....")
    else:
        return await rider.reply(f"**Error**\nusage `.scam <time in seconds> <action>`")
    try:
        if (scam_time > 0):            
            async with rider.client.action(e.chat_id, scam_action):
                await sleep(scam_time)
    except Exception as rider:      
        return await rider.reply(f"**Error**\nusage `.scam <time in seconds> <action>`")


@pearl.on(pearl_on_cmd(pattern=f"(?:rspam|rsp)\s(.*)"))
async def repeat(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    cnt, txt = rider.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt
    replyText = toBeRepeated + "\n"
    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"
    await rider.reply(replyText)
  except:      
        return await rider.reply(f"**Error**\nusage `. repeatspam <count> <text>`")


@pearl.on(pearl_on_cmd(pattern=f"(?:cspam|csp)\s(.*)"))
async def tmeme(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    cspam = str(rider.pattern_match.group(1))
    message = cspam.replace(" ", "")
    for letter in message:
        await rider.respond(letter)
  except:      
        return await rider.reply(f"**Error**\nusage `.cspam <text>`")

@pearl.on(pearl_on_cmd(pattern=f"(?:wspam|wsp)\s(.*)"))
async def tmeme(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    for word in message:
        await rider.respond(word)
  except:      
        return await rider.reply(f"**Error**\nusage `.wspam  <text> <text> <text>`")

@pearl.on(pearl_on_cmd(pattern=f"(?:spam|sp)\s(.*)"))
async def spammer(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    counter = int(rider.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(rider.pattern_match.group(1).split(' ', 1)[1])
    await asyncio.wait([rider.respond(spam_message) for i in range(counter)])
  except:      
        return await e.reply(f"**Error**\nusage `.spam <time in seconds> <text>`")

@pearl.on(pearl_on_cmd(pattern=f"(?:mspam|msp)\s(.*)"))
async def tiny_pic_spam(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    counter = int(rider.pattern_match.group(1).split(' ', 1)[0])
    reply_message = await rider.get_reply_message() 
    if not reply_message or not rider.reply_to_msg_id or not reply_message.media or not reply_message.media:
       return await rider.edit("```Reply to a media message```")
    message = reply_message.media
    for i in range(1, counter):
        await rider.client.send_file(e.chat_id, message)
  except:      
        return await rider.reply(f"**Error**\nusage `.dspam <count> reply to a media/photo/video`")

@pearl.on(pearl_on_cmd(pattern=f"(?:dmspam|dmsp)\s(.*)"))
async def tiny_pic_spam(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    spamDelay = float(rider.pattern_match.group(1).split(' ', 2)[0])
    counter = int(rider.pattern_match.group(1).split(' ', 2)[1])
    reply_message = await rider.get_reply_message() 
    if not reply_message or not rider.reply_to_msg_id or not reply_message.media or not reply_message.media:
       return await rider.edit("```Reply to a media message```")
    message = reply_message.media
    for i in range(1, counter):
        await rider.client.send_file(rider.chat_id, message)
        await sleep(spamDelay)
  except:      
        return await rider.reply(f"**Error**\nusage `.ddspam <time in seconds> <count> reply to a media/photo/video`")

@pearl.on(pearl_on_cmd(pattern=f"(?:delayspam|dsp)\s(.*)"))
async def spammer(rider):
  sender = await rider.get_sender() ; me = await rider.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await rider.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await rider.delete()
  except:
    	pass
  try:
    spamDelay = float(rider.pattern_match.group(1).split(' ', 2)[0])
    counter = int(rider.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(rider.pattern_match.group(1).split(' ', 2)[2])
    for i in range(1, counter):
        await rider.respond(spam_message)
        await sleep(spamDelay)
  except:      
        return await rider.reply(f"**Error**\nusage `.dealyspam <time in seconds> <count> <text>`")


CMD_HELP.update({
    "spam":
    "⚠️ Spam at your own risk !!\
\n\n`.spam/.sp` <count> <text>\
\n**Usage:**  Floods text in the chat !!\
\n\n`.scam/.sc` <time in seconds> <action>\
\n**Usage:**  Scam by fake actions like typing, sending photo......!!\
\n\n`.cspam/.csp` <text>\
\n**Usage:**  Spam the text letter by letter.\
\n\n`.rspam/.rsp` <count> <text>\
\n**Usage:**  Repeats the text for a number of times.\
\n\n`.wspam/.wsp` <text>\
\n**Usage:**  Spam the text word by word.\
\n\n`.mspam/.msp` <count> <reply to a media message>\
\n**Usage:**  As if text spam was not enough !!\
\n\n`.delayspam/.dsp` <delay> <count> <text>\
\n**Usage:**  spam with custom delay.\
\n\n`.dmspam/.dmsp` <delay> <count> <reply to a media message>\
\n**Usage:**  mspam with custom delay.\
\n\n**Spam_protect**\
\n**Usage:**  Protect your groups from scammers.\
\nFor on `.set var SPAM_PROTECT True` , for off `.del var SPAM_PROTECT`\
\n You need to set up api key for that\
\n More information click [here](https://t.me/pearlsupport)\
\n\n**All commands support sudo , type .help sudo for more info**\
"
})
