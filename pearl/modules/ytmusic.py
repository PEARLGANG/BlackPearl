from youtubesearchpython import SearchVideos
from pytube import YouTube
import os
import wget
from pearl.Configs import Config
import asyncio
from pearl.utils import sudo_cmd, pearl_on_cmd, edit_or_reply

@pearl.on(pearl_on_cmd(pattern="sg ?(.*)"))
@pearl.on(sudo_cmd(pattern="sg ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_pearl = await edit_or_reply(event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`")
    search = SearchVideos(f"{urlissed}", offset = 1, mode = "dict", max_results = 1)
    mi = search.result()
    mio = mi['search_result']
    mo = mio[0]['link']
    thum = mio[0]['title']
    Pearl = mio[0]['id']
    thums = mio[0]['channel']
    kekme = f"https://img.youtube.com/vi/{BlackPearl}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir('./music/'):
        os.makedirs('./music/')
    path = Config.TMP_DOWNLOAD_DIRECTORY
    sedlyf = wget.download(kekme, out = path)
    pearl = (f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k ' + mo)
    os.system(pearl)
    await asyncio.sleep(4)
    km = f"./music/{thum}.mp3"
    if os.path.exists(km):
        await myself_pearl.edit("`Song Downloaded Sucessfully. Let Me Upload it Here.`")
    else:
        await myself_pearl.edit("`SomeThing Went Wrong. Try Again After Sometime..`")
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`" 
    await borg.send_file(event.chat_id,
                km,
                force_document=False,
                allow_cache=False,
                caption=capy,
                thumb=sedlyf,
                performer=thums,
                supports_streaming=True) 
    await myself_pearl.edit("`Song Uploaded. By (C) @pearlsupport`")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)
