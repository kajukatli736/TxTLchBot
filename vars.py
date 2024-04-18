import re
import os
from os import getenv, environ




api_id = int(environ.get("api_id", "29917436"))
api_hash = environ.get("api_hash", "4a926822b076a086a167fe8f2701d3e9")
SUDO_USERS = int(environ.get("SUDO_USERS", "6141937812"))
bot_token = environ.get("bot_token", "6755014380:AAECxivro_dmP9qPIPmukG5qY6NQm-mUVk4")
OWNER_ID = int(environ.get("OWNER_ID", "6141937812"))

QRPICS = (environ.get('QRPICS', 'https://graph.org/file/b3125068739885e7109db.jpg https://graph.org/file/b3125068739885e7109db.jpg')).split()
PICS = (environ.get('PICS', 'https://graph.org/file/e96a0e77a0b9fddc5589e.jpg https://graph.org/file/7c3a74d033620ac063dbc.jpg https://graph.org/file/e96a0e77a0b9fddc5589e.jpg')).split()
START_TXT = """<b>Welcome to My Bot!</b>

/upload To use the bot and Plz Donate Some Amount /donate"""
DONATE_TXT = """<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> <code>PandaWep@ybl</code>"""
