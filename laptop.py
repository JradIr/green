import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s, %(message)s")

def process_order(order_name: str, base_price: float) -> float:
    """Handles order messaging and calculates discounts."""
    match order_name:
        case "coke":
            logging.info("You chose coke.")
        case "sprite":
            logging.info("You chose sprite.")
        case _:
            logging.info("The default order.")
            
    final_price = base_price
    
    if final_price > 50:
        final_price = final_price - (final_price * 0.2)
        
    return final_price

def run_counter() -> None:
    """Runs a simple 1 to 10 counter."""
    x = 0
    while True:
        x += 1
        print(x)
        if x >= 10:
            break

if __name__ == "__main__":
    order_input = input("What is your order: ").strip().lower()
    
    try:
        price_input = float(input("What is your price: "))
        calculated_price = process_order(order_input, price_input)
        
        print(f"Your order is {order_input}, pay at the counter.")
        print(f"${calculated_price:.2f} is the final price for {order_input}.")
        
        run_counter()
        
    except ValueError as e:
        logging.error(f"Invalid number entered for price: {e}")
