from category import create_category

categories = []

def add_category(categories):
    category = create_category()
    categories.append(category)
    print("Category added successfully.")

def list_categories():
    return categories

def get_category(category_id):
    return next((c for c in categories if c["id"] == category_id), None)

def remove_category(category_id):
    global categories
    categories = [c for c in categories if c["id"] != category_id]
    return get_category(category_id)   
    
def update_category(category_id):
    category = get_category(category_id)
    if category:
        name = input("Enter new name: ")
        category["name"] = name
        print("Category updated successfully.")
    return category

