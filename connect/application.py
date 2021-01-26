import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from init import MyOwnPeer2PeerNode

node = MyOwnPeer2PeerNode("192.168.0.102", 5001)

node.start()

node.connect_with_node('192.168.0.104', 5002)

data = str(input('Enter Message --> '))

node.send_to_nodes(data)

node.stop()