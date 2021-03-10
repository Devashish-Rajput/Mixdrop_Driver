#!/usr/bin/env python3
# This is bot coded reused by https://github.com/Devashish-Rajput/ and used for educational purposes only
from bot.filetocloud import CloudBot
from bot.plugins.helpers.dowloader import fileDownload


@CloudBot.on_callback_query()
async def server_selection(client, server):
    await fileDownload(client, server)
