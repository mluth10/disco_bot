import discord
from discord.ext import commands
import random

# run on Heroku (eventually)
# test server id = 712908102902743043
# cool server id = 653438528637894676

insults = [' is super not cool', ' is bad at Civ', ' listens to Ariana Grande']
dict_insult = {}
basic_cmd = ['hello', 'add', 'add command', 'insult', 'add to insults', 'add_to_insults', 'bully', 'remove_insult',
             'remove', 'remove_from_insults', 'list', 'list_insults', 'rj', 'sexiest_nba_player', 'info', 'subtract', 'thursday', 'help']
bad = ['sucks', 'is so bad', 'is stupid', 'listens to Ariana Grande']
my_dict = dict()
token = 'NzEyOTA4NTk4MTUzNTc2NDY4.XscByA.G48huhOus45J1LmQkefaZ09yBP8'
# client = discord.Client()
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():

    guild_list = client.guilds
    for guild in guild_list:
        dict_insult[guild.id] = [' is super not cool', ' is bad at Civ', ' listens to Ariana Grande']
        print(guild.id)
    print('ok')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='THOS MOSER'))


@client.command()
async def hello(ctx):
    await ctx.send('Hello')


@client.command(aliases=['sexiest_nba_player'])
async def rj(ctx):
    await ctx.send(file=discord.File('rj_1.jpg'))
    await ctx.send(file=discord.File('rj_2.jpg'))
    await ctx.send(file=discord.File('rj_3.jpg'))
    await ctx.send(file=discord.File('rj_4.jpeg'))
    await ctx.send(file=discord.File('rj_5.jpg'))


@client.command(aliases=['add'])
async def add_command(ctx, key, *, value):
    if key in basic_cmd:
        await ctx.send(f'${key} is already a command and cannot be modified')
    else:
        my_dict.update({key: value})
        await ctx.send(f'Upon execution of ${key}, I will say {value}')
        print(my_dict)


@client.command()
async def bully(ctx, *, name):
    server_id = ctx.guild.id
    print(server_id)
    await ctx.send(f'{name}{random.choice(dict_insult[server_id])}')


@client.command(aliases=['insult'])
async def add_to_insults(ctx, *, sult):
    server_id2 = ctx.guild.id
    print(server_id2)
    addi = ' ' + sult
    dict_insult[server_id2].append(addi)
    await ctx.send(f'{sult} was added to the list of insults')


@client.command(aliases=['remove_insult', 'remove'])
async def remove_from_insults(ctx, *, mult):
    server_id3 = ctx.guild.id
    delt = ' ' + mult
    if delt in dict_insult[server_id3]:
        dict_insult[server_id3].remove(delt)
        await ctx.send(f'{delt} was removed from the list of insults')
    else:
        await ctx.send(f'This is not a known insult. To add it, type $insult {delt}')


@client.command(aliases=['list'])
async def list_insults(ctx):
    server_id4 = ctx.guild.id
    print(server_id4)
    sent = ''
    for insult in dict_insult[server_id4]:
        sent += insult[1:]
        sent += ' | '
    await ctx.send(sent)


@client.command()
async def info(ctx):
    embedd = discord.Embed(title="Epic Bot Info", description="Info about epic bot", color=0xE91FF5)

    embedd.add_field(name='Author', value='@me llamo roberto')
    embedd.add_field(name='Creation Date', value='05/19/2020')
    embedd.add_field(name='Original Server', value='the cool server')
    embedd.add_field(name='Invite Link', value='https://discordapp.com/oauth2/authorize?client_id=712908598153576468'
                                               '&scope=bot&permissions=0')

    await ctx.send(embed=embedd)


@client.command()
async def subtract(ctx, kee):
    my_dict.pop(kee)
    await ctx.send(f'${kee} is no longer a command')


@client.command()
async def thursday(ctx):
    for k in range(10):
        await ctx.send('THURSDAY')


client.remove_command('help')


@client.command()
async def help(ctx):
    embed = discord.Embed(title="epic bot", description="The Most Epic of Bots", color=0x1FEAF5)
    embed.add_field(name="$hello", value="Says hello", inline=False)
    embed.add_field(name="$bully X", value="Insults X with a random insult", inline=False)
    embed.add_field(name="$insult X", value="Adds X to the list of potential insults invoked by $bully", inline=False)
    embed.add_field(name="$remove_insult X", value="Removes X from the list of potential insults invoked by $bully",
                    inline=False)
    embed.add_field(name='$list_insults', value='Gives a list of all insults potentially invoked by $bully')
    embed.add_field(name="$add X Y", value="Creates your own personal command $X to which the bot will reply Y",
                    inline=False)
    embed.add_field(name='$subtract X', value='Removes your personal command. The bot will no longer respond to the '
                                              'command $X')
    embed.add_field(name="$info", value="Gives info about bot")
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


@client.event
async def on_voice_state_update(member, before, after):
    b4 = before.channel
    state = after.channel
    first = member.guild.text_channels[1]
    second = member.guild.text_channels[1]
    chan_list = member.guild.text_channels
    for h in chan_list:
        if h.name == 'general':
            first = h
            break
    if state is not None:
        if (state.name == 'epic channel') & (b4 != state):
            await first.send(f'@everyone {member.display_name} is ready for gaming!')
    if state is None:
        print(hello)
        if (b4.name == 'epic channel') & (b4 != state):
            await first.send(f'{member.display_name} no longer wants to gaming!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = str(message.content)
    lowered = msg.lower()
    first_char = message.content[0]
    if first_char != '$':
        # server_id = client.get_guild(653438528637894676)
        print(message.author)

        #if str(message.author) == "me llamo roberto#3491":
        #    await message.channel.send("Manith is so secksy")

        if str(message.author) == "Dad Bot#2189":
            await message.add_reaction('\U0001F595')

        if str(message.author) == "dlee1828#1841":
            await message.add_reaction('\U0001F349')

        if lowered == "stephan is epic":
            await message.channel.send("i disagree")

        elif "strategy" in lowered:
            await message.channel.send("strategy is epic")

        elif ("is epic" in lowered) or ('am epic' in lowered):
            await message.channel.send("i agree")
            # await message.channel.send(message.author.mention)

        elif lowered == "stephan is not epic":
            await message.channel.send('i agree')
        elif lowered == "ryan is so sexy":
            await message.channel.send(file=discord.File('ryan.jpg'))
        elif lowered.startswith('i hate ') or lowered.startswith('fuck '):
            begin = str(lowered[0:1])
            x = lowered
            if begin == 'i':
                y = x.replace('i hate ', 'All my homies hate ')
            if begin == 'f':
                y = x.replace('fuck ', 'All my homies hate ')
            await message.channel.send(y)
        elif lowered.startswith('the bot '):
            xy = lowered.split('the bot ')
            if str(xy[1]) in bad:
                await message.channel.send('disagree!')
    if (first_char == '$') & (message.content[1:] in my_dict.keys()):
        await message.channel.send(my_dict.get(message.content[1:]))

    await client.process_commands(message)


client.run(token)
