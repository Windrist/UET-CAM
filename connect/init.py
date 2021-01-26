#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# MyOwnPeer2PeerNode is an example how to use the p2pnet.Node to implement your own peer-to-peer network node.        #
#######################################################################################################################
from p2pnetwork.node import Node

class MyOwnPeer2PeerNode (Node):

    # Python class constructor
    def __init__(self, host, port):
        super(MyOwnPeer2PeerNode, self).__init__(host, port, None)
        # print("MyPeer2PeerNode: Started")

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        # print("outbound_node_connected: " + node.id)
        pass
        
    def inbound_node_connected(self, node):
        # print("inbound_node_connected: " + node.id)
        pass

    def inbound_node_disconnected(self, node):
        # print("inbound_node_disconnected: " + node.id)
        pass

    def outbound_node_disconnected(self, node):
        # print("outbound_node_disconnected: " + node.id)
        pass

    def node_message(self, node, data):
        # print("node_message from " + node.id + ": " + str(data))
        print("Get message from Node: " + str(data))
        
    def node_disconnect_with_outbound_node(self, node):
        # print("node wants to disconnect with oher outbound node: " + node.id)
        pass
        
    def node_request_to_stop(self):
        # print("node is requested to stop!")
        pass
        