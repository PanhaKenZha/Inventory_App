from car import create_car
# car 
cars = []

def add_car():
    car = create_car()
    cars.append(car)
    print("Car added successfully.")

def show_all_cars():
    if len(cars) == 0:
        print("No cars available.")
        return

    for index, car in enumerate(cars, start=1):
        print(f"Car {index}")
        print(f"name: {car['name']}")
        print(f"Model: {car['model']}")
        print(f"Year: {car['year']}")
        print(f"Color: {car['color']}")
        print(f"Price: ${car['price']}")
        print(f"Sold: {car['sold']}")

def getcarbyid(car_id):
    if 0 < car_id <= len(cars):
        return cars[car_id - 1]
    else:
        return None

def mark_car_as_sold(car_id):
    car = getcarbyid(car_id)
    if car:
        car["sold"] = True
        print("Car marked as sold.")
    else:
        print("Car not found.")

def delete_car(car_id):
    car = getcarbyid(car_id)
    if car:
        cars.remove(car)
        print("Car deleted successfully.")
    else:
        print("Car not found.")

def count_cars():
    return len(cars)

