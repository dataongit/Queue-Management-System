import websockets
import asyncio
import os

async def send():
    url = "ws://127.0.0.1:7900"

    async with websockets.connect(url) as ws:
            while True:
                await ws.send("Status")
                print(await ws.recv())
                print("Give instruction: ")
                instruction = input()
                await ws.send(instruction)
                await asyncio.sleep(1)




asyncio.get_event_loop().run_until_complete(send())
