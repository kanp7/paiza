n = int(input())
l = []

for _ in range(n):
    a,b = list(map(int,input().split()))
    tmp = [a,b]
    l.append(tmp)

key_sort = sorted(l, reverse=True)

for apple,banana in key_sort:
    print(apple,banana)


# 解答2
# ソート用の関数は通常、配列（Python ではリスト）の配列をソートする際には、問題文で説明されたような優先順位でソートをおこないます。したがって、入力値を保持した配列をそのままソート関数に渡して降順ソートすれば答えが得られます。
n = int(input())
ab = [None] * n

for i in range(n):
    [a, b] = input().split()
    a = int(a)
    b = int(b)
    ab[i] = [a, b]

ab.sort(reverse=True)

for i in range(n):
    [a, b] = ab[i]
    print(a, b)