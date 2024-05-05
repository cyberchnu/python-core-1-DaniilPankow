def mean(number):
  # Type your code
  average = str(number)
  count = len(average)
  summa = sum(int(average) for average in average)
  return summa / count if count > 0 else 0
