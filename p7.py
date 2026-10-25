#Program to check if a character is a vowel or consonent
char = input("Enter the character")
char = char.lower()
if char in ('a','e','i','o','u'):
    print(char, "is a vowel")
else:
    print(char, "is a consonent")
    