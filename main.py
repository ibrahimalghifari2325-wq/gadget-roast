#!/usr/bin/env python3
"""Write a one-line roast of an everyday gadget to /output/entry.txt."""

import os

ROAST = "My earbuds die mid-call, so my left ear is still in the meeting while my right ear has already resigned."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST)
