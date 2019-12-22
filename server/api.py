import json

from flask import Flask, request
import redis

app = Flask(__name__)

rc = redis.Redis()
ps = rc.pubsub()
ps.subscribe(['responses'])


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    request_value = {'path': path, str('method'): str(request.method), 'body': str(request.data), 'headers': json.dumps(dict(request.headers))}
    rc.publish('requests', json.dumps(request_value))
    response = None
    for response_recv in ps.listen():
        if response_recv.get('data') in [1, 2]:
            continue
        response_event = json.loads(response_recv['data'])
        body = json.dumps(response_event['body'])
        status = response_event['status_code']
        headers = json.loads(response_event['headers'])
        response = app.response_class(response=body, status=status, headers=headers)
        break
    return response


if __name__ == '__main__':
    app.run(port='8080', host='ec2-54-172-251-23.compute-1.amazonaws.com')
