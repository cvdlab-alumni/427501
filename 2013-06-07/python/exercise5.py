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

## import exercise3.py

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

##import exercise4.py
def house(x,y,z1):
	random1 = random.random()+0.5;
	new_x = x *(random1);
	new_y = y *(random1);
	new_z = z1 *(random1);
	return COLOR(WHITE)(CUBOID([new_x,new_y,new_z]));







first_house = house(1,0.3,0.7);

subset_h1  = [[-6.0,-1.5],[-1.0,-5]]

subset_h2  = [[1.0,6.0],[-1.0,-5.0]]
  
def house0(object1,subset):
	result = list();
	for x in numpy.arange(subset[0][0],subset[0][1],2.5):
		for y in numpy.arange(subset[1][1],subset[1][0],1.0):
			z = COS(math.pow(x,2) + math.pow(y,2));
			dz = abs((x/5.0) * (y/5.0)) /20.0;
			result.append(T([1,2,3])([x,y,z*dz])(object1)) 
		
		
	return STRUCT(result)



h1 = house0(first_house,subset_h1)

h2 = house0(first_house,subset_h2)

h = STRUCT([h1,h2])


##exercise5.js
domain21 = T([1])([-10])(PROD([INTERVALS(10)(20),INTERVALS(1.3)(20)])) 
domain2line = T([1,2])([-10,1.0])(PROD([INTERVALS(10)(20),INTERVALS(0.10)(20)]))
domain21line = T([1,2])([-10,0.1])(PROD([INTERVALS(10)(20),INTERVALS(0.10)(20)]))
domain211line = T([1,2])([-10,0.1])(PROD([INTERVALS(10.7)(20),INTERVALS(0.1)(20)]))


domain11 = T([1])([-10])(PROD([INTERVALS(10)(20),INTERVALS(1.3)(20)]))
domain1line = T([2])([1.0])(PROD([INTERVALS(9)(20),INTERVALS(0.10)(20)]))
domain11line = T([2])([0.1])(PROD([INTERVALS(9)(20),INTERVALS(0.10)(20)]))
domain111line = T([1,2])([0.4,0.1])(PROD([INTERVALS(8.6)(20),INTERVALS(0.10)(20)]))

street11 = MAP(mounts1)(domain11) 
street21 = MAP(mounts2)(domain21)

street11line = COLOR(WHITE)(MAP(mounts1)(domain1line))
street21line = COLOR(WHITE)(MAP(mounts2)(domain2line))
street111line = COLOR(WHITE)(MAP(mounts1)(domain111line))
street212line = COLOR(WHITE)(MAP(mounts2)(domain211line))



domain31 = T([1,2])([-0.8,-5])(PROD([INTERVALS(1.3)(10),INTERVALS(5)(10)]))#DOMAIN([[-0.8,0.5], [-5,0]])([10,10]);
domain311 = T([1,2])([-0.7,-5])(PROD([INTERVALS(0.1)(10),INTERVALS(1.3)(10)]))#DOMAIN([[-0.7,-0.6], [-5,0]])([10,10]);
domain312 = T([1,2])([0.3,-5])(PROD([INTERVALS(0.1)(10),INTERVALS(1.3)(10)]))#DOMAIN([[0.3,0.4], [-5,0]])([10,10]);

street31 = MAP(mounts3)(domain31) 
street311 = COLOR(WHITE)(MAP(mounts3)(domain311))
street312 = COLOR(WHITE)( MAP(mounts3)(domain312) )

streetline = T([3])([0.11])(STRUCT([street212line,street111line,street21line,street11line,street311,street312]))

street1 = T([3])([0.1])(COLOR(BLACK)(STRUCT([street11,street21,street31])))

streeth = T([1,2])([-4.3,-0.5-4.4])(COLOR(BLACK)(CUBOID([0.5,5.6,0.07])))

streeth1 = T([1,2])([2.9,-0.5-4.4])(COLOR(BLACK)(CUBOID([0.5,5.6,0.07])))

streeth2 = T([1,2])([5.3,-0.5-4.4])(COLOR(BLACK)(CUBOID([0.5,5.6,0.07])))

streetv1 = T([1,2])([-3.9,-0.2-1.2])(COLOR(BLACK)(CUBOID([5,0.2,0.07])))

streetv2 = T([1,2])([0,-1.4])(COLOR(BLACK)(CUBOID([7,0.2,0.07])))

streetv = STRUCT([streetv1,streetv2]);

streetv00 = T([2])([-0.7])(STRUCT([streetv1,streetv2]));

streetv11 = T([2])([-0.7*2])(STRUCT([streetv1,streetv2]));

streetv22 = T([2])([-0.7*3])(STRUCT([streetv1,streetv2]));

streetv33 = T([2])([-0.7*4])(STRUCT([streetv1,streetv2]));

streetv_vertical = STRUCT([streetv,streetv00,streetv11,streetv22,streetv33]);

street = STRUCT([street1,streeth,streeth1,streeth2,streetv_vertical,streetline])

#END

model = STRUCT([terrain,lake,forest,h,street])

DRAW(model)
