import discord
client = discord.Client()

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

client.run("ODEyNTgyNTA4MDc1NTQ4Njkz.YDC2bg._cIvjhmVhHsadUek6UucITI0910
           ")
