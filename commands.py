import discord
from discord.ext import commands
from discord.ui import Modal, TextInput

# Модальное окно для ввода информации
class TicketModal(Modal):
    def __init__(self):
        super().__init__(title='Создание тикета')
        self.add_item(TextInput(label='Тема тикета', placeholder='Введите тему вашего тикета', required=True))
        self.add_item(TextInput(label='Описание проблемы', style=discord.TextStyle.long, placeholder='Опишите вашу проблему', required=True))
        self.add_item(TextInput(label='Сервер', placeholder='Укажите сервер', required=True))
        self.add_item(TextInput(label='Steam ID', placeholder='Введите ваш Steam ID', required=True))

    async def on_submit(self, interaction: discord.Interaction):
        # ID категории, в которой будут создаваться тикеты
        category_id = 1234567890  # Замените на ID вашей категории
        category = interaction.guild.get_channel(category_id)
        
        # Получение текущего номера тикета из файла
        with open('ticket_number.json', 'r') as file:
            data = json.load(file)
            ticket_number = data['ticket_number']
        
        # Создай новый текстовый канал для тикета в указанной категории
        ticket_channel = await interaction.guild.create_text_channel(f'ticket-{ticket_number}', category=category)
        
        # Добавь пользователя, который создал тикет, в канал
        await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
        
        # Добавь администратора или модератора в канал (если нужно)
        # await ticket_channel.set_permissions(interaction.guild.get_role(ADMIN_ROLE_ID), read_messages=True, send_messages=True)
        
        # Отправь сообщение в канал с информацией из модального окна
        await ticket_channel.send(f'Привет, {interaction.user.mention}! Это твой тикет №{ticket_number}. Тема: {self.children[0].value}. Описание: {self.children[1].value}. Сервер: {self.children[2].value}. Steam ID: {self.children[3].value}')
        
        # Отправь сообщение пользователю о создании тикета
        await interaction.response.send_message(f'{interaction.user.mention}, твой тикет №{ticket_number} создан в канале {ticket_channel.mention}.')
        
        # Увеличение номера тикета и сохранение в файл
        data['ticket_number'] += 1
        with open('ticket_number.json', 'w') as file:
            json.dump(data, file)

# Команда для создания тикета
async def ticket(interaction: discord.Interaction):
    # Отправь модальное окно пользователю
    await interaction.response.send_modal(TicketModal())

# Команда для закрытия тикета
async def close_ticket(interaction: discord.Interaction):
    # Закрытие канала тикета
    await interaction.channel.delete()
    await interaction.response.send_message('Тикет закрыт.', ephemeral=True)

# Команда для отправки сообщения с кнопками в определенный канал
async def send_ticket_message(ctx):
    # ID канала, в который нужно отправить сообщение
    channel_id = 1234567890  # Замените на ID вашего канала
    channel = ctx.guild.get_channel(channel_id)
    
    # Отправь сообщение с кнопками в канал
    await channel.send('Для создания тикета нажмите кнопку ниже.', view=TicketView())