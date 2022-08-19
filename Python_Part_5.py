from datetime import datetime
import random
import discord
import discord_components


# global var
TOKEN = "MTAwMzU0NDExMDQ2NjA4NDk0NQ.GqjNy7.8p7GNXm1HnCsICjjRdQqtKgQ3yAYPqeywmwO-E"
PREFIX = "!"

# discord objs
bot = discord.Client()
get = discord.utils.get
em = discord.Embed
DiscordComponents = discord_components.DiscordComponents
Button = discord_components.Button
ButtonStyle = discord_components.ButtonStyle
ddb = DiscordComponents(bot)

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
    if args[0] == f"{PREFIX}cool":
        role = get(msg.channel.guild.roles, name="I am cool😎")
        if role in msg.author.roles:
            await msg.add_reaction("❌")
        else:
            await msg.author.add_roles(role)
            await msg.add_reaction("✅")
    if args[0] == f"{PREFIX}op":
        role = get(msg.channel.guild.roles, id=1004842129903861760)
        if role in msg.author.roles:
            await msg.add_reaction("❌")
        else:
            await msg.author.add_roles(role)
            await msg.add_reaction("✅")
    if args[0] == f"{PREFIX}role":
        if get(msg.channel.guild.roles, id=1002551446358741083).position >= msg.author.roles[0].position:
            try:
                msg.mentions[0]
            except:
                return await msg.channel.send("לא תויג אף אחד")
            try:
                msg.role_mentions[0]
            except:
                return await msg.channel.send("לא תויג אף רול")
            try:
                if msg.role_mentions[0] in msg.mentions[0].roles:
                    await msg.mentions[0].remove_roles(msg.role_mentions[0])
                    await msg.channel.send(f"The user {msg.mentions[0].mention} now dont have the role {msg.role_mentions[0].mention}")
                else:
                    await msg.mentions[0].add_roles(msg.role_mentions[0])
                    await msg.channel.send(f"The user {msg.mentions[0].mention} got the role {msg.role_mentions[0].mention}")
            except:
                await msg.channel.send("קרה תקלה ככל הנראה לבוט אין גישה לרול זה!")
        else:
            await msg.channel.send("אין לך גישה")
    if args[0] == f"{PREFIX}url":
        await msg.channel.send(content='כפתור', components=[
            [Button(style=ButtonStyle.blue, label="Verify", id="verifyb"), Button(style=ButtonStyle.blue, label="Verify2", id="verify")],
            [Button(style=ButtonStyle.blue, label="Verify", id="verifyb0"), Button(style=ButtonStyle.blue, label="Verify2", id="verify7"), Button(style=ButtonStyle.blue, label="Verify2", id="verify3")]
        ])

@bot.event
async def on_button_click(res):
    if res.component.id == "verifyb":
        role = get(res.guild.roles, name="👤 | Members")
        member_role = await res.guild.fetch_member(res.user.id)
        await member_role.add_roles(role)
        await res.respond(type=4,
                          content=f'{role.mention} added')


if __name__ == "__main__":
    bot.run(TOKEN)
