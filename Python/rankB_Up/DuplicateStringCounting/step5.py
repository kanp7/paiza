# 文字列 s が入力されるので、n 文字目と n + 1 文字目を出力してください。 n + 1 文字目がない場合は何も出力しないでください。


n = int(input())
s = input()

if len(s) > n:
    print(s[n-1], s[n])


# 解答2
n = int(input()) - 1
string = input()

if n + 1 < len(string):
    print(string[n] + " " + string[n + 1])