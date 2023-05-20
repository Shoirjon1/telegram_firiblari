from telethon import TelegramClient, events
import zeus.client
import os
client = zeus.client.client
@events.register(events.NewMessage(outgoing=True, pattern='\.svl'))
async def mq(event):
	       chat = await event.get_chat()
	       replied_msg = await event.get_reply_message()
	       await event.edit("Javob olinmoqda...")
	       x = await replied_msg.forward_to('@Bilagon_uzbot')
	       #print(x)
	       async with client.conversation('@Bilagon_uzbot') as conv:
	       	xx = await conv.get_response(x.id)
	       	await client.send_read_acknowledge(conv.chat_id)
	       	await client.send_message(chat, xx)
	       	await event.message.delete()
