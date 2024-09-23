import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# IDs dos cargos de líderes e vice-líderes
LIDER_ROLE_ID = 1265335887189774387
VICE_LIDER_ROLE_ID = 1265354329460838430
VICE_LIDER2_ROLE_ID = 1265325613124685864

# IDs dos canais de texto
ID_CANAL_1 = 1271216531371724871
ID_CANAL_2 = 1286568914867847210
ID_CANAL_3 = 1271217999029735507
ID_CANAL_4 = 1271218675151536310

# Comando para mencionar todos os membros, restrito a líderes e vice-líderes
@bot.command()
async def mencionar_todos(ctx):
    if any(role.id in [LIDER_ROLE_ID, VICE_LIDER_ROLE_ID, VICE_LIDER2_ROLE_ID] for role in ctx.author.roles):
        await ctx.send("@everyone Atenção! Há um novo anúncio importante.")
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

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
    print(f"{bot.user.name} está pronto para administrar o servidor como Mikey!")
    channel = bot.get_channel(ID_CANAL_1)  # Canal de boas-vindas ou geral
    await channel.send(f"{bot.user.name} está online e pronto para ação!")

# Evento de boas-vindas
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(ID_CANAL_1)  # Canal de boas-vindas
    await channel.send(f"Bem-vindo ao servidor, {member.mention}! Certifique-se de ler as regras.")

# Evento de despedida
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(ID_CANAL_1)  # Canal de avisos
    await channel.send(f"{member.mention} saiu do servidor. Que a sorte esteja com eles!")

# Função para gerar convites
@bot.command()
async def criar_convite(ctx):
    link = await ctx.channel.create_invite(max_age=86400, max_uses=1)  # Convite válido por 1 dia com 1 uso
    await ctx.send(f"Seu convite foi criado: {link}")

# Token do bot administrador
TOKEN = 'MTI4NzE2OTgxMjk3MTEyNjkzOQ.GbxD31.hcAg-wVatqpBit_OSsDopY5oX4MTrtnt5a7HV4'
bot.run(TOKEN)
