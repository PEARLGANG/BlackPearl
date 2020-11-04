from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from pearl.utils import command, load_module
from var import Var


@command(pattern="^.extdl", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    chat = Var.PLUGIN_CHANNEL
    documentss = await borg.get_messages(chat, None, filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    await event.delete()
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await borg.get_messages(chat, ids=mxo), "pearl/modules/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            await borg.send_message(
                event.chat_id,
                "Black Pearl Has Safely Installed Plugin `{}`.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )
        else:
            await borg.send_message(
                event.chat_id,
                "Looks Like Some Dumbass Asshole Has Tried To Reinstall The existing Plugins: `{}` .".format(
                    os.path.basename(downloaded_file_name)
                ),
            )
