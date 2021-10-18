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

SEGMENTS = 64#128

eps = 0.01
rr = 2

wth = 1.5
a = 28
b = a + 4*wth
c = 40.5
d = c + 4*wth
gap = 0.2
# Height of pinheaders above rim
h = 14
# Dimple
dd1 = 9
dd2 = 6.75
dh = 1.5

def dimple(a):
    pad = roundccube(dd1, 2, dd1 + 2, 1)
    offset = wth
    if a > 0:
        offset = -offset
    return hole()(rot(a, 90, 90, cylinder(d1 = dd1, d2 = dd2, h = dh))) + trans(0, offset, -dd1/2, pad)

def wirehole():
    d = 2.5
    h = 4
    c = rot(0, 90, 0, cylinder(d = d, h = 3*wth))
    return hull()(trans(0, (h - d)/2, 0, c) + trans(0, -(h - d)/2, 0, c))

def assembly():
    base = roundxycube(d, b, h + wth, rr)
    cutout = roundxycube(c + 2*wth + gap, a + 2*wth + gap, h, rr/2)
    dimples = trans(0, b/2 + eps, (h + 2*wth)/2, dimple(180)) + trans(0, -b/2 - eps, (h + 2*wth)/2, dimple(0))
    return base - down(eps)(cutout) + dimples - trans(d/2 - 2*wth, 0, h - 3, wirehole())

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python esp32camtop.py"
# End:
