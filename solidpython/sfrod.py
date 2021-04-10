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

th = 5.8
def assembly():
    disc = cylinder(r = 20, h = th)
    cut1 = trans(10, -80, -1, cube([150, 150, th+2]))
    cut2 = trans(-20, -32, -1, rot(0, 0, -9, trans(-10, 0, 0, cube([50, 50, th+2]))))
    cut3 = trans(-50+1, -20, -1, cube([50, 50, th+2]))
    cut4 = trans(-65, 10, -1, rot(0, 0, -35, cube([50, 50, th+2])))
    pinhole = trans(8, 16, -1, cylinder(d = 2, h = 10))
    return disc - cut1 - cut2 - cut4 - pinhole
if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python sfrod.py"
# End:
