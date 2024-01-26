import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    account_age = datetime.utcnow().replace(tzinfo=timezone.utc) - member.created_at
    if account_age < timedelta(days=30):
        await member.send("Your account is too new to use this server and has been kicked.")
        await member.kick(reason="Account age is less than one month.")

@bot.command()
async def check_account(ctx):
    account_age = datetime.utcnow().replace(tzinfo=timezone.utc) - ctx.author.created_at
    account_age_days = account_age.days
    response = f"Your account age is {account_age_days} days."
    if account_age < timedelta(days=30):
        response += " Your account is too new to use the server."
    await ctx.send(response)

bot.run('BOT TOKEN')
