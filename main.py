class Order:

    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add an item to the shopping cart."""
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        """Calculate the total cost for all items and their quantities."""
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total

    def pay(self, payment_type: str, security_code: str) -> None:
        """Make payment using debit or credit card."""

        if payment_type == "debit":
            print("Processing debit card payment type...")
            print(f"Verifying security code {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit card payment type...")
            print(f"Verifying security code {security_code}")
            self.status = "paid"
        else:
            print(f"Error! Unknown payment type {payment_type}.")


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 250.50)
    order.add_item("Mouse", 1, 150.00)
    order.add_item("Monitor", 1, 3500.00)

    print(f"Total amount: {order.total_price()}")
    order.pay("debit", "abcd12345")
