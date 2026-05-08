class Order():
    total = 0
    price = 35

    def __init__(self, amount=1, spicy=False):
        self.amount = amount
        self.spicy = spicy

    def check(self):
        sum = self.amount * Order.price

        if self.spicy:
            sauce = '加辣'
        else:
            sauce = '不加辣'
            
        print(f'{self.amount}個肉圓{sauce}，共{sum}元')
