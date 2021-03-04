numbers = list(map(int, input().split()))
for _ in range(numbers[0]):
    nums = list(map(int, input().split()))
    i = 0
    for n in nums:
        if n == numbers[2]:
            i += 1
    print(i)

# 回答例2
N, M, K =  list(map(int, input().split()))

for _ in range(N):
    nums = list(map(int, input().split()))
    total = sum([num == K for num in nums])
    print(total)