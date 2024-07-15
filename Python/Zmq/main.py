import zmq
import time
import threading

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    
    while True:
        topic = b"updates"
        msg = b"Update message!"
        socket.send_multipart([topic, msg])
        time.sleep(1)

def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt(zmq.SUBSCRIBE, b"updates")
    
    while True:
        topic, msg = socket.recv_multipart()
        print(f"Received: {msg.decode('utf-8')}")

def worker():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://localhost:5556")
    
    while True:
        msg = socket.recv_string()
        print(f"Worker received: {msg}")
        time.sleep(1)
        socket.send_string("Work done by worker")

if __name__ == "__main__":
    # Start the publisher in a separate thread
    pub_thread = threading.Thread(target=publisher)
    pub_thread.start()
    
    # Start the subscriber in a separate thread
    sub_thread = threading.Thread(target=subscriber)
    sub_thread.start()
    
    # Start the worker
    worker()
