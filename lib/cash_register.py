#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
        self.items.extend([item] * quantity)
        self.total += price * quantity
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            discount_message = f"After the discount, the total comes to ${self.total:.2f}."
            print(discount_message)
            return discount_message
        else:
            return "No discount to apply."

    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
        else:
            return "No transactions to void."
        
        
