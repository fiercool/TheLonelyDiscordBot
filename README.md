# TheLonelyDiscordBot
My discord bot, uploaded to github. 

## How to run. 
### How to make a discord bot. 
Firstly set up a discord bot by going [here](https://discord.com/developers/applications)
Then click "New Application" in the top right, and pick any name you'd like. 
Click on the bot tab, and add a bot. 
Then copy the token as we'll need it for later.

## How to start hosting
I use repl.it to host my bot, as it is 100% free and runs 24/7. Go to https://replit.com/~ and make an account. Make a new repl, click import from github and paste https://github.com/fiercool/TheLonelyDiscordBot. Type *python bot.py* into the run button config. 

Once, you've done that go to settings.py and replace bot token with the bot token we copied earlier. Then go to the hypixel minecraft server and type in /api new. Now paste that code into "KEY". 

You can also change the bot prefix by changing COMMAND_PREFIX. 

Now if you click run its up and running, however it only stays on for 1 hour. 

###how to set up uptime robot
Go to https://uptimerobot.com/ and set up and account

click add new monitor, make the type HTTP(S) pick any name for the friendly name and paste the link you see on the right of the repl page (it will be https://TheLonelyDiscordBot.{your repl name}.repl.co). Finally click create monitor.

# How to add to server
go to this link and blank space with your discord bot's client id, which can be found at the same place as we found the bot token
https://discord.com/api/oauth2/authorize?client_id= &permissions=8&scope=bot

Thats it! My discord is finalhit#7739 if you need any help.
