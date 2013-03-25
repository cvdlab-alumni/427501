 function Triangle(e1,e2,e3){
this.e1 = e1;
this.e2 = e2;
this.e3 = e3;
}

var triangle1 = new Triangle(edge1,edge2,edge3);

Triangle.prototype.perimeter = function() { return this.e1.length() + this.e2.length() + this.e3.length() ; }

var per = triangle1.perimeter();

Triangle.prototype.area = function(){
var p = this.perimeter()/2; //semi-perimetro
return Math.sqrt(p*(p-this.e1.length())*(p-this.e2.length())*(p-this.e3.length()));
}

var area1 = triangle1.area();}
