#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 32

e = 0.0001

def assembly():
    d = 3
    screwhole = forward(5)(rotate([90])(hull()(left(2)(cylinder(d = 5, h = 10)) + right(2)(cylinder(d = 5, h = 10)))))
    plate = translate([0, 0, 0])(cube([40, d, 20])) - translate([10, 0, 10])(screwhole) - translate([30, 0, 10])(screwhole)
    join = translate([-5, 0, 19])(rotate([0, 45, 0])(cube([10, d, 10]))) + translate([-5, 0, 19])(cube([5, d, 2]))
    bw = 35
    chamfer = translate([-5, 0, 19.3])(rotate([45, 0, 0])(cube([bw, 2, 2])))
    mr = 2
    bd = 12
    tubehole = translate([7.5 - mr/2, bd - mr/2 - 6.5, -1])(hole()(cylinder(d = 4.25, h = 15)))
    ch = hull()(cylinder(d = 6, h = 15) + back(5)(cylinder(d = 4, h = 15)))
    cablehole = translate([7.5+15, bd - mr/2 - 6, -1])(hole()(ch))
    bc = minkowski()(cube([bw - mr, bd - mr, 8]), cylinder(d = mr, h = 0.1))
    block = translate([-5+mr/2, -bd+d+mr/2, 20-e])(bc - tubehole - cablehole)
    return plate + block + join + chamfer

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python bowdensupport.py"
# End:
