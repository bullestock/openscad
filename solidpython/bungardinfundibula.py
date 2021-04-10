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
    th = 2
    od1 = 19.8
    id1 = od1 - 2*th
    od2 = 25.7
    id2 = od2 - 2*th
    l1 = 15
    l2 = 15
    l_mid = 15
    c1o = cylinder(d = od1, h = l1)
    c1i = trans(0, 0, -1, cylinder(d = id1, h = l1 + 2))
    c2o = cylinder(d = od2, h = l2)
    c2i = trans(0, 0, -1, cylinder(d = id2, h = l2 + 2))
    c_mid_o = cylinder(d1 = od1, d2 = od2, h = l_mid)
    c_mid_i = trans(0, 0, -1, cylinder(d1 = id1, d2 = id2, h = l_mid + 2))
    tube1 = c1o - c1i
    tube2 = c2o - c2i
    infundibula = c_mid_o - c_mid_i
    return tube1 + trans(0, 0, l1, infundibula) + trans(0, 0, l1 + l_mid, tube2)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python bungardinfundibula.py"
# End:
