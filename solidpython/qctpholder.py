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

flange_w1 = 40
flange_w2 = 32
flange_d1 = 7
flange_d2 = 8
flange_h = 50

back_th = 3
bottom_th = 3
h = flange_h + 5
w = flange_w1 + 40
bottom_d = 35
# Radius of rounded corners
r1 = 3
# Screw hole radius
rs = 2
# Screw head radius
rsh = 7.5

def flange():
    shape = polygon(points = [ [ 0, 0 ],
                               [ flange_w1, 0 ],
                               [ flange_w1 - (flange_w1 - flange_w2)/2, flange_d1 ],
                               [ flange_w1 - (flange_w1 - flange_w2)/2, flange_d1 + flange_d2 ],
                               [ (flange_w1 - flange_w2)/2, flange_d1 + flange_d2 ],
                               [ (flange_w1 - flange_w2)/2, flange_d1 ] ])
    return linear_extrude(height = flange_h)(translate([-flange_w1/2, 0, 0])(shape))

def back_wall():
    c1 = translate([-(w/2 - r1) , back_th, h - r1])(rotate([90, 0, 0])(cylinder(r = r1, h = back_th)))
    c2 = translate([w/2 - r1, back_th, h - r1])(rotate([90, 0, 0])(cylinder(r = r1, h = back_th)))
    c3 = translate([-w/2, 0, 0])(cube([w, back_th, h - r1]))
    shp = hull()(c1 + c2 + c3)
    return translate([0, flange_d1 + flange_d2 - 0.1, 0])(shp)

def bottom():
    c1 = translate([-(w/2 - r1), r1*2, 0])(rotate([0, 0, 0])(cylinder(r = r1, h = bottom_th)))
    c2 = translate([w/2 - r1, r1*2, 0])(rotate([0, 0, 0])(cylinder(r = r1, h = bottom_th)))
    c3 = translate([-w/2, r1*2, 0])(cube([w, bottom_d - 2*r1, bottom_th]))
    shp = hull()(c1 + c2 + c3)
    return translate([0, -bottom_d, 0])(shp)

def screwhole():
    ho = cylinder(r = rs, h = 40) + translate([0, 0, flange_d1 + flange_d2])(cylinder(r1 = rs, r2 = rsh, h = 2*rsh))
    return translate([0, flange_d1 + flange_d2 + back_th + 1, flange_h/2])(rotate([90, 0, 0])(ho))

def assembly():
    f = flange()
    b = back_wall()
    sh = screwhole()
    d = 10
    shs = left(d)(sh) + right(d)(sh)
    return forward(flange_d1 + flange_d2 + 0.1)(bottom()) + b + f - shs

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

