#!/usr/bin/env python3
import os

os.system("convert test.png -dither none -remap ./pale.png out.png")
