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
    bw = 32
    bd = 15
    bh = 7
    block = translate([-bw/2, -bd/2, 0])(minkowski()(cylinder(d = 2, h = e), cube([bw, bd, bh])))
    mh = down(0.5)(cylinder(d = 6.3, h = 7))
    ud = 6.5
    hd = 3.5
    cone_h = ud - hd
    recess = .8
    h1 = bh - cone_h - recess
    h2 = h1 + cone_h - e
    sh = (down(1)(cylinder(d = 3.5, h = 10)) + up(h1)(cylinder(d1 = 3.5, d2 = ud, h = cone_h)) + up(h2)(cylinder(d = ud, h = 2)))
    return block - left(5)(mh) - right(5)(mh) - left(12)(sh) - right(12)(sh)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python blindsbottom.py"
# End:
