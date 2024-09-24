#!/usr/bin/env python

import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Path to your HTML files
HTML_DIR = os.path.join(os.path.dirname(__file__), "html")

# Serve static HTML files
app.mount("/static", StaticFiles(directory=HTML_DIR), name="static")

# Connected clients set
connected_clients = set()


# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")
            # Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(data)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)


@app.get("/countdown")
async def get_countdown():
    with open(os.path.join(HTML_DIR, "countdown.html")) as f:
        return HTMLResponse(content=f.read(), status_code=200)


# Serve control.html when visiting /control
@app.get("/control")
async def get_control():
    with open(os.path.join(HTML_DIR, "control.html")) as f:
        return HTMLResponse(content=f.read(), status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8081)
