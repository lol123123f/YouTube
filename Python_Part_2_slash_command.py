import ebDiscord, discord

ebbot = ebDiscord.settings(token="MTAwMzU0NDExMDQ2NjA4NDk0NQ.GDbu_6.IlwDLG-wMfFjXFNbZTislJGF_2SeFLdG6iEMPY",
                           server_id=932680938251493376,
                           start_message="Bot started!")


async def pingButton(interaction: discord.Interaction, button: discord.ui.Button):
    await ebDiscord.msg(interaction, f"Double ping{button.custom_id[-1]}!", ephemeral=True)


ping_btn = [ebDiscord.button(custom_id="Ping1", label="Ping1", style=discord.ButtonStyle.red, func=pingButton),
            ebDiscord.button(custom_id="Ping2", label="Ping2", style=discord.ButtonStyle.green, func=pingButton),
            ebDiscord.button(custom_id="Ping3", label="Ping3", style=discord.ButtonStyle.red, func=pingButton),
            ebDiscord.button(custom_id="Ping4", label="Ping4", style=discord.ButtonStyle.red, func=pingButton, row=1),
            ebDiscord.button(custom_id="Ping5", label="Ping5", style=discord.ButtonStyle.red, func=pingButton, row=1),
            ebDiscord.button(custom_id="Ping6", label="Ping6", style=discord.ButtonStyle.red, func=pingButton, row=1, emoji='😎')]

async def pingCommand(interaction):
    em = discord.Embed(title="Pong", description="Pong Pong", color=discord.Color.green())
    await ebDiscord.msg(interaction, "Text", em, components=ping_btn)


ebbot.new_command(name="ping", description="Send pong", command_func=pingCommand)

ebbot.on(to_save=[ping_btn])