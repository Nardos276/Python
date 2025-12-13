try:
    with open("message.txt", "w") as file:
        text = input("Enter text: ")
        file.write(text + "\n")
    with open("message.txt", "r") as file:
        for line in file:
            print(line.strip().upper())

except FileNotFoundError:
    print("Error: The file 'message.txt' was not found.")
