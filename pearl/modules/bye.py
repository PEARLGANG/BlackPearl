

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from pearl.utils import pearl_on_cmd, edit_or_reply, sudo_cmd
from pearl import CMD_HELP

@pearl.on(pearl_on_cmd("bye", outgoing=True))
@pearl.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    pearlgang = await edit_or_reply(e, "Bye Kek")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await pearlgang.edit("`Fuck This I'm Out.....!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await pearlgang.edit("`You Think This Is A Chat?... Then Fuck You Its Not!!`")

CMD_HELP.update({"bye": ".bye\nUsage - Leave the group."})            
