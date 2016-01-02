import sys
import colorsys as col

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.startswith("HSL"):
            h, s, l = [float(n) for n in line[4:-2].split(',')]
            h, s, l = h / 360.0, s / 100.0, l / 100.0
            ans = [int(round(255 * x)) for x in col.hls_to_rgb(h, l, s)]
        elif line.startswith("HSV"):
            h, s, v = [float(n) for n in line[4:-2].split(',')]
            h, s, v = h / 360.0, s / 100.0, v / 100.0
            ans = [int(round(255 * x)) for x in col.hsv_to_rgb(h, s, v)]
        elif line[0] == "#":
            ans = [int(line[i:i+2], 16) for i in (1, 3, 5)]
        else:
            c, m, y, k = [float(n) for n in line[1:-2].split(',')]
            ans = [int(round(255*(1-e)*(1-k))) for e in (c, m, y)]
        print "RGB(%d,%d,%d)" % (ans[0], ans[1], ans[2])
