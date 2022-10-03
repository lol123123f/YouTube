import ebDiscord, discord

ebbot = ebDiscord.settings(token="Token_here",
                           server_id=111111111111111111, #Id_here
                           start_message="Bot started!")

async def pingCommand(interaction):
    em = discord.Embed(title="Pong", description="Pong Pong", color=discord.Color.green())
    await ebDiscord.msg(interaction, "Text", em, ephemeral=True)


ebbot.new_command(name="ping", description="Send pong", command_func=pingCommand)

ebbot.on()