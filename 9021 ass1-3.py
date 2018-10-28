# Written by *** for COMP9021
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
dictionary=defaultdict(list)
with open(file_name) as data_file:
	n=0
	for line in data_file:
		line=line.replace(" ",",")
		line=line.split(',')
		for num in range(len(line)):
			dictionary[n].append(int(line[num]))
		n+=1
def check_in_or_not(X,Y,NO):
	result=1
	repeat_point=0
	L=[]
	for i in range(n):
		if i != NO:
			if X > dictionary[i][0] and X < dictionary[i][2] and Y > dictionary[i][1] and Y < dictionary[i][3]:
				result=0
				break
			if (X > dictionary[i][0] and X < dictionary[i][2] and Y==dictionary[i][1]) or (X > dictionary[i][0] and X < dictionary[i][2] and Y==dictionary[i][3]):
				repeat_point=1
			if (Y > dictionary[i][1] and Y < dictionary[i][3] and X==dictionary[i][0]) or (Y > dictionary[i][1] and Y < dictionary[i][3] and X==dictionary[i][2]):
				repeat_point=1
	L=[result,repeat_point]
	return (L)
	
def check_upper_lower():
	Result=0
	repeat_point=0
	L=[]
	for i in range(n):
		for X in range(dictionary[i][0],dictionary[i][2]+1):
			L=check_in_or_not(X,dictionary[i][1],i)
			Result=Result+L[0]
			repeat_point+=L[1]                             
			L=check_in_or_not(X,dictionary[i][3],i)
			Result=Result+L[0]
			repeat_point+=L[1]
		for Y in range(dictionary[i][1]+1,dictionary[i][3]):
			L=check_in_or_not(dictionary[i][0],Y,i)
			Result=Result+L[0]
			repeat_point+=L[1] 
			L=check_in_or_not(dictionary[i][2],Y,i)
			Result=Result+L[0]
			repeat_point+=L[1] 
	return (Result-int(repeat_point/2))


print(f'The perimeter is: {check_upper_lower()}')       


