s = input().strip()

left = 0
max_length = 0
seen = set()

for right in range(len(s)):
    # If character is repeated, move left
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    # Current window length
    max_length = max(max_length, right - left + 1)

print(max_length)