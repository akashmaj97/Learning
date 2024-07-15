import zmq

def pull_receiver():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://*:5555")  # Bind to port 5555 on all network interfaces
    
    print("Pull socket started, waiting for messages...")

    while True:
        message = socket.recv_string()
        print(f"Received message: {message}")

if __name__ == "__main__":
    pull_receiver()
