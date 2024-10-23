def add_product(product_id, name, products_dict):
    # Add product to inventory
    if product_id not in products_dict.keys():
        products_dict[product_id] = name
        save_product(product_id, name)
        print(f"Product added successfully. Product details: ID {product_id} - Name {name}")
    else:
        print("Product duplicated.")

def remove_product(product_id, products_dict):
    # Remove product from inventory
    if product_id in products_dict.keys():
        product = products_dict.pop(product_id)
        write_products(products_dict)
        print(f"Product removed successfully. Product details: ID {product_id} - Name {product}")
    else:
        print("Product not found.")

def update_product(product_id, name, products_dict):
    if product_id in products_dict.keys():
        products_dict[product_id] = name
        write_products(products_dict)
        print(f"Product updated successfully. Product details: ID {product_id} - Name {name}")
    else:
        print("Product not found.")

def get_product(product_id, products_dict):
    if product_id in products_dict.keys():
        return products_dict[product_id]
    else:
        return None

def list_products(products_dict):
    print("=== Product items ===")
    print("ID\t\t|\tName")
    for key, value in products_dict.items():
        print(f"{key}\t\t|\t{value}")
        
def load_products():
    product_dict = {}

    with open('products.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                id, name = line.split('|')
                product_dict[id] = name

    print("Products loaded.")
    return product_dict

def save_product(product_id, product_name):
    with open('products.txt', 'a') as file:
        file.write(f"\n{product_id}|{product_name}")
        
def write_products(dictionary):
    with open('products.txt', 'w') as file:
        for product_id, product_name in dictionary.items():
            file.write(f"{product_id}|{product_name}\n")