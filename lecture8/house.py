class House:
    def __init__(self):
        self.rooms = []
        self.yards = []

    def add_room(self, room_name, room_size):
        self.rooms.append((room_name, room_size))

    def add_yard(self, yard_name, yard_size):
        self.yards.append((yard_name, yard_size))

    def get_list_of_rooms(self):
        names, sizes = zip(*self.rooms)
        return list(names)

    def get_total_area(self):
        total_area = 0
        for name, size in self.rooms + self.yards:
            total_area += size

        return total_area

    def get_covered_area(self):
        covered_area = 0
        for name, size in self.rooms:
            covered_area += size

        return covered_area

    def find_area_cost(self, cost_per_sqft):
        return cost_per_sqft * self.get_total_area()


dream_house = House()
dream_house.add_room("Living room", 500)
dream_house.add_room("Kitchen", 200)
dream_house.add_room("Main bedroom", 300)
dream_house.add_room("Main bathroom", 150)
dream_house.add_room("Second bedroom", 250)
dream_house.add_room("Second bathroom", 125)
dream_house.add_room("Garage", 200)
dream_house.add_yard("Front Yard", 250)
dream_house.add_yard("Back Yard", 300)

print ("Rooms:", dream_house.get_list_of_rooms())
print ("Total area:", dream_house.get_total_area())
print ("Covered area:", dream_house.get_covered_area())
print ("Land cost:", dream_house.find_area_cost(400))

