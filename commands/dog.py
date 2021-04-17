from commands.base_command import BaseCommand
import requests
import discord 
class Dog(BaseCommand):
    def __init__(self):
        description = "gets a random dog from some bad api that has bad dogs"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        
        url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(url)
        dog = response.json()['message']
        embed = discord.Embed(
          title = "free dog",
          
          colour = discord.Colour.blue()
        )
        embed.set_footer(text = message.author.name)
        embed.set_image(url=dog)
        #embed.thumbnail(url='dog api')
        
       # embed.add_field(name = "hi",value = "hi", inline=false)
       # embed.add_field(name = "hi",value = "hi", inline=true)
        await message.channel.send(embed=embed)
        #await message.channel.send(dog)
        
        #put https://dog.ceo/dog-api/breeds-list later