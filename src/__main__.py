import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


class Chessbot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # 2. C'est l'étape cruciale : on synchronise les commandes avec Discord
        # Cela permet à Discord de "connaître" tes commandes pour les afficher avec le /
        await self.tree.sync()
        print("✨ Les commandes slash ont été synchronisées !")


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    match message.content:
        case "profile":
            print("ok")
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(TOKEN)

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
