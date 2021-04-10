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

lw = 95
ld = 107.2
th = 2
rh = 6

def assembly():
    lid = cube([lw, ld, rh])
    cutout = trans(th, th, th, cube([lw - 2*th, ld - 2*th, rh]))
    pothole = trans(79.5, 91.2, -1, cylinder(d = 7, h = th+2))
    displayhole = trans(8.9, 23.2, -1, cube([78.5, 51.5, th+2]))
    return lid - pothole - displayhole - cutout

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python endercontrolboxlid.py"
# End:
