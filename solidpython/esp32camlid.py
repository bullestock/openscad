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

SEGMENTS = 128

eps = 0.001
rr = 2

wth = 1.5
a = 28
b = a + 4*wth
c = 40.5
d = c + 4*wth
e = 2
f = 8
g = 12
h = 2.5
j = 8.5
k = 5
m = 2.5
# camhole offset
cho = 9.3


def assembly():
    base = roundxycube(d, b, h + e + m, rr)
    rim = roundxycube(c + 2*wth, a + 2*wth, k, rr) - down(0.5)(ccube(c, a, k+1))
    camhole = cylinder(d = f, h = 10)
    camcone = cylinder(d1 = g, d2 = f, h = e)
    cambox = ccube(j, j, m + 1)
    camcutout = camhole + camcone + up(h + e)(cambox)
    logo1 = rot(180, 0, 90, text('HAL', size = 9, font = 'Contour Generator', halign = 'center'))
    logo2 = rot(180, 0, 90, text('9K', size = 9, font = 'Contour Generator', halign = 'center'))
    logo = trans(-10, 0, -1, logo1 + trans(-10, 0, 0, logo2))
    return base + up(h + e + m - eps)(rim) - trans(cho, 0, -2*eps, camcutout) - up(-0.5)(linear_extrude(height = 1)(logo))

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python esp32camlid.py"
# End:
