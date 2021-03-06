import typing

from discord.ext import commands
from app.checks import mc_mod

if typing.TYPE_CHECKING:
    from app.bot import CCBot


class Manage(commands.Cog):
    def __init__(self, bot: "CCBot"):
        self.bot = bot

    @commands.command(
        name="run",
        help="Runs a MC command as root."
    )
    @mc_mod()
    async def run_mc(self, ctx: commands.Context, *, command: str):
        async with ctx.typing():
            result = await self.bot.mc.run_command(command)
        await ctx.send(f"Done!\n```\n{result}```")


def setup(bot: "CCBot"):
    bot.add_cog(Manage(bot))
