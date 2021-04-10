#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 128

e = 0.0001

def foot():
    h = 30
    pole = cube([20, 20, h - 10])
    top = rotate([0, 90, 0])(cylinder(d = 20, h = 20))
    cutout = translate([5, -1, h - 20])(cube([10, 22, 22]))
    screwhole = translate([-1, 10, h - 10])(rotate([0, 90, 0])(cylinder(d = 5, h = 22)))
    return pole + translate([0, 10, h - 10])(top) + hole()(cutout) - screwhole

def pie_slice(r, a):
  return intersection()(circle(r = r), square(r), rotate(a - 90)(square(r)))

def arc():
    id = 200
    od = id + 2*20
    a = 20
    peri = trans(-id/2, 0, 0, pie_slice(od/2, a) - pie_slice(id/2, a))
    return trans(20, 0, 0, rot(180+90, 0, 90, linear_extrude(20)(peri)))

def clip():
    c = trans(-11/2, 0, -1, cube([11, 4, 22])) + trans(-9/2, 3.9, -1, cube([9, 4, 22]))
    return rot(0, 90, 0, c)
        
def assembly():
    c = clip()
    c1 = trans(0, 14.5, 0, rot(-3, 0, 0, c))
    c2 = trans(0, 13, -15, rot(-8, 0, 0, c))
    c3 = trans(0, 10, -30, rot(-15, 0, 0, c))
    return foot() + arc() - c1 - c2 - c3

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python enderlightstop.py"
# End:
