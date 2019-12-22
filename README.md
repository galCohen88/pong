# Pong
Access local APIs using public domains 

## Hardware requirements

Publicly available machine (Linux) running with python 3.6, will be called remote in this README.md file

### Four main components

1. Remote - Public web server (API)
2. Remote - WebSocket handler
3. Remote - Redis pubsub broker
4. Local  - Listener
5. Development server - what ever language / http API

### Overall architecture

![Alt text](Pong.png?raw=true "Diagram")


* Remote API will get any request method / URL and will decode it as pubsub message

* The message will be consumed by WebSocket handler and will be sent to client machine

* The Listener in client machine would initiate the request once its received in the local machine

* Listener would return response value via websocket to calling remote WebSocket handler and returned to public web server API

 
