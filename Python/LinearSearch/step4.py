n = int(input())
numbers = list(map(int,input().split()))
k = int(input())

idx_list = []
for i, n in enumerate(numbers):
    if n == k:
        idx_list.append(i+1)

for i in idx_list:
    print(i)