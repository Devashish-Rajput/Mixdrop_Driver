#!/usr/bin/env python3
# This is bot coded reused by https://github.com/Devashish-Rajput/ and used for educational purposes only

import pyrogram
from bot.filetocloud import CloudBot
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    CloudBot().run()

