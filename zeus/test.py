from telethon import TelegramClient, events, sync

@events.register(events.NewMessage(pattern=".hello"))
async def test(event):
	await event.edit("Assalomu alaykum Telegramingizga ajoib bo'lgan skriptni uladingiz Ushbu skriptning hzmatlaridan foydalanish uchun <.yordam> yoki <.help> deb istalgan chatga yuboring Agar sizda ushbu skriptni kengaytirish va qo'shimcha hizmatlar uchun takliflar bo'lsa skript dasturchisi bilan bog'lanishingiz mumkun Dasturchi❯❯ @Shoirjon_No1 Shu va shunga o'xshash qiziqarli dasturlar va skriptlar Bizning muhokama va yangilillar guruximizdan topiladi ")
	