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

R = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });
   
  return function (angle) {
    return function (object) {
      return object.clone().rotate(dims, angle);
    };
  };
};

S3 = S2;
S2 = S1;
S1 = S0;


VIEW = DRAW

GRID = SIMPLEX_GRID

NN=REPLICA

window12 = COLOR(BLACK)(R([2,3])(PI/2)(CUBOID([10.4,1.17,0.25])))
 
window_general = COLOR(BLACK)(R([2,3])(PI/2)(CUBOID([4.7,1.17,0.25])))

window_trasl = T([1,2,3])([10.9,3.95,1.30])(window_general)

window1 = T([1,2,3])([10.9,0.25,2.5+1.36])(window_general)

stru = STRUCT(NN(3)([window1,T([3])(2.5)]))


windows_east = STRUCT([window_trasl,stru])

building = STRUCT([building, windows_east, T([3])([8.5])(window12)])

VIEW(building)