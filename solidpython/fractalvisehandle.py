#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re
import math

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 100

eps = 0.001

def knurl(d, h, r=1, numKnurls=360/15, center=False):
    """
    Makes simple knurls that wrap around a cylinder in z. (Useful for control knobs or thumbscrews.)

    It places knurls on the outside a cylinder of diameter d and height h.
    Each knurl is a 90 degree corner.
    Knurls extend to an additional radius of r (resulting outside diameter is therefore d+2*r).
    d is the diamter of the base cylinder (not including knurls)
    h is the height
    r is the additional radius of each knurl (in addition the cylinder radius)
    numKnurls is the number of knurls around the cylinder (rounded up to the next multiple of 4).
    center is the same as for "cylinder" OpenSCAD primitive

    """
    knurlSide = math.sqrt((d+2*r)**2/2)
    knurl = cylinder(d = 2*r, h = h)
    knurl = translate([-d/2, 0, 0])(knurl)

    knurls = []

    degreeStep = int(90/math.ceil(numKnurls/4))

    for deg in range(0, 360, degreeStep):
        knurls += rotate([0,0,deg])(knurl)

    knurls -= down(1)(cylinder(d=d, h=h+2))

    if center:
        knurls = down(h/2)(knurls)

    return knurls

def assembly():
    d2 = 24
    d1 = 22
    l2 = 8
    l1 = 20
    slit_w = 2
    screw_d = 6
    cutoff = 16.5
    cap = sphere(r = 20) - trans(-25, -25, -cutoff, cube([50, 50, 50]))
    return knurl(d1, l1, .5) + cylinder(d = d1, h = l1) + \
        trans(0, 0, l1, cylinder(d = d2, h = l2)) - \
        down(10)(cylinder(d = 8, h = 50)) - \
        trans(-slit_w/2, 0, 2, cube([slit_w, 20, 40])) + \
        trans(0, 0, cutoff - eps, cap) - \
        trans(5, d2/2 - screw_d/2 - 2, l1 + l2/2, rot(90, 0, 90, cylinder(d = screw_d, h = 20))) - \
        trans(-26, d2/2 - screw_d/2 - 2, l1 + l2/2, rot(90, 0, 90, cylinder(d = 6.8, h = 20, segments = 6))) - \
        trans(-25, d2/2 - screw_d/2 - 2, l1 + l2/2, rot(90, 0, 90, cylinder(d = 3.5, h = 50)))
        

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python fractalvisehandle.py"
# End:
