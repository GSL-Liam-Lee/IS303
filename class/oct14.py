has_error = True

while has_error:
    try:
        number = int(input("Enter a number: "))
        print(number)
        has_error = False
    except:
        print("Invalid number. Please try a gain.")
        continue
    else:
        has_error = False
    finally:
        print("Got through it!")