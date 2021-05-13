# 整数 n と、数列 a_1, ... , a_n が与えられます。

# 数列に含まれる数のうち、2 番目に大きいものを出力してください。

n = int(input())
numbers = list(map(int,input().split()))

biggest = max(numbers)
numbers.remove(biggest)

second = max(numbers)
print(second)