# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/SaitamaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 21927988  # integer value, dont use ""
    API_HASH = "e18f720acdff1e5b0ec80616aecd8a5a"
    TOKEN = "5932946559:AAGYPp-QymQAM84EA7oXWyL3bAMJ17tGROA"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2064735436  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "plumblossomsword"
    SUPPORT_CHAT = "theoneandonlymurim"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001707656835
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001707656835
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://plumblossomsword:xdpHvXSRC8UUKPxvxFkg4ecMRWhUzOWs@dpg-cekmvaha6gdkdn0ff1t0-a.oregon-postgres.render.com/rimuru_car4"  # needed for any database modules # its "URI" and not "URL" as herok and similar ones only accept it as such
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    ALLOW_CHATS = True
    URL = None
    SIBYL_KEY = "2064735436:qqp7Dio6yh0mePDvJwUN3UGNhU7zrb_1ql_gXrNXNXBfxq68c4fPYi2cwjNhJ8_N"
    SPAMWATCH_API = "zKSTO8g_x3qmaMrU_tiTRXibTb532qbmTKXYW3RdyW8Pq0qk1oEtqddo7HqxRp~1"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "6HZ09C7DZYKWBCCE"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "4ID9HHBVU5L8"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
