# あなたは集団行動のリーダーです。次のような指示を出すことで様々な列の操作ができます。

# ・swap A B
# 先頭から A 番目の人と、先頭から B 番目の人の位置を入れ替える。
# ・reverse
# 列の前後を入れ替える。
# ・resize C
# 先頭から C 人を列に残し、それ以外の人を全員列から離れさせる。ただし、列が既に C 人以下の場合、何も行わない。

# 初め、列には番号 1 〜 N の N 人がおり、先頭から番号の昇順に並んでいます。(1, 2 , 3, ..., N)
# あなたの出した指示の回数 Q とその指示の内容 S_i (1 ≦ i ≦ Q) が順に与えられるので、全ての操作を順に行った後の列を出力してください。


# 失敗
n, q = map(int,input().split())

people = list(range(1,n+1))

for _ in range(q):
    order = list(input().split())
    if "swap" in order:
        a = int(order[1])  # 正：int(order[1])-1
        b = int(order[2])  # 正：int(order[2])-1
        people[a], people[b] = people[b], people[a]
    elif "reverse" in order:
        people.reverse()
    elif "resize" in order:
        n = int(order[1])
        if len(people) > n:
            people = people[:n]

for n in people:
    print(n)


# 解答
n, q = map(int, input().split())
students = list(range(1, n + 1))

for _ in range(q):
    s = input().split()
    if s[0] == "swap":
        a = int(s[1]) - 1
        b = int(s[2]) - 1
        tmp = students[a]
        students[a] = students[b]
        students[b] = tmp
    elif s[0] == "reverse":
        students.reverse()
    else:
        c = int(s[1])
        if len(students) > c:
            students = students[:c]

for student in students:
    print(student)