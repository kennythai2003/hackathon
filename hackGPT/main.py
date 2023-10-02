import discord
import openai

intents = discord.Intents.default()
intents.message_content = True

token = 'MTE1Nzc1Mjc3NjIyNzU2MTU3NA.GmkcCz.INKc2YywxJGg0i0k8d8RB-NcAbNujkB3CU9bz0'
openai.api_key = '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'

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("{0.user} has hacked into the mainframe".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if username == "hackGPT":
        print(username + " RESPONDED " +
              user_message.lower() + " IN CHANNEL: " + channel)
    else:
        print(username + " SENT " + user_message.lower() +
              " IN CHANNEL: " + channel)

    if message.author == client.user:
        return

    if message.content == '!help':
        embed = discord.Embed(title="🦠W31C0M3 to hackGPT 🦠",
                              description="An answer to EVERYTHING...", color=0x006400)
        embed.set_thumbnail(url="https://cdna.artstation.com/p/assets/images/images/052/230/022/large/adam-nourse-dall-e-2022-07-27-02-53-29-a-fortune-telling-shiba-inu-reading-your-fate-in-a-giant-hamburger-digital-art.jpg?1659289847")
        embed.add_field(name="Ask hackGPT",
                        value="!hack {prompt}", inline=True)
        embed.add_field(name="Create an Image",
                        value="!spawn {prompt}", inline=True)
        embed.add_field(
            name="The First Step to Efficiency", value="Hack your lifestyle with hackGPT", inline=False)
        embed.set_footer(icon_url=message.author.display_avatar,
                         text="Session begun by: {}".format(message.author.display_name))
        await message.channel.send(embed=embed)

    if message.content.startswith('!hack'):
        user_message = message.content.replace('!hack', '')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=200,
            temperature=1
        )

        output = response["choices"][0]["message"]["content"]

        embed = discord.Embed(title="🧪 YOUR WISH IS MY COMMAND 🧪",
                              description="```" + output + "```", color=0x006400)

        await message.channel.send(embed=embed)
        print(output)

    if message.content.startswith('!spawn'):
        user_message = message.content.replace('!spawn', '')

        response = openai.Image.create(
            prompt=user_message,
            n=1,
            size="1024x1024"
        )

        output = response['data'][0]['url']

        embed = discord.Embed(title="🧬" + user_message +
                              " HAS BEEN SPAWNED 🧬", color=0x006400)
        embed.set_image(url=output)

        await message.channel.send(embed=embed)

client.run(token)
