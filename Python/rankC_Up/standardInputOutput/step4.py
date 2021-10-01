# 整数 n と n 個の数 a_1, ..., a_n が改行区切りで与えられます。与えられた a_1, ..., a_n の中で最も大きい数を出力してください。


n = int(input())

ans = 0
for _ in range(n):
    a = int(input())
    if a >= ans:
        ans = a
print(ans)
    

# 解答2
n = int(input())

A = [0] * n

for i in range(n):
    a = int(input())
    A[i] = a

print(max(A))