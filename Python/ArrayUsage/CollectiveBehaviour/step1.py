# paiza の入社試験では 科目 1 〜 5 の 5 科目のテストが課せられており、それぞれの科目には重みが設定されています。受験者の得点は各科目の (とった点数) * (科目の重み) となります。 5 科目の得点の合計が最も高かった受験者の得点を求めてください。


n = int(input())
m = list(map(int,input().split()))

ans = []
for _ in range(n):
    points = list(map(int,input().split()))
    sum_point = 0
    for i in range(5):
        sum_point += (m[i]*points[i])
    ans.append(sum_point)
print(max(ans))


# 解答2
n = int(input())
m = [int(input()) for _ in range(5)]
ans = 0

for i in range(n):
    a = list(map(int, input().split()))
    score = 0
    for j in range(5):
        score += a[j] * m[j]
    if score > ans:
        ans = score

print(ans)