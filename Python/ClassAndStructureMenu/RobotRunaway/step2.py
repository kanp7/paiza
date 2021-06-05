# paiza 村にたびたび魔物が訪れるため、 1 〜 N 番の番号が割り当てられた N 人の勇者を雇うことにしました。
# 勇者には次のようなステータスを持ちます。

# レベル l_i
# 体力 h_i
# 攻撃力 a_i
# 防御力 d_i
# 素早さ s_i
# 賢さ c_i
# 運 f_i

# また、各勇者には次のようなイベントが発生します。

# levelup h a d s c f
# レベルが 1 上昇
# 体力が h 上昇
# 攻撃力が a 上昇
# 防御力が d 上昇
# 素早さが s 上昇
# 賢さが c 上昇
# 運が f 上昇

# muscle_training h a
# 体力が h 上昇
# 攻撃力が a 上昇

# running d s
# 防御力が d 上昇
# 素早さが s 上昇

# study c
# 賢さが c 上昇

# pray f
# 運が f 上昇

# 各勇者の初期ステータスと起こるイベントの回数、
# また、起こるイベントとその対象の勇者の番号が与えられるので、
# 全てのイベントが終わった後の各勇者のステータスを出力してください。


class Hero:
    def __init__(self, level, hitpoint, attack, defence, speed, clever, fortune):
        self.level = level
        self.hitpoint = hitpoint
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.clever = clever
        self.fortune = fortune
    

    def muscle_training(self,up_h, up_a):
        self.hitpoint += up_h
        self.attack += up_a
    

    def running(self,up_d, up_s):
        self.defence += up_d
        self.speed += up_s
    

    def study(self, up_c):
        self.clever += up_c
    

    def pray(self, up_f):
        self.fortune += up_f
    

    def levelup(self, up_h, up_a, up_d, up_s, up_c, up_f):
        self.level += 1
        self.hitpoint += up_h
        self.attack += up_a
        self.defence += up_d
        self.speed += up_s
        self.clever += up_c
        self.fortune += up_f


heros = []
n, k = list(map(int,input().split(" ")))
for _ in range(n):
    level, hitpoint, attack, defence, speed, clever, fortune = list(map(int,input().split(" ")))
    hero = Hero(level, hitpoint, attack, defence, speed, clever, fortune)
    heros.append(hero)

for _ in range(k):
    inputs = input().split(" ")
    idx = int(inputs.pop(0))  
    event = (inputs.pop(0))  # Heroクラスのどのメソッドかを特定
    rise_value = list(map(int,inputs))  # 各メソッドのステータス上昇値

    if event == "muscle_training":
        heros[idx-1].muscle_training(*rise_value)  # *で配列を引数にアンパックして渡す
    elif event == "running":
        heros[idx-1].running(*rise_value)
    elif event == "study":
        heros[idx-1].study(*rise_value)
    elif event == "pray":
        heros[idx-1].pray(*rise_value)
    elif event == "levelup":
        heros[idx-1].levelup(*rise_value)


for hero in heros:
    status_list = []
    for status in hero.__dict__.values():
        status_list.append(str(status))
    print(" ".join(status_list))
