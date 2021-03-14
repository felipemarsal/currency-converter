import requests


class CurrencyConverter:
    cached_currencies = {
        "eur": {"eur"},
        "usd": {"usd"}
    }

    def __init__(self, x, y, z):
        self.user_initial_currency = x.lower()
        self.currency_converter = y.lower()
        self.amount = z
        self.data = requests.get(f"http://www.floatrates.com/daily/{self.user_initial_currency}.json").json()

    def cached_currency(self):
        if self.user_initial_currency == "usd":
            eur = self.data.get("eur")
            eur_rate = eur.get("rate") * self.amount
        elif self.user_initial_currency == "eur":
            usd = self.data.get("usd")
            usd_rate = usd.get("rate") * self.amount

        else:
            eur = self.data.get("eur")
            usd = self.data.get("usd")
            eur_rate = eur.get("rate") * self.amount
            usd_rate = usd.get("rate") * self.amount
        if self.currency_converter == "usd":
            return f"Exchanged amount is: {round(usd_rate, 2)} USD."
        elif self.currency_converter == "eur":
            return f"Exchanged amount is: {round(eur_rate, 2)} EUR."

    def not_cached_currency(self):
        nc_rate = self.data.get(f"{self.currency_converter}")
        nc_amount = nc_rate.get("rate") * self.amount
        return f"You would receive {round(nc_amount, 2)} {self.currency_converter.upper()}."

    def option(self):
        if self.currency_converter in self.cached_currencies:
            print("Oh! It is in the cache!")
            return self.cached_currency()
        else:
            print("Sorry, but it is not in the cache!")
            return self.not_cached_currency()


initial_currency = input("Enter your initial currency (USD, AUD, etc): ")

while True:
    change_to_currency = input("Enter currency you would like to view exchange rates for (USD, AUD, etc): ")
    amount = float(input("Enter amount: "))
    final = CurrencyConverter(initial_currency, change_to_currency, amount)

    print("\nChecking the cache...")
    print(final.option())
    user_option = input("\nEnter 'Exit' to quit the program, or 'Continue' to check other currencies: ").lower()
    print()

    if user_option == "continue":
        continue
    elif user_option == "exit":
        break
