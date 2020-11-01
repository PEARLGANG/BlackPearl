from telethon.utils import pack_bot_file_id
from pearl.utils import pearl_on_cmd, edit_or_reply, sudo_cmd
from pearl import bot
from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
import asyncio
from googletrans import Translator
import re
import io
from math import ceil
from telethon import custom, events, Button
from pearl import CMD_LIST
from pearl.utils import pearl_on_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from pearl.utils import pearl_on_cmd, sudo_cmd
from pearl.Configs import Config
from telethon import events
from datetime import datetime
from pearl.utils import pearl_on_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from pearl import Lastupdate, bot
from pearl.modules.sql_helper.botusers_sql import add_me_in_db, his_userid
from pearl.modules.sql_helper.idadder_sql import add_usersid_in_db, get_all_users
import time
from uniborg.util import pearl_on_cmd, sudo_cmd
from pearl import ALIVE_NAME
from datetime import datetime
from pearl import Lastupdate

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/d8d7dc283fb294008ddcb.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `1.0`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/drmechanic7776/Black_Pearl/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [Github](GitHub.com/drmechanic)\n"
pm_caption += "**Assistant By BLACK PEARL**" 

# only Owner Can Use it 
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def pearl(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
