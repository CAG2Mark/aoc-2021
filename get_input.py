import os
import sys

if len(sys.argv) < 3:
    print("Expected 2 arguments.")
    sys.exit()
day = int(sys.argv[1])
session = sys.argv[2]
os.system(f"curl https://adventofcode.com/2021/day/{day}/input --cookie \"session={session}\" -o ./day{day}/input")


