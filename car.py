def create_car():
    name = input("Enter name: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    color = input("Enter color: ")
    price = int(input("Enter price: "))

    car = {
        "name": name,
        "model": model,
        "year": year,
        "color": color,
        "price": price,
        "sold": False
    }

    return car