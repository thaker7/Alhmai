import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()




BOT_TOKEN = getenv("BOT_TOKEN")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Almortagel")

OWNER_ID = list(
  map(int, getenv("OWNER_ID", "").split())) + [5089553588]
USER_OWNER = getenv("USER_OWNER","Almortagel_12") 
