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
distance=[]
fish_amount=[]
with open(file_name) as data_file:
	for line in data_file:
		line=line.replace(" ",",")
		line=line.split(',')
		distance.append(int(line[0]))
		fish_amount.append(int(line[1]))
def IF_THIS_CHECK_NUM_IS_OK(check_num):
	temp_fish=fish_amount[:]
	for i in range(len(fish_amount)-1):
		if temp_fish[i]<check_num:
			temp_fish[i+1]=temp_fish[i+1] - ((check_num - temp_fish[i])+(distance[i+1] - distance[i]))
		if temp_fish[i] > check_num:
			if temp_fish[i]-check_num > distance[i+1] - distance[i]:
				temp_fish[i+1]=temp_fish[i+1] + ((temp_fish[i] - check_num)-(distance[i+1] - distance[i]))
	return temp_fish[len(temp_fish)-1]
def check_loop():
	average=int(sum(fish_amount)/len(fish_amount))
	min_fish_amount=min(fish_amount)
	check_num=int((average+min_fish_amount)/2)
	T_OR_F=False
	while T_OR_F==False:
		result_temp=IF_THIS_CHECK_NUM_IS_OK(check_num)
		if result_temp==check_num:
			T_OR_F=True
			break
		elif result_temp>check_num:
			min_fish_amount=check_num
			check_num=int(average+min_fish_amount)/2
		else:
			temp_average=check_num
			temp_check_num=(temp_average+min_fish_amount)/2
			if abs(check_num - temp_check_num) < 0.01:
				T_OR_F=True
				break
			else:
				check_num=temp_check_num
	return(check_num)
if distance:
	print(f'The maximum quantity of fish that each town can have is {int(check_loop())}.')
else:
	print('The maximum quantity of fish that each town can have is None.')
			

