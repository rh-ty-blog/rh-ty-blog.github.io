#!/usr/bin/env python3
import os
import time
import random

# Characters and colors
chars = "ｦｱｳｴｵｶｷｹｺｻｼｽｾｿﾀﾂﾃﾅﾆﾇﾈﾊﾋﾎﾏﾐﾑﾒﾓﾔﾕﾗﾘﾜ01@#$%^&*()"
BRIGHT = "\033[1;92m"  # Bright green
DIM = "\033[2;32m"     # Dim green

# Get terminal size
cols = os.get_terminal_size().columns
rows = os.get_terminal_size().lines

# Track each column: [position, length]
drops = [[random.randint(-10, 0), random.randint(8, 15)] for _ in range(0, cols, 2)]

try:
    print("\033[?25l", end="")  # Hide cursor
    print("\033[2J\033[H", end="", flush=True)  # Clear screen

    while True:
        for i, drop in enumerate(drops):
            y, length = drop
            col = i * 2 + 1

            # Draw the trail
            for j in range(length):
                row = y - j
                if 1 <= row <= rows:
                    print(f"\033[{row};{col}H", end="")  # Move cursor
                    color = BRIGHT if j == 0 else DIM
                    print(f"{color}{random.choice(chars)}\033[0m", end="", flush=True)

            # Move drop down
            drop[0] += 1

            # Reset if off screen
            if drop[0] - length > rows:
                drop[0] = random.randint(-10, 0)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\033[2J\033[H\033[?25h")  # Clear, show cursor
    print("Done!")
