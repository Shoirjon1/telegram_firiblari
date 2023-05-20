from telethon import TelegramClient, events, sync
import sh.client
client = sh.client.client
@events.register(events.NewMessage(pattern=".yordam"))
async def help(event):
	await event.edit("""

 Telegram hiylalari YORDAM MENUSI

 [01] Bombalar - Animatsiya emojisi — `.bombs`
 [02] Yordam - Yordam menyusi — `.yordam`
 [03] Loading - Yuklash Animatsiyasi — `.loading`
 [04] Emoji - Emoji matn muharriri - `.emoji `<bu yerda matn>
 [05] Dump - Candy dump animate - `.dump`
 [06] Yashirilgan
 [07] Typer - Animatsiya matnini yozish - `.type `<bu yerda matn>
 [08] Lul - animatsiya lul - `.lul`
 [09] Snake - Snake animatsiyasi - `.snake`
 [10] Nothappy - Abimation Nothappy - `.nothappy`
 [11] Soat - animatsion soat - `.clock`
 [12] Muah - animatsiya - `.muah`
 [13] Yurak - animatsiya - `.heart`
 [14] Sport zali - animatsion gimnastika - `.gym`
 [15] Yer - animatsion globus - `.earth`
 [16] Oy - animatsiya - `.moon`
 [17] Konfed - Animatilin - `.Candy`
 [18] Smoon - animatsiya - `.smoon`
 [19] Tmoon - animatsiya - `.tmoon`
 [20] Clown - animatsiya - `.clown`
 [21] Yulduz - batterfly va yulduz animatsiyasi - `.star`
 [22] Boxs - Rangli animatsiya - `.boxs`
 [23] Yomg'ir - suv animatsiyasi - `.rain`
 [24] Clol - "Nima?"  snimation - `.clol`
 [25] Odra - Animatsiya - `.odra`
 [26] Fleaveme - animatsiya - `.fleaveme`
 [27] Loveu - sevgi animatsiyasi - `.loveu`
 [28] Samolyot - animatsiya - `.plane`
 [29] Politsiya - animatsion sirena - `.police`
 [30] Jio - animatsiya - `.jio`
 [31] Quyosh tizimi - animatsiya - `.solarsystem`
 [32] Chatinfo - funksiya skanerlash chatinfo - `.chatinfo`
 [33] GPT3 - Savolga javob - `.svl` <Xabarga javob sifatida> yoki <matin>
 [34] Ovozni o'chirish - Administrator funksiyasi - .mute (m, h, d )
 [35] Qizuq - Kulgu vaqti - `.qzq 🔀Qiziq joyini eshitish🧐🤣♾`
 [36] Yashirilgan- 
 [37] Rev - teskari - `.rev`
 [38] Tr - Tarjimon - `.tr `<til kodi > <javob xabari>
 [39] Userinfo - Foydalanuvchi nomi haqida ma'lumot - `.userinfo` <javob berish>
 [40] Base64 - matnli xabarlarni kodlash va dekodlash - `.b64 en` <javob matni> `.b64 de` <kodlangan xabarga javob berish>
 [41] Reaksiya - reaksiyalar - `.react help`
 [42] Qor - animatsiya qor - `.snow`
 [43] Tts - ovozli matn - `.tts `<lang kodi> matnli xabarga javob berish
 [44] Itp - pdf to tasvir - `.itp` rasmga javob

 Yangiliklar: @Shoirjon_No1_1
""")
	