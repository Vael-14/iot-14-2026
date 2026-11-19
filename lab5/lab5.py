from enum import Enum


class CandyType(Enum):
    BAR = "bar"
    BUTTON = "button"
    POPCORN = "popcorn"
    GUM = "gum"
    LOLLIPOP = "lollipop"


class Candy:
    def __init__(self, name, mass_in_grams, amount, price, candy_type):
        self.__name = name
        self.__mass = mass_in_grams
        self.__amount = amount
        self.__price = price
        self.__type = candy_type
        print(f"[Constructor] Candy '{self.__name}' created")

    def __del__(self):
        print(f"[Destructor] Candy '{self.__name}' deleted")

    def get_name(self):
        return self.__name

    def get_mass(self):
        return self.__mass

    def get_amount(self):
        return self.__amount

    def get_price(self):
        return self.__price

    def get_type(self):
        return self.__type

    def set_name(self, name):
        self.__name = name

    def set_mass(self, mass):
        if mass > 0:
            self.__mass = mass
        else:
            print("Mass must be positive!")

    def set_amount(self, amount):
        if amount >= 0:
            self.__amount = amount
        else:
            print("Amount cannot be negative!")

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative!")

    def set_type(self, candy_type):
        self.__type = candy_type

    def total_mass_kg(self):
        return self.__mass * self.__amount / 1000

    def total_price(self):
        return self.__price * self.__amount

    def ate(self):
        if self.__mass * self.__amount > 2000:
            return "You're on a diet!"
        return "What delicious candies!"

    def show(self):
        print(f"Name: {self.__name:<12} | Type: {self.__type.name:<8} | "
              f"Mass: {self.__mass} g | Amount: {self.__amount} | "
              f"Price: {self.__price} UAH")

    def __str__(self):
        return (f"{self.__name} ({self.__type.name}), {self.__mass} g x "
                f"{self.__amount}, {self.__price} UAH")


class Dinner:
    def __init__(self, day, time):
        self.__day = day
        self.__time = time
        self.__candies = []
        print(f"[Constructor] Dinner on {self.__day} at {self.__time} created")

    def __del__(self):
        print(f"[Destructor] Dinner on {self.__day} deleted")

    def get_day(self):
        return self.__day

    def get_time(self):
        return self.__time

    def get_candies(self):
        return self.__candies

    def set_day(self, day):
        self.__day = day

    def set_time(self, time):
        self.__time = time

    def add_candy(self, candy):
        self.__candies.append(candy)

    def remove_candy(self, name):
        for candy in self.__candies:
            if candy.get_name() == name:
                self.__candies.remove(candy)
                print(f"Candy '{name}' removed from dinner")
                return
        print(f"Candy '{name}' not found")

    def findTheMostExpensiveCandies(self, candies, name=None):
        if name is None:
            found = list(candies)
        else:
            found = [c for c in candies if c.get_name() == name]
        found.sort(key=lambda c: c.get_price(), reverse=True)
        return found[:3]

    def sort_candies(self, parameter="price", reverse=False):
        keys = {
            "name": lambda c: c.get_name(),
            "mass": lambda c: c.get_mass(),
            "amount": lambda c: c.get_amount(),
            "price": lambda c: c.get_price(),
        }
        if parameter not in keys:
            print("Unknown parameter! Use: name, mass, amount, price")
            return
        self.__candies.sort(key=keys[parameter], reverse=reverse)

    def show(self):
        print(f"\n=== Dinner: {self.__day}, {self.__time} ===")
        if not self.__candies:
            print("No candies yet")
        for candy in self.__candies:
            candy.show()
        total = sum(c.total_price() for c in self.__candies)
        print(f"Total cost: {total} UAH")


def main():
    c1 = Candy("Roshen", 40, 10, 12.5, CandyType.BAR)
    c2 = Candy("Roshen", 30, 5, 20.0, CandyType.BUTTON)
    c3 = Candy("Roshen", 15, 8, 8.0, CandyType.GUM)
    c4 = Candy("Roshen", 25, 4, 15.0, CandyType.LOLLIPOP)
    c5 = Candy("PopCorn", 100, 3, 35.0, CandyType.POPCORN)
    c6 = Candy("Snickers", 50, 50, 25.0, CandyType.BAR)

    dinner = Dinner("Friday", "19:00")
    for candy in (c1, c2, c3, c4, c5, c6):
        dinner.add_candy(candy)
    dinner.show()

    print("\n--- Getters and setters ---")
    print("c5 name:", c5.get_name(), "| price:", c5.get_price())
    c5.set_price(30.0)
    print("c5 new price:", c5.get_price())
    c5.set_amount(-3)

    print("\n--- Method ate() ---")
    print(c1.get_name(), c1.total_mass_kg(), "kg ->", c1.ate())
    print(c6.get_name(), c6.total_mass_kg(), "kg ->", c6.ate())

    print("\n--- Top 3 most expensive 'Roshen' candies ---")
    top = dinner.findTheMostExpensiveCandies(dinner.get_candies(), "Roshen")
    for place, candy in enumerate(top, start=1):
        print(f"{place}. {candy}")

    print("\n--- Sorting by price (ascending) ---")
    dinner.sort_candies("price")
    dinner.show()

    print("\n--- Sorting by mass (descending) ---")
    dinner.sort_candies("mass", reverse=True)
    dinner.show()

    print("\n--- Remove candy ---")
    dinner.remove_candy("PopCorn")
    dinner.remove_candy("Unknown")
    dinner.show()

    print("\n--- End of program ---")


if __name__ == "__main__":
    main()