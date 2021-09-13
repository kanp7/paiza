# n 人の人に関して、それぞれの人の名前と財産が与えられます。その後に人名 S が与えられるので （S は最初に与えられた名前のうちのいずれか） 、 S の財産を表す整数を出力してください。


n = int(input())
dic = {}
for _ in range(n):
    key, value = input().split()
    dic[key] = value
s = input()
print(dic[s])