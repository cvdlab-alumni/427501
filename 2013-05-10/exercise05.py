######################
# support function
######################


def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])

def MAPBEZIERS1(controlpoints):
	def MAPBEZIERS10(domain):
		return MAP(BEZIER(S1)(controlpoints))(domain)
	return MAPBEZIERS10



def Scal_Tran(svalues,tvalues,obj):
	sv1,sv2,sv3 = svalues
	tv1,tv2,tv3 = tvalues
	obj1 = S([1,2,3])([sv1,sv2,sv3])(obj)
	obj2 =T([1,2,3])([tv1,tv2,tv3])(obj1)
	return obj2

def Scal_Tran_points(svalues,tvalues,points):
	sv1,sv2,sv3 = svalues
	tv1,tv2,tv3 = tvalues
	array_points = []
	for point in points:
		x,y,z = point
		array_points.append([(x*sv1)+tv1,(y*sv2)+tv2,(z*sv3)+tv3])
	return array_points


#get knot of cubicspline
def getKnots(controls):
	leng = len(controls)+3
	knots = []
	knots.append(0)
	knots.append(0)
	knots.append(0)
	i = 3
	while i<= leng-4:
		knots.append(i-2)
		i= i+1
	knots.append(leng-5)
	knots.append(leng-5)
	knots.append(leng-5)	
	return knots

##############
# domain
##############

domain = INTERVALS(1)(20)

##################
# exercise 2
##################


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

down = STRUCT([COLOR(BLUE)(wheel_lr1),COLOR(RED)(wheel_lr2),wheel_lr3,wheel_lr4,d, glass_up1,glass_up2,glass_up3,glass_up4])

##########
# front
##########

front01 = MAPBEZIERS1([[0.44, 0, 2.38],[0.32, 0.02, 2.38],[0.32, 2.8, 2.38],[0.44, 3, 2.38]])(domain)

front02 = MAPBEZIERS1([[0.38, 0, 1.79],[0.18, 0.01, 1.79],[0.18, 2.9, 1.79],[0.38, 3, 1.79]])(domain)

linefront1 = MAPBEZIERS1([[0.44, 0, 2.38],[0.29, 0.5, 1.79]])(domain)

linefront2 = MAPBEZIERS1([[0.44, 3, 2.38],[0.29, 2.5, 1.79]])(domain)

front = STRUCT([front01, COLOR(BLUE)(front02), linefront1, linefront2])

#########
# beside
#########

beside01 = MAPBEZIERS1([[5.07,0.,  2.64],[5.19, 0.02,  2.64],[5.19, 2.98,  2.64],[5.07,3,  2.64]])(domain)

beside02 = MAPBEZIERS1([ [5.36, 0, 2.21], [5.48, 0.02, 2.21], [5.48, 2.98, 2.21], [5.36, 3, 2.21]])(domain)

beside03 = MAPBEZIERS1([[5.41, 0,2.13],[5.53, 0.05,2.13],[5.53, 2.98,2.13],[5.41, 3,2.13]])(domain)

beside04 = MAPBEZIERS1([[5.33, 0, 1.92],[5.45, 0.05, 1.92],[5.45, 2.95, 1.92],[5.33, 3, 1.92]])(domain)

beside = STRUCT([COLOR(BLUE)(beside01),COLOR(RED)(beside02),beside03,beside04])


skeleton_car0=(STRUCT([left,right,down,front,beside]))

SIZE([1,2,3])(skeleton_car0)

transl_car = T([1,2,3])([-2.365,-1.5, -0.845 ])(skeleton_car0)


###############
# exercise 03
###############
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

steerling1 = STRUCT([steerling01,COLOR(BLACK)(middle_steerling_s),h_s])

steerling = R([1,3])(-PI/6)(steerling1)


###############
# exercise05
###############

##############
# domain2D
#############

domain2D = MAP([S2,S1])(GRID([10,10]))

##############
# top surface
##############

p_b_curve01 = BEZIER(S1)([[2.62 ,0, 3.08],[2.62, 0.30, 3.38],[2.62, 2.70, 3.38],[2.62, 3, 3.08]])

p_b_curve02 = BEZIER(S1)([[3.5, 0., 3.12],[3.5, 0.30, 3.24],[3.5, 2.70, 3.24],[3.5, 3, 3.12]])

p_b_curve03 = BEZIER(S1)([[4, 0, 3.1],[4, 0.02, 3.4],[4, 2.98, 3.4],[4, 3, 3.1]])

p_b_curve04 = BEZIER(S1)([[4.79, 0 , 2.97],[4.79, 3, 2.97]])

up_surface = MAP(BEZIER(S2)([p_b_curve01,p_b_curve02,p_b_curve03,p_b_curve04]))(domain2D)

color_up_surface = COLOR(RED)(up_surface)

############
# top glass
############

map_glass_up1 = BEZIER(S1)([[1.56, 0.05, 2.63],[0.9, 1, 2.3],[0.9, 2, 2.3] ,[1.56, 2.95, 2.63]])

map_glass_up2 = BEZIER(S1)([[1.60, 0.05, 2.70], [1.60, 0.3 , 2.90], [1.60, 2.70, 2.90], [1.6, 2.95, 2.70]])

map_glass_up3 = BEZIER(S1)([[2.55, 0.05, 3], [2.50, 0.3 , 3.60], [2.50, 2.70, 3.6], [2.55, 2.95, 3]])

map_glass_up4 = BEZIER(S1)([[2.62 ,0.05, 3.08],[2.62, 0.35, 3.38],[2.62, 2.65, 3.38],[2.62, 2.95, 3.08]])

glass = MAP(BEZIER(S2)([map_glass_up4,map_glass_up3,map_glass_up2,map_glass_up1]))(GRID([20,20]))

color_glass = COLOR(CYAN)(glass)

##############
# beside glass
##############

map_beside01 = BEZIER(S1)([[5.07,0.,  2.64],[5.19, 0.02,  2.64],[5.19, 2.98,  2.64],[5.07,3,  2.64]])

#map_beside02 = BEZIER(S1)([[4.90, 0,2.80],[5.05, 0.05,3.1],[5.05, 2.95 ,3.1],[4.9, 3,2.8]])

map_beside03 = BEZIER(S1)([[4.79, 0 , 2.97],[4.79, 3, 2.97]])

glass_beside = MAP(BEZIER(S2)([map_beside01,map_beside03]))(GRID([20,20]))

color_glass_beside = COLOR(CYAN)(glass_beside)

map_beside03 = BEZIER(S1)([ [5.36, 0, 2.21], [5.48, 0.02, 2.21], [5.48, 2.98, 2.21], [5.36, 3, 2.21]])

map_beside02 = BEZIER(S1)([ [5.16,  0,  2.64],[5.20, 0.02,  2.75],[5.20, 2.98,  2.75],[5.16,3,  2.64]])

map_beside01 = BEZIER(S1)([ [5.07, 0,  2.64],[5.19, 0.02,  2.64],[5.19, 2.98,  2.64],[5.07,3,  2.64]])

map_beside00 = MAP(BEZIER(S2)([map_beside01,map_beside02,map_beside03]))(domain2D)

color_beside0 = COLOR(RED)(map_beside00)

m_beside03 = BEZIER(S1)([[5.41, 0,2.13],[5.53, 0.05,2.13],[5.53, 2.98,2.13],[5.41, 3,2.13]])

m_beside04 = BEZIER(S1)([[5.33, 0, 1.92],[5.45, 0.05, 1.92],[5.45, 2.95, 1.92],[5.33, 3, 1.92]])

color_beside1 = COLOR(RED)(MAP(BEZIER(S2)([m_beside03,m_beside04]))(domain2D))

color_beside2 = COLOR(RED)(MAP(BEZIER(S2)([map_beside03,m_beside03]))(domain2D))

color_beside = STRUCT([color_beside0,color_beside1,color_beside2])

#############
# bottom surface
#############

map_bottom1 = BEZIER(S1)([[3.88, 0 , 1.73],[3.88, 3 , 1.73]])


map_bottom2 = BEZIER(S1)([[1.8, 0 , 1.72],[1.8, 3, 1.72]])


map_bottom = MAP(BEZIER(S2)([map_bottom1, map_bottom2]))(domain2D)

color_bottom = COLOR(RED)(STRUCT([map_bottom]))

#############
# front surface
#############

map_front1 = BEZIER(S1)([[1.56, 0.05, 2.63],[0.9, 1, 2.3],[0.9, 2, 2.3] ,[1.56, 2.95, 2.63]])


map_front2 = BEZIER(S1)([[1.40, 0.05, 2.63],[1.30, 0.2, 2.67],[1.3, 2.75, 2.67] ,[1.40, 2.95, 2.63]])


map_front3 = BEZIER(S1)([[0.70, 0.05, 2.63],[0.9, 0.2, 2.67],[0.9, 2.75, 2.67] ,[0.70, 2.95, 2.63]])


map_front4 = BEZIER(S1)([[0.44, 0, 2.38],[0.32, 0.02, 2.38],[0.32, 2.8, 2.38],[0.44, 3, 2.38]])


map_front = MAP(BEZIER(S2)([map_front1, map_front2, map_front3, map_front4]))(GRID([20,20]))

color_front0 = COLOR(RED)(STRUCT([map_front]))

map_front04 = BEZIER(S1)([[0.44, 0, 2.38],[0.32, 0.02, 2.38],[0.32, 2.8, 2.38],[0.44, 3, 2.38]])

m_linefront1 = BEZIER(S1)([[0.37, 0.5, 2.30],[0.30, 0.05, 2.28],[0.30, 2.45, 2.28],[0.37, 2.5, 2.30]])

m_linefront2 = BEZIER(S1)([[0.30, 0.5, 2],[0.23, 0.05, 1.98],[0.23, 2.45, 1.98],[0.30, 2.5, 2]])

m_front02 = BEZIER(S1)([[0.29, 0.5, 1.79],[0.29, 2.5, 1.79]])

map_front1 = MAP(BEZIER(S2)([map_front04, m_linefront1,m_linefront2, m_front02]))(GRID([20,20]))

prova = STRUCT([MAP(map_front04)(domain),MAP(m_linefront1)(domain),MAP(m_linefront2)(domain),MAP(m_front02)(domain)])

color_front1 = COLOR(RED)(map_front1)

surface = STRUCT([color_up_surface,color_glass,color_glass_beside, color_beside,color_bottom, color_front0, color_front1])

surface_transl = transl_car = T([1,2,3])([-2.365,-1.5, -0.845 ])(surface)


car = STRUCT([transl_car, surface_transl,car_wheel,T([2,3])([-0.4,1.50])(steerling)])

VIEW(car)

