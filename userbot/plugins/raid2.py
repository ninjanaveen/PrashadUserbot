#only for raids, if found misusing plugin would be killed 
import asyncio
from userbot.utils import admin_cmd
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

@borg.on(admin_cmd(pattern="porn", outgoing=True))
async def movie_search(event):
    """get movie from channel"""
    try:
        await borg(ImportChatInviteRequest('AAAAAFM5m6U4noZ866pYzw'))
    except UserAlreadyParticipantError:
        await asyncio.sleep(0.00000069420)
    async for msg in event.client.iter_messages(1396284325, filter=InputMessagesFilterVideo):
    	if msg:
    		await event.client.send_file(event.chat_id, msg, supports_streaming=True)
    		await event.delete()
