from commands.base_command import BaseCommand
import requests
import settings
import discord
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from discord.ext.commands import bot
import numpy as np
import math  
import shutil
import urllib.request
class S(BaseCommand):
    def __init__(self):
        description = "gets the stats of a person"
        params = ["Name"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        name = (params[0])
        url = f'https://api.mojang.com/users/profiles/minecraft/{name}?'
        response = requests.get(url)
        uuid = response.json()['id']

        
        data = requests.get(f"https://api.hypixel.net/player?key={settings.KEY}&name={name}").json()
        #if "player" in data == "null":
         # await message.channel.send("bad name")
        #else: 
        try:
          if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
            rank = data["player"]["rank"]
          elif "newPackageRank" in data["player"]:
            rank = data["player"]["newPackageRank"]
          elif "packageRank" in data["player"]:
            rank = data["player"]["packageRank"]
          else:
            rank = "non"
        except TypeError: 
          await message.channel.send("Player doesn't exist or has never played on hypixel")
        print("getting stats, please wait. ")
        
        #NameColor = (0,0,0)
          
       
          
        bwfinalkills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"] 
        bwstars = data["player"]["achievements"]["bedwars_level"]
        displayname = data["player"]["displayname"]
        networkxp = data["player"]["networkExp"]
        skywarslevel = data["player"]["stats"]["SkyWars"]["levelFormatted"]
        xp = data["player"]["stats"]["SkyWars"]["skywars_experience"]
        print(rank)




        networkLevel = (math.sqrt((2 * networkxp) + 30625) / 50) - 2.5
        networkLevel = round(networkLevel)
        def sw_xp_to_lvl(xp):
          xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
          if xp >= 15000:
            return (xp - 15000) / 10000. + 12
          else:
            for i in range(len(xps)):
              if xp < xps[i]:
                return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])
     
      #  skin = data2['value']
        skinrender = f'https://crafatar.com/renders/head/{uuid}.png?size=64'
        #size doesnt work maybe the passte thing cana make t bigger
        print(skinrender)
        urllib.request.urlretrieve(skinrender, "skin.png")
        skin=Image.open('skin.png')
        

        #
        img = Image.new('RGB', (1920,1080), color = (255, 255, 255))
        img2 = Image.open("darkbackground.jpg")
        enhancer = ImageEnhance.Brightness(img2)
        
        img2_output = enhancer.enhance(0.5)
        img2_output.save('darkbackground1.jpg')
        img2 = Image.open("darkbackground.jpg")
        #blurImage = img2.filter(ImageFilter.BLUR)
        #blurImage.save('blurbackground.png')
        img.paste(img2)
        img.paste(skin, (1800,0))
        fnt = ImageFont.truetype('fonts/Minecraftia-Regular.ttf', 100)
        fnt2 = ImageFont.truetype('fonts/Minecraftia-Regular.ttf',70)
       
        d = ImageDraw.Draw(img)
        d.text((50,45), "Stats", font=fnt, fill=(255, 255, 255))
      
        
        if displayname == "FinalHit":
          d.text((50,175), displayname, font=fnt2,fill=(211, 33, 255))
        elif displayname == "sekoh":
          d.text((50,175), displayname, font=fnt2,fill=(255,85,85))
        elif rank == "VIP":
          d.text((50,175), displayname, font=fnt2,fill=(255, 255, 85))
        elif rank == "VIP_PLUS":
          d.text((50,175), displayname, font=fnt2,fill=(85, 255, 85))
        elif rank == "MVP":
          d.text((50,175), displayname, font=fnt2,fill=(85, 255, 255))
        elif rank == "MVP_PLUS":
          try:
            monthlyPackageRank = data["player"]["monthlyPackageRank"]
            print(monthlyPackageRank)
            if monthlyPackageRank == "SUPERSTAR":
              d.text((50,175), displayname, font=fnt2,fill=(255, 170, 0))
            else: d.text((50,175), displayname, font=fnt2,fill=(85, 255, 255))
          except KeyError:
            print("never got mvp++ before")
            d.text((50,175), displayname, font=fnt2,fill=(85, 255, 255))
        
          
          
          #check if monthlypackagerank == superstar to see if mvp++
          
            
          
          #d.text((50,150), displayname, font=fnt2,fill=(85, 255, 255))
        elif rank == "YOUTUBER":
          d.text((50,175), displayname, font=fnt2,fill=(255, 85, 85))
        elif rank == "ADMIN":
          d.text((50,175), displayname, font=fnt2,fill=(255, 85, 85))
        elif rank == "HELPER":
          d.text((50,175), displayname, font=fnt2,fill=(85, 85, 255))
        elif rank == "MODERATOR":
          d.text((50,175), displayname, font=fnt2,fill=(0, 170, 0))
        else:
          rank = "NON"
          d.text((50,175), displayname, font=fnt2,fill=(170, 170, 170))

        print(networkLevel)
        #d.text((50,175), networkLevel, font=fnt2,fill=(170, 170, 170))
        
        hi = "hi"
        strnetworklevel = str(networkLevel)
        print(strnetworklevel)
        d.text((50,300), "hypixel level:", font=fnt2,fill=(255,255,255))
        d.text((610 ,300), strnetworklevel, font=fnt2,fill=(255,255,255))
        
        strbwstars = str(bwstars)
        print(strbwstars)
        d.text((50 ,370), "bedwars stars: ", font=fnt2,fill=(255,255,255))
        d.text((710 ,370), strbwstars, font=fnt2,fill=(255,255,255))

        strskywarslevel = str(skywarslevel)
        print(strskywarslevel)
        skywarslevels = sw_xp_to_lvl(xp)
        print(skywarslevels)
        roundskywarslevels = round(skywarslevels)
        strskywarslevels = str(roundskywarslevels)
        d.text((50 ,440), "skywars stars: ", font=fnt2,fill=(255,255,255))
        d.text((710 ,440), strskywarslevels, font=fnt2,fill=(255,255,255))
        #find skywars_experience and convert to level using
        #def sw_xp_to_lvl(xp):
    #xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
    #if xp >= 15000:
     #   return (xp - 15000) / 10000. + 12
    #else:
     #   for i in range(len(xps)):
      #      if xp < xps[i]:
       #         return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])

        img.save('test.png')
        
        embed = discord.Embed(
          title = "Bedwars Finals",
          description = f'Bedwars final kills = {bwfinalkills}',
          colour = discord.Colour.red()
        )
        
      
        embed.set_footer(text = f'message sent by {message.author.name}')
     
       # await message.channel.send(embed=embed)
        #await message.channel.send(skin)

       
        

        
        
       
        #await message.channel.send(bwfinalkills)
        await message.channel.send(file=discord.File('test.png'))
        print(networkxp)
        print(networkLevel)
        
        
        #settings.KEY