import asyncio
from core.telegram import main_tg

async def main():
    await asyncio.gather(
        main_tg()
    )

asyncio.run(main())