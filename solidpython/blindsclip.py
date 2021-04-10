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
    clip_h = 22
    cutout = up(-0.5)(scale([23.5/9, 1, 1])(cylinder(d = 9, h = clip_h+1)))
    cw = 22+3
    ch = 15
    block = translate([-5-3, -ch/2, 0])(minkowski()(cylinder(d = 2, h = e), cube([cw, ch, clip_h-e])))
    mh = hole()(translate([7, 0, 0])(rotate([0, 90, 0])(cylinder(d = 6.5, h = 10.5))))
    return block - cutout - up(6)(mh) - up(clip_h-6)(mh)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python blindsclip.py"
# End:
