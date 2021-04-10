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
    SEGMENTS = 6
    hole = cylinder(d = 27.5, h = 6)
    hole.add_param('$fn', 6)  # make the hole hexagonal
    outer = cylinder(d = 31, h = 12)
    return outer - down(e)(hole)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python komfursko.py"
# End:
