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

SEGMENTS = 16#64

eps = 0.001

pcb_w = 18
pcb_l = 25
pcb_h = 3.6

vga_w = 18
vga_h = 8
vga_l = 3.5

hdmi_w = 14.5
hdmi_l = 1.1
hdmi_h = 5

extra = 2

# shell thickness
sh = 1.5

def lower():
    pcb = yccube(pcb_w, pcb_l, pcb_h + extra)
    vga = yccube(vga_w, vga_l + 1, vga_h)
    hdmi = yccube(hdmi_w, hdmi_l + 1, hdmi_h + extra)
    hole = trans(0, -1 + eps, 0, vga) + trans(0, vga_l, 2, pcb) + trans(0, vga_l + pcb_l - eps, 1, hdmi)
    o_l = vga_l + pcb_l + hdmi_l
    o_h = vga_h + 2*sh
    outer = roundccube(pcb_w + 2*sh, o_l, o_h, 2)
    cutter_h = 20
    cutter_w = pcb_w * 2
    cutter = trans(-cutter_w/2, -5, 0, cube([cutter_w, o_l + 10, cutter_h]))
    cut_z = 7
    return trans(0, o_l/2, -sh, outer) - hole - up(cut_z)(cutter)

def upper():
    o_l = vga_l + pcb_l + hdmi_l
    tabs = trans(0, (o_l - pcb_l)/2, -eps, yccube(pcb_w, pcb_l, 1.5) - trans(0, -1, 0, yccube(pcb_w - 2, pcb_l + 2, 2)))
    o_h = vga_h + 2*sh
    o_w = pcb_w + 2*sh
    outer = roundccube(o_w, o_l, o_h, 2)
    sign_w = 55
    sign = roundccube(sign_w, o_l, 2, 1)
    cutter_h = 20
    cutter_w = pcb_w * 2
    cutter = trans(-cutter_w/2, -5, 0, cube([cutter_w, o_l + 10, cutter_h]))
    logo1 = rot(0, 0, 90, text('HAL', size = 8, font = 'Contour Generator', halign = 'center'))
    logo2 = rot(0, 0, 90, text('9K', size = 8, font = 'Contour Generator', halign = 'center'))
    logo = linear_extrude(1)(trans(30, 15, 1, logo1 + trans(10, 0, 0, logo2)))
    return logo + trans(0, o_l/2, -sh, outer + trans((sign_w - o_w)/2, 0, 0, sign)) - cutter + tabs + logo

def assembly():
    #return lower()
    return upper()

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python hdmicase.py"
# End:
