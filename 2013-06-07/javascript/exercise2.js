// import exercise1.js

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

// auxiliary terrain only to make 
var terrain2 = MAP(mounts2)(domain2) 
var terrain3 = MAP(mounts3)(domain3) 

var terrain = STRUCT([terrain1,terrain2,terrain3]);

DRAW(color([139,69,19])(terrain))

// exercise2.js
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

var lake1 = T([0,1])([3.2,2.7])(COLOR(greenWat)(CYLINDER(1,0.11)([20,20])))

var circle1 = Circum(1.3,0);

var lake_circle1 = STRUCT([MAP(BEZIER(S1)([circle1,[0,0,-0.75]]))(DOMAIN([[0,2*PI],[0,1]])([20,20])),
						MAP(BEZIER(S1)([circle1,[0,0,0]]))(DOMAIN([[0,2*PI],[0,1]])([20,20]))]);
var lake = STRUCT([lake1, T([0,1,2])([6.3,4.8,-0.3])(COLOR(greenWat)(lake_circle1))])


DRAW(lake)


