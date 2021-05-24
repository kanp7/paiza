# エンジニアであり、社員を管理を管理する立場にあるあなたの会社には、効率的に社員を管理するために、次のようなメンバ変数とメンバ関数を持つ社員クラス class employee が存在しています。

# メンバ変数
# 整数 number, 文字列 name

# メンバ関数

# getnum(){
#     return number;
# }
# getname(){
#     return name;
# }


# しかし、この社員クラスについて、社員番号や名前が変わった際にいちいち手動で更新するのは面倒だと感じたあなたは、引数に元の社員番号と新しい社員番号を指定すれば、新しい社員番号に更新してくれる関数 change_num と　引数に元の名前と新しい名前を指定すれば、新しい名前に更新してくれる関数 change_name を作成することにしました。

# 入力で make number name と入力された場合は変数にnumber, nameを持つ社員を作成し、getnum nと入力された場合は n 番目に作成された社員の number を、getname n と入力された場合は n 番目に作成された社員の name を出力してください。

# また、 change_num n newnum と入力された場合は、n 番目に作成された社員の number を、 newnum に変更し、 change_name n newname と入力された場合は、n 番目に作成された社員の name を、 newname に変更してください。

class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number
        
    def getname(self):
        return self.name
        
    def change_num(self, new_num):
        self.number = new_num

    def change_name(self, new_name):
        self.name = new_name


n = int(input())

employee_list = []
for _ in range(n):
    inputs = input().split()
    if inputs[0] == "make":
        num = inputs[1]
        name = inputs[2]
        employee = Employee(num, name)
        employee_list.append(employee)
    elif inputs[0] == "change_num":
        idx = int(inputs[1])
        num = inputs[2]
        employee_list[idx-1].change_num(num)
    elif inputs[0] == "change_name":
        idx = int(inputs[1])
        name = inputs[2]
        employee_list[idx-1].change_name(name)
    else:
        func = inputs[0]
        idx = int(inputs[1])
        if func == "getnum":
            print(employee_list[idx-1].getnum())
        elif func == "getname":
            print(employee_list[idx-1].getname())
