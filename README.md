# pong
Access local APIs using public domains

### Four main components

1. Remote - Public web server (API)
2. Remote - WebSocket handler
3. Remote - Redis pubsub broker
4. Local  - Listener


### Overall architecture
Remote API will get any request method / URL and will decode it as pubsub message

The message will be consumed by WebSocket handler and will be sent to client machine

The Listener in client machine would initiate the request once its received in the local machine

Listener would return response value via websocket to calling remote WebSocket handler and returned to public web server API

 
