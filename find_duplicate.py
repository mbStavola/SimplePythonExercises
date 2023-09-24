words = input("Enter list: ").split()

found_duplicate = False
duplicate = None
for i, word in enumerate(words):
    for other_word in words[i + 1:]:
        if word == other_word:
            found_duplicate = True
            duplicate = word

if found_duplicate:
    print("There was a duplicate", duplicate)
else:
    print("There was no duplicate")