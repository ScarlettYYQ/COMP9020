import os
import sys
from collections import defaultdict
import copy

class FriezeError(Exception):
	def __init__(self, message):
		self.message = message

class Frieze:
	def __init__(self,filename):
		grid=[]
		self.filename=filename
		x=0
		y=0
		N=True
		with open (filename) as frieze_file:
			for line in frieze_file:
				line=line.split()
				l=[]
				if len(line)!=0:
					if len(line)<5 or len(line)>51:
						raise FriezeError('Incorrect input.')
					self.length=len(line)
					for i in line:
						if str.isdigit(i)!=True:
							raise FriezeError('Incorrect input.')
						if int(i)==1 or int(i)==0:
							l.append('000'+bin(int(i))[-1])
						elif int(i)==3 or int(i)==2:
							l.append('00'+bin(int(i))[-2:])
						elif int(i)<=7 and int(i)>=4:
							l.append('0'+bin(int(i))[-3:])
						elif int(i)<=15 or int(i)>=8:
							l.append(bin(int(i))[-4:])
						else:
							raise FriezeError('Incorrect input.')
					if l:
						if grid:
							if len(l)!=len(grid[0]):
								raise FriezeError('Incorrect input.')
							else:
								grid.append(l)
						else:
							grid.append(l)
		if len(grid)<3 or len(grid)>17:
			raise FriezeError('Incorrect input.')
		self.grid=grid
		self.is_a_frieze()
		self.find_period()
		self.dis=self.decomposition_grid(self.grid)
		  
	def is_a_frieze(self):
		have_top_and_bottom_line=True
		for digit_t in self.grid[0][0:-1]:
			if int(digit_t,2)==4 or int(digit_t,2)==12:
				pass
			else:
				have_top_and_bottom_line=False
				break
		for digit_b in self.grid[-1][0:-1]:
			if int(digit_b,2)==4 or int(digit_b,2)==5 or int(digit_b,2)==6 or int(digit_b,2)==7:
				pass
			else:
				have_top_and_bottom_line=False
				break
			for i in range(len(self.grid)-1):
				for j in range(len(self.grid[i])-1):
					if self.grid[i][j][0]=='1' and self.grid[i+1][j][2]=='1':
						raise FriezeError('Input does not represent a frieze.')
		if not have_top_and_bottom_line:
			raise FriezeError('Input does not represent a frieze.')
		self.height=len(self.grid)
		  
	def find_period(self):
		grid_turn=list(map(list,zip(*self.grid[:])))
		for j in range(len(grid_turn[0])):
			if grid_turn[0][j][3]=='1' and grid_turn[-1][j]!='0001':
				raise FriezeError('Input does not represent a frieze.')
			if grid_turn[0][j][3]=='0':
				if grid_turn[-1][j]!='0000':
					raise FriezeError('Input does not represent a frieze.')
		for i in range (1,int(self.length/2)+1):
			is_period=True
			if grid_turn[0:i]!=grid_turn[i:2*i]:
				is_period=False
			else:
				if i!=1:
					for num in range(1,(self.length//i)-1):
						if grid_turn[0+(num*i):i+(num*i)]!=grid_turn[i+(num*i):2*i+(num*i)]:
							is_period=False
				else:
					for j in range(len(grid_turn)-2):
						if grid_turn[j]!=grid_turn[j+1]:
							is_period=False
			if is_period:
				if i==1:
					raise FriezeError('Input does not represent a frieze.')
				else:
					period=i
					break
		if is_period:
			if len(grid_turn) % period !=1:
				raise FriezeError('Input does not represent a frieze.')
			else:
				self.period=period
				self.grid_turn=grid_turn
		else:
			raise FriezeError('Input does not represent a frieze.')
	def decomposition_grid(self,grid):
		dis=defaultdict(list)
		dis['n']=copy.deepcopy(grid)
		dis['en']=copy.deepcopy(grid)
		dis['e']=copy.deepcopy(grid)
		dis['es']=copy.deepcopy(grid)
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				dis['n'][i][j]=dis['en'][i][j]=dis['e'][i][j]=dis['es'][i][j]=0
				if int(grid[i][j][3])==1:
					dis['n'][i][j]=1
				if int(grid[i][j][2])==1:
					dis['en'][i][j]=1
				if int(grid[i][j][1])==1:
					dis['e'][i][j]=1
				if int(grid[i][j][0])==1:
					dis['es'][i][j]=1
		return dis
	def horizontal(self):
		for i in range(int(self.period+1),int(2*self.period+1)):
			period_g=self.grid_turn[0:i]
			period_grid=list(map(list,zip(*period_g[:])))
			grid_horizontal_list=[]
			is_horizontal=0
			is_glided_horizontal=0
			dis_temp=self.decomposition_grid(period_grid)
			period_grid.reverse()
			grid_horizontal_list=self.decomposition_grid(period_grid)
			if grid_horizontal_list['e']==dis_temp['e'] and grid_horizontal_list['n'][:-1]==dis_temp['n'][1:] and grid_horizontal_list['es']==dis_temp['en'] and grid_horizontal_list['en']==dis_temp['es']:
				is_horizontal=1
			if self.height % 2==0:
				if is_horizontal==0:
					grid_turn_back_up=list(map(list,zip(*period_g[int(self.period/2):])))[:int(self.height/2)]
					grid_turn_back_down=list(map(list,zip(*period_g[:len(period_g)-int(self.period/2)])))[int(self.height/2):]
					grid_turn_back_up.reverse()
					up_list=self.decomposition_grid(grid_turn_back_up)
					down_list=self.decomposition_grid(grid_turn_back_down)
					if list(map(list,zip(*up_list['e'][:])))==list(map(list,zip(*down_list['e'][:]))) and up_list['n'][:int(len(up_list['n'])-1)]==down_list['n'][1:] and up_list['es']==down_list['en'] and  up_list['en']==down_list['es']:
						is_glided_horizontal=1
						break
			else:
				if is_horizontal==0:
					grid_turn_back_up=list(map(list,zip(*period_g[int(self.period/2):])))[:int(self.height/2)+1]
					grid_turn_back_down=list(map(list,zip(*period_g[:len(period_g)-int(self.period/2)])))[int(self.height/2)+1:]
					grid_turn_back_down.reverse()
					up_list=self.decomposition_grid(grid_turn_back_up)
					down_list=self.decomposition_grid(grid_turn_back_down)
					up=list(map(list,zip(*period_g)))[:int(self.height/2)+1]
					up_R=self.decomposition_grid(up)
					for k in range(len(up[0])):
						if k-int(self.period/2)>=0:
							if up_R['en'][-1][k]!=up_R['es'][-1][k-int(self.period/2)]:
								return (0,0)
							if k+int(self.period/2)<len(up[0]):
								if up_R['en'][-1][k]!=up_R['es'][-1][k+int(self.period/2)]:
									return (0,0)
					if up_list['e'][:-1]==down_list['e'] and up_list['n'][1:]==down_list['n'] and up_list['es'][:-1]==down_list['en'] and  up_list['en'][:-1]==down_list['es']:
						is_glided_horizontal=1
						break
		return (is_horizontal,is_glided_horizontal)
	 
	def vertical(self):
		is_vertical=0
		for i in range(int(self.period+1),int(2*self.period+1)):
			period_grid=self.grid_turn[0:i]
			period_grid=list(map(list,zip(*period_grid[:])))
			dis_temp=self.decomposition_grid(period_grid)
			grid_reverse=[]
			for line in period_grid:
				line.reverse()
				grid_reverse.append(line)
			vertical_display=self.decomposition_grid(grid_reverse)
			if list(map(list,zip(*vertical_display['n'][:])))[:-1]==list(map(list,zip(*dis_temp['n'][:])))[1:] and vertical_display['e']==dis_temp['e'] and vertical_display['en'][1:]==dis_temp['es'][:-1] and vertical_display['es'][:-1]==dis_temp['en'][1:]:
				return 1
			else:
				vertical_display_e=list(map(list,zip(*vertical_display['e'][:])))[1:]
				vertical_display_en=list(map(list,zip(*vertical_display['en'][1:])))[1:]
				vertical_display_es=list(map(list,zip(*vertical_display['es'][:-1])))[1:]
				if vertical_display['n']==dis_temp['n'] and vertical_display_e==list(map(list,zip(*dis_temp['e'][:])))[:-1] and vertical_display_en==list(map(list,zip(*dis_temp['es'][:-1])))[:-1] and vertical_display_es==list(map(list,zip(*dis_temp['en'][1:])))[:-1]:
					return 1
		return is_vertical

	def Rotation(self):
		is_rotation=0
		for i in range(int(self.period+1)):
			period_grid=self.grid_turn[i:self.period+1+i]
			period_grid=list(map(list,zip(*period_grid[:])))
			dis_temp=self.decomposition_grid(period_grid)
			period_grid.reverse()
			Rotation_grid=[]
			for line in period_grid:
				line.reverse()
				Rotation_grid.append(line)
			Rotation_display=self.decomposition_grid(Rotation_grid)
			if Rotation_display['n'][:-1]==dis_temp['n'][1:] and list(map(list,zip(*Rotation_display['en'][:-1])))[1:]==list(map(list,zip(*dis_temp['en'][1:])))[:-1] and list(map(list,zip(*Rotation_display['es'][1:])))[1:]==list(map(list,zip(*dis_temp['es'][:-1])))[:-1] and list(map(list,zip(*Rotation_display['e'][:])))[1:]==list(map(list,zip(*dis_temp['e'][:])))[:-1]:
				return 1
			else:
				if list(map(list,zip(*Rotation_display['n'][:-1])))[:-1]==list(map(list,zip(*dis_temp['n'][1:])))[1:] and Rotation_display['e']==dis_temp['e'] and Rotation_display['en'][:-1]==dis_temp['en'][1:] and Rotation_display['es'][1:]==dis_temp['es'][:-1]:
					return 1
		return is_rotation
	def analyse(self):
		R1,R2=self.horizontal()
		R3=self.vertical()
		R4=self.Rotation()
		if R1==1 and R3==R4==0:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and horizontal reflection only.')
		if R2==1 and R3==R4==0:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and glided horizontal reflection only.')
		if R1==R2==R4==0 and R3==1:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and vertical reflection only.')
		if R1==R2==R3==0 and R4==1:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and rotation only.')
		if R1==R3==R4==1:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
			print('        horizontal and vertical reflections, and rotation only.')
		if R2==R3==R4==1:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
			print('        glided horizontal and vertical reflections, and rotation only.')
		if R1==R2==R3==R4==0:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation only.')

	def output(self,dis):
		e_l,es_l,n_l,en_l=[],[],[],[]
		def es(i,j):
			if i+1<self.height and j+1<self.length:
				dis['es'][i][j]='*'
				if dis['es'][i+1][j+1]==1:
					return es(i+1,j+1)
				else:
					return (j+1,i+1)
		def e(i,j):
			if j+1<self.length:
				dis['e'][i][j]='*'
				if dis['e'][i][j+1]==1:
					return e(i,j+1)
				else:
					return (j+1,i)
		def n(i,j):
			dis['n'][i][j]='*'
			if i+1<self.height:
				if dis['n'][i+1][j]==1:
					return n(i+1,j)
				else:
					return (j,i)
			else:
				return (j,i)
		def en(i,j):
			dis['en'][i][j]='*'
			if i+1<self.height :
				if dis['en'][i+1][j-1]==1:
					return en(i+1,j-1)
				else:
					return (j,i)
			else:
					return (j,i)
		for i in range(self.height):
			for j in range(self.length):
				if dis['en'][i][j]==1:
					en_l.append([en(i,j),(j+1,i-1)])
				if dis['n'][i][j]==1:
					n_l.append([(j,i-1),n(i,j)])
				if dis['e'][i][j]==1:
					e_l.append([(j,i),e(i,j)])
				if dis['es'][i][j]==1:
					es_l.append([(j,i),es(i,j)])
		return ([sorted(n_l),sorted(es_l,key=lambda x:(x[0][1],x[0][0])),sorted(e_l,key=lambda x:(x[0][1],x[0][0])),sorted(en_l,key=lambda x:(x[0][1],x[0][0]))])
	def display(self):
		grid_display_list=self.output(self.dis)
		display_file_name=self.filename[:-4]+'.tex'
		displayfrieze=open(f'{display_file_name}','w')
		displayfrieze.write(r'\documentclass[10pt]{article}''\n')
		displayfrieze.write(r'\usepackage{tikz}''\n')
		displayfrieze.write(r'\usepackage[margin=0cm]{geometry}''\n')
		displayfrieze.write(r'\pagestyle{empty}''\n')
		displayfrieze.write('\n')
		displayfrieze.write(r'\begin{document}''\n')
		displayfrieze.write('\n')
		displayfrieze.write(r'\vspace*{\fill}''\n')
		displayfrieze.write(r'\begin{center}''\n')
		displayfrieze.write(r'\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]''\n')
		displayfrieze.write('% North to South lines''\n')
		for i in grid_display_list[0]:
			displayfrieze.write(f'    \draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});\n')
		displayfrieze.write('% North-West to South-East lines\n')
		for i in grid_display_list[1]:
			displayfrieze.write(f'    \draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});\n')
		displayfrieze.write('% West to East lines\n')
		for i in grid_display_list[2]:
			displayfrieze.write(f'    \draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});\n')
		displayfrieze.write('% South-West to North-East lines\n')
		for i in grid_display_list[3]:
			displayfrieze.write(f'    \draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});\n')
		displayfrieze.write('\end{tikzpicture}\n')
		displayfrieze.write('\end{center}\n')
		displayfrieze.write(r'\vspace*{\fill}''\n')
		displayfrieze.write('\n')
		displayfrieze.write('\end{document}\n')
		displayfrieze.close()
		  
	
