h,w,n = list(map(int,input().split()))
# print(h,w,n)
# 3 3 3

acml_sum = 0
acml_sums = []
for _ in range(h):
    nums = list(map(int,input().split()))
    temp = []
    for num in nums:
        acml_sum += num
        temp.append(acml_sum)
    acml_sums.append(temp)
# [[1, 3, 6], [10, 15, 21], [28, 36, 45]]

for _ in range(n):
    x,y = list(map(int,input().split()))
