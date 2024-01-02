from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=21016353,
    api_hash="99765dcc8db939e7c8049c034cc9f3fe",
    bot_token="6366625304:AAG3Cdt2nBDo6XY5-AhqmlGdTF-4hcN3NVc",
    plugins=dict(root="MZombie")
    )

DEVS = ["xsa_v"]

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
