##import exercise1.py
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

## import exercise2.py

def Circum(r, h):
	def Circum0(v):
		return [r*COS(v[0]), r*SIN(v[0]), h];
	return Circum0;


s = CYLINDER([1, 0.11])(20);
b1 = CIRCLE(1)([20,20]);
b2 = T([3])([0.11])(b1);


lake1 = T([1,2])([3.2,2.7])(COLOR(BLUE)(STRUCT([s,b1,b2])))

circle1 = Circum(1.3,0);

domain2d = PROD([INTERVALS(2*PI)(20),INTERVALS(1)(20)])

lake_circle1 = STRUCT([MAP(BEZIER(S2)([circle1,[0,0,-0.75]]))(domain2d),
						MAP(BEZIER(S2)([circle1,[0,0,0]]))(domain2d)]);

lake = STRUCT([lake1, T([1,2,3])([6.3,4.8,-0.3])(COLOR(BLUE)(lake_circle1))])

##exercise3.py

import numpy
import random

def CONE(r, h1, h2):
	def CONE0(l):
 		domainCircular = PROD([INTERVALS(2*PI)(20), INTERVALS(1)(20)]);
  		c = Circum(r, h1);
  		base = MAP(BEZIER(S2)([c, [0, 0, h1]]))(domainCircular);
  		s = MAP(BEZIER(S2)([c, [0, 0, h1+h2]]))(domainCircular);
		return STRUCT([s, base]);
	return CONE0;


def tree(r1,r2,h1,h2):
	t1 = r1 * (random.random() +0.5);
	ht1 = h1 * (random.random() +0.5);
	cyl = COLOR(BROWN)(CYLINDER([t1,ht1])(12))
	con = COLOR(GREEN)(CONE(r2,ht1,h2)(1))
	return T([1,2])([t1/2,t1/2])(STRUCT([cyl,con]))


first_tree = tree(0.05,0.2,0.4,0.7)

subset  = [[6,8],[1,3]]


def forest0(object1,subset):
	result = list()
	for x in numpy.arange(subset[0][0],subset[0][1],1.0):
		for y in numpy.arange(subset[1][0],subset[1][1],1.0):
			z = COS(x)*SIN(y)
			dz = (int(x)*int(y))/int(20)
			result.append(T([1,2,3])([x,y,z*dz])(object1)) 
			
	return STRUCT(result)


f = forest0(first_tree,subset)

subset1 = [[5.1,7.3],[6.4,8.5]]

f1 = forest0(first_tree,subset1);

subset2 = [[8.5,9.5],[-0.75,0]]

f2 = forest0(first_tree,subset2);

subset3 = [[-8,-7],[-1.5,-0.25]]

f3 = forest0(first_tree,subset3);

forest = STRUCT([f,f1,f2,f3])


model = STRUCT([terrain,lake,forest])

DRAW(model)
