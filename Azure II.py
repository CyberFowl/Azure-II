import discord
from discord import Webhook, AsyncWebhookAdapter
from config import token
import random
import sys
from time import time, ctime, sleep

t = time()

class MyClient(discord.Client):
    async def on_ready(self):
        print("Azure The Second online!")

        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "The Trio talk"))

    async def on_message(self, message):
        
        global flink, rlink, vlink
    
    #Main Variables
        mcu = message.content.upper()
        justmc = message.content

        mgi = message.guild.id
        mci = message.channel.id


        trio_id = 826117496692146216
        gen_id = 826117496692146220
        gaming_id = 826117566720245791
        mlane_id = 826117774702805012
        plans_id = 826117936271589377

        fizzy_id = 818895293428531220
        fizgen_id = 818895293428531224

        fizz = 817633704330526752
        rammy = 737661910194847836
        vaidehi = 546546354365435655

        guild_ids = [trio_id, fizzy_id]

        if mgi in guild_ids:
            pass

        if message.author != client.user and mgi in guild_ids:

                
#Variables/Lists
    #Emojis

    #Chance
        #8Ball
            ball_response = ["As I see it, yes", "As I see it, no", "Yes", "No", "Very likely", "Very unlikely", "It is certain", "Don't count on it", "Maybe", "Possibly"]

            lucky_phrase = random.randint(0, len(ball_response)-1)
        
        #Coinflip
            coinflip = random.choice(["Heads", "Tails"])

        #Dice
            dice = random.choice(["1", "2", "3", "4", "5", "6"])

    #Stats
        #Restart time
            restart_time = str(ctime(t))

        #Azure's ping
            bot_ping = f"{round(client.latency * 1000)}"

    #Tips
            tips = ["z!help for the help menu", "z!spotify to go to your liked songs", "z!stats to get all the bot stats", "z!invis or z!rminvis to change the visibility of your name", "z!coinflip to settle an argument"]
            
            tip = random.randint(0, len(tips)-1)

    #Roles
            invisi_role = discord.Object(827081315123724319)

    #Other
            space = " "

#Commands
    #Help
            if mcu == "Z!HELP":
                embed = discord.Embed(title = "Help Menu")
                embed.add_field(name = ":bar_chart: Stat Commands:", value = """z!begin - shows the last restart time in IST
z!ping - shows the ping/latency
z!stats - shows all the stats""", inline = False)
                embed.add_field(name = ":hammer_pick: Utility Commands", value = """z!purge <limit> - purges *[x]* messages (less than 1000 at a time)
z!avatar - shows your avatar
z!invis - makes your name invisible
z!rminvis - makes your name visible again
z!embed <content> - puts your text in an embed
z!plan <content> - adds a plan in <#826117936271589377>""", inline = False)
                embed.add_field(name = ":question: Chance Commands", value = """z!8ball <question> - replies to a yes/no question
                z!coinflip - flips a coin
z!dice - rolls a dice (1-6)""", inline = False)
                embed.add_field(name = ":jigsaw: Misc Commands", value = """z!spotify - sends a spotify link to your liked songs""", inline = False)
                embed.add_field(name = ":shield: Failsafe Commands", value = """z!exit - shuts the bot down. :warning: No way to restart the bot unless <@!817633704330526752> restarts manually :warning:""", inline = False)
                embed.set_footer(text = "Help Menu, by fizz#1707")
                help_embed = await message.channel.send(embed = embed)
                emoji = '\U0001F4A1'
                await message.add_reaction(emoji)
                tipsend = await message.channel.send(tips[tip])
                sleep(5)
                await tipsend.delete()

            if mcu == "Z!MHELP":
                embed = discord.Embed(title = "Member specific help menu")
                embed.add_field(name = "Fizz Commands (prefix:z!f)", value = """z!flink <paste a link here> - Remembers a link to be referenced later
z!flink - Displays the remembered link""", inline = False)
                embed.add_field(name = "Rammy Commands (prefix:z!r)", value = """z!rlink <paste a link here> - Remembers a link to be referenced later
z!rlink - Displays the remembered link""", inline = False)
                embed.add_field(name = "Vaidehi Commands(prefix:z!v)", value = """z!vlink <paste a link here> - Remembers a link to be referenced later
z!vlink - Displays the remembered link""", inline = False)
                embed.set_footer(text = "Help Menu, by fizz#1707")
                await message.channel.send(embed = embed)
                tipsend = await message.channel.send(tips[tip])
                sleep(5)
                await tipsend.delete()

    #Stats
        #Individual
            if mcu == "Z!BEGIN":
                print("Restart time")
                await message.channel.send("Azure was last restarted at " + restart_time + " IST")

            if mcu == "Z!PING":
                print("Azure's ping")
                await message.channel.send(":ping_pong: Pong! | Message took ***" + bot_ping + "ms*** to respond")

        #Bulk
            if mcu == "Z!STATS":
                print("All stats")
                embed = discord.Embed(title = "Bot Stats")
                embed.add_field(name = ":ping_pong: Latency/Ping", value = bot_ping, inline = False)
                embed.add_field(name = ":clock1030: Last restart time", value = restart_time, inline = False)
                embed.set_footer(text = "Stats, by fizz#1707")
                await message.channel.send(embed = embed)
                await message.channel.send(tip)
                sleep(5)
                await message.channel.purge(limit = 1)

    #Utility
            if mcu.startswith("Z!PURGE"):
                purge = mcu.split(" ")[-1]
                if int(purge) < 1000:
                    await message.channel.purge(limit = int((purge)) + 1)
                    await message.channel.send(purge + " messages purged")
                    sleep(2)
                    await message.channel.purge(limit = 1)
                    print(purge + " messages purged")

            if mcu.startswith("Z!PLAN"):
                content = justmc.split(" ")[1:]
                space = " "
                string = space.join(content)
                embed = discord.Embed(title = ":asterisk: " + string)
                embed.set_footer(text = "Planner, by fizz#1707")
                planner = client.get_channel(826117936271589377)
                await planner.send(embed = embed)
                print("New plan")

            if mcu == "Z!AVATAR":
                print(str(message.author) + " avatar")
                await message.channel.send("https://cdn.discordapp.com/avatars/" + str(message.author.id) + "/" + str(message.author.avatar) + ".png?size=128")

            if mcu == "Z!INVIS" and mgi == trio_id:
                print(str(message.author) + " going invis")
                await message.author.add_roles(invisi_role)
                await message.channel.send(str(message.author) + " is invisible!")
                sleep(2)
                await message.channel.purge(limit = 1)
            if mcu == "Z!RMINVIS" and mgi == trio_id:
                print(str(message.author) + " back to visual mode!")
                await message.author.remove_roles(invisi_role)
                await message.channel.send(str(message.author) + " back to visual mode")
                sleep(2)
                await message.channel.purge(limit = 1)

            if mcu.startswith("Z!EMBED"):
                print("Embedify")
                content = justmc.split(" ")[1:]
                space = " "
                string = space.join(content)
                embed = discord.Embed(title = string)
                embed.set_footer(text = "Embedify, by fizz#1707")
                await message.channel.send(embed = embed)

    #Misc
        
            if mcu == "Z!SPOTIFY":
                print("Spotify liked songs")
                embed = discord.Embed(title = "Spotify - Liked Songs", description = "Your liked songs from Spotify", url = "https://open.spotify.com/collection/tracks")
                embed.set_footer(text = "Spotify, by fizz#1707")
                await message.channel.send(embed = embed)

    #Chance
        
            if mcu.startswith("Z!8BALL"):
                print("8Ball")
                await message.channel.send(ball_response[lucky_phrase])

            if mcu == "Z!COINFLIP":
                print("Coinflip")
                await message.channel.send(coinflip)

            if mcu == "Z!DICE":
                print("Roll a die")
                await message.channel.send(dice)

    #Fizz
            if message.author.id == fizz:
        
        #Remembering stuff
                if mcu.startswith("Z!FLINK") and len(mcu) > 9:
                    print("Remember link")
                    flink = justmc.split(" ")[-1]
                    await message.channel.send("Added link")
                    sleep(1)
                    await message.channel.purge(limit = 1)

                if mcu == "Z!FLINK":
                    print("Display link")
                    await message.channel.send("Here it is:")
                    await message.channel.send(flink)

        #File Handling
                if mcu == "Z!FILE":
                    embed = discord.Embed(title = "File Handling", description = """Read - 'r'
Write - 'w'
Append - 'a'""")
                    embed.set_footer(text = "File Handler, by fizz#1707")
                    await message.channel.send(embed = embed)

                if mcu.startswith("Z!FILE") and len(mcu) > 6:
                    access_mode = justmc.split(" ")[1]
                    constants_txt = open("constants.txt", access_mode)

                    if access_mode == "r":
                        print("File Reader")
                        readdoc = constants_txt.readlines()
                        string = space.join(readdoc)
                        embed = discord.Embed(title = "Constants.txt - Content", description = string)
                        embed.set_footer(text = "File Reader, by fizz#1707")
                        await message.channel.send(embed = embed)
                    if access_mode == "w":
                        print("File Writer")
                        write_string = justmc.split(" ")[2:]
                        space = " "
                        string = space.join(write_string)
                        writedoc = constants_txt.write(string + "\n")
                        await message.channel.send("Overwritten file :grin:")
                    if access_mode == "a":
                        print("File Appender")
                        write_string = justmc.split(" ")[2:]
                        space = " "
                        string = space.join(write_string)
                        writedoc = constants_txt.write(string + "\n")
                        await message.channel.send("Text appended :+1:")

                    constants_txt.close()


    #Rammy
            if message.author.id == rammy:
                
        #Remembering stuff
                if mcu.startswith("Z!RLINK") and len(mcu) > 9:
                    print("Remember link")
                    rlink = justmc.split(" ")[-1]
                    await message.channel.send("Added link")
                    sleep(1)
                    await message.channel.purge(limit = 1)

                if mcu == "Z!RLINK":
                    print("Display link")
                    await message.channel.send("Here it is:")
                    await message.channel.send(rlink)

    #Vaidehi
            if message.author.id == vaidehi:
                
        #Remembering stuff
                if mcu.startswith("Z!VLINK") and len(mcu) > 9:
                    print("Remember link")
                    vlink = justmc.split(" ")[-1]
                    await message.channel.send("Added link")
                    sleep(1)
                    await message.channel.purge(limit = 1)

                if mcu == "Z!VLINK":
                    print("Display link")
                    await message.channel.send("Here it is:")
                    await message.channel.send(vlink)

    #The Tester's Paradise
            if mcu.startswith("Z!TEST"):
                print(justmc)

            if mcu == "Z!TESTRR":
                reactionmsg = await message.channel.send("This is a reaction role test")
                bulb = '\U0001F4A1'
                await reactionmsg.add_reaction(bulb)
                for user in reaction.users():
                    role = discord.Object(826796232919482369)
                    await user.add_roles(role)
                    await message.channel.send("Test successful?")

    #Failsafe
            if mcu == "Z!EXIT":
                await message.delete()
                shutdown_msg = await message.channel.send("Azure The Second is shutting down now.")
                sleep(2)
                await shutdown_msg.edit(content = "<@!" + str(fizz) + ">, Azure The Second was shutdown by <@!" + str(message.author.id) + ">")
                print("Azure The Second was shutdown by " + str(message.author))
                sys.exit()
    

print("Booting up...")

client = MyClient()
client.run(token)
