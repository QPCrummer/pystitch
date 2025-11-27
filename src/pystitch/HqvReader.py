# HqvReader.py
from .EmbPattern import EmbPattern

TENTH_MM_PER_INCH = 254

def read(f, out: EmbPattern, settings=None):

    for raw_line in f:
        # Handle both bytes (binary mode) and str (text mode)
        if isinstance(raw_line, bytes):
            try:
                line = raw_line.decode("utf-8", errors="ignore").strip()
            except Exception:
                continue
        else:
            line = raw_line.strip()

        # Stop before thumbnail block
        if line.startswith(":Thumbnail"):
            break

        # Skip metadata
        if not line or line.startswith(":"):
            continue

        # Expect: COMMAND,x,y
        parts = line.split(",")
        if len(parts) != 3:
            continue

        cmd = parts[0].upper()

        try:
            x = float(parts[1]) * TENTH_MM_PER_INCH
            y = float(parts[2]) * TENTH_MM_PER_INCH
        except ValueError:
            continue

        if cmd == "J":
            out.move_abs(x, y)
        elif cmd == "L":
            out.stitch_abs(x, y)

    out.end()