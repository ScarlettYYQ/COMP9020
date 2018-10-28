from math import sqrt


class PointError(Exception):
	def __init__(self, message):
		self.message = message


class Point():
	def __init__(self, x = None, y = None):
		if x is None and y is None:
			self.x = 0
			self.y = 0
		elif x is None or y is None:
			raise PointError('Need two coordinates, point not created.')
		else:
			self.x = x
			self.y = y
			
	# Possibly define other methods


class TriangleError(Exception):
	def __init__(self, message):
		self.message = message


class Triangle:
	def __init__(self, *, point_1, point_2, point_3):
		if sqrt((point_1.x-point_2.x)**2+(point_1.y-point_2.y)**2)+sqrt((point_2.x-point_3.x)**2+(point_2.y-point_3.y)**2)-sqrt((point_1.x-point_3.x)**2+(point_1.y-point_3.y)**2)>0 and \
		   sqrt((point_1.x-point_3.x)**2+(point_1.y-point_3.y)**2)+sqrt((point_2.x-point_3.x)**2+(point_2.y-point_3.y)**2)-sqrt((point_1.x-point_2.x)**2+(point_1.y-point_2.y)**2)>0 and \
		   sqrt((point_1.x-point_3.x)**2+(point_1.y-point_3.y)**2)+sqrt((point_1.x-point_2.x)**2+(point_1.y-point_2.y)**2)-sqrt((point_2.x-point_3.x)**2+(point_2.y-point_3.y)**2)>0 :
			self.point_1=point_1
			self.point_2=point_2
			self.point_3=point_3
			self.perimeter=self.triangle_perimeter()
			self.area=self.triangle_area()
		else:
			raise TriangleError('Incorrect input, triangle not created.')
	   
	def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
		if point_1 != None:
			self.point_1=point_1
		if point_2 != None:
			self.point_2=point_2
		if point_3 != None:
			self.point_3=point_3
		if sqrt((self.point_1.x-self.point_2.x)**2+(self.point_1.y-self.point_2.y)**2)+sqrt((self.point_2.x-self.point_3.x)**2+(self.point_2.y-self.point_3.y)**2)-sqrt((self.point_1.x-self.point_3.x)**2+(self.point_1.y-self.point_3.y)**2)>0 and \
		   sqrt((self.point_1.x-self.point_3.x)**2+(self.point_1.y-self.point_3.y)**2)+sqrt((self.point_2.x-self.point_3.x)**2+(self.point_2.y-self.point_3.y)**2)-sqrt((self.point_1.x-self.point_2.x)**2+(self.point_1.y-self.point_2.y)**2)>0 and \
		   sqrt((self.point_1.x-self.point_3.x)**2+(self.point_1.y-self.point_3.y)**2)+sqrt((self.point_1.x-self.point_2.x)**2+(self.point_1.y-self.point_2.y)**2)-sqrt((self.point_2.x-self.point_3.x)**2+(self.point_2.y-self.point_3.y)**2)>0 :
			self.perimeter=self.triangle_perimeter()
			self.area=self.triangle_area()
		else:
			print('Incorrect input, triangle not modified.')
	def triangle_perimeter(self):
		return sqrt((self.point_1.x-self.point_2.x)**2 +(self.point_1.y-self.point_2.y)**2)+sqrt((self.point_2.x-self.point_3.x)**2+(self.point_2.y-self.point_3.y)**2)+sqrt((self.point_1.x-self.point_3.x)**2+(self.point_1.y-self.point_3.y)**2)
		
	def triangle_area(self):
		LA=sqrt((self.point_1.x-self.point_2.x)**2 + (self.point_1.y-self.point_2.y)**2)
		LB=sqrt((self.point_2.x-self.point_3.x)**2 + (self.point_2.y-self.point_3.y)**2)
		LC=sqrt((self.point_1.x-self.point_3.x)**2 + (self.point_1.y-self.point_3.y)**2)
		length=(LA+LB+LC) /2
		return sqrt(length*(length-LA)*(length-LB)*(length-LC))
			
				
	

			
			
