# HqvReader.py
from typing import TextIO
from .EmbPattern import EmbPattern

TENTH_MM_PER_INCH = 254   # Pystitch uses 1/10 mm units

def read(f: TextIO, out: EmbPattern, settings=None):

    for raw_line in f:
        line = raw_line.strip()

        # Stop when reaching the embedded PNG section
        if line.startswith(":Thumbnail"):
            break

        # Skip header / metadata lines
        if line.startswith(":") or not line:
            continue

        # Expect format: X,xcoord,ycoord
        parts = line.split(",")
        if len(parts) != 3:
            continue

        cmd = parts[0].upper()

        try:
            x = float(parts[1]) * TENTH_MM_PER_INCH
            y = float(parts[2]) * TENTH_MM_PER_INCH
        except ValueError:
            continue

        if cmd == "J":          # Jump / move
            out.move_abs(x, y)

        elif cmd == "L":        # Stitch line
            out.stitch_abs(x, y)

        else:
            # Unknown command — ignore
            continue

    out.end()
