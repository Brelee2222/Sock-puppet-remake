global dm, channelid, userdmid, commandsl, commandsswl
channelid = input('channel id: ')
userdmid = input('dm user id: ')
dm = False
botstats = []

with open('commands.list', 'r') as f:
  commandsl = list(f.read().split('\u000a'))
with open('commandssw.list', 'r') as f:
  commandsswl = list(f.read().split('\u000a'))
def send_message(self, message):
  if int(message.author.id) == 479792413884547072 or int(message.author.id) == self.user.id:
    return False
  else:
    return True
def swapcond(cond):
  if cond:
    cond = False
  else:
    cond = True
  print(cond)
  return cond
def message_is_command(message):
  print(commandsl)
  if message.content in commandsl:
    return True
  else:
    for i in commandsswl:
      if message.content.startswith(i):
        return True
    return False
def command(message):
  if message.content == '/dm':
    global dm
    dm = swapcond(dm)
    return 'Switched'
  if message.content == '/channelc':
    channelid = input('Channel id: ')
    return 'changed'
  if message.content == '/dmc':
    userdmid = input('User dm id: ')
    return 'changed'
import datetime
from Encode import encrint, decrint
import random
import os
import discord
import http
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from asyncio import sleep
class MyClient(discord.Client):
  async def on_ready(self):
    CStat = input('Custom Status: ')
    try:
      await client.change_presence(activity=discord.Game(name=CStat))
      botstats.append('Good')
    except:
      botstats.append('Error')
    try:
      botstats.append(self.user.name)
      botstats.append(self.user.id)
    except:
      botstats.append('Error')
      botstats.append('Error')
    print('Custom status: ' + botstats[0])
    print('Username     : ' + botstats[1])
    print('Id           : ' + str(botstats[2]))
  async def on_message(self, message):
    if send_message(self, message):
      nonow = message
      try:
        nonow.channel.id = 806996393787916348
        await nonow.channel.send(embed=nonow.embeds[0])
        
      except:
        print('no embeds')
      
      embed=discord.Embed(title='Message', color=random.randint(0,16777215))
      embed.add_field(name='Channel', value=nonow.channel, inline=False)
      embed.add_field(name='Channel id', value=nonow.channel.id, inline=False)
      if not message.content == '':
        embed.add_field(name='Message content', value=nonow.content, inline=False)
      else:
        embed.add_field(name='Message', value='none', inline=False)
      embed.set_footer(icon_url = str(nonow.author.avatar_url), text = str("Author: " + nonow.author.name + '#' + nonow.author.discriminator))
      nonow.channel.id = 806996393787916348
      await nonow.channel.send(embed=embed)

      
      
      
    else:
      if message.author.id == self.user.id:
        print('me')
        return
      if message_is_command(message):
        if message.content.startswith('/user'):
          try:
            user = await client.fetch_user(int(message.content.replace('/user ', '')))
            await message.author.send((user.avatar_url, user.__init__))
          except:
            await message.author.send('couldn\u0027t find user')
          return
        else:
          message.channel.id = 806996393787916348
          await message.channel.send(command(message))
          return
          
        
      print(dm)
      if dm:
        print('dm')
        try:
          author = message.author
          author.id = int(userdmid)
          
        except:
          author = await client.fetch_user(int(userdmid))
        await author.send(message.content)
      else:
        global channelid
        print('channel')
        channel = message.channel
        channel.id = channelid
        await channel.send(message.content)
      
client = MyClient()
client.run(os.getenv('TOKEN'))