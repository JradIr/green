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
logging.info("starting session")

num=0
while True:
  if num < 5:
    num += 1
    print(num)
  else:
    break

def get_initial(initial: str):
  return f"Initial: {initial} "

print(get_initial("Argayosa"))
print(get_initial("De La Rosa"))

#logging for end
logging.info("ending...")

if __name__ == "__main__":
  logging.info("start")
