# paiza 国の大衆居酒屋で働きながらクラスの勉強をしていたあなたは、お客さんをクラスに見立てることで店内の情報を管理できることに気付きました。
# 全てのお客さんは、ソフトドリンクと食事を頼むことができます。
# paiza 国の法律では、 20 歳以上のお客さんは成人とみなされ、お酒を頼むことができます。
# 20 歳未満のお客さんは未成年とみなされ、お酒を頼もうとした場合はその注文は取り消されます。
# また、お酒を頼んだ場合、以降の全ての食事の注文 が毎回 200 円引きになります.

# 店内の全てのお客さんの数と注文の回数、各注文をしたお客さんの番号とその内容が与えられるので、各お客さんの会計を求めてください。

# ヒント

# 注文について、20 歳未満のお客さんにできて、 20 歳以上のお客さんにできないことはないので、20歳未満のお客さんのクラスを作成して、それを継承して 20歳以上のお客さんのクラスを作成することで効率よく実装することができます。


class Customer:
    def __init__(self, age ):
        self.age = age
        self.payment = 0
        # self.pay = pay

    def add_order(self, order, price):
        self.payment += price
        if self.age < 20 and order == 'alcohol':
            self.payment -= price


class Adult(Customer):
    def __init__(self, age):
        super().__init__(age)
        self.reduce_flag = False
    
    def add_order(self, order, price):
        self.payment += price
        if  order == 'alcohol':
            self.reduce_flag = True
        if order == 'food' and self.reduce_flag == True:
            self.payment -= 200


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
    idx, order, price = input().split()
    idx = int(idx)
    price = int(price)
    customer_list[idx-1].add_order(order, price)

for customer in customer_list:
    print(customer.payment)
