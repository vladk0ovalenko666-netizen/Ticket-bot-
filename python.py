import discord
from discord.ext import commands
from discord.ui import Button, View
import json
from dotenv import load_dotenv
import os

# Загрузи переменные окружения из файла .env
load_dotenv()

# Создай экземпляр бота с указанием intents
intents = discord.Intents.default()
intents.message_content = True  # Включи необходимые intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Импортируй команды из файла commands.py
from commands import ticket, close_ticket, send_ticket_message

# Кнопка для открытия тикета
class OpenTicketButton(Button):
    def __init__(self):
        super().__init__(label='Открыть тикет', style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        # Отправь модальное окно пользователю
        await interaction.response.send_modal(TicketModal())

# Кнопка для закрытия тикета
class CloseTicketButton(Button):
    def __init__(self):
        super().__init__(label='Закрыть тикет', style=discord.ButtonStyle.danger)

    async def callback(self, interaction: discord.Interaction):
        # Закрытие канала тикета
        await interaction.channel.delete()
        await interaction.response.send_message('Тикет закрыт.', ephemeral=True)

# Вью для кнопок
class TicketView(View):
    def __init__(self):
        super().__init__()
        self.add_item(OpenTicketButton())
        self.add_item(CloseTicketButton())

# Обработчик события готовности бота
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Регистрация команд
@bot.tree.command(name='ticket', description='Создать тикет')
async def ticket_command(interaction: discord.Interaction):
    await ticket(interaction)

@bot.tree.command(name='close_ticket', description='Закрыть тикет')
async def close_ticket_command(interaction: discord.Interaction):
    await close_ticket(interaction)

@bot.command()
async def send_ticket_message(ctx):
    await send_ticket_message(ctx)

# Запусти бота
bot.run(os.getenv('DISCORD_TOKEN'))