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

w = 29
h = 37
d = 25
th = 3

def cc(w, l, h):
    return translate([-w/2, -l/2, 0])(cube([w, l, h]))

def assembly():
    outer = cc(w + 2*th, h + 2*th, d + th)
    inner = down(0.1)(cc(w, h, d))
    hole = down(1)(cylinder(d = 5, h = d + th + 2))
    return outer - inner - hole

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

