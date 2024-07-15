import zmq
import time

def push_sender():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5555")  # Connect to the Pull socket
    
    while True:
        message = "Hello from Push socket!"
        socket.send_string(message)
        print(f"Sent message: {message}")
        time.sleep(1)

if __name__ == "__main__":
    push_sender()
