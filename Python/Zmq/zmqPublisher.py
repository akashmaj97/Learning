import zmq
import time
import random
import json

class Data:
    def __init__(self, id, value):
        self.id = id
        self.value = value
    
    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value
        }

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    
    while True:
        # Generate some example data
        data_obj = Data(id=random.randint(1, 100), value=random.uniform(0.0, 1.0))
        data_json = json.dumps(data_obj.to_dict())
        
        # Publish the data
        socket.send_string(data_json)
        
        print(f"Published: {data_json}")
        time.sleep(1)

if __name__ == "__main__":
    publisher()
