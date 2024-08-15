'''class Currency:
    RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def change_to(self, currency):
        self.amount *= self.RATE[self.currency][currency]
        self.currency = currency

    def __add__(self, other):
        return f"{self.amount + other.amount * self.RATE[self.currency][other.currency]} {self.currency}"

    def __sub__(self, other):
        return f"{self.amount - other.amount * self.RATE[self.currency][other.currency]} {self.currency}"'''
class Currency:
    exchange_rates = {'EUR': {'RUB': 90, 'USD': 1.1},
                      'USD': {'RUB': 1 / 1.1 * 90, 'EUR': 1 / 1.1},
                      'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1}}

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{round(self.value, 2)} {self.currency}"

    def change_to(self, new_currency):
        if new_currency == self.currency:
            return
        elif new_currency in self.exchange_rates[self.currency]:
            rate = self.exchange_rates[self.currency][new_currency]
            self.value *= rate
            self.currency = new_currency
        else:
            raise ValueError(f"Conversion from {self.currency} to {new_currency} is not supported.")

    def convert_to(self, new_currency):
        if new_currency == self.currency:
            return Currency(self.value, self.currency)
        elif new_currency in self.exchange_rates[self.currency]:
            rate = self.exchange_rates[self.currency][new_currency]
            return Currency(self.value * rate, new_currency)
        else:
            raise ValueError(f"Conversion from {self.currency} to {new_currency} is not supported.")

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value + other.value, self.currency)
            else:
                return Currency(self.value + other.convert_to(self.currency).value, self.currency)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value - other.value, self.currency)
            else:
                return Currency(self.value - other.convert_to(self.currency).value, self.currency)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value * other.value, self.currency)
            else:
                return Currency(self.value * other.convert_to(self.currency).value, self.currency)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value / other.value, self.currency)
            else:
                return Currency(self.value / other.convert_to(self.currency).value, self.currency)
        else:
            raise TypeError("Unsupported operand type for /")







