def create_user():
    user_id = int(input("Enter user ID: "))
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    user = {
        "id": user_id,
        "name": name,
        "email": email,
        "phone": phone
    }

    return user