Эта папка для пользователей РП сервера
## Для чего это
Эта папка обычна нужна для прав пользавателей.
Для кастомных прав просто добавьте право в default-perms.txt.
## Как получить право
Используйте класс manage.py и функцию getUserPermission(user, "perm"")
Возвращает true или false.

```python
import discord
from tools import manage
from discord.ext import commands


class MyCommand:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def my_command(self, ctx):
        if manage.getUserPermission(ctx.author, "use_command"):
            await ctx.send("Hello, i'm bot!")
            # Проверка есть ли право use_command
            # Если да то отправит сообщение
            # Если нет то ничего


def setup(client: discord.Client):
    client.add_cog(MyCommand())
```