# エンジニアのあなたの会社には、既に次のような社員クラス class employee が存在しています。

# メンバ変数
# 整数 number, 文字列 name

# メンバ関数

# getnumber(){
#     return number;
# }
# getname(){
#     return name;
# }


# 現状、この社員クラスの全てのメンバ変数・メンバ関数を設定するためには、インスタンス名.変数名 = 変数 といった具合に直接代入をしなくてはなりません。
# それは面倒なので、コンストラクタという機能を用いて、インスタンスを作成する際に インスタンス名 = new クラス名(number,name) とすることでメンバ変数を設定できるように書き換えましょう。

# 入力で make number name と入力された場合は各変数に number , name を持つ社員を作成し、getnum nと入力された場合は n 番目に作成された社員の number を、getname n と入力された場合は n 番目に作成された社員の name を出力してください。

class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number
        
    def getname(self):
        return self.name
        

n = int(input())

employee_list = []
for _ in range(n):
    inputs = input().split()
    if inputs[0] == "make":
        num = inputs[1]
        name = inputs[2]
        employee = Employee(num, name)
        employee_list.append(employee)
    else:
        func = inputs[0]
        idx = int(inputs[1])
        if func == "getnum":
            print(employee_list[idx-1].getnum())
        elif func == "getname":
            print(employee_list[idx-1].getname())
