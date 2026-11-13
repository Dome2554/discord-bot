import os
import threading
import discord
from discord.ext import commands
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_web_server():
    port = int(os.getenv("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'บอท {bot.user} ออนไลน์แล้วบน Cloud!')

@bot.command(name='สูตรคูณ')
async def multiplication(ctx, number: int):
    table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 13)])
    await ctx.send(f"```\nแม่สูตรคูณแม่ {number}:\n{table}\n```")

bot.run(os.getenv('TOKEN'))
