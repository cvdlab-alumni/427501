 function Edge(p1,p2){
this.p1=p1;
this.p2=p2;}

var edge1 = new Edge(punto1 , punto2);
var edge2 = new Edge(punto2 , punto3);
var edge3 = new Edge(punto1 , punto3);

Edge.prototype.length = function() { return Math.sqrt((Math.pow(this.p1.x-p2.x,2)-Math.pow(this.p1.y-this.p2.y,2)))); }

var length_edge = edge1.length();}
