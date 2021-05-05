# 整数 n と、数列 a_1, ... , a_n が与えられます。

# 数列を先頭から順に見たときに、最初に現れる偶数が何番目にあるかを求めてください。最初の要素 (a_1) を 1 番目とします。

# なお、与えられる数列には必ず偶数が含まれていることが保証されています。

n = int(input())
numbers = list(map(int,input().split()))

for i,n in enumerate(numbers):
    if n % 2 == 0:
        print(i+1)
        break
