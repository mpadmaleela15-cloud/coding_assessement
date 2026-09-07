n = int(input())

intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

# Sort by starting time
intervals.sort()

merged = []

for start, end in intervals:
    # If there is no range yet OR ranges don't overlap
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        # Overlapping ranges → merge them
        merged[-1][1] = max(merged[-1][1], end)

# Print result
for start, end in merged:
    print(start, end)