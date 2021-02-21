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

d1 = 35 + .4
d2 = 38 + .5
d3 = d2 + 4
h1 = 11.2
h2 = 6.9
sw_h = 10
sw_d = 5.9+.5
sw_w = 12.7

def assembly():
    hole1 = down(1)(cylinder(d = d1, h = h1+2))
    hole2 = down(1)(cylinder(d = d2, h = h2))
    holes = hole2 + up(h2 - e)(hole1)
    cyl1 = cylinder(d = d3, h = h1+h2)
    cyl2 = trans(0, d2/2 + 13, 0, cylinder(d = 10, h = h1+h2))
    swhole = trans(0, d2/2 + 5, 0, ccube(sw_d, sw_h + 5, sw_w + 1))
    pinhole = trans(-d1, d2/2 + 2, 2, rot(0, 90, 0, cylinder(d = 2, h = 2*d1)))
    wirehole = trans(0, 29, 0, cylinder(d = 3, h = 20))
    return hull()(cyl1 + cyl2) - holes - swhole - hole()(pinhole) + hole()(wirehole)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python solderfume.py"
# End:
