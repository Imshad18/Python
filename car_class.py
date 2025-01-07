class Car:
    """representing a car"""
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Getting a neatly formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        print(f"Long Name: {long_name}")

    def read_odometer(self):
        """Reading value in odometer"""
        print(f"The car has {self.odometer_reading} km on it.")

    def update_odometer(self, mileage):
        """setting odometer to given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't decrease odometer")

    def increment_odometer(self, miles):
        """adding the given amount to odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"This car has 100kg fuel tank")



class Battery():
    """describing a battery"""
    def __init__(self,battery_size=40):
        """initialize battery specs"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print the battery size """
        print(f"The car has {self.battery_size} kWh-battery")

    def update_battery(self, addon):
        self.battery_size = addon
        #print(f"The battery of this car is {self.battery_size}")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 275
        print(f"This car can go {range} km on full charge")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print(f"The car now has upgraded {self.battery_size} kWh battery")
        else:
            print(f"Please upgrade your battery.")



class ElectricCar(Car):
    """Represents aspects of Electric car"""
    def __init__(self, make, model, year):
        """initialize the attributes of parent class"""
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Electric cars don't have Gas Tank.")



my_car = ElectricCar('Ferrari','F1-75', 2024)
my_car.get_descriptive_name()

my_car.battery.update_battery(40)
my_car.battery.describe_battery()
my_car.battery.upgrade_battery()

my_car.battery.get_range()
