use <PiHoles.scad>
include <ladeacscommon.scad>

$fn = 50;

Cusb_x = 2;
Cusb_y=0;
Cusb_w=13.9;            // 13.3
Cusb_d=19.0;			// 17.2
Cusb_h=15.4;
Cusb_z = 15;

Cpwr_x = 28;
Cpwr_z = 15.5;
Cpwr_w = 8.8;            // 13.3
Cpwr_d=14.0;			// 17.2
Cpwr_h=10.9;

Clock_x = -28;
Clock_z = 15.5;
Clock_w = 10;
Clock_d = 15;
Clock_h = 10;

Crj45_y=-1;
Crj45_w=16.4;			// 15.4
Crj45_x = -(Cusb_x + 22.5) + 5;
Crj45_d=21.5;           //21.8
Crj45_h=20;
Crj45_z = 19;

box_w = 75;
box_l = 125;
box_h = 19+3;
pcb_z = 5;

dims = piBoardDim("1B");
xdim = dims[0];
ydim = dims[1];

hd = 3.5;

module topstandoff(x, y)
{
    height = box_h - 1;
    wall = 5;
    translate([x, y, -box_h/2+1])
       union() {
        cylinder(height, d=hd+wall, false);
        cylinder(wall*2, d1=hd+wall*2, d2=0, false);
    }
}

module standoffhole(x, y)
{
    height = box_h - 1;
    union()
    {
        translate([x, y, -height]) cylinder(2*height, d=hd, false);
        translate([x, y, -height+6]) cylinder(5, d = 6, false);
    }
}


module vent(end, n)
{
    spacing = 8;
    dia = 3;
    translate([n*spacing, end*(box_l + box_l_extra)/2 - 5, -5]) hull()
    {
        rotate([0, 90, 90]) cylinder(d = dia, h = 10);
        translate([0, 0, 8]) rotate([0, 90, 90]) cylinder(d = dia, h = 10);
    }
}

module maketop()
{
    union()
    {
        difference()
        {
            union()
            {
                rounded_box(box_w, box_l + box_l_extra, box_h, 2, 5, false, 2, 2, 1);
                topstandoff(32.5, 55 + box_l_extra/2);
                topstandoff(-32.5, 55 + box_l_extra/2);
                topstandoff(32.5, -40 - box_l_extra/2);
                topstandoff(-32.5, -40 - box_l_extra/2);
            }
            set_cutout(Cusb_x, box_l/2 + box_l_extra/2, Cusb_z, Cusb_w,Cusb_d,Cusb_h+0.1);
            set_cutout(Crj45_x, box_l/2 + box_l_extra/2, Crj45_z,   Crj45_w+0.1,Crj45_d+3,Crj45_h);
            set_cutout(Clock_x, -box_l/2 - box_l_extra/2, Clock_z, Clock_w, Clock_d*2, Clock_h+0.1);
            //set_cutout(Cpwr_x, -box_l/2 - box_l_extra/2, Cpwr_z, Cpwr_w, 2*Cpwr_d, Cpwr_h+0.1);
            // Display
            dw = 34;
            translate([-dw/2, 46.5 - 15 + box_l_extra/2, -20]) cube([dw, 18, 20]);
            standoffhole(32.5, 55 + box_l_extra/2);
            standoffhole(-32.5, 55 + box_l_extra/2);
            standoffhole(32.5, -40 - box_l_extra/2);
            standoffhole(-32.5, -40 - box_l_extra/2);
            vent(-1, 0);
            vent(-1, 1);
            vent(-1, 2);
            vent(-1, 3);
            vent(-1, -1);
            vent(-1, -2);
            vent(-1, -3);
            vent(1, 0);
            vent(1, 1);
            vent(1, 2);
            vent(1, 3);
            vent(1, -1);
            vent(1, -2);
            vent(1, -3);
        }
    }
}
