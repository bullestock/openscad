$fn=20;

union() {
    th = 1.5;
    // 45 x 22 x 15
    iw = 22;
    ih = 15+th;
    id = 45;
    ow = iw + 2*th;
    oh = ih + th;
    od = id + 2*th;
    difference() {
        translate([-ow/2, -oh, 0]) cube([ow, oh, od]);
        translate([-iw/2, -ih-th-1, th]) cube([iw, ih+1, id]);
        offset = 8;
        hull() {
            translate([offset, -ih+th, -5]) cylinder(d = 3, h = 60);
            translate([offset, -ih-th, -5]) cylinder(d = 3, h = 60);
        }
        hull() {
            translate([-offset, -ih+th, -5]) cylinder(d = 3, h = 60);
            translate([-offset, -ih-th, -5]) cylinder(d = 3, h = 60);
        }
    }
}
