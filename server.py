#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json
import pprint

USERS = set()
ROOMS = {}
EXCHANGES = []
STICKERS = {'Lucas': ["1", "2", "3"], 'Teste': ["4", "5", "6"]}


async def messenger(web_socket, path):
    USERS.add(web_socket)
    try:
        while True:
            message = await web_socket.recv()
            data = json.loads(message)
            set_user(web_socket, data.get("sender"))
            print(data)
            if data.get("type", 0) == "join_room":
                await join_room(web_socket, data.get("content"))
                await asyncio.wait([web_socket.send(message)])
                continue
            if data.get("type", 0) == "open_private":
                print(data)
                await join_room(web_socket, data.get("sender") + data.get("content"))
                data.update({"room": data.get("sender") + data.get("content")})
                message = json.dumps(data)

            if data.get("type", "message") == "private":
                user = ROOMS[data.get("room")]
                print(user)
                await asyncio.wait([user.send(message), web_socket.send(message)])
                continue

            if data.get("type", "message") == "exchange":
                trade = False
                print(data.get("mine"))
                print(data.get("sender"))
                print(data.get("mine") not in STICKERS.get(data.get("sender")))
                print(STICKERS)
                print(STICKERS.get(data.get("sender")))
                print(EXCHANGES)
                if data.get("mine") not in STICKERS.get(data.get("sender")):
                    await asyncio.wait([web_socket.send(message)])
                    continue
                
                for exchange in EXCHANGES:
                    aux = data.copy()
                    del aux["room"]
                    del aux["type"]
                    aux["accept"] = data.get("sender")
                    aux["sender"] = data.get("room")
                    aux["mine"] = data.get("his")
                    aux["his"] = data.get("mine")
                    print('Accept: ', data.get("room"))
                    print('Exchange: ', exchange)
                    print('Aux: ', aux)
                    if (exchange == aux):
                        print("Troca")
                        trade = True
                        
                        if data.get("mine") in STICKERS.get(data.get("sender")):
                            STICKERS.get(data.get("sender")).remove(data.get("mine"))
                        if data.get("his") in STICKERS.get(data.get("room")):
                            STICKERS.get(data.get("room")).remove(data.get("his"))


                        STICKERS.get(data.get("sender")).append(data.get("his"))
                        STICKERS.get(data.get("room")).append(data.get("mine"))
                        messageSender = {'sender': data.get("sender"), 'type': 'exchange_success', 'content': 'A troca foi efetuada com sucesso!', 'room': data.get("room"), 'stickers': ', '.join(STICKERS.get(data.get("sender")))}
                        messageSender = json.dumps(messageSender)
                        messageRoom = {'sender': data.get("sender"), 'type': 'exchange_success', 'content': 'A troca foi efetuada com sucesso!', 'room': data.get("room"), 'stickers': ', '.join(STICKERS.get(data.get("room")))}
                        messageRoom = json.dumps(messageRoom)
                        print(data.get("room"))
                        print(ROOMS)
                        await asyncio.wait([ROOMS[data.get("sender")].send(messageSender), ROOMS[data.get("room")].send(messageRoom)])
                        EXCHANGES.remove(exchange)


                if trade is False:
                    EXCHANGES.append({"sender": data.get("sender"), "accept": data.get("room"), "mine": data.get("mine"), "his": data.get("his")})

            
            await asyncio.wait([user.send(message) for user in USERS])
    except:
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
