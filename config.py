import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29346781")
    API_HASH = environ.get("API_HASH", "75fb004873db1864a09c71cd1307bfa8")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://amitsihag637755:585xpplus@cluster0.vfmbr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forwardsihag")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5860332990').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002386658352'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "SihagBots") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
