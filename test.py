output = ""

for i in range(1, 100):
    ++i
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output)
