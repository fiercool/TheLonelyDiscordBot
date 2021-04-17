import requests

from commands.base_command import BaseCommand

class Name(BaseCommand):
    def __init__(self):
        description = "finds all used names of an mc account"
        params = ["username"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        name = (params[0])
        url = f'https://api.mojang.com/users/profiles/minecraft/{name}?'
        response = requests.get(url)
        uuid = response.json()['id']
        url2 = f'https://api.mojang.com/user/profiles/{uuid}/names'
        response2 = requests.get(url2)
        for name in response2.json():
          await message.channel.send(name)
        #await message.channel.send(name)
        #await message.channel.send(uuid)
        
        