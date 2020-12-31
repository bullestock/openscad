#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhere in sys.path
from solid import *
from solid.utils import *
from utils import *


SEGMENTS = 32

e = 0.0001
dia = 59
lid_w = 36
corner_r = 3
lid_th = 2

def assembly():
    outer = cylinder(d = dia, h = lid_w)
    inner = down(1)(cylinder(d = dia - 2*lid_th, h = lid_w+2))
    cutter = trans(0, dia/2, -1, ccube(dia + 2, dia, lid_w + 2))
    rounder_cube = cube([lid_th + 2, corner_r, corner_r])
    rounder_cyl = trans(-1, 0, 0, rot(0, 90, 0, cylinder(r = corner_r, h = lid_th + 4)))
    rounder = rounder_cube - rounder_cyl
    rounder1 = trans(-dia/2 - 1, -corner_r, lid_w - corner_r, rounder)
    rounder2 = trans(dia/2 - lid_th - 1, -corner_r, lid_w - corner_r, rounder)
    return outer - inner - cutter - rounder1 - rounder2

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python lid.py"
# End:
