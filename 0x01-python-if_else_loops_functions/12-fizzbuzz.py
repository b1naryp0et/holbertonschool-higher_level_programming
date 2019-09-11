#!/usr/bin/python3
#!/usr/bin/python3
def fizzbuzz():
    x = 1
    while (x <= 100):
        if (x % 15 == 0):
            print("FizzBuzz", end=" ")
        elif (x % 3 == 0):
            print("Fizz", end=" ")
        elif (x % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(x, end=" ")
        x = x + 1
