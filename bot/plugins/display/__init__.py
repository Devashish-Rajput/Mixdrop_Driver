#!/usr/bin/env python3

from bot.plugins.display.time import time_data

async def progress(current, total, up_msg, message, start_time):

    try:
        await message.edit(
            text=f"{up_msg} {current * 100 / total:.1f}% in {time_data(start_time)}"
        )
    except Exception as e:
        await message.edit(
            text=f"ERROR: {e}"
        )

