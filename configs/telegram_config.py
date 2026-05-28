# That's all about telegram messages/bio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from core.system import get_now_playing_info

async def get_tgbio_text():
    # this text will be inserted into your bio when you update music or something similar. The maximum text without premium telegram is 70 CHARACTERS, with a subscription - 140 CHARACTERS.
    # get_now_playing_info returns "app" (spotify.exe, chrome.exe like this), "artist" and "music title" 
    app, artist, title = await get_now_playing_info()
    
    if not app and not artist and not title:
        return f"Nothing right now, but it's not forever"
    
    return f'^_~ NOW PLAYING - "{artist} - {title}"'[:70]