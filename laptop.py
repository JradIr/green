order = input("What is your order: ").strip().lower()
price = float(input("What is your price: "))

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
  
print(f"Your order is {order}, pay at the counter.")
print(f"${price:.2f} dollars is the price for {order}")
