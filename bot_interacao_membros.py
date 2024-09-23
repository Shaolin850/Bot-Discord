import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# IDs dos canais de texto
ID_CANAL_1 = 1271216531371724871
ID_CANAL_2 = 1286568914867847210

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
    print(f"{bot.user.name} está online e pronto para interagir com os membros!")
    channel = bot.get_channel(ID_CANAL_1)  # Canal de boas-vindas ou geral
    await channel.send(f"{bot.user.name} está pronto para interagir com vocês!")

# Token do bot de interação com membros
TOKEN = 'MTI4NzQ0ODI1MTA1Nzk2NzE5Mg.GbY1ql.RV2Do9CsM4Gf0c-ONRo7ZG2OG8INvYlUWPaATM'
bot.run(TOKEN)
