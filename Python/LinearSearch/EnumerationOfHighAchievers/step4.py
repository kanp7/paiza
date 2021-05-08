# 整数 n と、数列 a_1, ... , a_n と、整数 k が与えられます。

# 数列に含まれる値で、k 以下であるもののうち、値が最大のものを出力してください。

# なお、k 以下である値が必ず数列に含まれていることが保証されています。

n = int(input())
numbers = list(map(int,input().split()))
# [-5, 11, 3, -9, 0]
k = int(input())

min_nums = []
for n in numbers:
    if n <= k:
        min_nums.append(n)
print(max(min_nums))