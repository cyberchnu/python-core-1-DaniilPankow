def fizz_buzz(param):
  #Type your code here
    if param//3 and param//5:
      return "FizzBuzz"
    elif param//3:
      return "Fizz"
    elif param//5:
      return "Buzz"
    else:
      return str(param)
print(fizz_buzz(2))

