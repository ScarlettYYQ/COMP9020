import os
import sys
from collections import defaultdict
try:
	file_name = input('Which data file do you want to use? ')
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
try:
	if not os.path.exists(file_name):
		raise ValueError
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
L=[]
remove_List=[]
Old_List=[]
dictionary=defaultdict(list)
with open(file_name) as data_file:
	for line in data_file:
		L.append(int(line[2]))
		Old_List.append((int(line[2]),int(line[4])))
		dictionary[int(line[2])].append(int(line[4]))
n=len(set(L))
set_L=set(L)
def find(j,l):
	if j in set_L:
		for m in dictionary[j]:
			l.append(m)
			find(m,l)
for i in set_L:
	l=[]
	for j in dictionary[i]:
		if j not in l:
			l.append(j)
			find(j,l)
		else:
			remove_List.append((i,j))
if Old_List:
	print('The nonredundant facts are:')
	for element in Old_List:
		if element not in remove_List:
			print(f'R({element[0]},{element[1]})')
else:
	print('The nonredundant facts are:')
	print('None')
						 

			
		
