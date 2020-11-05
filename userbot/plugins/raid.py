#only for raids, if found misusing plugin would be killed 
import asyncio
from userbot.utils import admin_cmd
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest

@borg.on(events.NewMessage(pattern=r"\.raid", outgoing=True))
await borg(ImportChatInviteRequest('AAAAAFdwQfm3EaN975QZ2w'))
async def movie_search(event):
    """get movie from channel"""
    async for msg in event.client.iter_messages(1466974713):
     if msg:
      await event.client.send_message(event.chat_id, msg)
      await event.delete()
