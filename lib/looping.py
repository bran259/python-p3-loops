#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -=1
  
    print("Happy New Year!")

    pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]
    # squared = []
    # for num in int_list:
    #     squared.append(num ** 2)
    # return squared    
    # code goes here!
    pass

def fizzbuzz_value(num):
    # for num in range(1, 101):
        if num % 15 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return str(num)
        
def fizzbuzz():
    for num in range(1, 101):
        print(fizzbuzz_value(num))       
        
    # code goes here!
    pass
