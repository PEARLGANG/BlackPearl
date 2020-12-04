"""Check if Black Pearl alive. If you change these, you become the Badass NuB such that even the BoT world will disown you."""
import time
from uniborg.util import pearl_on_cmd, sudo_cmd
from pearl import ALIVE_NAME
from pearl.Configs import Config
from datetime import datetime
from pearl import Lastupdate
from pearl import CMD_HELP

#Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "➢ **BLACK PEARL IS:** SAILING\n\n"
pm_caption += "✪༺ ──•◈•───•◈•──༻✪\n"
pm_caption += "➢ **SYSTEMS STATS**\n"
pm_caption += "➢ **Telethon Version:** `1.15.0` \n"
pm_caption += "➢ **Python:** `3.7.4` \n"
pm_caption += f"➢ **Uptime** : `{uptime}` \n"
pm_caption += "➢ **Database Status:**  `Functional`\n"
pm_caption += "➢ **Current Branch** : `master`\n"
pm_caption += f"➢ **Version** : `1.0`\n"
pm_caption += f"➢ **My Captian** : {DEFAULTUSER} \n"
pm_caption += "➢ **Heroku Database** : `AWS - WORKS LIKE A CHARM`\n"
pm_caption += "➢ **License** : [GNU General Public License v3.0](github.com/PEARLGANG/BlackPearl/blob/main/LICENSE)\n"
pm_caption += "➢ **Copyright** : By [Github](GitHub.com/PEARLGANG)\n"
pm_caption += "➢ **Check Stats By Doing** `.stat`. \n"
pm_caption += "✪༺ ──•◈•───•◈•──༻✪\n\n"
pm_caption += "➢ **[Deploy Black Pearl](https://heroku.com/deploy?template=https://github.com/PEARLGANG/BlackPearl)** \n"


@pearl.on(pearl_on_cmd(pattern=r"alive"))
@pearl.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def pearl(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if Black Pearl is Alive"
    }
)    
