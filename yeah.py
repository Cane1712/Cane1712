import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

class View(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.Button(label="Mute")
    async def yeah(self, interaction):
        await interaction.response.send("yeah")

@bot.hybrid_command()
async def mute(ctx):
    await ctx.send(view=View())

bot.run("YOUR ")
