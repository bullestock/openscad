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

e = 0.001

def assembly():
    body = cylinder(d = 25, h = 6)
    hole = cylinder(d = 4.5, h = 8)
    dd = 7
    return body - trans(-dd, 0, -1, hole) - trans(dd, 0, -1, hole)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python boschplug.py"
# End:
