#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 32

e = 0.001

stud_h = 20
iw = 95
id = 90+12
ih = stud_h + 8 + 3
th = 2

def hinge():
    h = 30
    pole = cube([20, 20, h - 10])
    top = rotate([0, 90, 0])(cylinder(d = 20, h = 20))
    slot_width = 5.5
    cutout = translate([(20 - slot_width)/2, -1, h - 25])(cube([slot_width, 22, 30]))
    screwhole = translate([-1, 10, h - 10])(rotate([0, 90, 0])(cylinder(d = 5, h = 22)))
    return pole + translate([0, 10, h - 10])(top) + hole()(cutout) - screwhole

def assembly():
    w = 110
    foot = left(w/2)(tslotfoot(w, 5))
    th = 2
    iw = 95
    ow = iw + 2*th
    h_inset = 20
    hinges = trans(h_inset, 0, 0, hinge()) + trans(ow-h_inset, 0, 0, hinge())
    return foot() + trans(-(ow+h_inset)/2, 0, 0, hinges())

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python endercontrolboxhinge.py"
# End:
