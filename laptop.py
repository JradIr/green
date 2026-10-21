import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s, %(message)s")


def order_processing(order_name: str, base_price: float) -> float:
    match order_name:
        case "coke":
            logging.info("You chose coke.")
        case "sprite":
            logging.info("You chose sprite.")
        case "pizza":
            logging.info("You chose pizza.")
        case "burger":
            logging.info("You chose burger.")
        case "fries":
            logging.info("You chose fries.")
        case "rice":
            logging.info("You chose rice.")
        case "adobo":
            logging.info("ansarap ng adobo")
        case _:
            logging.info("The default order.")
    final_price = base_price
    if final_price > 50:
        final_price = final_price - (final_price * 0.2)
    return final_price


def run_counter() -> None:
    x = 0
    while True:
        x += 1
        print(x)
        if x >= 10:
            break


def print_receipt(order: str, price: float) -> None:
    print("----------")
    print("-" * 20)
    print(f"Order: {order}")
    print(f"Total is: ${price:.2f}")
    print("-" * 20)

def interact(action):
    return f"You will {action}"


if __name__ == "__main__":
    order_input = input("What is your order: ").strip().lower()
    try:
        price_input = float(input("What is your price: "))
        calculated_price = order_processing(order_input, price_input)
        print_receipt(order_input, calculated_price)
        run_counter()
    except ValueError as e:
        logging.error(f"Invalid number entered: {e}")
