import asyncio
import websockets

async def test():
    async with websockets.connect('ws://127.0.0.1:8080') as websocket:
        # Send the initial message
        await websocket.send('{"type": "join","roomId": "clzq337w10002ejwwf5ayw1jj", "authorId": "clzpxoljo0000vatwog7iacc5", "content": "Frost gui delicioso"}')
        await websocket.send('{"type": "message","roomId": "clzq337w10002ejwwf5ayw1jj", "authorId": "clzpxoljo0000vatwog7iacc5", "content": "Frost gui delicioso"}')
        # Keep the connection open and listen for incoming messages
        try:
            while True:
                response = await websocket.recv()
                print(response)
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")

asyncio.get_event_loop().run_until_complete(test())
