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

threadlib = import_scad('threadlib/threadlib.scad')

SEGMENTS = 32

e = 0.001

corner_radius = 5
inner_corner_radius = 5
h = 30
th = 3

def threadhole(x, y):
    # 'turns' must match h
    return trans(x, y, 1, threadlib.nut("G1/4", turns=h/1.337, Douter = 25));

def corner(x, y):
    return trans(x, y, 0, cylinder(r = corner_radius, h = th))

def i_corner(x, y):
    return trans(x, y, 0, cylinder(r = inner_corner_radius, h = h))

def assembly():
    w = 170
    l = 120
    inset = 8
    x = w/2 - inset
    y = l/2 - inset
    h1 = threadhole(x, y)
    h2 = threadhole(-x, y)
    h3 = threadhole(x, -y)
    h4 = threadhole(-x, -y)
    bottom = hull()(corner(w/2, l/2) + corner(-w/2, l/2) + corner(w/2, -l/2) + corner(-w/2, -l/2))
    outer = hull()(up(1)(bottom) + up(h - 2)(bottom))
    inner = up(th)(hull()(i_corner(w/2 - th, l/2 - th) + i_corner(-(w/2 - th), l/2 - th) + i_corner(w/2 - th, -(l/2 - th)) + i_corner(-(w/2 - th), -(l/2 - th))))
    return bottom + outer - inner + h1 + h2 + h3 + h4

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python thirdhandbase.py"
# End:
