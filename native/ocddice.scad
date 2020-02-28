/*
 * 6-sided play cube
 */

$fn         = 128 ;
WIDTH       = 64  ;
DOT_DEEP    = 3   ;
DOT_DENSITY = .2  ;
DOT_TABLE   = [
      [  2, [   2, 3, 4, 5, 6 ] ]
    , [  5, [               6 ] ]
    , [  8, [         4, 5, 6 ] ]
    , [  0, [ 1,   3,    5    ] ] ];

tr = [ cos($t*360)*360 , sin($t*360)*360  ];
tc = [ abs(cos($t*360)), abs(sin($t*360)) ];

  rotate([tr[0],tr[1],0])
    color([tc[0],tc[1],tc[0]*tc[1]])
      playcube();

module playcube()
difference() {
    intersection(){
        cube(WIDTH,center=true);
        sphere(WIDTH*2/3,center=true);
    }

    for(i=[
       [1,0,0]
      ,[2,90,0]
      ,[3,0,90]
      ,[4,0,270]
      ,[5,270,0]
      ,[6,180,0]
    ])
        rotate([i[1],i[2],0])_dots(i[0]);
}

module _dots( n )
    for(i=[-1:1],j=[-1:1])
        if(search(n,DOT_TABLE[search(abs(i*3+j*5),DOT_TABLE)[0]][1]))
            _dot(1,DOT_DENSITY*i,DOT_DENSITY*j);

module _dot( n, x, y ) {
    translate([WIDTH*x,WIDTH*y,WIDTH*.5-DOT_DEEP])
    cylinder(DOT_DEEP+1,r=WIDTH*.075);
}
