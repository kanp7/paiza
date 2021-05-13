# 整数 n と、数列 a_1, ... , a_n と、整数 k が与えられます。

# 整数 k が数列の何番目にあるかを求めてください。なお、最初の要素 (a_1) を 1 番目とします。

# ただし、数列に整数 k が含まれていない場合は、0 を出力してください。

# また、数列に整数 k が複数含まれている場合は、数列を先頭から順に見たときに最初に現れる k が数列の何番目にあるかを求めてください。

n = int(input())
numbers = list(map(int,input().split()))
k = int(input())
if k in numbers:
    print(numbers.index(k)+1)
else:
    print(0)