import json
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import datetime
import time
from pearl.utils import pearl_on_cmd, sudo_cmd
from pearl.events import register 
from pearl import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
import glob
import os
from pearl.utils import progress, humanbytes
from youtubesearchpython import SearchVideos
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
try:
 import instantmusic , subprocess
except:
 os.system("pip install instantmusic")
 


os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    


@pearl.on(pearl_on_cmd(pattern="netease ?(.*)"))
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await netase.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.reply("```Please unblock @WooMaiBot and try again```")
              return
          await netase.edit("`Sending Your Music...`")
          await asyncio.sleep(3)
          await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await netase.delete()


@pearl.on(pearl_on_cmd(pattern=f"song2(?: |$)(.*)"))
async def vkm(vkmusic):
  sender = await vkmusic.get_sender() ; me = await vkmusic.client.get_me()
  if not sender.id == me.id:
        cyber = await vkmusic.reply("`processing...`")
  else:
    	cyber = await vkmusic.edit("`processing...`")    
  try:
    reply_message = vkmusic.pattern_match.group(1)
    if not reply_message:
       reply_message = await vkmusic.get_reply_message() 
       if reply_message:
           if reply_message.media:
       	    return await cyber.edit("`Reply to a text message`")
    if not reply_message:
          return await cyber.edit("`Error\n**Usage** song2 <song> or reply to a message`")
    chat = "@vkmusic_bot"   
    async with vkmusic.client.conversation(chat, timeout=7) as conv:
          try:                   
              await conv.send_message(reply_message)
              response = await conv.get_response()
          except YouBlockedUserError: 
              await cyber.edit("`Please unblock @iLyricsBot and try again`")
              return
          try:
           await response.click(1, 1) 
          except:
             return await cyber.edit(f"`Failed to find {reply_message}`")    
          test = await conv.get_response()
          await cyber.delete()
          await vkmusic.client.send_file(vkmusic.chat_id, test, caption=f"`{reply_message} song`", reply_to=vkmusic.message.reply_to_msg_id)          
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await cyber.edit(f"**Error**\n\n{error}")

@pearl.on(pearl_on_cmd(pattern=f"song (.*)"))
async def download_video(v_url):  
    hell = v_url ; sender = await hell.get_sender() ; me = await hell.client.get_me()
    if not sender.id == me.id:
        cyber = await hell.reply("`processing...`")
    else:
    	cyber = await hell.edit("`processing...`")
    url = v_url.pattern_match.group(1)	
    if not url:
         return await cyber.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await cyber.edit("`failed to find`")
    type = "audio"
    await cyber.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True    
    try:
        await cyber.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await cyber.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await cyber.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await cyber.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await cyber.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await cyber.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await cyber.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await cyber.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await cyber.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await cyber.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await cyber.edit(f"`Preparing to upload song:`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await cyber.edit(f"`Preparing to upload song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=url,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await cyber.delete()
          
              
@pearl.on(pearl_on_cmd(pattern=f"vsong (.*)"))
async def download_video(v_url):  
    heaven = v_url ; sender = await heaven.get_sender() ; me = await heaven.client.get_me()
    if not sender.id == me.id:
        rider = await heaven.reply("`processing...`")
    else:
    	rider = await heaven.edit("`processing...`")   
    url = v_url.pattern_match.group(1)
    if not url:
         return await rider.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await rider.edit("`failed to find`")
    type = "audio"
    await rider.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True
    try:
        await rider.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rider.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rider.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rider.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rider.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rider.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rider.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rider.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rider.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rider.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await rider.edit(f"`Preparing to upload song `\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rider.edit(f"`Preparing to upload video song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=rip_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await rider.delete()
