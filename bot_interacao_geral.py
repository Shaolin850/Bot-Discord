import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# IDs dos canais de texto
ID_CANAL_3 = 1271217999029735507
ID_CANAL_4 = 1271218675151536310

# Função de pesquisa na web
@bot.command()
async def pesquisar(ctx, *, query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("h3", class_="zBAuLc")
    if results:
        await ctx.send(f"Resultado: {results[0].text}")
    else:
        await ctx.send("Nenhum resultado encontrado.")

# Evento de inicialização
@bot.event
async def on_ready():
    print(f"{bot.user.name} está online para a interação geral!")
    channel = bot.get_channel(ID_CANAL_3)  # Canal de interação geral
    await channel.send(f"{bot.user.name} está pronto para interagir com vocês!")

# Token do bot de interação geral
TOKEN = 'MTI4NzQ0NjA2OTMxOTQzODQyNw.G94R6i.tLFS4-ceHByYXd3jaHTodSJrW5IkIQ_Gb6_QAA'
bot.run(TOKEN)
