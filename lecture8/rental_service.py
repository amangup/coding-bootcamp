class Car:
    def __init__(self, make, model, model_year, size, license_plate):
        self.make = make
        self.model = model
        self.model_year = model_year
        self.size = size
        self.license_plate = license_plate
        self.mileage = 0

    def add_mileage(self, miles):
        self.mileage += miles

    def __repr__(self):
        return "%s %s %s" % (self.model_year, self.make, self.model)

class RentalService:
    def __init__(self, max_mileage):
        self.fleet = {}
        self.available = {}
        self.max_mileage = max_mileage

    def add_car_to_fleet(self, car):
        self.fleet[car.license_plate] = car
        self.available[car.license_plate] = True

    def get_available_cars(self, size):
        available_cars = []
        for license_plate, car in self.fleet.items():
            if (car.size == size and car.mileage <= self.max_mileage and
                    self.available[license_plate]):
                available_cars.append(car)

        return available_cars

    def rent_car(self, license_plate):
        self.available[license_plate] = False

    def return_car(self, license_plate, miles_driven):
        self.available[license_plate] = True
        self.fleet[license_plate].mileage += miles_driven

    def get_cars_for_sale(self):
        cars_for_sale = []
        for _, car in self.fleet.items():
            if car.mileage > self.max_mileage:
                cars_for_sale.append(car)

        return cars_for_sale

hurtz = RentalService(250)
hurtz.add_car_to_fleet(Car("Ford", "Focus", 2017, "Compact", "YAB123"))
hurtz.add_car_to_fleet(Car("Hyundai", "Sonata", 2018, "Mid-size", "ABC123"))
hurtz.add_car_to_fleet(Car("Mazda", "6", 2018, "Mid-size", "Z0MZ0M"))

print(hurtz.get_available_cars("Mid-size"))

hurtz.rent_car("Z0MZ0M")

print(hurtz.get_available_cars("Mid-size"))

hurtz.return_car("Z0MZ0M", 300)

print(hurtz.get_available_cars("Mid-size"))
print(hurtz.get_cars_for_sale())




