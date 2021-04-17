from commands.base_command import BaseCommand
import requests
import settings
class Weight(BaseCommand):
    def __init__(self):
        description = "finds your hypixel skyblock weight"
        params = ['name']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        name = (params[0])
        url = f'https://api.mojang.com/users/profiles/minecraft/{name}?'
        response = requests.get(url)
        uuid = response.json()['id']
        #uuid = uuid[0:8] + "-" + uuid[8:4] + "-" + uuid[12:4] + "-" + uuid[16:4] + "-" + uuid[20]
        print(uuid)
        url2 = f'https://hypixel-api.senither.com/v1/profiles/{uuid}/we?key={settings.KEY}'
        response2 = requests.get(url2)
        print(url2)
        weight = response2.json()['data']['weight']
        
        await message.channel.send(weight)
#https://hypixel-api.senither.com/v1/profiles/16b33d0e-9ba3-42f4-9e15-bd0c319c2957//we?key=ff445ca0-1edf-4275-b7de-789124c2ed68