def create_category():
    category_id = int(input("Enter category ID: "))
    name = input("Enter name: ")

    category = {
        "id": category_id,
        "name": name
    }

    return category
