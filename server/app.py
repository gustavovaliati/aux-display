#!/usr/bin/env python

import asyncio

import websockets

connected_clients = set()


async def echo(websocket, path):
    # Register the new client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Broadcast the message to all connected clients
            for client in connected_clients:
                if client != websocket:  # Don't send the message back to the sender
                    await client.send(message)
    finally:
        # Unregister the client when it disconnects
        connected_clients.remove(websocket)


start_server = websockets.serve(echo, "0.0.0.0", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server is running on ws://localhost:8080")
asyncio.get_event_loop().run_forever()
