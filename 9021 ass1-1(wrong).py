import os
import sys
from collections import defaultdict



Global_Y=defaultdict(list)
Global=defaultdict(list)
Global_L=defaultdict(list)
l=[]
def New_global():
	for i in range(n-1,0,-1):
		for j in range (i-1):
			if Global[i][j]+Global[i-1][j]>Global[i][j+1]+Global[i-1][j]:
				Global[i-1][j]=Global[i][j]+Global[i-1][j]
				Global_L[i-1][j]=Global_L[i][j]
			elif Global[i][j]+Global[i-1][j] == Global[i][j+1]+Global[i-1][j]:
				Global[i-1][j]=Global[i][j]+Global[i-1][j]
				Global_L[i-1][j]=Global_L[i][j]+Global_L[i][j+1]
			else:
				Global[i-1][j]=Global[i][j+1]+Global[i-1][j]
				Global_L[i-1][j]=Global_L[i][j+1]

def leftpath():
	if Global_Y:
		l.append(Global_Y[1][0])
		m=0
		for k in range(2,n):
			if Global[k][m]>=Global[k][m+1]:
				l.append(Global_Y[k][m])
			else:
				l.append(Global_Y[k][m+1])
				m+=1
	return l


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

with open(file_name) as data_file:
	n=1
	for line in data_file:
		line=line.replace(" ","")
		line=line.replace("\n","")
		if len(line)!=0:
			for i in range(len(line)):
				Global_Y[n].append(int(line[i]))
				Global[n].append(int(line[i]))
				Global_L[n].append(1)
			n+=1
New_global()
leftpath()
if Global:
	print(f'The largest sum is: {Global[1][0]}')
else:
	print('The largest sum is: None')
if Global_L:
	print(f'The number of paths yielding this sum is: {Global_L[1][0]}')
else:
	print('The number of paths yielding this sum is: None')
if l:
	print(f'The leftmost path yielding this sum is: {l}')
else:
	print('The leftmost path yielding this sum is: None')