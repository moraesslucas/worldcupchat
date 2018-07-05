#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json

USERS = set()

async def messenger(websocket, path):
    USERS.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            print(f"{message}")
            await asyncio.wait([user.send(message) for user in USERS])
    except:
        USERS.remove(websocket)

start_server = websockets.serve(messenger, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
