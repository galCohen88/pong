import asyncio
import websockets
import redis

rc = redis.Redis()
ps = rc.pubsub()
ps.subscribe(['requests'])


async def handle_request(websocket, path):
    initiation = await websocket.recv()
    print(initiation)
    for request_recv in ps.listen():
        if request_recv['data'] in [1, 2]:
            continue
        print(request_recv['data'])
        await websocket.send(request_recv['data'])
        response = await websocket.recv()
        rc.publish('responses', response)
        print('published response!')


start_server = websockets.serve(handle_request, "ec2-54-172-251-23.compute-1.amazonaws.com", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
