class Node:
    def __init__(self, node_id, docker_container):
        self.node_id = node_id
        self.docker_container = docker_container
        self.peers = []

    def __str__(self):
        return "Node {} with {} CPU units and {} MB of memory".format(self.node_id, self.docker_container.cpu_capacity,self.docker_container.memory_capacity)

    def connect_to_peer(self, node):
        self.peers.append(node)
