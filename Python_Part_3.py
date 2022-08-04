from datetime import datetime
import random

import discord

# global var
TOKEN = ""
PREFIX = "!"

# discord objs
bot = discord.Client()
get = discord.utils.get
em = discord.Embed


# on_ready func

@bot.event
async def on_ready():
    print(f"The bot {bot.user.name} is up")


@bot.event  # Event that eun every time someone send message
async def on_message(msg):
    global PREFIX
    args = msg.content.split()
    if msg.author.bot:
        return
    if msg.author.id == bot.user.id:
        return
    if args[0] == f"{PREFIX}ping":
        await msg.channel.send(content="Pong!🐴")
    if "http" in msg.content or msg.content.endswith(".com"):
        await msg.delete()
        await msg.author.send("קיבלת מיוט לשעה!")
    if args[0] == f"{PREFIX}myfirstembed":
        try:
            color = int(args[1].replace("#", "0x"),0)
            embed_var = em(title="ואו איזה מגניב", description="אוי זה קטן", color=color, timestamp=datetime.now())
        except:
            embed_var = em(title="ואו איזה מגניב", description="אוי זה קטן", color=0x00ffc3, timestamp=datetime.now())
        embed_var.set_image(url="https://media.istockphoto.com/photos/rendered-galaxy-space-scene-with-planets-picture-id1298997952?b=1&k=20&m=1298997952&s=170667a&w=0&h=DsD2R0U-Z6RZOAtoVH1pPVDvlAFMEgaZtqX-Y936zTo=")
        embed_var.set_author(icon_url=msg.author.avatar_url, name=msg.author.name)
        embed_var.add_field(name="Number:", value="1")
        embed_var.add_field(name="Number:", value="2")
        embed_var.add_field(name="Number:", value="3", inline=False)
        embed_var.set_thumbnail(url="https://www.paperspecs.com/wp-content/uploads/2016/08/lynx-art-space-posters6.jpg")
        embed_var.set_footer(text="This an space images", icon_url=bot.user.avatar_url)
        await msg.channel.send(embed=embed_var)
    if args[0] == f"{PREFIX}coinflip":
        number = random.randint(1, 10)
        if (number % 2 == 0) and args[1] == 'head' or (number % 2 != 0) and args[1] == 'tail':
            await msg.channel.send("ניצחת!")
        else:
            await msg.channel.send("הפסדת!")


if __name__ == "__main__":
    bot.run(TOKEN)
