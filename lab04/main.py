import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
valid = read_valid(lines)

total_lines = len([l for l in lines if l.strip()])
skipped = total_lines - len(valid)

print(len(valid))
print(skipped)
if valid:
    best = warmest_city(valid)
    avg = average_by_city(valid)[best]
    print(f'{avg:.1f}')
