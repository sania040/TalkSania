# generate_pixel_days.py
from datetime import datetime, timedelta
import json

START_DATE = datetime(2025, 10, 20)  # Monday, Oct 20, 2025
WORD = "SANIA"

# Pixel font (7 rows x 5 columns)
# GitHub shows: Sunday(row 0), Monday(row 1), ..., Saturday(row 6)
FONT = {
    'S': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'A': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'N': [
        [1,0,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'I': [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [1,1,1,1,1],
    ],
    ' ': [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
    ],
}

# Build grid
grid = [[] for _ in range(7)]
for i, char in enumerate(WORD.upper()):
    letter = FONT.get(char, FONT[' '])
    for row in range(7):
        grid[row].extend(letter[row])
    if i < len(WORD) - 1:
        for row in range(7):
            grid[row].append(0)  # space between letters

# Find the Sunday before or on START_DATE
days_since_sunday = (START_DATE.weekday() + 1) % 7
grid_start = START_DATE - timedelta(days=days_since_sunday)

# Generate dates
pixel_days = []
for week in range(len(grid[0])):
    for day in range(7):  # day 0 = Sunday, day 6 = Saturday
        if grid[day][week] == 1:
            d = grid_start + timedelta(weeks=week, days=day)
            pixel_days.append(d.strftime("%Y-%m-%d"))

# Save
with open("pixel_days.json", "w") as f:
    json.dump(sorted(set(pixel_days)), f, indent=2)

print(f"✅ Generated {len(set(pixel_days))} dates for 'SANIA'")
print(f"📅 From {min(pixel_days)} to {max(pixel_days)}")
print(f"📍 Grid starts on Sunday: {grid_start.strftime('%Y-%m-%d')}")