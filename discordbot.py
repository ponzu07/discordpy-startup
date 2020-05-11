from discord.ext import commands
import os
import traceback
import discord
from datetime import datetime, timedelta

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

    
@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 544882228677705738 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(709227262251106344)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)
            
            
@bot.command()
async def ping(ctx):
    await ctx.send('じるこ')



bot.run(token)
