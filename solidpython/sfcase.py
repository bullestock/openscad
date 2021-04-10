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
    outer = roundxycube(length, width, height + th, cr)
    inner = trans(th, th, th, roundxycube(length - 2*th, width - 2*th, height+1, cr))
    whcyl = rot(0, 90, 0, cylinder(d = 2, h = 20))
    wirehole = trans(-10, width/2, height + th - 1, hull()(whcyl + up(2)(whcyl)))
    glandhole1 = trans(-10, width*3/4, th + height/2, rot(0, 90, 0, cylinder(d = 12.5, h = 20)))
    glandhole2 = trans(-10, width/4, th + height/2, rot(0, 90, 0, cylinder(d = 12.5, h = 20)))
    return outer - inner - wirehole - glandhole1 - glandhole2

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python sfcase.py"
# End:
