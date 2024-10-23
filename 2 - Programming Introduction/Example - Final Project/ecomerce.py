import cart
import products

def display_menu():
    print()
    print("=== E-Commerce Menu ===")
    print("1. Add Product to Cart")
    print("2. Remove Product from Cart")
    print("3. Update Product Quantity")
    print("4. View Cart")
    print("5. Product actions")
    print("6. Exit")

def display_product_actions_submenu():
    print()
    print("=== Product Actions ===")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product")
    print("4. Get Product")
    print("5. List Products")
    print("6. Load Products")
    print("7. Back to Main Menu")

def product_actions(product_dict):
    while True:
        display_product_actions_submenu()
        product_action_choice = input("Enter your choice: ")

        if product_action_choice == "1":
            # Add Product
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            products.add_product(product_id, name, product_dict)

        elif product_action_choice == "2":
            # Remove Product
            product_id = input("Enter product ID: ")
            products.remove_product(product_id, product_dict)

        elif product_action_choice == "3":
            # Update Product
            product_id = input("Enter product ID: ")
            name = input("Enter updated product name: ")
            products.update_product(product_id, name, product_dict)

        elif product_action_choice == "4":
            # Get Product
            product_id = input("Enter product ID: ")
            product = products.get_product(product_id, product_dict)
            if product:
                print("Product found:")
                print(f"ID: {product_id}, Name: {product}")
            else:
                print("Product not found.")

        elif product_action_choice == "5":
            # List Products
            products.list_products(product_dict)

        elif product_action_choice == "6":
            # Load Products
            product_dict = products.load_products()
        
        elif product_action_choice == "7":
            # Back to Main Menu
            break

        else:
            print("Invalid choice. Please try again.")

def run_ecommerce():
    product_dict = products.load_products()
    cart_dict = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Product to Cart
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            product = products.get_product(product_id, product_dict)
            if product:
                cart.add_to_cart(product, quantity, cart_dict)
            else:
                print("Product not found.")

        elif choice == "2":
            # Remove Product from Cart
            product_id = input("Enter product ID: ")
            product = products.get_product(product_id, product_dict)
            if product:
                cart.remove_from_cart(product, cart_dict)
            else:
                print("Product not found.")

        elif choice == "3":
            # Update Product Quantity
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter new quantity: "))
            product = products.get_product(product_id, product_dict)
            if product:
                cart.update_quantity(product, quantity, cart_dict)
            else:
                print("Product not found.")

        elif choice == "4":
            # View Cart
            cart.view_cart(cart_dict)

        elif choice == "5":
            # Product Actions
            product_actions(product_dict)

        elif choice == "6":
            # Exit the program
            print("Thank you for using the e-commerce system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_ecommerce()
