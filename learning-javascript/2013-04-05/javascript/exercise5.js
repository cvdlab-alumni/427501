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

VIEW = DRAW


''' step '''

step2D = MKPOL([[[0,0],[0.50,0.19],[0.5,0.33],[0,0.33]],[[1,2,3,4]],None])

step3D = MAP([S1,S3,S2])(PROD([step2D,Q(1.1)]))

''' ramp '''

ramp_origin = STRUCT(NN(13)([step3D, T([1,3])([0.50,0.19])]))

stair2 = T([1,2,3])([2.3,9.7,2.64])(ramp_origin)

stair3 = T([1,2,3])([8.8,9.7,2.64+2.5])(ramp_origin)

stair1 = T([1,2,3])([3,9.7,0.14])(R([1,2])(PI*2)(ramp_origin))

VIEW(STRUCT([building,stair1,stair2,stair3]))