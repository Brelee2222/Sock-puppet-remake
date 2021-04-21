global dm, channelid, userdmid, commandsl, commandsswl, hexi, binary, inte
channelid = input('channel id: ')
userdmid = input('dm user id: ')
dm = False
botstats = []
hexi = False
binary = False
inte = False
stop = False
avoids = False
with open('commands.list', 'r') as f:
  commandsl = list(f.read().split('\u000a'))
with open('commandssw.list', 'r') as f:
  commandsswl = list(f.read().split('\u000a'))
def send_message(self, message):
  if int(message.author.id) == 479792413884547072 or int(message.author.id) == self.user.id:
    return False
  
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
  if message.content.startswith('/channelc '):
    global channelid
    channelid = message.content.replace('/channelc ', '')
    return 'changed'
  if message.content.startswith('/dmc '):
    global userdmid
    userdmid = message.content.replace('/dmc ', '')
    return 'changed'
  if message.content == '/hex':
    global hexi, binary, inte
    hexi = swapcond(hexi)
    binary = False
    inte = False
  if message.content == '/avoid':
    global avoids
    avoids = swapcond(avoids)
    return 'avoid turned on : ' + str(avoids)
  if message.content == '/bin':
    
    binary = swapcond(binary)
    hexi = False
    inte = False
  if message.content == '/int':
    
    inte = swapcond(inte)
    binary = False
    hexi = False
  if message.content == '/stop-':
    global stop
    stop = True
    return 'stopped'
def msgsendconv(message):
  if hexi:
    hexic = ''
    for i in message.content:
      hexic = hexic + ' ' + hex(ord(i))
    return hexic
  if binary:
    binc = ''
    for i in message.content:
      binc = binc + ' ' + bin(ord(i))
    return binc
  if inte:
    return decrint(message.content)
  return message.content
    

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
intents = discord.Intents().all()

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
    
    print(message.content)
    if send_message(self, message):
      nonow = message
      if len(nonow.embeds) >= 1:
        await (await client.fetch_user(479792413884547072)).send(command(message))
      
      embed=discord.Embed(title='Message', color=random.randint(0,16777215))
      embed.add_field(name='Channel', value=nonow.channel, inline=False)
      embed.add_field(name='Channel id', value=nonow.channel.id, inline=False)
      if not message.content == '':
        embed.add_field(name='Message content', value=nonow.content, inline=False)
      else:
        embed.add_field(name='Message content', value='none', inline=False)
      embed.add_field(name='Message id', value=nonow.id, inline=False)
      embed.add_field(name='Author id', value=nonow.author.id, inline=False)
      embed.set_footer(icon_url = str(nonow.author.avatar_url), text = str("Author: " + nonow.author.name + '#' + nonow.author.discriminator))
      await (await client.fetch_user(479792413884547072)).send(embed=embed)

      
      
      
    else:
      if message.author.id == self.user.id:
        print(message.author)
        print('me')
        return
      if message_is_command(message):
        if message.content.startswith('/user '):
          try:
            user = await client.fetch_user(int(message.content.replace('/user ', '')))
            await message.author.send((user.avatar_url, user.__init__))
          except:
            await message.author.send('couldn\u0027t find user')
          return
        if message.content.startswith('/mass dm guild using id and i meant it please '):
          tomass = list(message.content.replace('/mass dm guild using id and i meant it please ', '').split(' '))

          
            
          guild = client.get_guild(int(tomass[0]))
          
          print(guild.members)
          print(tomass)
          donot = []
          del(tomass[0])
          global stop, avoids
          if avoids:
            donot = list(tomass[0].split(','))
            del(tomass[0])
            print(donot)
          for member in guild.members:
            if stop:
              stop = False
              return
            print(member)
            if not str(member.id) in donot:
              message.author = member
              try:
                await message.author.send(' '.join([str(elem) for elem in tomass]))
              except:
                print('error')
          await (await client.fetch_user(479792413884547072)).send('done')
          return
        if message.content.startswith('/reply '):
          reply = message
          
          toreply = list(reply.content.replace('/reply ', '').split(' '))
          print(toreply)
          reply.id = toreply[0]
          del(toreply[0])
          reply.channel.id = toreply[0]
          del(toreply[0])
          dia = str(' '.join([str(elem) for elem in toreply]))
          
          await reply.reply((' '.join([str(elem) for elem in toreply])))
          
          
          return 
        if message.content.startswith('/spam '):
          tospam = list(message.content.replace('/spam ', '').split(' '))
          channel = message.channel
          channel.id = tospam[0]
          del(tospam[0])
          times = int(tospam[0])
          del(tospam[0])
          for i in range(times):
            if stop:
              stop = False
              return
            await channel.send(' '.join([str(elem) for elem in tospam]))
          return
        if message.content.startswith('/spamdm '):
          message.content = message.content.replace('/spamdm ', '')
          tospam = list(message.content.split(' '))
          spamee = message
          author = spamee.author
          
          spamee.author = await client.fetch_user(int(tospam[0]))
          del(tospam[0])
          times = int(tospam[0])
          del(tospam[0])
          tospam = ' '.join([str(elem) for elem in tospam])
          
          for i in range(times):
            if stop:
              stop = False
              return
            await spamee.author.send(tospam)
          return

        else:
          try: 
            await (await client.fetch_user(479792413884547072)).send(command(message))
          except:
            print('invalid')
          return
          
      message.content = msgsendconv(message)
      print(dm)
      if dm:
        print('dm')
        
        
        print(userdmid)
        author = await client.fetch_user(int(userdmid))
        print(author)
        
        try:
          await author.send(message.content)
        except:
          print('error')
      else:
        global channelid
        print('channel')
        
        message.channel.id = int(channelid)
        try:
          await message.channel.send(message.content)
        except:
          print('error')
      
client = MyClient(intents=intents)
TOKEN = input('TOKEN: ')
if TOKEN == '':
  TOKEN = os.getenv('TOKEN')
client.run(TOKEN)

