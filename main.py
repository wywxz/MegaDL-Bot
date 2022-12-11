# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>

import os
import asyncio
from config import Config
from pyrogram import Client, idle
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(_):
    return web.json_response(
        {
            "server_status": "running"
        }
    )

def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_services():
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="megadl")
    app = Client(
        "MegaDL-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.start()
    print('\n\n>>> MegaDL-Bot Started. Join @AsmSafone!')
    server = web.AppRunner(web_server())
    await server.setup()
    await web.TCPSite(server, "0.0.0.0", 8080).start()
    idle()
    app.stop()
    print('\n\n>>> MegaDL-Bot Stopped. Join @AsmSafone!')

if __name__ == "__main__" :
    start_services()