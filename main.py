"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set): a concrete, unhurried scene, written to relax the reader
and leave them steadier. Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "At dusk the keeper climbs the lighthouse stairs, one step at a "
    "time, his palm on the cool iron rail. The lamp is already warm. "
    "Out on the water the dark gathers slowly, and the light turns, "
    "and turns again. There is all the night ahead to reach the ships."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    Path(out_dir, "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
