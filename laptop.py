import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s, %(message)s")

order = input("What is your order: ").strip().lower()
price = float(input("What is your price: "))

#Checking the specific order
def process_order(order_name: str, base_price: float) -> float:
  final_price = base_price
  if final_price < 100:
    final_price = final_price - (final_price * 0.2)
  return final_price
  

if __name__ == "__main__":
  try:
    match order:
      case "coke":
        print("you chose coke")
      case "sprite":
        print("You chose sprite.")
      case _:
        print("The default order.")
    if price > 50:
      price = price * 0.2
  except TypeError as e:
    print(f"the error: {e}")

#Printing the result
print(f"Your order is {order}, pay at the counter.")
print(f"${price:.2f} dollars is the price for {order}")

logging.info("this is a log.")

x = 0
while True:
  x += 1
  print(x)
  if x >= 10:
    break
