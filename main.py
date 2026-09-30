from pdb import main


sentence = input("Provide a random sentence: ")

print(sentence)

while True:
    user_input = input("Type 'exit' to quit or press Enter to continue: ")
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    else:
        print(sentence)

if __name__ == "__main__":
    main()