!(function (exports){

  var fs = require('fs');

  var plasm_lib = require('plasm.js');
  var obj = plasm_lib.plasm;
  var fun = plasm_lib.plasm_fun;
  var plasm = obj.plasm;
  var Plasm = obj.Plasm;

  var root = this;

  Object.keys(fun).forEach(function (k) { 
    root[k] = fun[k];
  });

  var p = new Plasm();
  fun.PLASM(p);


  var scmodel = (function () {
    var domain2d = DOMAIN([[0,2*PI],[0,1]])([50,50]);

var domain1d = DOMAIN([[0,1]])([50]);

var domain2 = DOMAIN([[0,1],[0,1]])([50,50]);

var domain1 =  DOMAIN([[0,2*PI]])([50]);

var yellow = [1,1,0,0.5]

var grey = [84/255, 84/255, 84/255]

 var silver = [230/255,232/255,250/255,.8]

/* function circle : input radius and height return: function that has to map with a domain 2D*/
var circle = function (r,h) {
  return function (v) {
    return [r*COS(v[0]), r*SIN(v[0]),h];
  };
};

var bezierS0 = function(curve) {
  return MAP(BEZIER(S0)(curve))(domain1d)
}

var bezierS1 = function(curve) {
  return MAP(BEZIER(S1)(curve))(domain2d)
}

var bezierS1domain = function(curve) {
  return MAP(BEZIER(S1)(curve))(domain2)
}

function generateKnot(controlPoints){
  lun = controlPoints.length + 2 + 1;
  //var nodeSeq =  new Array(lun);
  var nodeSeq = []
  nodeSeq[0] = 0;
  nodeSeq[1] = 0;
  nodeSeq[2] = 0;
  for (i = 3; i <= lun - 4 ; i++) {
    nodeSeq[i] = i-2;
  };
  nodeSeq[lun-1] = i-2
  nodeSeq[lun-2] = i-2
  nodeSeq[lun-3] = i-2
  return nodeSeq
}

function genNUBS (controlPoints){
  var domain = INTERVALS(1)(20)
  var knots = generateKnot(controlPoints)
  var nubs = NUBS(S0)(2)(knots)(controlPoints)
  var curve = MAP(nubs)(domain)
  return [curve,nubs]
}


var INTER_C2C = function(sel){
  return function(args){ //array di punti
    var C2 = args[1]; 
    var C1 = args[0];

    return function(point) { // dominio
      v = sel(point); 
      var C1u = C1(point);
      var C2u = C2(point);

    var mapped = new Array(3); 
    var i;
    for(i=0; i<3; i +=1) {
      mapped[i] = C1u[i] + v*(C2u[i] - C1u[i]); // P1 e P2 sono punti quindi array di cordinate A*u + B(1-u);
    }
    return mapped;
    };
  };
};

var obiettivo0 = circle(1.5,0)

var obiettivo1 = circle(1,0)

var obiettivo2 = circle(1.5,1)

var obiettivo3 = circle(1,1)

var obiettivo = STRUCT([bezierS1([obiettivo0,obiettivo1]),bezierS1([obiettivo0,obiettivo2]),bezierS1([obiettivo1,obiettivo3]),
            bezierS1([obiettivo2,obiettivo3])])

var supporto_obiettivo0 = circle(1.53,-0.1);
var supporto_obiettivo1 = circle(1.63,-0.1);
var supporto_obiettivo2 = circle(1.53,0.2);
var supporto_obiettivo3 = circle(1.63,0.2);

var supporto_obiettivo1 = STRUCT([bezierS1([supporto_obiettivo0,supporto_obiettivo1]),bezierS1([supporto_obiettivo0,supporto_obiettivo2])
  ,bezierS1([supporto_obiettivo1,supporto_obiettivo3]),bezierS1([supporto_obiettivo2,supporto_obiettivo3])])

var supporto_obiettivo4 = circle(1.64,-0.1);
var supporto_obiettivo5 = circle(1.74,-0.1);
var supporto_obiettivo6 = circle(1.64,-0.7);
var supporto_obiettivo7 = circle(1.74,-0.7);

var supporto_obiettivo2 = STRUCT([bezierS1([supporto_obiettivo4,supporto_obiettivo5]),bezierS1([supporto_obiettivo4,supporto_obiettivo6])
  ,bezierS1([supporto_obiettivo5,supporto_obiettivo7]),bezierS1([supporto_obiettivo6,supporto_obiettivo7])])


var supporto_obiettivo8 = circle(1.75,-0.7);
var supporto_obiettivo9 = circle(1.90,-0.5);
var supporto_obiettivo10 = circle(2.40,-0.5);
var supporto_obiettivo11 = circle(2.55,-0.7);

var supporto_obiettivo3 = STRUCT([bezierS1([supporto_obiettivo8,supporto_obiettivo9]),bezierS1([supporto_obiettivo9,supporto_obiettivo10])
  ,bezierS1([supporto_obiettivo10,supporto_obiettivo11])])

var supporto_obiettivo = STRUCT([supporto_obiettivo1,supporto_obiettivo2,supporto_obiettivo3])


//lente
var points = [[0,0.6,1],[0.6,0.6,1],[0.7,0.5,1],[0.7,0,1],[0.7,-0.5,1],[0.6,-0.6,1],[0,-0.6,1],[-0.6,-0.6,1],
        [-0.7,-0.5,1],[-0.7,0,1],[-0.7,0.5,1],[-0.6,0.6,1],[0,0.6,1]]

var lente1 = genNUBS(points) // curve=[0] nubs=[1] parte superiore

var copertura1 = [[-1,1,0.96],[0,1,0.96],[1,1,0.96],[1,0,0.96],[1,-1,0.96],[0,-1,0.96],
                  [-1,-1,0.96],[-1,0,0.96],[-1,1,0.96]]

var copertura2 = genNUBS(copertura1)

function translatePoints (arrayOfPoints,dx,dy,dz) {
  var result = [];
  for (i=0; i < arrayOfPoints.length; i++) {
    var temp = arrayOfPoints[i];
    result.push([temp[0]+dx,temp[1]+dy,temp[2]+dz])
  }
  return result
}

var lente = bezierS1domain([lente1[1],genNUBS(translatePoints(points,0,0,-0.1))[1]])

var copertura = COLOR(grey)(bezierS1domain([copertura2[1],lente1[1]]))

var d = COLOR(yellow)(bezierS1domain([genNUBS(translatePoints(points,0,0,-0.05))[1],[0,0,0]]))

var c = COLOR(yellow)(bezierS1domain([genNUBS(translatePoints(points,0,0,-0.05))[1],[0,0,0.899]]))
//fine lente1

//photo camera body

var bodyPoints = [[0,0,0.5],[4,0,0.5],[4.1,0,0.3],[4.2,0,0.2],[4.3,0,0],
          [4.2,0,-0.2],[4.1,0,-0.3],[4,0,-0.5],[0,0,-0.5],
          [-4,0,-0.5],[-4.1,0,-0.3],[-4.2,0,-0.2],[-4.3,0,0],
          [-4.2,0,0.2],[-4.1,0,0.3],[-4,0,0.5],[0,0,0.5]];


var body = genNUBS(translatePoints(bodyPoints,0,0.2,0))


var bodyPoints1 = [[0,0,0.5],[3.7,0,0.5],[3.8,0,0.3],[3.9,0,0.2],[4,0,0],
          [3.9,0,-0.2],[3.8,0,-0.3],[3.7,0,-0.5],[0,0,-0.5],
          [-3.7,0,-0.5],[-3.8,0,-0.3],[-3.9,0,-0.2],[-4,0,0],
          [-3.9,0,0.2],[-3.8,0,0.3],[-3.7,0,0.5],[0,0,0.5]];


var body1 = genNUBS(bodyPoints1)

var bodyPoints2 = [[0,0,0.5],[4.2,0,0.5],[4.3,0,0.3],[4.4,0,0.2],[4.5,0,0],
          [4.4,0,-0.2],[4.3,0,-0.3],[4.2,0,-0.5],[0,0,-0.5],
          [-4.2,0,-0.5],[-4.3,0,-0.3],[-4.4,0,-0.2],[-4.5,0,0],
          [-4.4,0,0.2],[-4.3,0,0.3],[-4.2,0,0.5],[0,0,0.5]];


var body2 = genNUBS(translatePoints(bodyPoints2,0,0.4,0))

//parte superiore
var body3 = genNUBS(translatePoints(bodyPoints2,0,5.6,0))

var body4 = genNUBS(translatePoints(bodyPoints,0,5.8,0))

var body5 = genNUBS(translatePoints(bodyPoints1,0,6,0))


/*DRAW(body[0])
DRAW(body1[0])
DRAW(body2[0])
DRAW(body3[0])
DRAW(body4[0])
DRAW(body5[0])*/

var bodyStruct = STRUCT(
          [
          bezierS1domain([body1[1],[0,0,0]]),
          bezierS1domain([body1[1],body[1]]),
          bezierS1domain([body[1],body2[1]]),
          bezierS1domain([body2[1],body3[1]]),
          bezierS1domain([body3[1],body4[1]]),
          bezierS1domain([body4[1],body5[1]]),
          bezierS1domain([body5[1],[0,6,0]])
          ]
          );



//end body

//start write SONY
var s0_1 = bezierS0([[1.46,0, 0.26],[1.36,0,0.26]])
var s0 = bezierS0([[1.46, 0,0.36], [1.46,0, 0.26]])
var s1 = bezierS0([[1.46, 0,0.36], [2.14, 0,-0.01], [2.97,0, 0.29], [2.85,0, 0.67]])
var s2 = bezierS0([[2.85,0, 0.67],[2.81,0, 1.21],[0.98,0, 0.91],[1.79,0, 1.35]])
var s3 = bezierS0([[1.79,0, 1.35], [2.25,0, 1.4], [2.63,0, 1.23], [2.62,0, 1.08]])
var s4 = bezierS0([[2.62,0, 1.08],[2.79,0,1.08]])
var s5 = bezierS0([[1.46,0, 0.68],[1.36,0,.68]])
var s6 = bezierS0([[1.46,0, 0.68], [1.66,0, 0.05], [3.19, 0,0.5], [2.21,0, 0.71]])
var s7 = bezierS0([[1.4,0, 1.36], [1, 0,1.04], [1.4, 0,0.67], [2.21,0, 0.71]])
var s8 = bezierS0([[1.4, 0,1.36], [1.63,0, 1.57], [2.18, 0,1.61], [2.62, 0,1.37]])
var s9 = bezierS0([[2.62, 0,1.37],[2.62, 0,1.47]])
var s10 = bezierS0([[2.62, 0,1.47],[2.79,0,1.47]])
var s0_15 = bezierS0([[1.36,0,0.26],[1.36,0,0.68]])
var s4_15 = bezierS0([[2.79,0,1.08],[2.79,0,1.47]])

var s = STRUCT([s0_1,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s0_15,s4_15])

var o1 = bezierS0([[3.11, 0,0.84], [3.02, 0,1.53], [4.7, 0,1.92], [4.90, 0,0.88]])
var o2 = bezierS0([[3.11,0, 0.84], [3.11, 0,-0.01], [4.94,0, -0.03], [4.90, 0,0.88]])
var o3 = bezierS0([[3.48, 0,0.85], [3.54,0, 0.17], [4.54,0, 0.18], [4.56,0, 0.86]])
var o4 = bezierS0([[3.48,0, 0.85], [3.58,0, 1.57], [4.56,0, 1.45], [4.56, 0,0.86]])
var o = STRUCT([o1,o2,o3,o4])

var n = POLYLINE([[5.11,0, 1.47], [5.11, 0,1.37], [5.21, 0,1.37], [5.21,0, 0.36],
                        [5.11,0,0.36],[5.11,0,0.26],
                        [5.21,0, 0.26],[5.41,0, 0.26],[5.41,0, 0.36],[5.31,0, 0.36],
                        [5.31,0, 0.87],[5.71+0.2,0,0.26],
                        [5.81+0.2,0,0.26],[5.81+0.2,0,1.37],[5.91+0.2,0,1.37],[5.91+0.2,0,1.47],
                        [5.61+0.2,0,1.47],[5.61+0.2,0,1.37],[5.71+0.2,0,1.37],[5.71+0.2,0,0.87],
                        [5.31,0,1.47],[5.11,0,1.47],[5.11,0,1.37]])

var i1 = POLYLINE([[7.71,0,0.26],[7.31,0,0.26],[7.31,0,0.36],
                  [7.51,0,0.36],[7.51,0,0.67],[7.24,0,1.37],[7.14,0,1.37],
                  [7.14,0,1.47],[7.44,0,1.47],[7.44,0,1.37],[7.71,0,0.77]])

var i2 = T([0])([7.71*2])(R([0,1])([PI])(i1))

var i = STRUCT([i1,i2])

var sony = STRUCT([s,o,n,T([0])([-0.8])(i)])

//END WRITE SONY

var opacWhite = [1,1,1]

var light1 = genNUBS([[0,0,0.2],[0.6,0,0.2],[0.6,0,-0.2],[0,0,-0.2],[-0.6,0,-0.2],
              [-0.6,0,0.2],[0,0,0.2]])[1]

var light2 = genNUBS([[0,0,0.18],[0.5,0,0.18],[0.5,0,-0.18],[0,0,-0.18],[-0.5,0,-0.18],
              [-0.5,0,0.18],[0,0,0.18]])[1] // [0,0,0]+skeleton

var light3 = genNUBS([[0,0.05,0.18],[0.5,0.05,0.18],[0.5,0.05,-0.18],[0,0.05,-0.18],[-0.5,0.05,-0.18],
              [-0.5,0.05,0.18],[0,0.05,0.18]])[1]//[0,0.06,0]

var light = COLOR(opacWhite)(STRUCT([
                              bezierS1domain([light1,light3]),bezierS1domain([light3,[0,0.06,0]])
                            ])
                              )

var skeleton = SKELETON(1)(bezierS1domain([light2,[0,0,0]]))

var light_sk  = R([1,2])(PI/2)(STRUCT([light,skeleton]))

var CYLINDER = function(r,h){
  function C0(l){
  var s = COLOR([0,0,0])(CYL_SURFACE([r,h])(l));
  var b1 = COLOR([250/255,250/255,250/255,0.6])(DISK(r)(l));
  var b2 = T([2])([h])(b1);
  return STRUCT([s,b1,b2]);
  }
  return C0;
}

var mirino = T([0,1,2])([2,2.95,-0.79])(CYLINDER(0.1,0.1)(30))

//behind side

var behind1 = genNUBS([[0,0,2],[4.2-0.5,0,1.99],[4.3-0.5,0,1.98],[4.4-0.5,0,1.97],[4,0,0],
                        [3.9,0,-1.97],[3.8,0,-1.98],[3.7,0,-1.99],[0,0,-2],
                        [-3.7,0,-1.99],[-3.8,0,-1.98],[-3.9,0,-1.97],[-4,0,0],
                        [-3.9,0,1.97],[-3.8,0,1.98],[-3.7,0,1.99],[0,0,2] ])[1]

var behind2 = genNUBS([[0,0.07,2],[3.7,0.07,1.99],[3.8,0.07,1.98],[3.9,0.07,1.97],[4,0.07,0],
                        [3.9,0.07,-1.97],[3.8,0.07,-1.98],[3.7,0.07,-1.99],[0,0.07,-2],
                        [-3.7,0.07,-1.99],[-3.8,0.07,-1.98],[-3.9,0.07,-1.97],[-4,0.07,0],
                        [-3.9,0.07,1.97],[-3.8,0.07,1.98],[-3.7,0.07,1.99],[0,0.07,2] ])[1]

var behind3 = bezierS1domain([behind1,behind2])


var behind4 = COLOR([0,0,0])(bezierS1domain([behind1,[0,0,0]]))


var behind5 = COLOR([0,0,0])(bezierS1domain([behind2,[0,0.07,0]]))

var behind = T([0,1,2])([1,0,-1.75])(R([1,2])(PI/2)(STRUCT([behind3,behind4,behind5,COLOR([1,1,1])(
                                      T([0,2])([-1,-0.35])(
                                            S([0,1,2])([0.2,1,0.4])(sony)
                                          ))
                                      ]))
                                      )


//start button

var button1 = circle(0.3,0);
var button2 = circle(0.2,0.05);

var button_0 = T([0])([1.3])
              (R([1,2])([-PI/2])(STRUCT([bezierS1([button1,button2]),bezierS1([button2,[0,0,0.05]])]))
              )


var button_1 = STRUCT([ bezierS1domain([light1,light3]),bezierS1domain([light3,[0,0.05,0]])
                            ])
                              
var button = T([0,1,2])([-3.8,3.4,-1.2])(STRUCT([button_0,button_1]))


//end button

var glass = COLOR([0,0,0,.90])(c)

var lente_behind = STRUCT([lente,glass,d]);

var lente_behind_T = T([0,1,2])([-3.6,2.67,-0.8])(R([0,2])(PI)(lente_behind))



var body_T = T([0,1,2])([-1,-2.60,-1.2])(bodyStruct);

var sony_TRS = T([0,1,2])([-4.5,0,-0.7])(R([1,2])([3*PI/2])(S([0,1,2])([0.2,1,0.4])(sony)));

var behind_T = R([0,1])([PI])(behind);

var light_T = T([0,1,2])([-2, 2.95,-0.7])(light_sk);


var arrayColor = new Array();

arrayColor.push([139/255,35/255,35/255]); // brown4
arrayColor.push([205/255,133/255,63/255]); // tan3
arrayColor.push([173/255,255/255,47/255]); // greenYellow
arrayColor.push([1,1,0]); // yellow
arrayColor.push([1,0,0]); // red
arrayColor.push([1,0,1]); // blue

var n = Math.floor((Math.random()*10));

if(n>=0 && n<=5){
  color = arrayColor[n]
  body_T = COLOR(color)(body_T)
}

var model = STRUCT([obiettivo,
                    supporto_obiettivo,
                    lente,
                    copertura,
                    c,
                    d,
                    body_T, sony_TRS,
                    behind_T,
                    mirino,
                    light_T,
                    button,
                    lente_behind_T
                  ]);


DRAW(model)
  return model
  })();

  exports.author = 'marley1990';
  exports.category = 'others';
  exports.scmodel = scmodel;

  if (!module.parent) {
    fs.writeFile('./data.json', JSON.stringify(scmodel.toJSON()));
  }

}(this));