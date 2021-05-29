# 居酒屋で働きながらクラスの勉強をしていたあなたは、お客さんをクラスに見立てることで店内の情報を管理できることに気付きました。
# 全てのお客さんは、ソフトドリンクと食事を頼むことができます。加えて 20 歳以上のお客さんはお酒を頼むことができます。
# 20 歳未満のお客さんがお酒を頼もうとした場合はその注文は取り消されます。
# また、お酒（ビールを含む）を頼んだ場合、以降の全ての食事の注文 が毎回 200 円引きになります。

# 今回、この居酒屋でビールフェスをやることになり、ビールの注文が相次いだため、いちいちビールの値段である 500 円を書くのをやめ、伝票に注文の種類と値段を書く代わりに 0 とだけを書くことになりました。

# 店内の全てのお客さんの数と注文の回数、各注文をしたお客さんの番号とその内容が与えられるので、各お客さんの会計を求めてください

class Customer:
    def __init__(self, age ):
        self.age = age
        self.payment = 0

    def add_order(self, check):
        if len(check) >= 2:
            order = check[0]
            price = int(check[1])
            self.payment += price
            if self.age < 20 and order == 'alcohol':
                self.payment -= price


class Adult(Customer):
    def __init__(self, age):
        super().__init__(age)
        self.reduce_flag = False
    
    def add_order(self, check):
        if len(check) >= 2:
            order = check[0]
            price = int(check[1])        
            self.payment += price
            if  order == 'alcohol':
                self.reduce_flag = True
            if order == 'food' and self.reduce_flag == True:
                self.payment -= 200
        else:
            self.payment += 500
            self.reduce_flag = True



customer_num, order_num = list(map(int,input().split()))

customer_list = []
for _ in range(customer_num):
    age = int(input())
    if age < 20:
        customer = Customer(age)
        customer_list.append(customer)
    else:
        customer = Adult(age)
        customer_list.append(customer)

for _ in range(order_num):
    check = input().split()
    idx = int(check.pop(0))
    customer_list[idx-1].add_order(check)

for customer in customer_list:
    print(customer.payment)