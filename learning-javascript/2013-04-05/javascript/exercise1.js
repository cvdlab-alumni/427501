

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

NN = REPLICA

CYLINDER = CYL_SURFACE

//primo piano 

cyl =T([1,2])([0.25,0.25])(CYLINDER([0.25,2.36])([24,1]))

cyls = STRUCT(NN(5)([cyl,T([1])([5.2])]))

cub_pils = SIMPLEX_GRID([[-2.7,0.5,-2,0.5,-4.7,0.5,-4.7,0.5],[-9.2,0.5],[2.36]])

pillars0 = STRUCT([cyls, T([2])([9.2])(cyl), cub_pils])


//secondo piano
cub_pils2 = SIMPLEX_GRID([[0.5,-4.7,0.5,-4.7,0.5,-4.7,0.5,-4.7,0.5],[0.5],[2.36]])

cub_pils3 = SIMPLEX_GRID([[0.5,-4.7,0.5,-4.7,0.5,-4.7,-0.5,-4.7,0.5],[-9.2,0.5],[2.36]])

min_pil = T([1,2])([1.4,9.2])(CUBOID([0.25,0.25,2.36]))

cyl2 =T([1,2])([15.85,9.45])(CYLINDER([0.25,2.36])(24))

pillars1 = STRUCT([cub_pils2, cub_pils3, min_pil, cyl2])

//terzo piano
cub_pils4 = SIMPLEX_GRID([[0.5,-4.7,0.5,-4.7,-0.5,-4.7,-0.5,-4.7,0.5],[0.5],[2.36]])

cub_pils5 = SIMPLEX_GRID([[0.5,-4.7,0.5,-4.7,0.5,-4.7,0.5,-4.7,0.5],[-9.2,0.5],[2.36]])

pillars2 = STRUCT([cub_pils4,cub_pils5])


//quarto piano
min_pil1 = T([2])([9.2])(CUBOID([0.25,0.25,2.36]))

min_pil2 = T([1,2])([5.2,9.2])(CUBOID([0.25,0.25,2.36]))

cub_pil6 = SIMPLEX_GRID([[-0.5,-4.7,-0.5,-4.7,0.5,-4.7,-0.5,-4.7,0.5],[0.5,-8.7,0.5],[2.36]])

cub_pil7 = T([1,2])([15.6, 9.2])(CUBOID([0.50,0.5,2.36]))

pillars3 = STRUCT([min_pil1,min_pil2, cub_pil6, cub_pil7])


exercise01 = STRUCT([pillars0,T([3])([2.36+0.14]),pillars1,T([3])([2.36+0.14]),pillars2,T([3])([2.36+0.14]),pillars3])

building = STRUCT([exercise01])

VIEW(building)

