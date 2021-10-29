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

SEGMENTS = 64

eps = 0.001

pcb_w = 18
pcb_l = 28.75
pcb_h = 3.6

vga_w = 18
vga_h = 8
vga_l = 3.5

hdmi_w = 14.5
hdmi_l = 1.1
hdmi_h = 5

# shell thickness
sh = 1.5

def assembly():
    pcb = yccube(pcb_w, pcb_l, pcb_h)
    vga = yccube(vga_w, vga_l + 1, vga_h)
    hdmi = yccube(hdmi_w, hdmi_l + 1, hdmi_h)
    hole = trans(0, -1 + eps, 0, vga) + trans(0, vga_l, 2, pcb) + trans(0, vga_l + pcb_l - eps, 1, hdmi)
    o_l = vga_l + pcb_l + hdmi_l
    o_h = vga_h + 2*sh
    outer = roundccube(pcb_w + 2*sh, o_l, o_h, 2)
    cutter_h = 20
    cutter_w = pcb_w * 2
    cutter = trans(-cutter_w/2, -5, 0, cube([cutter_w, o_l + 10, cutter_h]))
    cut_z = 5
    return trans(0, o_l/2, -sh, outer) - hole - up(cut_z)(cutter)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python hdmicase.py"
# End:
