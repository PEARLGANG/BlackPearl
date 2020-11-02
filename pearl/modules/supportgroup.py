"""Emoji
Available Commands:
.support
"""


import asyncio

from pearl.utils import pearl_on_cmd


@pearl.on(pearl_on_cmd("BlackPearl"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("For Our Support Group")
    animation_chars = [
        "Click Here",
        "[Support Group](https://t.me/pearlsupport)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
