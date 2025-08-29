# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # private attribute (encapsulation)

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged to {self.__battery}%")

    def get_battery(self):
        return self.__battery


# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, refresh_rate):
        super().__init__(brand, model, battery)  # call parent constructor
        self.refresh_rate = refresh_rate

    def play_game(self, game):
        if self.get_battery() > 10:
            print(f"Playing {game} at {self.refresh_rate}Hz 🎮")
        else:
            print("Battery too low to play a game! 🔋")


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 80)
phone2 = GamingPhone("Asus", "ROG Phone", 50, 144)

phone1.charge(15)
phone2.play_game("PUBG")
