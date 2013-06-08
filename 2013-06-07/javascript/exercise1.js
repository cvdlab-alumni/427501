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

