$fn = 20;

difference() {
    union() {
        th = 1.5;
        // 45 x 22 x 15
        iw = 22;
        id = 45;
        ow = 44;
        oh = th;
        od = id + 2*20;
        translate([-ow/2, -oh, -20]) cube([ow, oh, od]);
        translate([-iw/2, -2*th, th]) cube([iw, 2*th, id]);
    }
    translate([10, 5, -10]) rotate([90]) cylinder(d = 4, h = 10);
    translate([-10, 5, 55]) rotate([90]) cylinder(d = 4, h = 10);
}
