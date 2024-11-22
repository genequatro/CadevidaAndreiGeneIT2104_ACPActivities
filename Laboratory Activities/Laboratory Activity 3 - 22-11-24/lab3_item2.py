try:

  num = int(input("Enter a number: "))

  divisorSum = 0

  for divisor in range(1, num):
    if num % divisor == 0:
      divisorSum += divisor
    
  if divisorSum == num:
    print(f"{num} is a perfect number.")
  else: 
    print(f"{num} is not a perfect number.")

except ValueError:
  print("Please enter a valid integer.")