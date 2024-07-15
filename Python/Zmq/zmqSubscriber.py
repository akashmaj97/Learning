import zmq
import json

def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all topics
    
    while True:
        message = socket.recv_string()
        data = json.loads(message)
        process_data(data)

def process_data(data):
    # Example processing function, you can modify this as needed
    print(f"Received: ID={data['id']}, Value={data['value']}")

if __name__ == "__main__":
    subscriber()
