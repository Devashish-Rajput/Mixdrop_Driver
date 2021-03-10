#!/usr/bin/env python3
# This is bot coded reused by https://github.com/Devashish-Rajput/ and used for educational purposes only

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select():
    upload_selection = [
        [
            InlineKeyboardButton(
                "MixDrop",
                callback_data="MixDrop"
            ),
            InlineKeyboardButton(
                "File.io",
                callback_data="File.io"
            )
        ],
    ]
    return InlineKeyboardMarkup(upload_selection)
