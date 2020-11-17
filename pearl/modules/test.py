from uniborg.util import pearl_on_cmd


@pearl.on(pearl_on_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Black Pearl Is Sailing At Full Speed!")
