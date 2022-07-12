import websockets
import os
import json
import asyncio
import time

PORT = 7900
orders_ready = []
orders_progress = []
orders = []
print("Server started on port " + str(PORT))

async def echo(websocket,path):
    print("Client connected")
    try:
        async for message in websocket:
            if "Prog" in message:
                finalnumber = message.replace("Prog", "")
                orders_progress.append(int(finalnumber))
                orders.remove(int(finalnumber))
                print("Orders progress: " + str(orders_progress))
            elif "Ready" in message:
                finalnumber = message.replace("Ready", "")
                orders_ready.append(int(finalnumber))
                orders_progress.remove(int(finalnumber))
                print("Orders ready: " + str(orders_ready))
            elif message == "Status":
                update = """
                -----------------------------------
                Orders: 
                """+str(orders)+"""
                Orders in progress: 
                """+str(orders_progress)+"""
                Orders ready: 
                """+str(orders_ready)+"""
                -----------------------------------
                """
                await websocket.send(update)
            else:
             orders.append(int(message))
             print("Orders list: " + str(orders))
             await websocket.send("Order number " + message + " received. Thank you for choosing McArioni!")   
    except websockets.exceptions.ConnectionClosed as e:
        print("Connection closed")



async def delete():
    while True:
        await asyncio.sleep(9)
        if not orders_ready:
            print("List empty")
            time.sleep(0.1)
        else:
            orders_ready.pop(0)
            print("Orders ready list: " + str(orders_ready))
            time.sleep(0.1)


start_server = websockets.serve(echo, "localhost", PORT)
loop = asyncio.get_event_loop()
asyncio.ensure_future(start_server)
asyncio.ensure_future(delete())
loop.run_forever()

