class AlchemyShop:

    goods = {
        "healing_potion": 12,
        "mana_potion": 10,
        "invisibility_dust": 25,
        "dragon_scale": 50,
        "phonix_fether": 75,
        "cursed_ring": 40
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.goods[item]

    def print_bill(self, tax):
        tax = (tax/100) *self.total
        total = self.total + tax

        for item in self.items:
            print (f'{item} ${self.goods[item]}')
        
        print (f'{"Total":20} ${total:.2f}')
        

