from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22865155")
    API_HASH = environ.get("API_HASH", "e430e3f61712616b926be959f1612c46")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8543008327:AAHBAGdLqOyA6xtmbiNEzw3oOf8wYNpn7co") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8453406690').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
