# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''

import math
import sys
from math import gcd
from math import sqrt


try:
	numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
try:
	numerator, denominator = int(numerator), int(denominator)
	if numerator <= 0 or denominator <= 0:
		raise ValueError
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()


has_finite_expansion = False
sigma = ''
tau = ''
integral_part=0




if numerator % denominator == 0:
	has_finite_expansion = True
	integral_part=int(numerator / denominator)

else:  
	transform = gcd(numerator, denominator)
	numerator_gcd = int(numerator / transform)
	denominator_gcd = int(denominator / transform)
	integral_part=str(int(numerator // denominator))
	L=[]
	l=[]
	L_1=[]
	L_2=[]
	new_numerator=numerator_gcd
	L.append(int(new_numerator//denominator_gcd))
	while True:
			numerator_temp = int(new_numerator% denominator_gcd)*10
			p=int(new_numerator % denominator_gcd)
			q=int(new_numerator // denominator_gcd)
			L_1.append(p)
			if int(numerator_temp)==0:
				print(int(new_numerator% denominator_gcd))
				has_finite_expansion = True
				decimal=(numerator/denominator)-(numerator // denominator)
				decimal_str=str(decimal)[2::]
				integral_part= int(numerator // denominator)
				sigma= decimal_str
				break
			else:
				if len(set(L_1))==len(L_1):
					L.append(int(numerator_temp//denominator_gcd))
					new_numerator = numerator_temp
						 
				else:
					L_2.append(p)
					if len(set(L_2))==len(L_2):
						l.append(int(numerator_temp // denominator_gcd))
						new_numerator = numerator_temp

					else:
						sigema_temp=''.join(str(L))
						sigema_temp=sigema_temp.replace(",","")
						sigma=sigema_temp.replace(" ","")[len(integral_part)+1:len(L)-len(l)+1]
						tau_temp=''.join(str(l))
						tau_temp=tau_temp.replace(",","")
						tau=tau_temp.replace(" ","")[1:len(l)+1]
						break
		
		
if has_finite_expansion:
	print(f'\n{numerator} / {denominator} has a finite expansion')
else:
	print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
	if not sigma:
		print(f'{numerator} / {denominator} = {integral_part}')
	else:
		print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
	print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

