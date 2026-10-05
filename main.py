import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! Eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            print(f"Recebendo imagem: {file_name} - URL: {file_url}")
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Imagem salva em ./{attachment.filename}")
            #fazer a previsão com o modelo
            class_name, confidence_score = get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path= f"./{attachment.filename}")
            await ctx.send(f"Classe: {class_name}, Confiança: {confidence_score:.2f}")
    else:
        await ctx.send("Nenhuma imagem foi enviada.")
