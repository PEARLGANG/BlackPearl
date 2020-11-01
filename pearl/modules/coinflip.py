"""Syntax: .coinflip [optional_choice]"""
import random

from uniborg.util import pearl_on_cmd


@pearl.on(pearl_on_cmd(pattern="coin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "Heads":
            await event.edit("The coin landed on: **Heads**. \n K You Win .")
        elif input_str == "Tails":
            await event.edit(
                "The coin landed on: **Heads**. \n Sed Laife, You weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Heads**.")
    elif r % 2 == 0:
        if input_str == "Tails":
            await event.edit("The coin landed on: **Tails**. \n K You Win.")
        elif input_str == "Heads":
            await event.edit(
                "The coin landed on: **Tails**. \n Sed Laife, You weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Tails**.")
    else:
        await event.edit("¯\_(ツ)_/¯")
