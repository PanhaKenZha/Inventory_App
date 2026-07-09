from inventory import show_all_cars, add_car, getcarbyid, mark_car_as_sold, delete_car, count_cars
from user_management import show_all_users, add_user, get_user_by_id, users, delete_user ,update_user
from category_management import add_category, list_categories, get_category, remove_category, update_category

while True:
    print("===== Car Inventory System =====")
    print("1. Show all cars")
    print("2. Add new car")
    print("3. Get car by ID")
    print("4. Mark car as sold")
    print("5. Delete car")
    print("6. Total cars")
    print("7. Show all users")
    print("8. Show all categories")
    print("9. Add new user")
    print("10. Get user by ID")
    print("11. Update user")
    print("12. Delete user")
    print("13. Add new category")
    print("14. Update category")
    print("15. Remove category")

    print("16. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_all_cars()
        
    elif choice == "2":
        add_car()

    elif choice == "3":
        car_id = int(input("Enter car ID: "))
        car = getcarbyid(car_id)
        if car:
            print(f"name: {car['name']}")
            print(f"Model: {car['model']}")
            print(f"Year: {car['year']}")
            print(f"Color: {car['color']}")
            print(f"Price: ${car['price']}")
            print(f"Sold: {car['sold']}")
        else:
            print("Car not found.")
            
    elif choice == "4":
        car_id = int(input("Enter car ID: "))
        mark_car_as_sold(car_id)
        
    elif choice == "5":
        car_id = int(input("Enter car ID: "))
        delete_car(car_id)
        
    elif choice == "6":
        print(f"Total cars: {count_cars()}")

    elif choice == "7":
        show_all_users(users)

    elif choice == "8":
        categories = list_categories()
        for category in categories:
            print(f"ID: {category['id']}, Name: {category['name']}")
    

    elif choice == "9":
        add_user(users)
        
    elif choice == "10":
        user_id = int(input("Enter user ID: "))
        user = get_user_by_id(users, user_id)
        if user:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Phone: {user['phone']}")
        else:
            print("User not found.")
            
    elif choice == "11":
        user_id = int(input("Enter user ID: "))
        update_user(users, user_id)

    elif choice == "12":
        user_id = int(input("Enter user ID: "))
        delete_user(users, user_id)

    elif choice == "13":
        add_category(categories)

    elif choice == "14":
        category_id = int(input("Enter category ID: "))
        update_category(category_id)

    elif choice == "14":
        category_id = int(input("Enter category ID: "))
        remove_category(category_id)

    elif choice == "15":    
        print("Goodbye!")
        break
    else:
        print("Invalid option.")