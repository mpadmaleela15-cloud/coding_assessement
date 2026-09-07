n = int(input())

arr = list(map(int, input().split()))

k = int(input())

# Sum of the first k elements
window_sum = sum(arr[:k])
max_sum = window_sum

# Slide the window
for i in range(k, n):
    window_sum = window_sum + arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)