from os import environ 

class Config:
    API_ID = environ.get("API_ID", "228....")
    API_HASH = environ.get("API_HASH", "e430e3f61712616...")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8543008327:AAHBAGdLqOyA6xOf8wYNpn7co") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srer0.o9mn6hb.mongodb.net/?")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '06690').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
