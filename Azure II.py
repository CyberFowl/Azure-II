import discord
from discord import Webhook, AsyncWebhookAdapter
from config import token
import random
import sys
from time import time, ctime, sleep
import base64

t = time()

class MyClient(discord.Client):
    async def on_ready(self):
        print("Azure The Second online!")

        games = ["with fizz#1707", "z!help", "GitHub.com/CyberFowl/Azure-II/", "with Azure", "tag", "WolfQuest"]
        choice = random.randint(0, len(games)-1)

        game = discord.Game(games[choice])
        await client.change_presence(status=discord.Status.dnd, activity=game)


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
        cyberfowl = 743009565242556526
        nighthawk = 794570615041556532
        rep = 813957898434379818
        rammy = 737661910194847836
        vaidehi = 546546354365435655

        guild_ids = [trio_id, fizzy_id]
        owner = [fizz, cyberfowl, nighthawk, rep]

        if mgi in guild_ids:
            pass

        if message.author != client.user and mgi in guild_ids or message.author.id in owner:


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
                tipsend = await message.channel.send(tips[tip])
                sleep(5)
                await tipsend.delete()

    #Utility
            if mcu.startswith("Z!PURGE"):
                purge = mcu.split(" ")[-1]
                if int(purge) < 1000:
                    await message.channel.purge(limit = int((purge)) + 1)
                    await message.channel.send(purge + " messages purged")
                    sleep(2)
                    await message.channel.purge(limit = 1)
                    print(purge + " messages purged")
                if int(purge) >= 1000:
                    await message.channel.send("Purge limit exceeded. Please specify a number below 1000.")
                    print("Purge limit exceeded")

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
                await message.channel.send(str(message.author.avatar_url))
            if mcu.startswith("Z!AVATAR") and "<@" in mcu:
                user_id = mcu[-19:-1]
                user = await client.fetch_user(user_id)
                await message.channel.send(str(user.avatar_url))

            if mcu == "Z!INVIS" and mgi == trio_id:
                print(str(message.author) + " going invis")
                await message.author.add_roles(invisi_role)
                reply = await message.channel.send(str(message.author) + " is invisible!")
                sleep(2)
                await reply.delete()
            if mcu == "Z!RMINVIS" and mgi == trio_id:
                print(str(message.author) + " back to visual mode!")
                await message.author.remove_roles(invisi_role)
                reply = await message.channel.send(str(message.author) + " back to visual mode")
                sleep(2)
                await reply.delete()

            if mcu.startswith("Z!EMBED"):
                print("Embedify")
                content = justmc.split(" ")[1:]
                space = " "
                string = space.join(content)
                embed = discord.Embed(title = string)
                embed.set_footer(text = "Embedify, by fizz#1707")
                await message.channel.send(embed = embed)

            if mcu == "Z!RICHEMBED":
                embed = discord.Embed(title = "Rich Embed", description = "To make a full embed", color = 0xff0000)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                embed.add_field(name = "Syntax - z!richembed,title,description,url,field,value", value = "*Remember to add the commas*", inline = False)
                embed.add_field(name = "Title", value = "Title of the embed", inline = False)
                embed.add_field(name = "Description", value = "Description of the embed", inline = False)
                embed.add_field(name = "Url", value = "Url in the title", inline = False)
                embed.add_field(name = "Field", value = "Title of the first field", inline = False)
                embed.add_field(name = "Value", value = "description of the first field", inline = False)
                embed.set_footer(text = "Rich Embed Help, by fizz#1707", icon_url = "https://cdn.discordapp.com/avatars/826795796640563230/ba3b1563a71e0ad8433d07a7ad66c4d7.png?size=128")
                await message.channel.send(embed = embed)
            if mcu.startswith("Z!RICHEMBED") and len(mcu) > 12:
                print("Rich Embed")
                title = justmc.split(",")[1]
                desc = justmc.split(",")[2]
                url = justmc.split(",")[3]
                field = justmc.split(",")[4]
                value = justmc.split(",")[5]
                video = justmc.split(",")[6]
                embed = discord.Embed(title = title, description = desc, url = url, color = 0xff0000)
                embed.set_author(name = message.author, url = message.author.avatar_url, icon_url = message.author.avatar_url)
                embed.set_thumbnail(url = video)#"https://cdn.discordapp.com/avatars/826795796640563230/ba3b1563a71e0ad8433d07a7ad66c4d7.png?size=128")
                embed.add_field(name = field, value = value, inline = False)
                embed.set_footer(text = "Rich Embed, by fizz#1707", icon_url = "https://cdn.discordapp.com/avatars/826795796640563230/ba3b1563a71e0ad8433d07a7ad66c4d7.png?size=128")
                await message.channel.send(embed = embed)
            if mcu.startswith("Z!MEDEMBED"):
                media = justmc.split(" ")[1]
                embed = discord.Embed(color = 0xff0000)
                embed.set_image(url = media)
                await message.channel.send(embed = embed)
            if mcu.startswith("Z!TURL"):
                title = justmc.split(",")[1]
                url = justmc.split(",")[2]
                embed = discord.Embed(title = title, url = url)
                embed.set_footer(text = "Title Embed Url, by fizz#1707", icon_url = "https://cdn.discordapp.com/avatars/826795796640563230/ba3b1563a71e0ad8433d07a7ad66c4d7.png?size=128")
                await message.channel.send(embed = embed)


    #Misc
        
            if mcu == "Z!SPOTIFY":
                print("Spotify liked songs")
                embed = discord.Embed(title = "Spotify - Liked Songs", description = "Your liked songs from Spotify", url = "https://open.spotify.com/collection/tracks")
                embed.set_footer(text = "Spotify, by fizz#1707")
                await message.channel.send(embed = embed)

            if mcu.startswith("Z!PING") and len(mcu) > 10:
                content = justmc.split(" ")[-1]
                for i in range(1,11):
                    await message.channel.send(content)

            if mcu == "Z!REPO":
                embed = discord.Embed(title = "Azure II Repo", url = "https://github.com/CyberFowl/Azure-II/")
                embed.set_footer(text = "Repository, by fizz#1707")
                await message.channel.send(embed = embed)

            if mcu == "Z!FILE":
                embed = discord.Embed(title = "File Handling", description = """Read - 'r'
Write - 'w'
Append - 'a'""")
                embed.set_footer(text = "File Handler, by fizz#1707")
                await message.channel.send(embed = embed)

            if mcu == "Z!FILE R":
                autotype_txt = open("autotype.txt", "r")
                print("File Reader")
                readdoc = autotype_txt.readlines()
                string = space.join(readdoc)
                embed = discord.Embed(title = "AutoType.txt - Content", description = string)
                embed.set_footer(text = "File Reader, by fizz#1707")
                await message.channel.send(embed = embed)
        
            if mcu.startswith("Z!LMGTFY"):
                print("Lmgtfy")
                search = justmc.split(" ")[1:]
                search = space.join(search)
                search_bytes = search.encode("ascii")
                
                base64_bytes = base64.b64encode(search_bytes)
                encoded = base64_bytes.decode("ascii")
                await message.channel.send("https://radiantly.github.io/lmgtfy/#" + str(encoded))


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
                if mcu.startswith("Z!FILE") and len(mcu) > 6:
                    access_mode = justmc.split(" ")[1]
                    autotype_txt = open("autotype.txt", access_mode)

                    if access_mode == "w":
                        print("File Writer")
                        write_string = justmc.split(" ")[2:]
                        string = space.join(write_string)
                        writedoc = autotype_txt.write(string + "\n")
                        await message.channel.send("Overwritten file :grin:")

                        readdoc = autotype_txt.readlines()
                        string = space.join(readdoc)
                        embed = discord.Embed(title = "AutoType.txt - Content", description = string)
                        embed.set_footer(text = "File Reader, by fizz#1707")
                        display = await message.channel.send(embed = embed)
                        sleep(4)
                        edit = await display.edit(content = "Type 'z!file r' to display it without deleting")
                        sleep(2)
                        await readdoc.delete()

                    if access_mode == "a":
                        print("File Appender")
                        write_string = justmc.split(" ")[2:]
                        string = space.join(write_string)
                        writedoc = autotype_txt.write(string + "\n")
                        await message.channel.send("Text appended :+1:")

                        readdoc = autotype_txt.readlines()
                        string = space.join(readdoc)
                        embed = discord.Embed(title = "AutoType.txt - Content", description = string)
                        embed.set_footer(text = "File Reader, by fizz#1707")
                        display = await message.channel.send(embed = embed)
                        sleep(4)
                        edit = await display.edit(content = "Type 'z!file' r to display it without deleting")
                        sleep(2)
                        await edit.delete()

                    autotype_txt.close()


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
                guild_id = message.guild.id
                guild = await client.fetch_guild(guild_id)
                user_id = mcu[-19:-1]
                user = await client.fetch_user(user_id)
                await guild.kick(user)               

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
