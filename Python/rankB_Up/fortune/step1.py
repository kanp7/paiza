# 次のような「ユーザー」と「ユーザーに対応する血液型」を連想配列（辞書）として定義して、それらのキーと値のペアを順に出力してください。


# ユーザー	ユーザーに対応する血液型
# Kyoko	B	
# Rio	O	
# Tsubame	AB	
# KurodaSensei	A	
# NekoSensei	A	



dic = {"Kyoko":"B", "Rio":"O", "Tsubame":"AB", "KurodaSensei":"A", "NekoSensei":"A"}

for key,value in dic.items():
    print(key,value)