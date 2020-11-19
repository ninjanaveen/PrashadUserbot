from telethon import events
import io
from userbot.utils import admin_cmd
import asyncio

@borg.on(admin_cmd(pattern="mkc (.*)"))
async def monu(mkc):
 name = mkc.pattern_match.group(1)
 A = (f"{name} madharchod h uski maa ki choot uski maa ko ulta taang ke pelangai tab usko pata chalega.\n\n"
     "\n"
     f"{name} ki maa ka bhosra\n\n"
     "Sale randi ke aulad\n\n"
     f"{name} Madharjatt \n\n"
     "Tere khandan ko kutta chode \n\n"
     f"Randi Jatt {name} ki MKC \n\n")
 await mkc.edit(A)
