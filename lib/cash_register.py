#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount

    def add_item(self, item_name, price, quantity=1):
        for _ in range(quantity):
            self.items.append((item_name, price))
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"Discount applied. New total: ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1]


