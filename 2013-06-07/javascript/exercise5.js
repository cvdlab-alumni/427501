
//import exercise1
var domain1 = DOMAIN([[0,10], [0, 10]])([20,20]);

var color = function(rgb){
	return COLOR([rgb[0]/255, rgb[1]/255,rgb[2]/255])
}


var mounts1 = function(domain){
	var x = domain[0];
	var y = domain[1];
	var z = 0 
	var height = x * y /20

	if( x<=5 && y<=5)
		z = SIN(x*x+y*y) * COS(x*x + y*y) 
	else if (x<= 9 && y<=9)
		z =  COS(x)*SIN(y)
	else{
		temp_x = x-9
		temp_y = y-9
		z = SIN(temp_x*temp_x+temp_y*temp_y) * COS(temp_x*temp_x + temp_y*temp_y) 
		height = temp_x * temp_y / 20
	}


	return [x,y,z*height]

}

var terrain1 = MAP(mounts1)(domain1) // principal terrain for exercise1.js

var domain2 = DOMAIN([[-10,0], [0,10]])([20,20]);
var domain3 = DOMAIN([[-10,10], [-5,0]])([10,10]);


var mounts2 = function(domain){
	var x = domain[0];
	var y = domain[1];
	var z = 0 
	var height = Math.abs(x * y) /20
	
	z = SIN(x)*COS(y)

	return [x,y,z*height]

}

var mounts3 = function(domain){
	var x = domain[0];
	var y = domain[1];
	var z = 0 
	var height = Math.abs(x * y) /20
	z = SIN(x)*COS(y)
	if(x>=-6 && x<=6){
		z= COS(x*x + y*y)
		height = Math.abs((x/5) * (y/5)) /20
	}
	return [x,y,z*height]

}

// TERRAIN 4 è di prova
var domainBEZ = DOMAIN([[0,1],[0,1]])([10,10])

var terrain41 = MAP(BEZIER(S1)([ BEZIER(S0)([[-10,-5,COS(125)*Math.abs((-2) * (-1)) /20],
											 [-10,-5,-5],[10,-5,-5],
											 [10,-5,COS(125)*Math.abs((-2) * (-1)) /20]]),
								BEZIER(S0)([[-10,0,COS(100)*Math.abs((-2) * (0)) /20],
											 [-10,0,-10],[10,0,-10],
											 [10,0,COS(100)*Math.abs((-2) * (0)) /20]]),
								BEZIER(S0)([[-10, 5,COS(125)*Math.abs((-2) * (-1)) /20],
											 [-10,5,-15],[10,5,-15],
											 [10,5,COS(125)*Math.abs((-2) * (-1)) /20]]),
								BEZIER(S0)([[-10,10,SIN(-10)*COS(10)*Math.abs(-10 * 10 /20)],
											 [-10,10,-10],[10,10,-10],
											 [10,10,SIN(1)*COS(1)*(1/20)]])
																
								]))(domainBEZ)


var terrain42 = MAP(BEZIER(S1)([ BEZIER(S0)([[-10,-5,COS(125)*Math.abs((-2) * (-1)) /20],
											 [-10,-5,-5],[10,-5,-5],
											 [10,-5,COS(125)*Math.abs((-2) * (-1)) /20]]),
								[0,-5,0]
									]))(domainBEZ)


var terrain43 = MAP(BEZIER(S1)([ BEZIER(S0)([[-10,10,SIN(-10)*COS(10)*Math.abs(-10 * 10 /20)],
											 [-10,10,-10],[10,10,-10],
											 [10,10,SIN(1)*COS(1)*(1/20)]]),
								[0,10,0]
									]))(domainBEZ)

var terrain4 = STRUCT([terrain41,terrain42,terrain43])

// auxiliary terrain only to make 
var terrain2 = MAP(mounts2)(domain2) 
var terrain3 = MAP(mounts3)(domain3) 

var terrain = STRUCT([terrain1,terrain2,terrain3,terrain4]);

console.log("terrein4 è stato inserito alla fine per chiudere la superfice solo in PLASM.JS"+
"Ssolo per questo ultimo esercizio ed non è presente in python")

DRAW(color([139,69,19])(terrain))


//import exercise2
var  greenWat = [32/255,178/255,170/255];

var Circum = function(r, h){
var Circum0 = function(v){
return [r*COS(v[0]), r*SIN(v[0]), h];
}
return Circum0;
}

var CYLINDER = function(r, h){
function CYLINDER0(l){
var s = CYL_SURFACE([r, h])(l);
var b1 = DISK(r)(l);
var b2 = T([2])([h])(b1);
return STRUCT([s, b1, b2]);
}
return CYLINDER0;
}


var nastri = function(){
	var temp1 = Circum(1.0025,0);
	var temp2 = Circum(1.0025,0.2);
	var nastro = COLOR([1,1,0])(MAP(BEZIER(S1)([temp1,temp2]))(DOMAIN([[0,2*PI],[0,1]])([20,20])));
	var result = [];
	result[0] = T([2])([0.2])(nastro)
	for(var i=1; i<=2;i++){
		result[i] = T([2])([0.4])(result[i-1])
	}
	return STRUCT(result)
}
var pale_temp = T([0])([1])(COLOR([1,1,1])(CYLINDER(0.05,1.2)([20,20])))

var pale_temp1 = R([0,1])(PI/2)(pale_temp);

var pale_temp2 = R([0,1])(PI/2)(pale_temp1);

var pale_temp3 = R([0,1])(PI/2)(pale_temp2);

var pales1 = STRUCT([pale_temp,pale_temp1,pale_temp2,pale_temp3]);

var pales2 = R([0,1])([PI/4])(pales1)

var pales = T([0,1])([3.2,2.7])(STRUCT([pales1,pales2,nastri()]))

var lake1 = T([0,1])([3.2,2.7])(COLOR(greenWat)(CYLINDER(1,0.11)([20,20])))

var circle1 = Circum(1.3,0);

var lake_circle1 = STRUCT([MAP(BEZIER(S1)([circle1,[0,0,-0.75]]))(DOMAIN([[0,2*PI],[0,1]])([20,20])),
						MAP(BEZIER(S1)([circle1,[0,0,0]]))(DOMAIN([[0,2*PI],[0,1]])([20,20]))]);
var lake = STRUCT([lake1, T([0,1,2])([6.3,4.8,-0.3])(COLOR(greenWat)(lake_circle1)),pales])

console.log("nastri e pali per il primo lago sono presenti solo in plasm.js e solo per quest'ultimo esercizio e non in python")

DRAW(lake)


//import exercise3.JS
var Circum = function(r, h){
var Circum0 = function(v){
return [r*COS(v[0]), r*SIN(v[0]), h];
}
return Circum0;
}


var CYLINDER = function(r, h){
function CYLINDER0(l){
var s = CYL_SURFACE([r, h])(l);
var b1 = DISK(r)(l);
var b2 = T([2])([h])(b1);
return STRUCT([s, b1, b2]);
}
return CYLINDER0;
}

var CONE = function(r, h1, h2){
function CONE0(l){
var domainCircular = PROD1x1([INTERVALS(2*PI)(l[0]), INTERVALS(1)(l[1])]);
var c = Circum(r, h1);
var base = MAP(BEZIER(S1)([c, [0, 0, h1]]))(domainCircular);
var s = MAP(BEZIER(S1)([c, [0, 0, h1+h2]]))(domainCircular);
return STRUCT([s, base]);
}
return CONE0;
}

var tree = function(r1,r2,h1,h2){
	return function(intervals){
		r1 = r1 * (Math.random() +0.5);
		h1 = h1 * (Math.random() +0.5);
		var cyl = color([165,42,42])(CYLINDER(r1,h1)(intervals))
		var con = color([0,100,0])(CONE(r2,h1,h2)(intervals))
	return T([0,1])([r1/2,r1/2])(STRUCT([cyl,con]))

}}

var first_tree = tree(0.05,0.2,0.4,0.7)([12,1])

var subset  = [[6,8],[1,3]]

var num_replica = Math.floor(Math.random()*10) // numero random di alberi da 0 a 10

var forest0 = function(object,subset){
	var result = [];
	var n=0;
	for (var x = subset[0][0]; x<=subset[0][1]; x = x+0.30){
		for(var y = subset[1][0]; y<=subset[1][1]; y = y+0.30){
			var z = COS(x)*SIN(y);
			var dz = (x * y /20);
			result[n] = T([0,1,2])([x,y,z*dz])(object) 
			n++;
		}
		}
	return STRUCT(result)

}



var f = forest0(first_tree,subset)

var subset1 = [[5.1,7.3],[6.4,8.5]]

var f1 = forest0(first_tree,subset1);

var subset2 = [[8.5,9.5],[-0.75,0]]

var f2 = forest0(first_tree,subset2);

var subset3 = [[-8,-7],[-1.5,-0.25]]

var f3 = forest0(first_tree,subset3);

var forest = STRUCT([f,f1,f2,f3])

DRAW(forest)

// import exercise4.js

var house = function(x,y,z1){
	var random = Math.random()+0.5;
	var new_x = x *(random);
	var new_y = y *(random);
	var new_z = z1 *(random);

	return COLOR([1,1,1])(CUBOID([new_x,new_y,new_z]));

}

var first_house = house(1,0.3,0.7);

var subset_h1  = [[-6,-1.5],[-1,-5]]

var subset_h2  = [[1,6],[-1,-5]]
  
var house0 = function(object,subset){
	var result = [];
	var n=0;
	for (var x = subset[0][0]; x<=subset[0][1]; x = x+2.5){
		for(var y = subset[1][1]; y<=subset[1][0]; y = y+1){
			var z = COS(x*x + y*y);
			var dz =  Math.abs((x/5) * (y/5)) /20;
			result[n] = T([0,1,2])([x,y,z*dz])(object) 
			n++;
		}
		}
	return STRUCT(result)

}


var h1 = house0(first_house,subset_h1)

var h2 = house0(first_house,subset_h2)

var h = STRUCT([h1,h2])

DRAW(h)



//exercise5.js

var domain21 = DOMAIN([[-10,0], [0,1.3]])([20,20]);
var domain2line = DOMAIN([[-10,0], [1,1.1]])([20,20]);
var domain21line = DOMAIN([[-10,0], [0.1,0.2]])([20,20]);
var domain211line = DOMAIN([[-10,-0.7], [0.1,0.2]])([20,20]);


var domain11 = DOMAIN([[0,9], [0, 1.3]])([20,20]);
var domain1line = DOMAIN([[0,9], [1, 1.1]])([20,20]);
var domain11line = DOMAIN([[0,9], [0.1, 0.2]])([20,20]);
var domain111line = DOMAIN([[0.4,9], [0.1, 0.2]])([20,20]);




var street11 = MAP(mounts1)(domain11) 
var street21 = MAP(mounts2)(domain21)

var street11line = COLOR([1,1,1])(MAP(mounts1)(domain1line))
var street21line = COLOR([1,1,1])(MAP(mounts2)(domain2line))
var street111line = COLOR([1,1,1])(MAP(mounts1)(domain111line))
var street212line = COLOR([1,1,1])(MAP(mounts2)(domain211line))



var domain31 = DOMAIN([[-0.8,0.5], [-5,0]])([10,10]);
var domain311 = DOMAIN([[-0.7,-0.6], [-5,0]])([10,10]);
var domain312 = DOMAIN([[0.3,0.4], [-5,0]])([10,10]);

var street31 = MAP(mounts3)(domain31) 
var street311 = COLOR([1,1,1])(MAP(mounts3)(domain311))
var street312 = COLOR([1,1,1])( MAP(mounts3)(domain312) )

var streetline = T([2])([0.1])(STRUCT([street212line,street111line,
									   street21line,street11line,street311,street312]))

var street1 = T([2])([0.08])(COLOR([0,0,0])(STRUCT([street11,street21,street31])))

var streeth = T([0,1])([-4.3,-0.5-4.4])(COLOR([0,0,0])(CUBOID([0.5,5.6,0.07])))

var streeth1 = T([0,1])([2.9,-0.5-4.4])(COLOR([0,0,0])(CUBOID([0.5,5.6,0.07])))

var streeth2 = T([0,1])([5.3,-0.5-4.4])(COLOR([0,0,0])(CUBOID([0.5,5.6,0.07])))

var streetv1 = T([0,1])([-3.9,-0.2-1.2])(COLOR([0,0,0])(CUBOID([5,0.2,0.07])))

var streetv2 = T([0,1])([0,-1.4])(COLOR([0,0,0])(CUBOID([7,0.2,0.07])))

var streetv = STRUCT([streetv1,streetv2]);

var streetv00 = T([1])([-0.7])(STRUCT([streetv1,streetv2]));

var streetv11 = T([1])([-0.7*2])(STRUCT([streetv1,streetv2]));

var streetv22 = T([1])([-0.7*3])(STRUCT([streetv1,streetv2]));

var streetv33 = T([1])([-0.7*4])(STRUCT([streetv1,streetv2]));

var streetv_vertical = STRUCT([streetv,streetv00,streetv11,streetv22,streetv33]);

var street = STRUCT([street1,streeth,streeth1,streeth2,streetv_vertical,streetline])

DRAW(street)

