# 整数 n と、数列 a_1, ... , a_n と、整数 k が与えられます。

# 数列に含まれる数のうち、k 番目に大きいものを出力してください。

n = int(input())
numbers = list(map(int,input().split()))
k = int(input())
kth_biggets = 0
for i in range(n):
    if i+1 == k:
        kth_biggets = max(numbers)
    numbers.remove(max(numbers))
print(kth_biggets)