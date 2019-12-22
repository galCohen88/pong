import asyncio
import json

import websockets
from pip._vendor import requests


LOCALHOST = 'http://localhost:8080/{path}'


async def handle_request():
    # uri = "ws://localhost:8765"
    uri = "ws://ec2-54-172-251-23.compute-1.amazonaws.com:8765"

    async with websockets.connect(uri) as websocket:
        await websocket.send('initiated web socket')
        while True:
            try:
                request_event = await websocket.recv()
                response = dispatch_request(request_event)
                response_body = {'status_code': response.status_code, 'body': response.content.decode('utf-8'), 'headers': json.dumps(dict(response.headers))}
                await websocket.send(json.dumps(response_body))
            except Exception as e:
                print(f"Error handling request message {e}")


def dispatch_request(request_message):
    if request_message is None:
        return
    request_dict = json.loads(request_message.decode("utf-8"))
    method = request_dict['method']
    headers = json.loads(request_dict['headers'])
    url = LOCALHOST.format(path=request_dict['path'])
    data = request_dict['body']
    response = requests.request(method, headers=headers, url=url, data=data)
    return response


asyncio.get_event_loop().run_until_complete(handle_request())


