n, k = input().split()
l = list(map(int, input().split()))
threshold_score = l[int(k) - 1]

count = sum(1 for score in l if score >= threshold_score and score > 0)

print(count)