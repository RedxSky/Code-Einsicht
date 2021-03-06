from discord.ext import commands
import discord
from time import sleep
from time import strftime
import asyncio

client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Artificial Intelligence", url='https://elearning.hs-offenburg.de/moodle/course/view.php?id=5306'))
    print('Bot hat sich eingeloggt.')
    await client.get_channel(819525857973370892).send('Mein Host hat mich leider neugestartet, kann jemand bitte ***Vorlesungsplan** in den Chat schreiben um mich zu reaktivieren?')
    await client.get_channel(821481823787024447).send('Mein Host hat mich leider neugestartet, kann jemand bitte ***Vorlesungsplan** in den Chat schreiben um mich zu reaktivieren?')


@client.command()
async def latency(ctx):
    #sleep(10)
    await ctx.send(f'Die Latenz beträgt {round(client.latency *1000)} ms')

@client.command()
async def repeat(ctx, *, arg):
    await ctx.send(arg)

@client.command(aliases=['AKI'])
async def hello(ctx, *, arg):
    await ctx.send(f'hello {ctx.author}')

@client.command()
async def channel_id(ctx):
    await ctx.send(ctx.channel.id)

@client.command()
async def asdf(ctx):
    await ctx.send('*Vorlesungsplan')


one = 'https://www.bilder-upload.eu/upload/419a84-1615928902.png'
two = 'https://www.bilder-upload.eu/upload/9b807f-1615928932.png'
three = 'https://www.bilder-upload.eu/upload/fb87e2-1615928960.png'
four = 'https://www.bilder-upload.eu/upload/356f07-1615928982.png'
five = 'https://www.bilder-upload.eu/upload/828769-1615929001.png'
six = 'https://www.bilder-upload.eu/upload/9aebd0-1615929028.png'
seven = 'https://www.bilder-upload.eu/upload/3b159b-1615929058.png'
eight = 'https://www.bilder-upload.eu/upload/75497b-1615929077.png'
nine = 'https://www.bilder-upload.eu/upload/32efb7-1615929097.png'
ten = 'https://www.bilder-upload.eu/upload/87c2c2-1615929117.png'
eleven = 'https://www.bilder-upload.eu/upload/a17c2b-1615929155.png'
twelve = 'https://www.bilder-upload.eu/upload/8e5ef4-1615929171.png'
thirteen = 'https://www.bilder-upload.eu/upload/bdadb1-1615929200.png'

@client.command()
async def Testnachricht(ctx):
    await ctx.send(eins, delete_after=5*2+3)
    await ctx.send(one, delete_after=5)

# Eingabe: Uhrzeit in der From [HH, MM, SS]
# Ausgabe: Wartezeit
def WartezeitInSekunden(Uhrzeit):
    a = strftime('%H:%M:%S')
    a = a.split(':')
    a = (int(a[0])*60 + int(a[1]) ) *60 + int(a[2]) + 60*60 #falls Uhr nach geht
    #print(Uhrzeit[0])
            
    b = (int(Uhrzeit[0]) * 60 + int(Uhrzeit[1])) * 60 + int(Uhrzeit[2])
    
    if b < a:
        return 24 * 60 * 60 + (b - a)
    
    else:
        return (b - a)

def richtigeUhrzeit(Uhrzeit):
    a = strftime('%H:%M:%S')
    a = a.split(':')
    a = (int(a[0])*60 + int(a[1]) ) *60 + int(a[2]) + 60*60 # falls Uhr nach geht
   

    b = (int(Uhrzeit[0]) * 60 + int(Uhrzeit[1])) * 60
    
    if b >= a:
        return True


@client.command()
async def Wecker(ctx, *, arg):

    a = str(arg)
    #a = a.replace('Uhrzeit:', '')
    a = a.split(':')

    # await ctx.send(strftime("%a, %d %b %Y %H:%M:%S"))
    await ctx.send('Wecker wurde erfolgreich gestellt')
    Zeit = WartezeitInSekunden(a)
    sleep(Zeit)
    await ctx.send(strftime("%a, %d %b %Y %H:%M:%S Hier ist Ihre Erinnerung"))

@client.command(aliases=['V'])
async def Vorlesungsplan(ctx):

    # Bot startet erst am nächsten Tag um 8 Uhr
    
    await ctx.send(f'Vielen Dank! {ctx.author}! Vorlesungsbenachrichtigungen wurden aktiviert')

    while True:

        # Montag
        if int(strftime('%w')) == 1:
             # Sicherheit für evtle Korrektur
            if richtigeUhrzeit([9, 30]) == True:
                await asyncio.sleep(WartezeitInSekunden([9, 35, 00]))

            # erste Vorlesung
            if richtigeUhrzeit([9, 45]) == True:
                await ctx.send(eins, delete_after=60*90+10)
                await ctx.send(one, delete_after=60*90+10)                  
                await asyncio.sleep(WartezeitInSekunden([11, 25, 00]))                

            if richtigeUhrzeit([11, 35]) == True:
                await ctx.send(zwei, delete_after=60*90+10)
                await ctx.send(two, delete_after=60*90+10) 
                await asyncio.sleep(WartezeitInSekunden([13, 50, 00]))                

            if richtigeUhrzeit([14, 00]) == True:     
                await ctx.send(drei, delete_after=60*90+10)
                await ctx.send(three, delete_after=60*90+10)
            
            # Vorlesung am nächsten Morgen
            await asyncio.sleep(WartezeitInSekunden([9, 35, 00]))

        # Dienstag
        elif int(strftime('%w')) == 2:

            # Sicherheit für evtle Korrektur
            if richtigeUhrzeit([9, 30]) == True:
                await asyncio.sleep(WartezeitInSekunden([9, 35, 00]))

            # erste Vorlesung
            if richtigeUhrzeit([9, 45]) == True:
                await ctx.send(vier, delete_after=60*90+10)
                await ctx.send(four, delete_after=60*90+10)                  
                await asyncio.sleep(WartezeitInSekunden([11, 25, 00]))                

            if richtigeUhrzeit([11, 35]) == True:
                await ctx.send(fuenf, delete_after=60*90+10)
                await ctx.send(five, delete_after=60*90+10) 
                await asyncio.sleep(WartezeitInSekunden([13, 50, 00]))                

            if richtigeUhrzeit([14, 00]) == True:     
                await ctx.send(sechs, delete_after=(60*90*2+15+10))
                await ctx.send(six, delete_after=(60*90*2+15+10))

            # Vorlesung am nächsten Morgen     
            await asyncio.sleep(WartezeitInSekunden([7, 50, 00]))

        # Mittwoch
        if int(strftime('%w')) == 3:
             # Sicherheit für evtle Korrektur
            if richtigeUhrzeit([7, 45]) == True:
                await asyncio.sleep(WartezeitInSekunden([7, 50, 00]))

            if richtigeUhrzeit([8, 00]) == True:
                await ctx.send(acht, delete_after=60*90+10)
                await ctx.send(eight, delete_after=60*90+10)                  
                await asyncio.sleep(WartezeitInSekunden([9, 35, 00]))                

            if richtigeUhrzeit([9, 45]) == True:
                await ctx.send(neun, delete_after=60*90+10)
                await ctx.send(nine, delete_after=60*90+10) 
                await asyncio.sleep(WartezeitInSekunden([11, 25, 00]))                

            if richtigeUhrzeit([11, 35]) == True:     
                await ctx.send(zehn, delete_after=60*90+10)
                await ctx.send(ten, delete_after=60*90+10)
                await asyncio.sleep(WartezeitInSekunden([13, 50, 00]))

            if richtigeUhrzeit([14, 00]) == True:     
                await ctx.send(elf, delete_after=60*90+10)
                await ctx.send(eleven, delete_after=60*90+10)

            # Vorlesung am nächsten Morgen
            await asyncio.sleep(WartezeitInSekunden([7, 50, 00]))

        # Donnerstag
        if int(strftime('%w')) == 4:
             # Sicherheit für evtle Korrektur
            if richtigeUhrzeit([7, 45]) == True:
                await asyncio.sleep(WartezeitInSekunden([7, 50, 00]))

            if richtigeUhrzeit([8, 00]) == True:
                await ctx.send(zwoelf, delete_after=(60*90*2+20+10))
                await ctx.send(twelve, delete_after=(60*90*2+20+10))                  
                await asyncio.sleep(WartezeitInSekunden([11, 25, 00]))                

            # Sicherheit für evtle Korrektur
            if richtigeUhrzeit([11, 20]) == True:
                await asyncio.sleep(WartezeitInSekunden([11, 25, 00]))

            if richtigeUhrzeit([11, 35]) == True:     
                await ctx.send(dreizehn, delete_after=(60*90*2+20+10))
                await ctx.send(thirteen, delete_after=(60*90*2+20+10))
                
            # Vorlesung am nächsten Morgen
            await asyncio.sleep(WartezeitInSekunden([11, 00, 00]))

        # Freitag
        if int(strftime('%w')) == 5:
                         
            # Vorlesung am nächsten Morgen
            await asyncio.sleep(WartezeitInSekunden([10, 40, 00]))

        # Samstag
        if int(strftime('%w')) == 6:
                         
            # Vorlesung am nächsten Morgen
            await asyncio.sleep(WartezeitInSekunden([10, 20, 00]))

        # Sonntag
        if int(strftime('%w')) == 7:
                         
            # Vorlesung am nächsten Morgen
            await asyncio.sleep(WartezeitInSekunden([9, 35, 00]))
        

client.run('TOKEN_hier_einfuegen')
