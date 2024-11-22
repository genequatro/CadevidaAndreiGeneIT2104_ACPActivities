def roman_to_integer(inputRoman):

  roman_values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C": 100, "D" : 500, "M" : 1000}

  inputRoman = inputRoman.upper()

  total = 0

  for i in range(len(inputRoman)): #iterates through the index of the string input
    if i + 1 < len(inputRoman) and roman_values[inputRoman[i]] < roman_values[inputRoman[i + 1]]: #checks if there is a character right after then checks if the first character is smaller than the next character beside.
      total -= roman_values[inputRoman[i]] #subtract to the total if the current char is smaller than the next char
    else: 
      total += roman_values[inputRoman[i]]# adds to the total if the current char is larger than the next char

  return total

inputRoman = input("Enter a Roman numeral: ")

result = roman_to_integer(inputRoman)

print(f"The integer value of '{inputRoman.upper()}' is: {result}")