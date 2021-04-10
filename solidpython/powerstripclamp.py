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

def assembly():
    bd = 2
    th = 9 - bd
    w = 9
    l = 54 + w
    oh = 7+17 + bd - .5
    ball = sphere(d = bd)
    hbar = cube([l, w, th])
    vbar = cube([th, w, 2*th + oh])    
    a = hbar + up(oh + th)(hbar) + vbar
    return minkowski()(a, ball)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python powerstripclamp.py"
# End:
