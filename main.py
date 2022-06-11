import discord
import asyncio


if message.channel.id == 123:
        channel = client.get_channel(123)
        global slowmode_running

        if slowmode_running == True:
            print("Server cooling down running skipping task")
            return       

        if channel.last_message.author == client.user:
            print("Previous msg still exist so skipping...")
            return       
        
        
        if slowmode_running == False:
            await channel.send("Hello World")        
            print("Message Sent ")

            slowdown = channel.slowmode_delay       
            print(channel.slowmode_delay)
            print("server cooldown running")
            slowmode_running = True

            await asyncio.sleep(slowdown)
            print("cooldown finish")
            slowmode_running = False
