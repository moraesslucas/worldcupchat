#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json

USERS = set()
ROOMS = {}


async def messenger(web_socket, path):
    USERS.add(web_socket)
    try:
        while True:
            message = await web_socket.recv()
            data = json.loads(message)
            set_user(web_socket, data.get("sender"))
            if data.get("type", 0) == "join_room":
                await join_room(web_socket, data.get("content"))
                continue
            if data.get("type", 0) == "open_private":
                print(data)
                await join_room(web_socket, data.get("sender") + data.get("content"))
                data.update({"room": data.get("sender") + data.get("content")})
                message = json.dumps(data)

            if data.get("room", "Broadcast") != "Broadcast" and data.get("type", 0) == "message":
                user = ROOMS[data.get("room")]
                user.send(message)
                print(user)

            await asyncio.wait([user.send(message) for user in USERS])
    except ImportError:
        USERS.remove(web_socket)


async def join_room(web_socket, room):
    if ROOMS.get(room, None) is None:
        ROOMS.update({room: []})
    ROOMS[room].append(web_socket)


def set_user(web_socket, sender):
    ROOMS.update({sender: web_socket})


start_server = websockets.serve(messenger, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
