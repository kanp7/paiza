# 英語の名前が与えられたとき、その名前をイニシャルに変換するシステムを作ることにしました。

# 「ファーストネーム ラストネーム」で与えられる半角アルファベットの氏名をイニシャルで表してください。

fn, ln = input().split()
print(fn[:1]+"."+ln[:1]+".")