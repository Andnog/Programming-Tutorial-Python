def add_to_cart(product, quantity, cart_dict):
    # Add product to the shopping cart
    if product not in cart_dict.keys():
        cart_dict[product] = quantity
        print(f"Product added to cart successfully. Product details: Name {product} - Quantity {quantity}")
    else:
        cart_dict[product] += quantity
        print(f"Product updated to cart successfully. Product details: Name {product} - Quantity {quantity}")


def remove_from_cart(product, cart_dict):
    # Remove product from the shopping cart
    if product in cart_dict.keys():
        product_details = cart_dict.pop(product)
        print(f"Product removed from the cart successfully. Product details: Name {product} - Quantity {product_details}")
    else:
        print("Product not found in the cart.")


def update_quantity(product, quantity, cart_dict):
    # Update product quantity in the cart
    if product in cart_dict.keys():
        cart_dict[product] = quantity
        print(f"Product updated to cart successfully. Product details: Name {product} - Quantity {quantity}")
    else:
        print("Product not found in the cart.")


def get_cart_total(cart_dict):
    # Calculate the total cost of items in the cart
    total = 0
    for key, value in cart_dict.items():
        total += value
    return total


def view_cart(cart_dict):
    # Display the contents of the shopping cart
    print("=== Cart items ===")
    print("Product\t\t|\tQuantity")
    for key, value in cart_dict.items():
        print(f"{key}\t\t|\t{value}")
