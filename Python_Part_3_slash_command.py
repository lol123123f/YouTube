import ebDiscord, discord

ebbot = ebDiscord.settings(token="*******************************",
                           server_id=11111111111111111111111111,
                           start_message="Bot started!")


async def pingButton(interaction: discord.Interaction, button: discord.ui.Button):
    await ebDiscord.msg(interaction, f"Double ping{button.custom_id[-1]}!", ephemeral=True)


ping_btn = [ebDiscord.button(custom_id="Ping1", label="Ping1", style=discord.ButtonStyle.red, func=pingButton),
            ebDiscord.button(custom_id="Ping2", label="Ping2", style=discord.ButtonStyle.green, func=pingButton),
            ebDiscord.button(custom_id="Ping3", label="Ping3", style=discord.ButtonStyle.red, func=pingButton),
            ebDiscord.select(custom_id="pingSelect", placeholder="Ping!", row=1, disabled=True, options=[discord.SelectOption(label='1', value='1')]),
            ebDiscord.button(custom_id="Ping4", label="Ping4", style=discord.ButtonStyle.red, func=pingButton, row=2),
            ebDiscord.button(custom_id="Ping5", label="Ping5", style=discord.ButtonStyle.red, func=pingButton, row=2),
            ebDiscord.button(custom_id="Ping6", label="Ping6", style=discord.ButtonStyle.red, func=pingButton, row=2, emoji='😎')]


async def pingCommand(interaction):
    em = discord.Embed(title="Pong", description="Pong Pong", color=discord.Color.green())
    await ebDiscord.msg(interaction, "Text", em, components=ping_btn)


async def testSelect(interaction, select: discord.ui.Select):
    await ebDiscord.msg(interaction, " ".join(select.values), ephemeral=True)


sel = [ebDiscord.select(custom_id="test1", options=[
        discord.SelectOption(label='Apple', value='🍎'),
        discord.SelectOption(label='Pineapple', value='🍍'),
        discord.SelectOption(label='Tomato', value='🍅'),
        discord.SelectOption(label='Falafel', value='🥙'),
        discord.SelectOption(label='Pizza', value='🍕')
    ], func=testSelect, min_values=2, max_values=4)]


async def testCommand(interaction):

    await ebDiscord.msg(interaction, 'Test', components=sel)


ebbot.new_command(name="ping", description="Send pong", command_func=pingCommand)
ebbot.new_command(name="test" ,description="Test for select", command_func=testCommand)

ebbot.on(to_save=[ping_btn, sel])
