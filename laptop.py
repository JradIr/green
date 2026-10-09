order = input("What is your order: ")
price = input("What is your price: ")

try:
  if price > 50:
    price = price * 0.2
except TypeError as e:
  print(f"the error: {e}")
  
print(f"Your order is {order}, pay at the counter.")
print(f"${price} dollars is the price for {order}")
