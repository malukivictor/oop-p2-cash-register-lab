#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        cost = price * quantity
        self.total += cost
        self.items.extend([item] * quantity)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if self.discount > 0 and self.total > 0:
            self.total = self.total * (100 - self.discount) / 100
            if self.total == int(self.total):
                self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        if last["quantity"] > 0:
            del self.items[-last["quantity"]:]
