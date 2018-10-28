# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021

import os
import sys
from collections import defaultdict

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

years_by_names={'Female':[],'Male':[]}
for filename in os.listdir(directory):
		if not filename.endswith('.txt'):
				continue
		year= int(filename[3:7])
		F_count=0
		M_count=0
		F_count_eachone=0
		M_count_eachone=0
		with open(directory +'/'+ filename) as data_file:
				for line in data_file:
						name,gender,count=line.split(',')
						if gender=='F':
								F_count += int(count)
						if gender=='M':
								M_count += int(count)
						if name==first_name:
								if gender=='F':
										F_count_eachone=int(count)
								else:
										M_count_eachone=int(count)
				if F_count_eachone != 0:
						years_by_names['Female'].append((year,F_count_eachone/F_count*100))
				if M_count_eachone != 0:
						years_by_names['Male'].append((year,M_count_eachone/M_count*100))
if len(years_by_names['Female'])!=0:
		(female_first_year,min_female_frequency)=(sorted(years_by_names['Female'],key=lambda x:(x[1],-x[0])))[-1]
if len(years_by_names['Male'])!=0:
		(male_first_year,min_male_frequency)=(sorted(years_by_names['Male'],key=lambda x:(x[1],-x[0])))[-1]

if not female_first_year:
		print(f'In all years, {first_name} was never given as a female name.')
else:
		print(f'In terms of frequency, {first_name} was the most popular '
					f'as a female name first in the year {female_first_year}.\n'
					f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
				 )
if not male_first_year:
		print(f'In all years, {first_name} was never given as a male name.')
else:
		print(f'In terms of frequency, {first_name} was the most popular '
					f'as a male name first in the year {male_first_year}.\n'
					f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
				 )
