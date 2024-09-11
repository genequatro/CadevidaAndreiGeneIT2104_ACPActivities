input_string = input("Enter a string: ")

vowels = 'aeiouAEIOU'

vowel_list = []

for char in input_string:
  if char in vowels:
    vowel_list.append(char)

print(vowel_list)