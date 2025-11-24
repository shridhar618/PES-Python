from collections import Counter

text = input("Enter a string: ")

char_count = Counter(text)

print("\nCharacters with frequency greater than 2:")
for char, count in char_count.items():
    if count > 2:
        print(f"'{char}' occurs {count} times")
    
