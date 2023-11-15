def calculate_order_price(is_tuesday, num_pizzas, is_delivery, ordered_via_app):
    PIZZA_PRICE = 12.0
    DELIVERY_COST = 2.5
    DISCOUNT_PERCENTAGE_TUESDAY = 50
    DISCOUNT_PERCENTAGE_APP = 25
    FREE_DELIVERY_THRESHOLD = 5

    # Calculate pizza cost
    total_pizza_cost = num_pizzas * PIZZA_PRICE

    # Apply Tuesday discount
    if is_tuesday:
        total_pizza_cost *= (1 - DISCOUNT_PERCENTAGE_TUESDAY / 100)

    # Calculate delivery cost
    total_delivery_cost = 0.0
    if is_delivery:
        if num_pizzas >= FREE_DELIVERY_THRESHOLD:
            total_delivery_cost = 0.0
        else:
            total_delivery_cost = DELIVERY_COST

    # Calculate total cost before app discount
    total_cost_before_app_discount = total_pizza_cost + total_delivery_cost

    # Apply app discount
    if ordered_via_app:
        total_cost_before_app_discount *= (1 - DISCOUNT_PERCENTAGE_APP / 100)

    # Calculate and return the final total price
    return round(total_cost_before_app_discount, 2)


def main():
    # Get user input
    is_tuesday = input("Is it Tuesday? (yes/no): ").lower() == 'yes'
    num_pizzas = int(input("Enter the number of pizzas in the order: "))
    is_delivery = input("Is it a delivery? (yes/no): ").lower() == 'yes'
    ordered_via_app = input("Did the customer order via the BPP App? (yes/no): ").lower() == 'yes'

    # Calculate and display the total price
    total_price = calculate_order_price(is_tuesday, num_pizzas, is_delivery, ordered_via_app)
    print(f"Total Price: £{total_price}")


if __name__ == "__main__":
    main()
