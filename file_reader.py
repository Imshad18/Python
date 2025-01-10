#!/usr/bin/env python3

# usage: file_reader.py <file name>

from pathlib import Path
import sys

path = Path(sys.argv[1])

try:
    content = path.read_text()
    print(content)
except Exception as e:
    print(f"Error {e}")
