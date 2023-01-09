from os import getenv

API_ID = int(getenv("API_ID", "9885470")) #optional
API_HASH = getenv("API_HASH", "84ff6bdb8eeb6e8bedf8a8192e3da3dd") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5440768701").split()))
OWNER_ID = int(getenv("OWNER_ID", "5440768701"))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://AbishnoiMusic:AbishnoiMusic29@cluster0.k7sfn.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5679118460:AAGk3yW-UWgXvicdGSnANtSnS2DmoOnlnAU")
ALIVE_PIC = getenv("ALIVE_PIC","https://te.legra.ph/file/cec5a117ff959166f7b6f.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT","NehalG")
PM_LOGGER = getenv("PM_LOGGER","")
LOG_GROUP = getenv("LOG_GROUP","-1001598879298")

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
