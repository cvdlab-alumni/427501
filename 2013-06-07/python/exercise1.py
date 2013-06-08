## exercise1.py
from pyplasm import *

DRAW = VIEW

domain1 = PROD([INTERVALS(10)(20),INTERVALS(10)(20)])




def mounts1(domain):
	x = domain[0];
	y = domain[1];
	z = 0 
	height = x * y /20
	if( x<=5 and y<=5):
		z = SIN(x*x+y*y) * COS(x*x + y*y) 
	else:
		if (x<= 9 and y<=9):
			z =  COS(x)*SIN(y)
		else:
			temp_x = x-9
			temp_y = y-9
			z = SIN(temp_x*temp_x+temp_y*temp_y) * COS(temp_x*temp_x + temp_y*temp_y) 
			height = temp_x * temp_y / 20



	return [x,y,z*height]

terrain1 = MAP(mounts1)(domain1) ## principal terrain for exercise1.js

domain2 = T([1])([-10])(PROD([INTERVALS(10)(20),INTERVALS(10)(36)]))

domain3 = T([1,2])([-10,-5])(PROD([INTERVALS(20)(20),INTERVALS(5)(36)]))



def mounts2(domain):
	x = domain[0];
	y = domain[1];
	z = 0 
	height = abs(x * y) /20
	z = SIN(x)*COS(y)
	return [x,y,z*height]



def mounts3(domain):
	x = domain[0];
	y = domain[1];
	z = 0 
	height = abs(x * y) /20
	z = SIN(x)*COS(y)
	if(x>=-6 and x<=6):
		z= COS(x*x + y*y)
		height = abs((x/5) * (y/5)) /20

	return [x,y,z*height]





## auxiliary terrain only to make 
terrain2 = MAP(mounts2)(domain2) 
terrain3 = MAP(mounts3)(domain3) 

terrain = STRUCT([terrain1,terrain2,terrain3]);

DRAW(terrain)
