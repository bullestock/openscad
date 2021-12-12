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

SEGMENTS = 64

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
    d2 = 25
    d1 = 23
    l2 = 5
    l1 = 10
    return knurl(d1, l1, .5) + cylinder(d = d1, h = l1) + trans(0, 0, l1, cylinder(d = d2, h = l2)) + trans(-d2/2, 0, l1+l2, cube([d2, 1, 2]))

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python lensremover.py"
# End:
