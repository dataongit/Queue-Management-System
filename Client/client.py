import websockets
import asyncio
import os


async def listen():
    url = "ws://127.0.0.1:7900"

    async with websockets.connect(url) as ws:
        while True:
                print("Order number: ")
                order_number = input()
                await ws.send(order_number)
                msg = await ws.recv()
                print(msg)




asyncio.get_event_loop().run_until_complete(listen())

