/*
 * Raspberry Pi3 case for Prusa MK3

 * Originally not intended for use with the Prusa MK3; I just wanted a openscad code base to work with to make future cases.
 * I have borrowed the standoff design and the supports at the ports from https://www.thingiverse.com/thing:1325370
 
*/

/* [Main] */

// Which part to render
part = "base"; // [ lid: Lid, base: Base, both: Box ]

/* [Hidden] */

board = [85, 56 , 1.3 ];  //dimension of rasp pi
t     = 1.40;             //Thickness of rasp pi board
p     = 3;              //Thickness of plastic case

_t_wall    = 2;              // Thickness of outer walls
_t_b  = 2;              // Thickness of top and bottom
_rpi_w = 56;
_rpi_l = 85;
_rpi_padding = 0.2;
_rpi_t = 1.4;
_rpi_hole_l_offset = 58;

_inner_h = 12.8; // Just guessing here

_h_rpi_offset = 4 + _t_b;

// This cannot be fiddle with too much as it will break the stereo jack hole
_split_offset = 7.5;

_hole_offset = 3.5;

_outer_l = _t_wall*2 + _rpi_padding*2 + _rpi_l;
_outer_w = _t_wall*2 + _rpi_padding*2 + _rpi_w;
_outer_h = _t_b*2+_inner_h+_h_rpi_offset;

$fn=20;


show();

module show() {
    base();
}

module rpi() {
    difference() {
        cube([_rpi_w,_rpi_l,_rpi_t]);

        // rpi holes
        translate([_hole_offset,_rpi_l-_hole_offset,-1]) cylinder(r=2.75/2,h=_rpi_t+2);
        translate([_rpi_w-_hole_offset,_rpi_l-_hole_offset,-1]) cylinder(r=2.75/2,h=_rpi_t+2);
        translate([_hole_offset,_rpi_l-3.5-_rpi_hole_l_offset,-1]) cylinder(r=2.75/2,h=_rpi_t+2);
        translate([_rpi_w-_hole_offset,_rpi_l-_hole_offset-_rpi_hole_l_offset,-1]) cylinder(r=2.75/2,h=_rpi_t+2);
    }
}

module box() {
    
    _sd_width = 12;
    _sd_depth = 3;
    _sd_inset = 4;

    difference() {

        cube([_t_wall*2+_rpi_padding*2+_rpi_w,_t_wall*2+_rpi_padding*2+_rpi_l,_outer_h]);

        difference() {
            translate([_t_wall,_t_wall,_t_b])
                cube([_rpi_padding*2+_rpi_w,_rpi_padding*2+_rpi_l,_outer_h-2*_t_b]);

            translate([0,_t_wall,_outer_h-_t_b])
            rotate([0,90,0])
            linear_extrude(height=_outer_w)
                polygon([[0,0],[0,(_outer_h-_split_offset-_t_b)*0.8],[_outer_h-_split_offset-_t_b,0]]);

        }


        _hole_padding=0.2;

        // SD card slot
        // We assume the slot is "almost" centered
        translate([_t_wall + _rpi_padding + _rpi_w/2 - _sd_width/2, _outer_l-_t_wall-_rpi_padding-_sd_inset,-1])
            cube([_sd_width,_sd_depth+_rpi_padding+_t_wall+_sd_inset+1,_h_rpi_offset+1]);

    }
}

module rounded_slot(l,t,h) {
    translate([t/2,t/2,0])
    hull() {
        cylinder(r=t/2,h=h);
        translate([l-t,0,0]) cylinder(r=t/2,h=h);
    }
}


module base_cut() {
    difference() {
        box();
        translate([-1,-1,_split_offset])
            cube([_rpi_w*2,_rpi_l*2,(_inner_h+_h_rpi_offset)*2]);
    }
}

module base() {

    difference() {

        union() {

            base_cut();

            _standoff_r=3.5;
            _standoff_hole_r=1.5;


            // Screw standoffs
            translate([_t_wall+_rpi_padding+_hole_offset,_t_wall+_rpi_padding+_rpi_l-_hole_offset,0])
            {
                difference() {
                    hull() {
                        cylinder(r=_standoff_r,h=_h_rpi_offset);
                        translate([-_standoff_r,_hole_offset+_rpi_padding-1,0]) cube([_standoff_r*2,1,_h_rpi_offset]);
                        translate([-_hole_offset-_rpi_padding,-_standoff_r,0]) cube([1,_standoff_r*2,_h_rpi_offset]);
                        translate([-_rpi_padding-_hole_offset,0,0])  cube([_rpi_padding+_hole_offset,_rpi_padding+_hole_offset,_h_rpi_offset]);
                    }
                    translate([0,0,_t_b]) cylinder(r=_standoff_hole_r,h=_h_rpi_offset);
                }
            }


            translate([_t_wall+_rpi_padding+_rpi_w-_hole_offset,_t_wall+_rpi_padding+_rpi_l-_hole_offset,0])
            {
                difference() {
                    hull() {
                        cylinder(r=_standoff_r,h=_h_rpi_offset);
                        translate([-_standoff_r,_hole_offset+_rpi_padding-1,0]) cube([_standoff_r*2,1,_h_rpi_offset]);
                        translate([_hole_offset+_rpi_padding,-_standoff_r,0]) cube([1,_standoff_r*2,_h_rpi_offset]);
                        translate([0,0,0])  cube([_rpi_padding+_hole_offset,_rpi_padding+_hole_offset,_h_rpi_offset]);
                    }
                    translate([0,0,_t_b]) cylinder(r=_standoff_hole_r,h=_h_rpi_offset);
                }
            }

            translate([_t_wall+_rpi_padding+_hole_offset,_t_wall+_rpi_padding+_rpi_l-_hole_offset-_rpi_hole_l_offset,0])
            {
                difference() {
                    hull() {
                        cylinder(r=_standoff_r,h=_h_rpi_offset);
                        translate([-_hole_offset-_rpi_padding,-_standoff_r,0]) cube([1,_standoff_r*2,_h_rpi_offset]);
                    }
                    translate([0,0,_t_b]) cylinder(r=_standoff_hole_r,h=_h_rpi_offset);
                }
            }

            translate([_t_wall+_rpi_padding+_rpi_w-_hole_offset,_t_wall+_rpi_padding+_rpi_l-_hole_offset-_rpi_hole_l_offset,0])
            {
                difference() {
                    hull() {
                        cylinder(r=_standoff_r,h=_h_rpi_offset);
                        translate([_hole_offset+_rpi_padding,-_standoff_r,0]) cube([1,_standoff_r*2,_h_rpi_offset]);
                    }
                    translate([0,0,_t_b]) cylinder(r=_standoff_hole_r,h=_h_rpi_offset);
                }
            }
        }

        // mounting holes
        translate([10, 15, -1]) cylinder(r=2.5,h=10);
        translate([10, 75, -1]) cylinder(r=2.5,h=10);

        // Cut out for the SD card
        _sd_width = 12;
        _sd_depth = 3;
        translate([_t_wall + _rpi_padding + _rpi_w/2 - _sd_width/2, _outer_l-_t_wall-_rpi_padding,4])
            cube([_sd_width,_sd_depth+_rpi_padding+_t_wall+1,_h_rpi_offset+1]);

    }
}
