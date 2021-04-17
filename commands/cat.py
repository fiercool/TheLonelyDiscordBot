from commands.base_command import BaseCommand
import requests

class Cat(BaseCommand):
    def __init__(self):
        description = "gets a random cat from some bad api that has bad cat"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(url)
        cat = response.json()['url']
        await message.channel.send(cat)
        