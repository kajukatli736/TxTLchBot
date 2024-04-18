import re
import os
from os import getenv, environ




api_id = int(environ.get("api_id", "29502752"))
api_hash = environ.get("api_hash", "157128976a11261d2b548378fcaebcf9")
SUDO_USERS = int(environ.get("SUDO_USERS", "6945082854"))
bot_token = environ.get("bot_token", "7199644678:AAHu4CL9H6IeLS6a_8CnWMuosxxfn2HRsZ0")
OWNER_ID = int(environ.get("OWNER_ID", "6945082854"))

QRPICS = (environ.get('QRPICS', 'https://graph.org/file/b3125068739885e7109db.jpg https://graph.org/file/b3125068739885e7109db.jpg')).split()
PICS = (environ.get('PICS', 'https://graph.org/file/e5dbfe43f501618000369.jpg https://graph.org/file/e5dbfe43f501618000369.jpg https://graph.org/file/e5dbfe43f501618000369.jpg')).split()
START_TXT = """<b>Welcome to My Bot!</b>

/upload To use the bot and Plz Donate Some Amount
𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.
<code>PandaWep@ybl</code>"""
DONATE_TXT = """<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> <code>PandaWep@ybl</code>"""
