from pathlib import Path

# The SVG headers are already generated in this repository.
# This file is kept as a simple regeneration entry point.
# Edit dark.svg and light.svg directly, or replace this script
# with a custom SVG generator later.

BASE = Path(__file__).parent
print(f"GitHub profile assets are in: {BASE}")
print("Files: README.md, dark.svg, light.svg")
