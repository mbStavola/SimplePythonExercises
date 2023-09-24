word = input("Word to check: ")

reversed = ""
for character in word:
    reversed = character + reversed

if word == reversed:
    print("Is a palindrome")
else:
    print("Not a palindrome")