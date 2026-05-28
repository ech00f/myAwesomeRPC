import asyncio
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def get_now_playing_info():
    manager = await MediaManager.request_async()
    current_session = manager.get_current_session()
    
    if not current_session:
        return

    app_id = current_session.source_app_user_model_id 
    properties = await current_session.try_get_media_properties_async()
    
    return [app_id, properties.artist, properties.title]

# if __name__ == "__main__":
#     asyncio.run(get_now_playing_info())
