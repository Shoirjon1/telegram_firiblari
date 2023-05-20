from telethon import TelegramClient, events
import sh.client
client = sh.client.client

@events.register(events.NewMessage(pattern=".fuck"))
async def fuck(event):
	await event.edit("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┗━┻━┻━┻┛┗━━━┛")