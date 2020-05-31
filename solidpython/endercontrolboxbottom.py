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

e = 0.001

stud_h = 20
iw = 95
id = 90+12
ih = stud_h + 8 + 3
th = 2

def stud(x, y):
    return translate([x + th/2, y + th/2, 0])(cylinder(h = stud_h, d2 = 6, d1 = 10) - up(stud_h - 5 + 0.1)(hole()(cylinder(h = 5, d = 3.7))))

def hinge(x):
    rd = 10
    hw = 20
    hth = 5
    cu = cube([hth, hw - rd, hw - rd])
    cy = rotate([0, 90])(cylinder(d = rd, h = 0.01))
    ho = rotate([0, 90])(cylinder(d = 5, h = 10))
    min = minkowski()(cu, cy)
    return translate([x - hth/2, -hw/2 - rd/2 + 7, rd/2])(min + translate([0, rd, -5])(cube([hth, rd, hw])) - translate([-2, hw/2 - rd/2, hw/2 - rd/2])(ho))

def assembly():
    stud_x = 5
    stud_y = 17
    stud_x_sep = 87.75
    stud_y_sep = 64.85
    studs = stud(stud_x, stud_y) + \
    stud(stud_x + stud_x_sep, stud_y) + \
    stud(stud_x, stud_y + stud_y_sep) + \
    stud(stud_x + stud_x_sep, stud_y + stud_y_sep)
    ow = iw + 2*th
    od = id + 2*th
    oh = ih + th
    slanted = rotate([20, 0, 0])(cube([2*ow, 1.5*ih, 2*ih]))
    outer = cube([ow, od, oh]) - translate([-5, -26, -ih])(slanted)
    inner = translate([th, th, th])(cube([iw, id, ih + 1])) - translate([0, -24, -ih])(slanted)
    h_inset = 20
    hinges = hinge(h_inset) + hinge(ow - h_inset)
    cablehole = translate([60+th, 15, -5])(cube([20, 10, 10]))
    return outer + hinges - inner + studs - cablehole

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python endercontrolboxbottom.py"
# End:
