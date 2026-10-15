import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s, %(message)s")

def myfunction(message: str):
  if message == "God":
    print(" is good!")
  else:
    print("null")
  return {message}
result = myfunction("God")
print(result)
logging.info("ending session")
