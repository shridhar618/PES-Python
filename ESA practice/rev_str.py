def reverse_string(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev

text = input("Enter a string: ")
result = reverse_string(text)
print("Reversed string:", result)