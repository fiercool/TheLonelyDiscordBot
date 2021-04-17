from commands.base_command import BaseCommand
from random import randint
import discord
from discord.ext.commands import bot
x = ["rock", "paper", "scissors"]

class Rps(BaseCommand):
    def __init__(self):
        description = "rock paper scissors"
        params = ["rock/paper/scissors"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        computer = x[randint(0,2)]
        choices = (params[0])
        choice = choices.lower()
        if choice in x:
          texts = ("You picked "+ choice + ", the computer picked "+  computer)
          if choice == computer:
            answer = ("You tied")
            return
          if choice == 'rock':
            if computer == "paper":
              answer = ("You lose")
            else:
              answer = ("You win")
          elif choice == 'paper': 
            if computer == "scissors":
              answer = ("You lose")
            else:
              answer = ("You win") 
          elif choice == 'scissors':
            if computer == "rock":
              answer = ("You lose")
            else:
              answer = ("You win")
          else:
           await message.channel.send("thats not an option")
        else: 
          await message.channel.send("thats not an option")
        embed = discord.Embed(
          title = answer,
          description = texts,
          colour = discord.Colour.red()
        )
        embed.set_footer(text = message.author.name)
        await message.channel.send(embed=embed)
        
         