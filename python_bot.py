import discord
from discord.ext import commands
from discord.ui import Button, View

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Create Button View

class PanelButtons(View):
    def __init__(self):
        super().__init__(timeout=None)  # Buttons never expire
        
        # Buy Panel Button
        buy_button = Button(
            label="🎫 BUY PANEL",
            style=discord.ButtonStyle.green,
            custom_id="buy_panel"
        )
        buy_button.callback = self.buy_panel_callback
        self.add_item(buy_button)
        
        # Contact Button
        contact_button = Button(
            label="📩 CONTACT",
            style=discord.ButtonStyle.blurple,
            custom_id="contact"
        )
        contact_button.callback = self.contact_callback
        self.add_item(contact_button)
    
    async def buy_panel_callback(self, interaction: discord.Interaction):
        # CHANGE THIS: Replace with your ticket channel ID
        ticket_channel_id = 1430944211527798824  # ← PUT YOUR CHANNEL ID HERE
        
        channel = bot.get_channel(ticket_channel_id)
        
        if channel:
            await interaction.response.send_message(
                f"✅ **Thank you for your interest!**\n"
                f"Please head to {channel.mention} to create a ticket and complete your purchase!",
                ephemeral=True  # Only visible to user who clicked
            )
        else:
            # If channel not found, show alternative
            await interaction.response.send_message(
                "✅ **Thank you for your interest!**\n"
                "Please DM <@1376959531275391016> to complete your purchase!",
                ephemeral=True
            )
    
    async def contact_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "📩 **Contact Information:**\n\n"
            "**Discord:** <@1376959531275391016>\n"
            "**For purchases:** DM me directly or create a ticket!\n\n"
            "⚡ Fast response guaranteed!",
            ephemeral=True
        )

@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')

@bot.command()
async def panel(ctx):
    # Create the embed
    embed = discord.Embed(
        title="DARK REGEDIT PREMIUM PANEL",
        color=0xDC143C,  # Crimson red color
        timestamp=discord.utils.utcnow()
    )
    
    # Add fields for each section
    embed.add_field(
        name="PREMIUM V1",
        value="",
        inline=False
    )
    
    embed.add_field(
        name="AIM / SNIPER FUNCTION",
        value=(
            "```[+] AIMBOT AI\n\n"
            "[+] SNIPER SCOPE (AWM + AWM-Y + M82B + M24)\n\n"
            "[+] AWM/AWM-Y FAST SWITCH\n\n"
            "[+] M82B FAST SWITCH\n\n"
            "[+] M24 FAST SWITCH\n\n"
            "[+] M82B LOCATION\n\n"
            "[+] AWM LOCATION\n\n"
            "[+] AWM-Y LOCATION```"
        ),
        inline=False
    )
    
    embed.add_field(
        name="BRUTAL / LOCATION",
        value=(
            "```[+] SPEED HACK \n\n"
            "[+] WALL HACK \n\n"
            "[+] FAST LANDING\n\n"
            "[+] CAMERA LEFT\n\n"
            "[+] AIM FOV/ GLITCH FIRE\n\n"
            "[+] CHARMS MENU\n\n"
            "[+] STREAMER LOCATION\n\u200b"
            "```"
        ),
        inline=False
    )
    
    
    
    embed.add_field(
        name="💰 PRICING",
        value=(
            "```"
            "Lifetime: $15.00 / 1500tk / 1300 INR\n\n"
            "Per Update: $5.00 / 500tk / 400 INR"
            "```"
        ),
        inline=False
    )

    

    embed.add_field(
        name="📩 HOW TO BUY",
        value=(
            "**Click the button below to purchase!**\n"
            "Or DM <@1376959531275391016> directly\n\u200b"
        ),
        inline=False
    )

    
    # Set image banner
    
    embed.set_image(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3p4YmNpMWgxamhnbGJ2dDczMmszZzUwZzF3Ym9lYzZ2OWJib2Y4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4ES2KU2BbGrMjSzfLH/giphy.gif")
    
    
    # Set footer
    embed.set_footer(text="DARK REGEDIT MEANS SAFE")

    
    
    # Create view with buttons
    view = PanelButtons()
    
    # Send embed with buttons
    await ctx.send(embed=embed, view=view)

# Run the bot
bot.run('MTQ0NDY5NzcyNTg5ODU5MjI1Ng.GhIkV2.DghQXGM4qbd5SsnMtnRBKpYu3TuC87HchSJKAM')