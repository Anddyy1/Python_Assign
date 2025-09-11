class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"Battery now at {self.battery}%")

    def take_photo(self):
        print(f"{self.device_info()} takes a photo!")


phone1 = Smartphone("Samsung", "Galaxy S22", "128GB", 50)
phone2 = Smartphone("Apple", "iPhone 14", "256GB", 80)

print(phone1.device_info())
phone1.charge(30)
phone1.take_photo()

print(phone2.device_info())
phone2.take_photo()

# ------------------ Activity 2: Polymorphism Challenge ------------------


class Car:
    def move(self):
        print(" The car is driving on the road!")


class Plane:
    def move(self):
        print("The plane is flying in the sky!")


class Boat:
    def move(self):
        print("The boat is sailing on the water!")


vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
