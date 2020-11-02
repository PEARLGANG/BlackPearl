"""
Syntax : .gps <location name>
"""


from geopy.geocoders import Nominatim
from telethon.tl import types

from pearl.utils import pearl_on_cmd, edit_or_reply, sudo_cmd


@pearl.on(pearl_on_cmd(pattern="gps ?(.*)"))
@pearl.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    pearlislub = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await pearlislub.edit("what should i find give me location.")

    await pearlislub.edit("finding")

    geolocator = Nominatim(user_agent="BlackPearl")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await pearlislub.edit("i coudn't find it")
