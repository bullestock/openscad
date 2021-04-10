#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 128

e = 0.0001

def assembly():
    width = 20.5
    length = 150.5
    c1 = trans(0, 0, 0, cylinder(d = width, h = 6))
    c2 = trans(length-width, 0, 0, cylinder(d = width, h = 6))
    body = hull()(c1, c2)
    cw = 10
    cutout = cube([138, cw, 6])
    cw1 = 14
    cutout2 = cube([120, cw1, 6])
    ledhole = trans(3, 0.5, 0, cylinder(d = 2, h = 10))
    return body - trans(-4, -cw/2, 1.5, cutout) - trans(5, -cw1/2, 1.5, cutout2) - ledhole

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python gmbuttons.py"
# End:
