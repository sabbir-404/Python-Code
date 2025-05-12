def domino(m, n):
    return (m * n) // 2

m, n = input().split()
print(domino(int(m), int(n)))