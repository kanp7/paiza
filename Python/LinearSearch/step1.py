# 整数 n と、数列 a_1, ... , a_n と、整数 k が与えられます。

# a_1, ... , a_n のうち k は何個あるかを求めてください。

n = int(input())
numbers = list(map(int,input().split()))
k = int(input())

print(numbers.count(k))
