# HqfWriter.py
from .EmbPattern import EmbPattern
from .WriteHelper import write_string_utf8

TENTH_MM_PER_INCH = 254  # 1/10 mm per inch

def write(pattern: EmbPattern, stream, settings=None):
    stitches = pattern.stitches
    if not stitches:
        return

    # Start at first stitch
    xx, yy = stitches[0][0], stitches[0][1]

    for i in range(1, len(stitches)):
        x1, y1 = xx / TENTH_MM_PER_INCH, -yy / TENTH_MM_PER_INCH  # convert to inches, invert y
        x2, y2 = stitches[i][0] / TENTH_MM_PER_INCH, -stitches[i][1] / TENTH_MM_PER_INCH

        # Write the line
        write_string_utf8(stream, f"{x1:.3f} {y1:.3f} {x2:.3f} {y2:.3f}\n")

        # Move to next stitch
        xx, yy = stitches[i][0], stitches[i][1]
