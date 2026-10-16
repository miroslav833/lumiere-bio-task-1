#!/usr/bin/env python3
"""Measure AST and ALT bar tops in panel B of PLoS Fig 4, ignoring error bars."""
from PIL import Image

im = Image.open("plos_g004.png").convert("L")
W, H = im.size
px = im.load()

AX_Y = 3686
AX_X = 2212
TICK0 = 2850          # 500 U/L
PER100 = (AX_Y - TICK0) / 5.0
def val(y): return (AX_Y - y) / PER100 * 100

def ink(x, y, t=215): return px[x, y] < t     # black bars and grey bars both

# locate bars on a row 12 px above the axis
y_probe = AX_Y - 12
runs, cur = [], None
for x in range(AX_X + 4, W - 2):
    if ink(x, y_probe):
        cur = [x] if cur is None else cur + [x]
    else:
        if cur and len(cur) > 25: runs.append((cur[0], cur[-1]))
        cur = None
if cur and len(cur) > 25: runs.append((cur[0], cur[-1]))
print(f"{len(runs)} bars found")

NAMES = ["Base-line AST", "Base-line ALT", "Chow AST", "Chow ALT",
         "MTPi AST", "MTPi ALT", "Progression AST", "Progression ALT",
         "Western only AST", "Western only ALT"]

for i, (xa, xb) in enumerate(runs):
    width = xb - xa + 1
    top = None
    for y in range(TICK0 - 80, AX_Y - 4):
        n = sum(1 for x in range(xa, xb + 1) if ink(x, y))
        if n >= 0.9 * width:
            top = y
            break
    name = NAMES[i] if i < len(NAMES) else f"bar {i}"
    shade = px[(xa + xb) // 2, AX_Y - 40]
    print(f"  {name:20s} x {xa}-{xb} w{width:3d}  top {top}  "
          f"value {val(top):6.1f} U/L  fill grey {shade}")
