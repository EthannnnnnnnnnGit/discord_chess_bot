import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


class Chessbot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="/", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = Chessbot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.tree.command(name="linked", description="Link your chesscom account")
async def linked(interaction: discord.Interaction, unsername: str):
    await interaction.response.send_message(unsername)


@bot.tree.command(name="clear", description="Clear k messages")
@discord.app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, k: int):
    await interaction.response.defer(ephemeral=True)
    await interaction.channel.purge(limit=k)
    await interaction.delete_original_response()

bot.run(TOKEN)

# embed = discord.Embed(
#     title=f"♟️ Profil Échecs de moi",
#     description="Statistiques officielles et classement du club.",
#     color=discord.Color.blue(),  # Couleur de la bordure latérale
# )
# # 3. Ajout de champs structurés
# embed.add_field(name="🌐 Chess.com (Rapid)", value="1420", inline=True)
# embed.add_field(name="🏆 Elo Club (Interne)", value="1500", inline=True)
# embed.add_field(
#     name="📊 Matchs joués", value="12 joués (8 victoires)", inline=False
# )

# # 4. Ajouter un pied de page
# embed.set_footer(
#     text="Bot d'échecs du Club", icon_url=message.channel.guild.icon.url
#     if message.channel.guild.icon
#     else None
# )

# # 5. Envoyer l'embed dans le salon
# await message.channel.send(embed=embed)
