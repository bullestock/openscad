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

def assembly():
    radius = 2
    sph = sphere(r = radius)
    w = 85
    h = 12.5
    outer = ccube(w - 2*radius, w - 2*radius, h)
    iw = 75
    il = 75
    inner = ccube(iw, il, 2*h)
    cyl = rot(90, 0, 0, cylinder(h = w, d = 6))
    c1 = trans(-3, 0, 3.7-e, cyl)
    c2 = trans(3, 0, 3.7-e, cyl)
    c3 = trans(0, 0, -3, c1)
    c4 = trans(0, 0, -3, c2)
    sup = trans(0, -w/2 + 2.5, 0, ccube(1, 6-1, 7))
    slicer = ccube(w+10, w + 10, h)
    mh = down(1)(cylinder(d = 3.4, h = 4.5))
    o = (w + iw)/4 - .5
    mholes = trans(o, o, 0, mh) + trans(-o, o, 0, mh) + trans(o, -o, 0, mh) + trans(-o, -o, 0, mh)
    return minkowski()(outer, sph) - down(h)(slicer) - down(e)(inner) - hull()(c1 + c2 + c3 + c4) + sup - mholes

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python bm16frame.py"
# End:
