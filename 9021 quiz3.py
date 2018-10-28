from random import seed, randint
import sys
from collections import defaultdict
from collections import Counter 



#def display_grid():
#    for i in range(len(grid)):
#        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
L_N=[]
L_S=[]
L_W=[]
L_E=[]

def digui(m):
	if m==-n:
		return int(grid[o+n][p+m])
	else:
		return int(grid[o+n][p+m])+int(digui(m-1))

def xinsilu():
	L=[]
	t=False
	global o
	global p
	for o in range (dim-1):
		for p in range (1,dim-1):
			if int(grid[o][p])==1:
				global n
				t=True
				for n in range (1,new_dim//2):
					if p-n>=0 and p+n<dim and o+n<dim:
						m=n
						digui_1=digui(m)
						if digui_1 == 2*n+1:
							if t:
								L.append(n+1)
								t=False
							else:
								L.pop()
								L.append(n+1)
						else:
							break
							
					else:
						break
			
	L_1=Counter(L)
	L_2= L_1.most_common()
	L_2=list(reversed(L_2))
	return L_2
	
	
					
					


				



def grid_90():
	global grid
	grid.reverse()
	grid=[[j[i] for j in grid] for i in range(len(grid[0]))]



def triangles_in_grid():
	L_N=xinsilu()
	grid_90()
	L_W=xinsilu()
	grid_90()
	L_S=xinsilu()
	grid_90()
	L_E=xinsilu()
	triangles={}
	if len(L_N)!=0:
		N_dic={'N':L_N}
		triangles.update(N_dic)
	if len(L_S)!=0:
		S_dic={'S':L_S}
		triangles.update(S_dic)
	if len(L_W)!=0:
		W_dic={'W':L_W}
		triangles.update(W_dic)
	if len(L_E)!=0:
		E_dic={'E':L_E}
		triangles.update(E_dic)
	return triangles

try:
	arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
try:
	arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
	if arg_for_seed < 0 or density < 0 or dim < 0:
		raise ValueError
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')



#display_grid()
for i in range(len(grid)):
	for j in range(len(grid)):
		grid[i][j]= (str(int(grid[i][j] != 0)))

new_dim=dim
if dim%2!=0:
	new_dim=dim+1
triangles = triangles_in_grid()

for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
	print(f'\nFor triangles pointing {direction}, we have:')
	for size, nb_of_triangles in triangles[direction]:
		triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
		print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
