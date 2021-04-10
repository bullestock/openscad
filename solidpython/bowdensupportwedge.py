#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 32

e = 0.0001

def assembly():
    ch = hull()(cylinder(d = 6, h = 8) + back(5)(cylinder(d = 4, h = 8)))
    cablehole = ch - down(1)(cylinder(d = 6+20*e, h = 10)) - translate([-5, -2, -1])(cube([10, 10, 10]))
    return cablehole

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python bowdensupportwedge.py"
# End:
