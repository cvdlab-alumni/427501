###############
# exercise 04
###############

###################
# import
###################

from lar import *
from pyplasm import *


# ====================
# support function
# ====================

def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])

# Return a function that must be map on a domain
def Circle(h,r):
	def Circle0(v):
		return [r*COS(v[0]), r*SIN(v[0]), h]
	return Circle0

# Return a Array of circle function
def array_circle(args):
	array = []
	for a in args:
		array.append(Circle(a[0],a[1]))
	return array


##############
# domain
##############

domain = INTERVALS(1)(20)
domain2D = PROD([INTERVALS(1)(36), INTERVALS(1)(36)])


#################
# steerling wheel
#################
def Scal_points(svalues,points):
	sv1,sv2,sv3 = svalues
	array_points = []
	for point in points:
		x,y,z = point
		array_points.append([(x*sv1),(y*sv2),(z*sv3)])
	return array_points

def Scal_Tran_points(svalues,tvalues,points):
	sv1,sv2,sv3 = svalues
	tv1,tv2,tv3 = tvalues
	array_points = []
	for point in points:
		x,y,z = point
		array_points.append([(x*sv1)+tv1,(y*sv2)+tv2,(z*sv3)+tv3])
	return array_points

steerling01 = COLOR(BLACK)(TORUS([0.40,0.35])([36,36]))

middle_steerling01 = BEZIER(S1)([[4.25, 2.65,0], [4.67, 3.16, 0], [6.27, 3.16, 0], [6.61, 2.67, 0]])

middle_steerling02 = BEZIER(S1)([[4.25, 2.65, 0], [4.10, -0.5, 0], [6.76, -0.02, 0], [6.61, 2.67, 0]])

middle_steerling11 = BEZIER(S1)(Scal_Tran_points([0.5,0.5,1],[2.65,1,0],[[4.25, 2.65,0.05], [4.67, 3.16, 0.05], [6.27, 3.16, 0.05], [6.61, 2.67, 0.05]]))


middle_steerling12 = BEZIER(S1)(Scal_Tran_points([0.5,0.5,1],[2.65,1,0],[[4.25, 2.65, 0.05], [4.10, -0.5, 0.05], [6.76, -0.02, 0.05], [6.61, 2.67, 0.05]]))


middle_steerling1 = MAP(BEZIER(S2)([middle_steerling01,middle_steerling11]))(domain2D)
middle_steerling2 = MAP(BEZIER(S2)([middle_steerling02,middle_steerling12]))(domain2D)
middle_sterling3 = MAP(BEZIER(S2)([middle_steerling11,middle_steerling12]))(domain2D)


middle_steerling= T([1,2,3])([-5.55,-1.7,-0.025])(STRUCT([middle_steerling1,middle_steerling2,middle_steerling2,middle_sterling3]))
middle_steerling_s = S([1,2])([0.1,0.1])(middle_steerling)



alpha=BEZIER(S1)([[0.1,0,0],[0.1,0,1]])

beta =BEZIER(S2)([[0,0,0],[3,0,0],[3,3,0],[0,3,0]])

domain=PROD([INTERVALS(1)(20),INTERVALS(1)(20)])

steerling_hand=MAP(PROFILEPRODSURFACE([alpha,beta]))(domain)

color_hand = steerling_hand

color_hand1 = R([1,2])(PI)(color_hand)

hand_steerling = COLOR(BLACK)(STRUCT([color_hand,T([2])([0.3])(color_hand1)]) )

hand_steerling1 = R([2,3])(PI/2)(hand_steerling)


hand_steerling2 = R([1,2])(PI/2)(hand_steerling1)


hand_steerling2_scalate = S([1,2,3])([0.3,0.3,0.1])(hand_steerling2)

hand_steerling2_translate = T([1,3])([0.05,-0.025])(hand_steerling2_scalate)

hand_steerling2_R = STRUCT(NN(4)([hand_steerling2_translate ,R([1,2])(-PI/3)]))



h_s = STRUCT([hand_steerling2_translate,hand_steerling2_R])

cubo = COLOR(BLACK)(CUBOID([0.1,0.1,0.05]))

steerling = STRUCT([steerling01,COLOR(BLACK)(middle_steerling_s),h_s])



