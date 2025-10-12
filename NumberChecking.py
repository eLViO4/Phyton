while True:
    number = int(input("Write number: "))
    if number < 10:
        continue
    if number > 100:
        break
    print(number)
