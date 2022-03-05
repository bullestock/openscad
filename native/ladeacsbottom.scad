use <PiHoles.scad>
include <ladeacscommon.scad>

$fn = 50;

Cusb_x = -2;
Cusb_y=0;
Cusb_w=13.9;            // 13.3
Cusb_d=19.0;			// 17.2
Cusb_h=15.4;

Cpwr_x = -28;
Cpwr_z = 5.5;
Cpwr_w = 8.8;            // 13.3
Cpwr_d=14.0;			// 17.2
Cpwr_h=11;

Clock_x = 28;
Clock_z = 7;
Clock_w = 10;
Clock_d = 12.0;
Clock_h = 7.8;

Crj45_x = Cusb_x + 22.5 - 1;
Crj45_y = -1;
Crj45_w = 16.4;			// 15.4
Crj45_d = 21.5;           //21.8
Crj45_h = 15;

dims = piBoardDim("1B");
xdim = dims[0];
ydim = dims[1];

module standoff(x, y)
{
    height = box_h - 1;
    wall = 5;
    hd = 3.9; // M3 x 6 x 4
    translate([x, y, -box_h/2+1])
       difference(){
        union() {
            cylinder(height, d=hd+wall, false);
            cylinder(wall*2, d1=hd+wall*2, d2=0, false);
        }
        translate([0, 0, height - 6]) cylinder(height, d=hd, false);
    }
}

module makebottom()
{
    union()
    {
        difference()
        {
            union()
            {
                rounded_box(box_w, box_l + box_l_extra, box_h, 2, 5, false, 2, 2, 1);
                translate([Clock_x, -(box_l + box_l_extra)/2+Clock_d/2, 0]) cube([Clock_w*1.8, Clock_d, box_h-.1], center = true);
                standoff(32.5, 55 + box_l_extra/2);
                standoff(-32.5, 55 + box_l_extra/2);
                standoff(32.5, -40 - box_l_extra/2);
                standoff(-32.5, -40 - box_l_extra/2);
                translate([Cpwr_x-Cpwr_w, -(box_l + box_l_extra)/2, -box_h/2]) cube([2*Cpwr_w, Cpwr_d, box_h], center = false);
            }
            set_cutout(Cusb_x, (box_l + box_l_extra)/2, pcb_z + 2, Cusb_w, Cusb_d, Cusb_h+0.1);
            set_cutout(Crj45_x, (box_l + box_l_extra)/2, pcb_z + 2,   Crj45_w+0.1,Crj45_d+3,Crj45_h);
            set_cutout(Cpwr_x, -(box_l + box_l_extra)/2, Cpwr_z, Cpwr_w, 2*Cpwr_d, Cpwr_h+0.1);
            set_cutout(Clock_x, -(box_l + box_l_extra)/2, Clock_z, Clock_w,Clock_d*2,Clock_h+0.1);
            set_cutout(Clock_x, -(box_l + box_l_extra)/2, Clock_z - 3, 3, Clock_d,Clock_h+0.1);
            translate([20, -40, -15]) cylinder(d = 5, h = 10);
            translate([-20, -40, -15]) cylinder(d = 5, h = 10);
            translate([20, 50 + box_l_extra/2, -8]) hull()
            {
                cube([10, 10, 1]);
                translate([-1, 0, 10]) cube([10, 10, 1]);
            }
        }
        translate([2+ydim/2 - 1, 18-xdim/2 + 1 + box_l_extra/2, -3]) rotate([0, 0, 90]) piStandoffs("1B", height = 5, preview = false);
    }
}
