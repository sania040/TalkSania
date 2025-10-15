# commit_if_pixel_day.py
import json
import os
from datetime import datetime
import subprocess

TODAY = datetime.utcnow().strftime("%Y-%m-%d")

# Load pixel days
if not os.path.exists("pixel_days.json"):
    print("❌ pixel_days.json not found!")
    exit(1)

with open("pixel_days.json") as f:
    pixel_days = set(json.load(f))

if TODAY not in pixel_days:
    print(f"📅 {TODAY} is not a sania day. Skipping.")
    exit(0)

print(f"🎉 {TODAY} is a sania day!")

# Read methods
if not os.path.exists("ml_methods.txt"):
    print("❌ ml_methods.txt not found!")
    exit(1)

with open("ml_methods.txt", "r") as f:
    all_methods = [line.strip() for line in f if line.strip()]

if not all_methods:
    print("❌ ml_methods.txt is empty!")
    exit(1)

# Take up to 12
methods_to_use = all_methods[:12]
remaining = all_methods[12:]

print(f"📦 Using {len(methods_to_use)} methods")

# Write log and commit each
for i, method in enumerate(methods_to_use, 1):
    with open("committed_methods.log", "a") as log:
        log.write(f"{TODAY}: {method}\n")
    subprocess.run(["git", "add", "committed_methods.log"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add: {method} ({i}/{len(methods_to_use)})"], check=True)

# Save remaining methods
with open("ml_methods.txt", "w") as f:
    for m in remaining:
        f.write(m + "\n")

print(f"💾 {len(remaining)} methods left")