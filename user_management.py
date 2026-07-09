from user import create_user

users = []

def add_user(users):
    user = create_user()
    users.append(user)
    print("User added successfully.")

def show_all_users(users):
    if len(users) == 0:
        print("No users available.")
        return

    for index, user in enumerate(users, start=1):
        print(f"User {index}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone']}")
        print()

def get_user_by_id(users, user_id):
    if 0 < user_id <= len(users):
        return users[user_id - 1]
    else:
        return None

def delete_user(users, user_id):
    user = get_user_by_id(users, user_id)
    if user:
        users.remove(user)
        print("User deleted successfully.")
    else:
        print("User not found.")

def update_user(users, user_id):
    user = get_user_by_id(users, user_id)
    if user:
        user['name'] = input(f"Enter new name ({user['name']}): ") or user['name']
        user['email'] = input(f"Enter new email ({user['email']}): ") or user['email']
        user['phone'] = input(f"Enter new phone ({user['phone']}): ") or user['phone']
        print("User updated successfully.")
    else:
        print("User not found.")

