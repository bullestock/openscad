/*
 * 6-sided play cube
 */

$fn         = 128 ;
WIDTH       = 16  ;
DOT_DEEP    = .5   ;
DOT_DENSITY = .2  ;
DOT_TABLE   = [
      [  2, [   2, 3, 4, 5, 6 ] ],
      [  5, [               6 ] ],
      [  8, [         4, 5, 6 ] ],
      [  0, [ 1,   3,    5    ] ] ];

tr = [ cos($t*360)*360 , sin($t*360)*360  ];
tc = [ abs(cos($t*360)), abs(sin($t*360)) ];

  rotate([tr[0],tr[1],0])
    color([tc[0],tc[1],tc[0]*tc[1]])
      playcube();

module playcube()
difference() {
    intersection(){
        cube(WIDTH,center=true);
        sphere(WIDTH*0.75,center=true);
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
{
    if (n == 1)
    {
        _dot(1, 0.1, 0.2);
    }
    else if (n == 2)
    {
        _dot(1, 0.15, 0.18);
        _dot(1, -0.05, -0.17);
    }
    if (n == 3)
    {
        _dot(1, 0.15, 0.25);
        _dot(1, -0.15, -0.17);
        _dot(1, 0.08, -0.03);
    }
    if (n == 4)
    {
        _dot(1, 0.25, 0.33);
        _dot(1, -0.05, -0.27);
        _dot(1, -0.23, -0.18);
        _dot(1, 0.25, -0.17);
    }
    if (n == 5)
    {
        _dot(1, 0.25, 0.35);
        _dot(1, -0.05, -0.27);
        _dot(1, -0.235, -0.18);
        _dot(1, 0.25, -0.17);
        _dot(1, 0.09, 0.02);
    }
    if (n == 6)
    {
        _dot(1, 0.25, 0.35);
        _dot(1, -0.05, -0.27);
        _dot(1, -0.235, -0.18);
        _dot(1, 0.25, -0.17);
        _dot(1, -0.209, 0.402);
        _dot(1, 0.1, 0.2);
    }
}

module _dot( n, x, y ) {
    translate([WIDTH*x,WIDTH*y,WIDTH*.5-DOT_DEEP])
    cylinder(DOT_DEEP+1,r=WIDTH*.075);
}
