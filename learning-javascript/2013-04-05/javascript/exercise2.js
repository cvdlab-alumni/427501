T = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
     return object.clone().translate(dims, values);
    };
  };
};

S3 = S2;
S2 = S1;
S1 = S0;

VIEW = DRAW

GRID = SIMPLEX_GRID

CYLINDER = CYL_SURFACE

MKPOL = SIMPLICIAL_COMPLEX

square1 = GRID([[3],[-9.2,3],[0.14]])
square2 = GRID([[-2.5,7.2],[-3.8,5.9],[0.14]])
square3 = GRID([[-2.5,2.2],[-3.5,0.8],[0.14]])
square4 = GRID([[-9.7,4.7],[-3.8,4.6],[0.14]])
square5 = GRID([[-14.4,0.5],[-3.8,2.1],[0.14]])
square6 = GRID([[-14.4,1.1],[-4.4,7],[0.14]])
square7 = GRID([[-3,13.8],[-6.5,5.7],[0.14]])
cylinder1 = T([1,2])([3.6,3.5])(CYLINDER([1.1,0.14])(24))
cylinder2 =  T([1,2])([16.8,9.6])(CYLINDER([2.6,0.14])(24))
floor0 = STRUCT([square1,square2,square3,square4,square5,square6,square7,cylinder1,cylinder2])



two_square1 = GRID([[21.3],[9.45],[-0.14-2.36,0.14]])
two_square2 = T([1])([-2])(GRID([[2],[-10,1.3],[-0.14-2.36,0.14]]))
two_square3 = GRID([[5.45,-6.2,9.75],[-9.45,2.75],[-0.14-2.36,0.14]])
line = T([1,2,3])([5.45,11.7,2.50])(CUBOID([6.2,0.5,0.14]))
floor1 = STRUCT([two_square1,two_square2,two_square3,line])


three_square = MKPOL([[10.4,0],[21.3,0],[21.3,12.2],[9,12.2],[9,9.45]])([[0,1,4],[2,3,4],[1,2,4]])
three_square1 = GRID([[10.4],[0.5],[-0.14-2.36-0.14-2.36,0.14]])
three_square2 = GRID([[9],[-11.7,0.5],[-0.14-2.36-0.14-2.36,0.14]])
three_square3 = GRID([[0.5],[-9.2,2.5],[-0.14-2.36-0.14-2.36,0.14]])
three_square4 = GRID([[0.25],[-0.5,8.7],[-0.14-2.36-0.14-2.36,0.14]])
three_square5 = GRID([[0.5,-0.9,7.7],[-0.5,-8.7,-0.25,0.25],[-0.14-2.36-0.14-2.36,0.14]])
three_square6 = GRID([[-0.5,1.15,-3.55,0.5],[-0.5,-8.7,0.25],[-0.14-2.36-0.14-2.36,0.14]])
empty_square = STRUCT([three_square1,three_square2,three_square3,three_square4,three_square5,three_square6])
floor2 = STRUCT([T([3])([+0.14+2.36+0.14+2.36])(EXTRUDE([0.14])(three_square)),empty_square])


four_square1 = GRID([[-10.9,5.3],[9.7,-2,0.5],[-7.5,0.14]])
four_square2 = GRID([[10.9],[12.2],[-7.5,0.14]])
four_square3 = GRID([[-10.9,-5.3,5.1],[12.2],[-7.5,0.14]])
floor3 = STRUCT([four_square1,four_square2,four_square3])


square51 = GRID([[((0.5+4.7)*4)+0.5],[0.5],[0.14]])
square52 = GRID([[0.5,-4.7-0.5-4.7,((0.5+4.7)*2)+0.5],[-0.5,+9.1],[0.14]])
square53 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1,0.5+1.8+0.5],[0.14]])
floor4 = T([3])([(2.36+0.14)*4])(STRUCT([square51,square52,square53]))



building = STRUCT([building,floor0,floor1,floor2,floor3,floor4])

VIEW(building)