import os
import discord
import json_manager


def getUserPermission(user: discord.User, permission: str) -> bool:
    if json_manager.json(f"users/{user, id}.json").read()["permissions"]["all"]:
        return True
    elif json_manager.json(f"users/{user, id}.json").read()["permissions"][permission]:
        return True
    else:
        return False


def getUserOnlyPermission(user: discord.User, permission: str) -> bool:
    return json_manager.json(f"users/{user, id}.json").read()["permissions"][permission]
