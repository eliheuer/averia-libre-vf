# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLES
W,H,M = 1000,1000,20  # WIDTH, HEIGHT, MARGIN
VAR_WGHT = 100        # VARIABLE FONT WEIGHT
U = 32                # ONE GRID UNIT

def set_font_roman():
    font("fonts/TitilliumWeb-Roman-VF.ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))

def set_font_italic():
    font("fonts/TitilliumWeb-Roman-VF.ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))

def grid(inc):
    stroke(0)
    stpX, stpY = 0, 0
    incX, incY = (W-(M*2))/inc, (H-(M*2))/inc
    for x in range(inc+1):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(inc+1):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

def set_box_style_a():
    fill(0)
    stroke(0)

def set_box_style_b():
    fill(1)
    stroke(0)

def draw_boxes():
    # HEADLINE
    set_box_style_b()
    rect(M, M+(U*26), (U*30), (U*4))
    # ROW 1
    rect(M+(U*1),  M+(U*15), (U*13), (U*10))
    rect(M+(U*16), M+(U*15), (U*13), (U*10))
    # ROW 2
    rect(M+(U*1),  M+(U*8), (U*13), (U*6))
    rect(M+(U*16), M+(U*8), (U*13), (U*6))
    # ROW 3
    rect(M+(U*1),  M+(U*1), (U*13), (U*6))
    rect(M+(U*16), M+(U*1), (U*13), (U*6))

# DRAW NEW PAGE
newPage(W, H)
fill(1)
rect(0, 0, W, H)
grid(30)
draw_boxes()
set_font_roman()
fill(0)
