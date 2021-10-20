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
gap = 0.3
# Height of pinheaders above rim
h = 14
# Dimple
dd1 = 9
dd2 = 6.75
dh = 1.5

def dimple(a):
    pad = roundccube(dd1, 3, dd1 + 2, 1)
    return rot(a, 90, 90, cylinder(d1 = dd1, d2 = dd2, h = dh))

def screwhole():
    return cylinder(d = 3.5, h = 2*dd1)

def assembly():
    ah = d/2+15
    arm = down(dd1/2)(roundccube(dd1, dd1/2, ah, rr))
    brace = up(ah - dd1)(roundccube(dd1, b + 6*dh, dd1/2, rr))
    comp = 0.1 # Increase for tighter fit
    print("b: %d" % b)
    dimples = trans(0, b/2 - comp, 0, dimple(180)) + trans(0, -b/2 + comp, 0, dimple(0))
    spacer = rot(0, 90, 90, cylinder(d = dd1, h = dh))
    spacers = trans(0, b/2, 0, spacer) + trans(0, -b/2 - dh, 0, spacer)
    arms = trans(0, b/2 + dh*2, 0, arm) + trans(0, -(b/2 + dh*2), 0, arm)
    return dimples + brace + arms + spacers - up(ah - 2*dd1)(screwhole())

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python esp32cammount.py"
# End:
