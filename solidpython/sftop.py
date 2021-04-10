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

SEGMENTS = 256

e = 0.001

width = 65
length = 164.5
height = 19
th = 3
cr = 2.5

def assembly():
    ow = 15
    outer = roundxycube(ow, width - 2*th, height, cr)
    cutter = trans(-1, th, -3, cube([20, width - 4*th, height]))
    cw = 10
    middle = trans(0, (width - 2*th - cw)/2, 0, cube([ow, cw, height]))
    sh = trans(ow/2, (width - 2*th)/2, -1, cylinder(d = 2, h = 10))
    return outer - cutter + middle - sh

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python sftop.py"
# End:
