# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *
L=[]
class stack:
	def __init__(self):
		self.stack_l=[]
	def add_value(self, data_value):
		if data_value not in self.stack_l:
			self.stack_l.append(data_value)
			return True
		else:
			return False
	def top_one(self):
			return self.stack_l.pop()
	def empty(self):
		if len(self.stack_l)==0:
			return False
		else:
			return True

def max_diff_in_consecutive_leaves(tree):
	Tree=stack()
	Tree.add_value(tree)
	while Tree.empty():
		temp_top_node=Tree.top_one()
		if temp_top_node.value!=None:
			if temp_top_node.height()!=0:
				if temp_top_node.right_node.value!=None:
					Tree.add_value(temp_top_node.right_node)
				if temp_top_node.left_node.value!=None:
					Tree.add_value(temp_top_node.left_node)
			else:
				L.append(temp_top_node.value)
	max_diff=0
	l=sorted(L)
	for i in range(len(l)-1):
		if l[i+1]-l[i]>max_diff:
			max_diff=l[i+1]-l[i]
	return max_diff
		
		
			
		


provided_input = input('Enter two integers, the second one being positive: ')
try:
	arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
try:
	arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
	if nb_of_nodes < 0:
		raise ValueError
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
	datum = randrange(1000000)
	tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
		   
