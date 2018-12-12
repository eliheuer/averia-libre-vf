# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os


# STATIC VARIABLE
# Width, Height, Margin, Frames
W, H, M, F = 1000, 1000, 100, 100
VAR = 0  # Variation for variable font
DOT = 19  # Dot size
AMP = 160  # Distance from center
STP = 0  # Step in sequence
XPO = 0  # X position
YPO = 0  # Y position
U = 80  # Unit


# SET FONT
def set_font():
    font("fonts/Averia-Serif-Libre-Roman-VF.ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))


# GRID
def grid(INC):
    # SET STYLE
    lineCap("round")
    stroke(0)
    STX, STY = 0, 0
    INX, INY = (W - (M * 2)) / INC, (H - (M * 2)) / INC
    for x in range(INC + 1):
        polygon((M + STX, M), (M + STX, H - M))
        STX += INX
    for y in range(INC + 1):
        polygon((M, M + STY), (H - M, M + STY))
        STY += INY


# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1 / 30)
    set_font()
    fill(1)
    rect(0, 0, W, H)

def draw_dot(X, Y):
    oval(int(X) + (W / 2), int(Y) + (W / 2), DOT, DOT)


for frame in range(F):
    # Draw PAGE
    new_page()
    strokeWidth(1)
    stroke(0)
    oval(M + 240, M + 240, 320, 320)
    grid(10)

    # Type demo
    fontSize(100)
    fontVariations(wght=300 + VAR)
    fill(0)
    stroke(None)
    text("A", (M, 800))

    # SET DOT POS
    XPO_A = (math.cos(STP) * AMP) - DOT / 2
    YPO_A = (-1 * math.sin(STP) * AMP) - DOT / 2

    draw_dot(XPO_A, YPO_A)
    STP += (0.02) * math.pi
    VAR += 10

# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("animated-specimen.gif")
os.chdir("..")
os.chdir("..")
