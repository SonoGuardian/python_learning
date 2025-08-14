class AlchemistShop:
    
    # Прайс-лист
    price_list = {
        'healing_potion': 12,
        'mana_potion': 10,
        'invisibility_dust': 25,
        'dragon_scale': 50,
        'phoenix_feather': 75,
        'cursed_ring': 40
    }

    def __init__(self):
        self.total = 0
        self.items = {}  # {товар: количество}

    def add_item(self, item):
        if item not in self.price_list:
            print(f"Товар '{item}' отсутствует в лавке алхимика!")
            return
        
        # проверка на количество
        if self.items.get(item, 0) >= 3:
            print(f"Алхимик не продаёт больше 3 '{item}' за раз!")
            return
        
        # добавляем товар
        self.items[item] = self.items.get(item, 0) + 1
        self.total += self.price_list[item]
        print(f"Добавлено: {item} ({self.price_list[item]} зол.)")

    def print_bill(self):
        tax = (5 / 100) * self.total
        total_with_tax = self.total + tax

        print("\n--- Чек лавки алхимика ---")
        for item, qty in self.items.items():
            price = self.price_list[item]
            print(f"{item} x{qty} — {price * qty} зол.")
        
        print(f"\nПодытог: {self.total:.2f} зол.")
        print(f"Налог (5%): {tax:.2f} зол.")
        print(f"Итого: {total_with_tax:.2f} зол.")