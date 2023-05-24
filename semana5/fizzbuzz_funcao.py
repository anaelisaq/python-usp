def fizzbuzz(n):
    if n % 5 == 0  and n % 3 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)
fizzbuzz(4)