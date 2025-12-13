with open("numbers.txt", "w") as file:
    n = int(input("How many numbers do you want to enter? "))
    for i in range(n):
        value = input(f"Enter value {i+1}: ")
        file.write(value + "\n")
sum = 0
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            num = int(line)
            sum += num
        except ValueError:
            continue

print("Sum =", sum)
