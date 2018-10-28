import sys
from random import seed, randint
import copy
dim = 10
grid = [[None] * dim for _ in range(dim)]
homogenous_grid = [[None] * dim for _ in range(dim)]
def display_grid(change_grid):
		for i in range(dim):
				print('   ', ' '.join(str(change_grid[i][j]) for j in range(dim)))
def largest_homogenous(i,j):
		global size_of_largest_homogenous_region_from_top_left_corner
		if homogenous_grid[i][j] == corner:
				homogenous_grid[i][j]='*'
				size_of_largest_homogenous_region_from_top_left_corner +=1
				if i!=0:
						largest_homogenous(i-1,j)
				if i < dim-1:
						largest_homogenous(i+1,j)
				if j!= 0:
						largest_homogenous(i,j-1)
				if j< dim-1:
						largest_homogenous(i,j+1)           
def checkers_structure(i,j,size):
		if grid[i][j]!='*':
				num=grid[i][j]
				grid[i][j]='*'
				size +=1
				if i!=0 and grid[i-1][j] != num and grid[i-1][j]!='*':
						size+=checkers_structure(i-1,j,0)
				if i < dim-1 and grid[i+1][j] != num and grid[i+1][j]!='*':
						size+=checkers_structure(i+1,j,0)
				if j!= 0 and grid[i][j-1] != num and grid[i][j-1]!='*':
						size+=checkers_structure(i,j-1,0)
				if j< dim-1 and grid[i][j+1] != num and grid[i][j+1]!='*':
						size+=checkers_structure(i,j+1,0)
		return size       
def max_size(i,j):
		global max_size_of_region_with_checkers_structure
		for i in range(dim):
				for j in range(dim):
						if grid[i][j]!='*':
								size_of_region_with_checkers_structure=checkers_structure(i,j,0)
								if max_size_of_region_with_checkers_structure < size_of_region_with_checkers_structure:
										max_size_of_region_with_checkers_structure = size_of_region_with_checkers_structure
try:
		arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
		print('Incorrect input, giving up.')
		sys.exit()
try:
		arg_for_seed, density = int(arg_for_seed), int(density)
		if arg_for_seed < 0 or density < 0:
				raise ValueError
except ValueError:
		print('Incorrect input, giving up.')
		sys.exit()
seed(arg_for_seed)
for i in range(dim):
		for j in range(dim):
				grid[i][j] = int(randint(0, density) != 0)

print('Here is the grid that has been generated:')
display_grid(grid)

size_of_largest_homogenous_region_from_top_left_corner  = 0
homogenous_grid= copy.deepcopy(grid)
corner=grid[0][0]
largest_homogenous(0,0)
print('The size_of the largest homogenous region from the top left corner is '
			f'{size_of_largest_homogenous_region_from_top_left_corner}.'
		 )
max_size_of_region_with_checkers_structure = 0
max_size(0,0)
print('The size of the largest area with a checkers structure is '
			f'{max_size_of_region_with_checkers_structure}.'
		 )




						

