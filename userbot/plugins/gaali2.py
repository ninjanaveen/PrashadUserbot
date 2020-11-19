from telethon.tl.types import ChannelParticipantsAdmins
from userbot.util import admin_cmd


@borg.on(admin_cmd(pattern="gaali2"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "आज तेरी माँ के भोसड़े में 786 बोफोर्स तोंपो की सलामी दुंगा। उसके बाद उस रंडी के भोसड़े के परखच्चे ऐसे उड़ जाएंगे कि उस फटे भोसड़े पे चंडीगढ़ एयरपोर्ट का शिलान्यास करूँगा। तेरी माँ के भोसड़े से ले के बोबों तक हवाई पट्टी बनाकर उसपर भारतीय वायुसेना में मिराज-17 बमवर्षक विम्मान लैंड करवाऊंगा मादरचोद वेस्या पुत्र 😂😂😂  !"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
