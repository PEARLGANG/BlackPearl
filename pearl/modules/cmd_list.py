import asyncio

from pearl.utils import pearl_on_cmd
from pearl import CMD_HELP


# @command(pattern="^.cmds", outgoing=True)
@pearl.on(pearl_on_cmd(pattern=r"cmds"))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls pearl/modules"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**List of Plugins:**\n - {o}\n\n**HELP:** __All commands are can be viewed by, doing:-__ \n `.help <plugin name>` **without the < > brackets.**\n__All modules might not work directly__"
    await event.edit(OUTPUT)

CMD_HELP.update(
    {"cmd_list": ".cmds\nUsage - Get the list of all plugins in Black Pearl."}
)    
