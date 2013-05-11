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

###############
# left side
###############

points_left01 = [[1.8, 0, 1.72], [2.37,0, 1.72], [3.88, 0,1.73]]
left01 = MAPBEZIERS1(points_left01)(domain)

points_cover_wheel01= [[4.79,0, 1.72], [4.72,0, 2.43], [3.91, 0, 2.43], [3.88, 0, 1.73]]
cover_wheel01 = MAPBEZIERS1(points_cover_wheel01)(domain)

cover_wheel011 = MAPBEZIERS1([[4.78, 0, 1.72], [5.44,0, 1.88], [5.12,0, 1.72], [5.33, 0, 1.92]])(domain)
cover_wheel012 = MAPBEZIERS1([[5.33, 0, 1.92],[5.41, 0,2.13]])(domain)
cover_wheel013 = MAPBEZIERS1([[5.41, 0,2.13],[5.36,0, 2.21]])(domain)
cover_wheel014 = POLYLINE([[4.94, 0,  2.64], [4.94, 0, 2.55], [5.19, 0, 2.18], [5.36, 0, 2.21]])
cover_wheel015 = MAPBEZIERS1([[4.79, 0, 2.97], [4.69, 0, 2.95], [5, 0, 2.81], [5.07,0,  2.64]])(domain)

points_cover_wheel02 = [[1.8, 0, 1.72], [1.69, 0, 2.47], [0.93,0,  2.38], [0.86,0,  1.73]]
cover_wheel02 = MAPBEZIERS1(points_cover_wheel02)(domain)

left011 = POLYLINE([[0.86,0, 1.72],[0.79, 0, 1.64],[0.56, 0, 1.7], [0.38, 0, 1.79],[0.37, 0, 1.85], [0.39, 0, 1.92] ,[0.49, 0, 2.35],[0.45,0, 2.38]])

points_left_up01 = [[1.8,0.05, 2.62],[2.88, 0.05, 3.39], [4.21, 0.05, 3.03], [4.79,0.05,  2.97]]
left_up01 = MAPBEZIERS1(points_left_up01)(domain)

points_left_up02 = [[1.8, 0.05,2.62], [1.69, 0.05,2.53],[1.51,0.05, 2.51],[1.41, 0.05,2.51],[1.19, 0.05, 2.49],[1.03, 0.05, 2.45],[0.99,0.05, 2.45],[0.98,0.05, 2.44],[0.95, 0.05 ,2.43],[0.89, 0.05, 2.42]]
left_up02 = MAPBEZIERS1(points_left_up02)(domain)

left_up022 = MAPBEZIERS1([[1.8, 0.05, 2.62],[1.72, 0.05, 2.61]])(domain)
left_up023 = MAPBEZIERS1([[1.72, 0, 2.61], [1.56, 0, 2.63]])(domain)
left_up024 = MAPBEZIERS1([[1.56, 0, 2.63], [0.25,0,  2.51], [0.62, 0, 2.33], [0.44, 0, 2.38]])(domain)

points_left_up03 = [[0.89, 0.05, 2.42], [0.8, 0.05, 2.41],[0.69,0.05,  2.4], [0.48, 0.05, 2.34]]
left_up03 =MAPBEZIERS1(points_left_up03)(domain)

left = STRUCT([left01, cover_wheel01,cover_wheel011,cover_wheel012, cover_wheel013, cover_wheel014, cover_wheel015 ,cover_wheel02, left_up01,left011, left_up02, left_up022, left_up023,left_up024 ,left_up03])


#################
# glass left side
#################



line01 = MAPBEZIERS1([[4.17,0,  2.24], [4.16, 0, 2.52]])(domain)
line02 = MAPBEZIERS1([[4.16, 0, 2.52],[4.16, 0.05 ,2.64]])(domain)
line03 = MAPBEZIERS1([[4.16, 0.05, 2.64], [4.17, 0.05 ,3.02]])(domain)
line0  = STRUCT([line01, line02, line03])

line11 = MAPBEZIERS1([[3.11, 0, 1.72], [3.02, 0, 1.84], [3.08, 0, 2.34], [3.06, 0, 2.5]])(domain)
line12 = MAPBEZIERS1([[3.06, 0, 2.5],[3.06, 0.05, 2.62]])(domain)
line13 = MAPBEZIERS1([[3.06, 0.05, 2.62],[3.16, 0.05 ,3.06]])(domain)
line1 = STRUCT([line11, line12, line13])

line2 = MAPBEZIERS1([[1.91, 0, 2.43], [1.87,0,  2.21], [1.93, 0,  1.8], [1.96,0,  1.71]])(domain)
line3 = MAPBEZIERS1([[1.91, 0, 2.43],[1.91,0.05,2.53]])(domain)
line4 = MAPBEZIERS1([[1.91, 0.05 , 2.53], [2.5, 0.05, 3.35], [4.15, 0.05, 2.94], [4.48, 0.05,2.96]])(domain)
line5 = MAPBEZIERS1([[4.76, 0.05, 2.64], [4.69, 0.05, 2.8], [4.6,0.05, 2.85], [4.48, 0.05, 2.96]])(domain)
line6 = MAPBEZIERS1([[4.76, 0.05, 2.64], [1.91, 0.05 , 2.53]])(domain)


left = STRUCT([left, line0, line1, line2, line3 ,line4, line5, line6])


##############
# right side
#############

points_right01 = [[1.8, 3, 1.72], [2.37,3, 1.72], [3.88, 3,1.73]]
right01 = MAPBEZIERS1(points_right01)(domain)

points_cover_wheel01r= [[4.79,3, 1.72], [4.72,3, 2.43], [3.91, 3, 2.43], [3.88, 3, 1.73]]
cover_wheel01r = MAPBEZIERS1(points_cover_wheel01r)(domain)

cover_wheel011r = MAPBEZIERS1([[4.78, 3, 1.72], [5.44,3, 1.88], [5.12,3, 1.72], [5.33, 3, 1.92]])(domain)
cover_wheel012r = MAPBEZIERS1([[5.33, 3, 1.92],[5.41, 3,2.13]])(domain)
cover_wheel013r = MAPBEZIERS1([[5.41, 3,2.13],[5.36,3, 2.21]])(domain)
cover_wheel014r = POLYLINE([[4.94, 3,  2.64], [4.94, 3, 2.55], [5.19, 3, 2.18], [5.36, 3, 2.21]])
cover_wheel015r = MAPBEZIERS1([[4.79, 3, 2.97], [4.69, 3, 2.95], [5, 3, 2.81], [5.07,3,  2.64]])(domain)

points_cover_wheel02r = [[1.8, 3, 1.72], [1.69, 3, 2.47], [0.93,3,  2.38], [0.86,3,  1.73]]
cover_wheel02r = MAPBEZIERS1(points_cover_wheel02r)(domain)

right011 = POLYLINE([[0.86,3, 1.72],[0.79, 3, 1.64],[0.56, 3, 1.7], [0.38, 3, 1.79],[0.37, 3, 1.85], [0.39, 3, 1.92] ,[0.49, 3, 2.35],[0.45,3, 2.38]])

points_right_up01 = [[1.8,2.95, 2.62],[2.88, 2.95, 3.39], [4.21, 2.95, 3.03], [4.79,2.95,  2.97]]
right_up01 = MAPBEZIERS1(points_right_up01)(domain)

points_right_up02 = [[1.8, 2.95,2.62], [1.69, 2.95,2.53],[1.51,2.95, 2.51],[1.41, 2.95,2.51],[1.19, 2.95, 2.49],[1.03, 2.95, 2.45],[0.99,2.95, 2.45],[0.98,2.95, 2.44],[0.95, 2.95 ,2.43],[0.89, 2.95, 2.42]]
right_up02 = MAPBEZIERS1(points_right_up02)(domain)

right_up022 = MAPBEZIERS1([[1.8,2.95, 2.62],[1.72, 2.95, 2.61]])(domain)
right_up023 = MAPBEZIERS1([[1.72, 3, 2.61], [1.56, 3, 2.63]])(domain)
right_up024 = MAPBEZIERS1([[1.56, 3, 2.63], [0.25,3,  2.51], [0.62, 3, 2.33], [0.44, 3, 2.38]])(domain)

points_right_up03 = [[0.89, 2.95, 2.42], [0.8, 2.95, 2.41],[0.69,2.95,  2.4], [0.48, 2.95, 2.34]]
right_up03 = MAPBEZIERS1(points_right_up03)(domain)


right_o = STRUCT([right01, cover_wheel01r,cover_wheel011r,cover_wheel012r, cover_wheel013r, cover_wheel014r, cover_wheel015r ,cover_wheel02r, right_up01,right011, right_up02, right_up022, right_up023,right_up024 ,right_up03])


#################
# glass left side
#################



line01r = MAPBEZIERS1([[4.17,3,  2.24], [4.16, 3, 2.52]])(domain)
line02r = MAPBEZIERS1([[4.16, 3, 2.52],[4.16, 2.95 ,2.64]])(domain)
line03r = MAPBEZIERS1([[4.16, 2.95, 2.64], [4.17, 2.95 ,3.02]])(domain)
line0r = STRUCT([line01r, line02r, line03r])

line11r = MAPBEZIERS1([[3.11, 3, 1.72], [3.02, 3, 1.84], [3.08, 3, 2.34], [3.06, 3, 2.5]])(domain)
line12r = MAPBEZIERS1([[3.06, 3, 2.5],[3.06, 2.95, 2.62]])(domain)
line13r = MAPBEZIERS1([[3.06, 2.95, 2.62],[3.16, 2.95 ,3.06]])(domain)
line1r = STRUCT([line11r, line12r, line13r])

line2r = MAPBEZIERS1([[1.91, 3, 2.43], [1.87,3,  2.21], [1.93, 3,  1.8], [1.96,3,  1.71]])(domain)
line3r = MAPBEZIERS1([[1.91, 3, 2.43],[1.91,2.95,2.53]])(domain)
line4r = MAPBEZIERS1([[1.91, 2.95 , 2.53], [2.5, 2.95, 3.35], [4.15, 2.95, 2.94], [4.48, 2.95,2.96]])(domain)
line5r = MAPBEZIERS1([[4.76, 2.95, 2.64], [4.69, 2.95, 2.8], [4.6,2.95, 2.85], [4.48, 2.95, 2.96]])(domain)
line6r = MAPBEZIERS1([[4.76, 2.95, 2.64], [1.91, 2.95 , 2.53]])(domain)


right = STRUCT([right_o, line0r, line1r, line2r, line3r ,line4r, line5r, line6r])

############
# down
###########

wheel_lr1 = MAPBEZIERS1([[4.79, 0 , 1.72],[4.79, 3, 1.72]])(domain)

wheel_lr2 = MAPBEZIERS1([[3.88, 0 , 1.73],[3.88, 3 , 1.73]])(domain)

wheel_lr3 = MAPBEZIERS1([[1.8, 0 , 1.72],[1.8, 3, 1.72]])(domain)

wheel_lr4 = MAPBEZIERS1([[0.86, 0 , 1.72],[0.86, 3, 1.72]])(domain)

d = MAPBEZIERS1([[4.79, 0 , 2.97],[4.79, 3, 2.97]])(domain)

glass_up1 = MAPBEZIERS1([[1.56, 0.05, 2.63],[0.9, 1, 2.3],[0.9, 2, 2.3] ,[1.56, 2.95, 2.63]])(domain)

glass_up2 = MAPBEZIERS1([[1.56, 0.05, 2.63], [1.87,0.05, 2.88], [2.46, 0.05, 3.14], [2.62 ,0.05, 3.08]])(domain)

glass_up3 = MAPBEZIERS1([[1.56, 2.95, 2.63], [1.87,2.95, 2.88], [2.46, 2.95, 3.14], [2.62, 2.95, 3.08]])(domain)

glass_up4 = MAPBEZIERS1([[2.62 ,0.05, 3.08],[2.62, 0.35, 3.38],[2.62, 2.65, 3.38],[2.62, 2.95, 3.08]])(domain)

down = STRUCT([wheel_lr1,wheel_lr2,wheel_lr3,wheel_lr4,d, glass_up1,glass_up2,glass_up3,glass_up4])

##########
# front
##########

front01 = MAPBEZIERS1([[0.44, 0, 2.38],[0.32, 0.02, 2.38],[0.32, 2.8, 2.38],[0.44, 3, 2.38]])(domain)

front02 = MAPBEZIERS1([[0.38, 0, 1.79],[0.18, 0.01, 1.79],[0.18, 2.9, 1.79],[0.38, 3, 1.79]])(domain)

linefront1 = MAPBEZIERS1([[0.44, 0, 2.38],[0.29, 0.5, 1.79]])(domain)

linefront2 = MAPBEZIERS1([[0.44, 3, 2.38],[0.29, 2.5, 1.79]])(domain)

front = STRUCT([front01, front02, linefront1, linefront2])

#########
# beside
#########

beside01 = MAPBEZIERS1([[5.07,0.,  2.64],[5.19, 0.02,  2.64],[5.19, 2.98,  2.64],[5.07,3,  2.64]])(domain)

beside02 = MAPBEZIERS1([ [5.36, 0, 2.21], [5.48, 0.02, 2.21], [5.48, 2.98, 2.21], [5.36, 3, 2.21]])(domain)

beside03 = MAPBEZIERS1([[5.41, 0,2.13],[5.53, 0.05,2.13],[5.53, 2.98,2.13],[5.41, 3,2.13]])(domain)

beside04 = MAPBEZIERS1([[5.33, 0, 1.92],[5.45, 0.05, 1.92],[5.45, 2.95, 1.92],[5.33, 3, 1.92]])(domain)

beside = STRUCT([beside01,beside02,beside03,beside04])

skeleton_car0=(STRUCT([left,right,down,front,beside]))

SIZE([1,2,3])(skeleton_car0)

transl_car = T([1,2,3])([-2.365,-1.5, -0.845 ])(skeleton_car0)

# ================
# rim
# ================

domain2d = PROD([INTERVALS(2*PI)(20),INTERVALS(1)(36)])

domain2D = GRID([20,20])

circles = array_circle([[0,0.8],[0,0.7],[0.3,0.5]])

map_circles0 = MAP(BEZIER(S2)([circles[0],circles[1]]))(domain2d)



map_circles01 = STRUCT([map_circles0])

# =================
# radius
# =================

radius01 = CUBOID([0.03, 0.35, 0.01])
 

radius = STRUCT(NN(5)([radius01,ROTN([2*PI/5,[0,0,1]])]))

cyl01 = CYLINDER([0.35,0.3])(36)

cyl02 = CYLINDER([0.3,0.3])(36)

cyl = DIFF([cyl01,cyl02])

cyl03 = CYLINDER([0.1,0.01])(36)
cyl04 = T([3])([-0.005])(CYLINDER([0.05,0.01])(36))

cyl1 = DIFF([cyl03,cyl04])

rim = STRUCT([radius,cyl,T([3])([-0.005])(cyl1)])

circles = array_circle([[0,0.35],[0.1,0.40],[0.15,0.43],[0.20, 0.40], [0.30, 0.35]])

wheel01 = MAP(BEZIER(S2)(circles))(domain2d)

wheel02 = R([2,3])(PI/2)(STRUCT([rim,COLOR(BLACK)(wheel01)]))

wheel1 = T([1,2,3])([1.95,1.7,0.9])(wheel02)

wheel2 = T([1])([-3])(wheel1)

wheels1 = STRUCT([wheel1, wheel2])

wheels2 = R([1,2])(-PI)(wheels1)

wheels = STRUCT([wheels1,T([1])([0.95])(wheels2)])

car_wheel = STRUCT([wheels,transl_car])

VIEW(car_wheel)
