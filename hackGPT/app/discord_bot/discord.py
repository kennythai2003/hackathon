from app.chatgpt_ai.openai import chatgpt_response
from dotenv import load_dotenv
import app.discord_bot.discord as discord
import os

load_dotenv()


discord_token = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as : ", self.user)

    async def on_message(self, message):
        print(message.content)
        # prevents bot from replying to itself
        if message.author == self.user:
            return

        command, user_message = None, None

        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")


intents = discord.intents.default()
intents.message_contents = True

client = MyClient(intents=intents)
