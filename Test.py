class Car:
    def __init__(self, car_id, brand, colour, year):
        self.car_id = car_id
        self.brand = brand
        self.colour = colour
        self.year = year

    def __str__(self):
        return f"ID: {self.car_id}, Brand: {self.brand}, Colour: {self.colour}, Year: {self.year}"


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added: {car}")

    def get_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
        return "Car not found."

    def list_cars(self):
        if not self.cars:
            print("No cars in the system.")
        else:
            print("Car List:")
            for car in self.cars:
                print(car)

    def update_car(self, car_id, brand=None, colour=None, year=None):
        for car in self.cars:
            if car.car_id == car_id:
                if brand:
                    car.brand = brand
                if colour:
                    car.colour = colour
                if year:
                    car.year = year
                print(f"Updated: {car}")
                return
        print("Car not found.")

    def remove_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                print(f"Removed car with ID {car_id}")
                return
        print("Car not found.")

    def sort_cars(self, by="year"):
        if by == "year":
            self.cars.sort(key=lambda x: x.year)
        elif by == "brand":
            self.cars.sort(key=lambda x: x.brand.lower())
        else:
            print("Invalid sort key. Use 'year' or 'brand'.")
            return
        print(f"Cars sorted by {by}.")


# Example usage
if __name__ == "__main__":
    manager = CarManager()

    # Adding cars
    manager.add_car(Car(1, "aaa", "green", 20223))
    manager.add_car(Car(2, "bbb", "red", 2021))
    manager.add_car(Car(3, "ccc", "Black", 2022))

    # Listing all cars
    manager.list_cars()

    # Getting a car by ID
    print("Get car with ID 2:")
    print(manager.get_car(2))

    # Updating a car
    manager.update_car(1, colour="White", year=2020)

    # Removing a car
    manager.remove_car(3)

    # Sorting cars
    manager.sort_cars(by="brand")
    manager.list_cars()


    



    
      





       

    
        

     

