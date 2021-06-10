import asyncio
from datetime import datetime

import discord
from discord.ext import commands


class CustomHelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        if not ctx.author.bot:
            embed = discord.Embed(title="Dein Text", description="Text", color=0x9A2EFE)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}",
                             icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            mess = await ctx.send(embed=embed)
            await mess.add_reaction("deinemoji")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if not user.bot:
            if reaction.emoji == "deinemoji":
                embed = discord.Embed(title="Dein Text", description="Text", color=0x9A2EFE)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}",
                                 icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await reaction.message.edit(embed=embed)
                await reaction.message.remove_reaction("deinemoji", user)


def setup(bot):
    bot.add_cog(CustomHelpCommand(bot))
