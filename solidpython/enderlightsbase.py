#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 32

e = 0.0001

def assembly():
    w = 50
    foot = left(w/2)(tslotfoot(w, 5))
    h = 200
    pole = cube([20, 20, h - 10 - 5])
    top = rotate([0, 90, 0])(cylinder(d = 20, h = 20))
    cutout1 = translate([-11, -1, h - 20])(cube([6, 22, 22]))
    cutout2 = translate([5, -1, h - 20])(cube([6, 22, 22]))
    screwhole = translate([-11, 10, h - 10])(rotate([0, 90, 0])(cylinder(d = 5, h = 22)))
    return foot + translate([-10, 0, 5 - e])(pole) + translate([-10, 10, h - 10])(top) + hole()(cutout1 + cutout2) - screwhole

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python enderlightsbase.py"
# End:
