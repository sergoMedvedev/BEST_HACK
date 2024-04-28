import asyncio

from services.master.protos.api import run

if __name__ == '__main__':
    asyncio.run(run())