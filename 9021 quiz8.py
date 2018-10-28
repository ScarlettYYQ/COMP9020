# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
	for i in range(len(grid)):
		print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner():
	if grid[0][0]!=1:
		return ([])
	queue=Queue(10)
	queue.enqueue(([(0,0)],START_Point))
	while queue.is_empty()==False:
		l=[]
		l=queue.dequeue()
		temp_path=l[0]

		realtime_direction_list=l[1]

		test_point=temp_path[len(temp_path)-1]

		for i in realtime_direction_list:
			l=[]
			#print(i)
			if i == (-1,0):
				next_point=(test_point[0]-1,test_point[1])
				l=N
			if i == (1,0):
				next_point=(test_point[0]+1,test_point[1])
				#print('next_point',next_point)
				l=S
			if i == (0,-1):
				next_point=(test_point[0],test_point[1]-1)
				l=W
			if i == (0,1):
				next_point=(test_point[0],test_point[1]+1)
				l=E
			if not (next_point[0]>=10 or next_point[0]<0 or next_point[1]>=10 or next_point[1]<0):
				if grid[next_point[0]][next_point[1]]!=1:
					continue
				if next_point in temp_path : 
					continue
				path=temp_path[:]
				path.append(next_point)
				queue.enqueue((path,l))
			else:
				continue

	return temp_path


	
provided_input = input('Enter one integer: ')
try:
	for_seed = int(provided_input)
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
START_Point=[(1,0),(0,1)]
N=[(0,1),(-1,0),(0,-1)]
S=[(0,-1),(1,0),(0,1)]
W=[(-1,0),(0,-1),(1,0)]
E=[(1,0),(0,1),(-1,0)]

path = leftmost_longest_path_from_top_left_corner()

if not path:
	print('There is no path from the top left corner.')
else:
	print(f'The leftmost longest path from the top left corner is: {path}')
		   
