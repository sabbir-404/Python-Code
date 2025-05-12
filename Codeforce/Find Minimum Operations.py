def min_stepcount(n, k):
    step = 0
    current_power = 1
    i = 0

    while current_power * k <= n:
        current_power *= k
        i += 1

    while n > 0:
        n -= current_power
        step += 1

        if current_power * k <= n:
            current_power *= k
        elif current_power > 1:
            current_power //= k  

    return step

# Read input
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(min_stepcount(n, k))
