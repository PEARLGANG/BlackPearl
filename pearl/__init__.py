import asyncio
import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

import pylast
from dotenv import load_dotenv
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession

from var import Var

from .function import pearlfunction as topfunc

Lastupdate = time.time()

from var import Var

if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)


CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

ENV = os.environ.get("ENV", False)
""" PPE initialization. """

# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    LOGS = getLogger(__name__)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None
    )

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome For Carbon
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")

    # Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

    # Spotify Account
    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME") or None
    SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS") or None

    # Pm Permit Img
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    # PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    # Log It
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", True)
     
    CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", ""))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    
    # User Terminal alias
    USER_TERM_ALIAS = os.environ.get("USER_TERM_ALIAS") or "master"

    # Updater alias
    UPDATER_ALIAS = os.environ.get("UPDATER_ALIAS") or "BlackPearl"

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

    # Spamwatch Module
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    WHITE_CHAT = PRIVATE_GROUP_ID = int(os.environ.get("WHITE_CHAT", False))

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    else:
        lastfm = None
        
    # JustWatch Country
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY") or None
    
    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
else:
  from pearl.Configs import Config 
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None
    APP_ID = 5204354
    API_HASH = "f99ae24d5cfb143e7d548f0bcc1315a6"
    ALIVE_NAME = "RnD"
    STRING_SESSION = "1AZWarzQBu3JiuJg0xmvO35Nlr1Tq8QNLjY16vOH7YDHqmXDKstqNh1NYI0MzWQcKRqXY-WXFKde9SVxGq-kEuIpMkJgNzc-k-CXohYZeXgjVThu0NBJYb7x_J-UvpvMZQ1UZ-MNa_xTr0rBHwnWIfhRdOIRGtXNiS8O8Ae5vD880pMVP3a1s36UGQFGSnRPSftRlmY-Pup41dueTh8JPGE054Q7m-xS8TAnYN5nSVIvG_IZifyWoW6GTYkYl42lVj6GJ2L3m63WWWlKYDsePGt4vZpSNFqWTkgVbZbHVvOU9l3s2xPYgmLuAPrSHfkQHBWd33A_kfxiz-HknsmPCAI4CIhTkY-4="
    DB_URI = "postgresql://ubmfefjetnoeq8:p1399f9fae28e97210ac800eafbd472fafe40000cb2b17f441a85a0eede28cc1d@ec2-52-20-131-55.compute-1.amazonaws.com:5432/d6hsni6nds4hid"
    ENV = "ANYTHING"
    PLUGIN_CHANNEL = 1001531459997
    PRIVATE_GROUP_ID = 1001531459997
    TESSDATA_PREFIX = "./.apt/usr/share/tesseract-ocr/4.00/tessdata"
    TG_BOT_TOKEN_BF_HER = "1496391120:AAGk4fxU3KNumodTBFpsos7XFUIsX-YC_A8"
    TG_BOT_USER_NAME_BF_HER = "@Drmechanic_bot"
    TZ = "Asia/Kolkata"
    LOGGER = True
        # Get this value from my.telegram.org! Please do not steal
    LOCATION = os.environ.get("LOCATION", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        # Send .get_id in any group to fill this value.

        # This is required for the modules involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
        )
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the hash to torrent file functionality to work.
    HASH_TO_TORRENT_API = os.environ.get(
            "HASH_TO_TORRENT_API", "https://example.com/torrent/{}"
        )
        # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Black Pearl")
        # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001198699233))
        # TG API limit. An album can have atmost 10 media!
    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # Telegram BOT Token from @BotFather
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    PRIVATE_GROUP_BOT_API_ID = int(
            os.environ.get("PRIVATE_GROUP_BOT_API_ID", False)
        )
        #
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want pearl's features
    UB_BLACK_LIST_CHAT = set(
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        )
        # maximum number of messages for antiflood
    MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
        # define "spam" in PMs
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
        # send .get_id in any channel to forward all your NEW PMs to this group
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
        if PM_LOGGR_BOT_API_ID:
            PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        # For Databases
        # can be None in which case modules requiring
        # DataBase would not work
    DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .helpme command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5)
        )
        # specify command handler that should be used for the modules
        # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", "\.")
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    WHITELIST_USERS = set(
            int(x) for x in os.environ.get("WHITELIST_USERS", "").split()
        )
    BLACKLIST_USERS = set(
            int(x) for x in os.environ.get("BLACKLIST_USERS", "").split()
        )
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
        # Very Stream
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        # Google Chrome Stuff
    CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
    GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome"
        )
        # Google Drive ()
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        # MongoDB
    MONGO_URI = os.environ.get("MONGO_URI", None)
        # Lydia API
    LYDIA_API = os.environ.get("LYDIA_API", None)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", False))
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", False))
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", False))
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    TAG_FEATURE = os.environ.get("TAG_FEATURE", "DISABLE")
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/PEARLGANG/BlackPearl")
    ALIVE_IMAGE = os.environ.get("ALIVE_IMAGE", "https://telegra.ph/file/d8d7dc283fb294008ddcb.jpg")
    TESSDATA_PREFIX = os.environ.get("TESSDATA_PREFIX", "./.apt/usr/share/tesseract-ocr/4.00/tessdata")
     DB_URI = None    
# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
SUDO_LIST = {}
CMD_HELP = {}

ISAFK = False
AFKREASON = None
# End of PaperPlaneExtended Support Vars
