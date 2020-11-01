
import requests

from pearl.utils import pearl_on_cmd


@pearl.on(pearl_on_cmd("ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "[{}]({})\n`Click on this you crap  🙃` ".format(input_str, response_api.rstrip())
        )
    else:
        await event.edit(" Strange!!..I Dind't found anything...")
