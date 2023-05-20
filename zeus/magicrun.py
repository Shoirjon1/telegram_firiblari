from telethon import TelegramClient, events
import sh.client
from sh.magic import Magic
import time
magic = Magic()
client = sh.client.client
@events.register(events.NewMessage)
async def magicrun(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)