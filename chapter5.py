largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            number = float(num)
        except:
            print("Invalid input")
            continue
        if smallest is None:
            smallest = number
        if largest is None:
            largest = number
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number

def done(max, min):
    print("Maximum is", int(largest))
    print("Minimum is", int(largest))

done(largest, smallest)