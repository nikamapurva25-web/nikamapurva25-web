from pathlib import Path

BASE = Path(__file__).parent

print("Profile assets:")
for name in ("README.md", "dark.svg", "light.svg"):
    path = BASE / name
    print(f" - {name}: {'ready' if path.exists() else 'missing'}")

print("\nTo update the profile banner, edit dark.svg and light.svg.")
