import asyncio
import websockets

async def receive_data():
    uri = "ws://localhost:8000/stream"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            print(data)

asyncio.run(receive_data())
