# Written by *** for COMP9021

from binary_tree_adt import *
from math import log




class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.value != None:
	        position = 2 ** int(log(self.size() + 1, 2))
    	    new_position = position
        	node = self
	        exist_node = [node]
    	    for i in range(int(log(self.size() + 1, 2)) - 1):
        	    position //= 2
            	if self.size() + 1 < new_position + position:
                	node = node.left_node
            	else:
                	new_position += position
                	node = node.right_node
            	exist_node.append(node)
	        if self.size() + 1 == new_position:
    	        node.left_node = BinaryTree(value)
        	    node1 = node.left_node
	        else:
    	        node.right_node = BinaryTree(value)
        	    node1 = node.right_node
	        while exist_node:
    	        node2 = node1
        	    node1 = exist_node.pop()
            	if node2.value < node1.value:
                	node2.value, node1.value = node1.value, node2.value
        else:
        	self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return




