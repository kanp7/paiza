# エンジニアであり、社員を管理を管理する立場にあるあなたは、効率的に社員を管理するために、
# 各社員の社員番号 number と名前 name を持ち、加えて情報を返す関数を持つような構造体、すなわち次のようなメンバ変数とメンバ関数を持つ社員クラス class employee を作成することにしました。

# メンバ変数

# number : 整数
# name : 文字列


# メンバ関数
# getnum(){
#     return number;
# }
# getname(){
#     return name;
# }


# 入力で make number name と入力された場合は変数に number , name を持つ社員を作成し、 getnum n と入力された場合は n 番目に作成された社員の number を、getname n と入力された場合は n 番目に作成された社員の name を出力してください。


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
