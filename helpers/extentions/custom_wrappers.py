from discord.ext import commands
from discord.ext.bridge import bridge_command


def guild_only(name: str = None, aliases: list[str] = None, usage: int = 1, cooldown: int = 5,
               guild_permissions: dict[str, bool] = None, bot_permissions: dict[str, bool] = None):
    """
    A decorator to create a guild-only command with optional parameters for command name, aliases, cooldown, and permissions.

    Parameters:
    - name (str): The name of the command. Defaults to the function name if not provided.
    - aliases (list[str]): A list of aliases for the command.
    - usage (int): The number of times a command can be used before triggering a cooldown. Default is 1.
    - cooldown (int): The cooldown period in seconds. Default is 5.
    - guild_permissions (dict[str, bool]): A dictionary of required guild permissions.
    - bot_permissions (dict[str, bool]): A dictionary of required bot permissions.

    Returns:
    - function: The decorated function as a guild-only command.
    """

    def decorator(func):
        @bridge_command(name=name or func.__name__, aliases=aliases or [])
        @commands.guild_only()
        @commands.has_guild_permissions(**(guild_permissions or {}))
        @commands.bot_has_permissions(**(bot_permissions or {}))
        @commands.cooldown(usage, cooldown, commands.BucketType.user)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        return wrapper

    return decorator


def private_only(name: str = None, aliases: list[str] = None, usage: int = 1, cooldown: int = 5):
    """
    A decorator to create a private (DM-only) command with optional parameters for command name, aliases, and cooldown.

    Parameters:
    - name (str): The name of the command. Defaults to the function name if not provided.
    - aliases (list[str]): A list of aliases for the command.
    - usage (int): The number of times a command can be used before triggering a cooldown. Default is 1.
    - cooldown (int): The cooldown period in seconds. Default is 5.

    Returns:
    - function: The decorated function as a private-only command.
    """

    def decorator(func):
        @bridge_command(name=name or func.__name__, aliases=aliases or [])
        @commands.dm_only()
        @commands.cooldown(usage, cooldown, commands.BucketType.user)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        return wrapper

    return decorator
