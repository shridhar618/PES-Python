# Reading integers from a text file and handling invalid entries
# try:
#     with open("file1.txt", "r") as f:
#         for line in f:
#             line = line.strip()
#             try:
#                 num = int(line)
#                 print("Valid integer:", num)
#             except ValueError:
#                 print("Value error: cannot convert string to int:", line)
# except FileNotFoundError:
#     print("File not found.")
    
    
#open file and read first 5 lines
# try:
#     with open("data.txt", "r") as f:
#         lines = f.readlines()
#         if not lines:
#             raise Exception("File is empty")
#         for line in lines[:5]:
#             print(line.strip())
# except FileNotFoundError:
#     print("File not found.")
# except Exception as e:
#     print(e)
    
    
# try:
#     with open("data.txt", "r") as file:
#         lines = file.readlines()
#         if len(lines) == 0:
#             print("File is empty!")
#         else:
#             print("First 5 lines:")
#             for line in lines[:5]:
#                 print(line.strip())
# except FileNotFoundError:
#     print("File not found!")
    
    
#write user input to a file
# text = input("Enter text to save in file: ")

# try:
#     with open("output.txt", "w") as file:
#         file.write(text)
#     print("Data written successfully.")
# except PermissionError:
#     print("You don’t have permission to write the file.")


#Convert strings to integers (ignore invalid ones)
# values = ["12", "shr", "56", "9x", "78"]

# for item in values:
#     try:
#         print("Number:", int(item))
#     except ValueError:
#         print("Skipping invalid data:", item)
        
        
#Search a name and display marks

# name = input("Enter student name: ")
# found = False

# try:
#     with open("marks.txt", "r") as file:
#         for line in file:
#             student, marks = line.strip().split()
#             if student == name:
#                 print("Marks:", marks)
#                 found = True
#                 break
#     if not found:
#         print("Name not found.")
# except FileNotFoundError:
#     print("marks.txt not found!")


#Read marks, handle invalid, find total and average
# total = 0
# count = 0

# with open("marks.txt", "r") as file:
#     for line in file:
#         line = line.strip()
#         try:
#             mark = int(line)
#             total += mark
#             count += 1
#         except ValueError:
#             print("Invalid mark:", line)

# if count > 0:
#     print("Total:", total)
#     print("Average:", total / count)
# else:
#     print("No valid marks found.")


#Save valid integers to another file
# with open("numbers.txt", "r") as inp, open("clean_numbers.txt", "w") as out:
#     for line in inp:
#         line = line.strip()
#         try:
#             num = int(line)
#             out.write(str(num) + "\n")
#         except ValueError:
#             print("Invalid number skipped:", line)
#         except FileNotFoundError:
#             print("Input file not found.")
            
            
            
#Read daily expenses, separate valid and invalid data
# with open("expenses.txt", "r") as inp, \
#      open("clean_expenses.txt", "w") as clean, \
#      open("rejected_expenses.txt", "w") as reject:

#     for line in inp:
#         parts = line.strip().split()
#         if len(parts) != 2:
#             reject.write(line)
#             continue

#         category, amount = parts
#         try:
#             amt = float(amount)
#             clean.write(f"{category} {amt}\n")
#         except ValueError:
#             reject.write(line)
#         except FileNotFoundError:
#             print("Expenses file not found.")


#Simple contacts program
while True:
    print("\n1. Search  2. Add  3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name to search: ")
        try:
            with open("contacts.txt", "r") as file:
                found = False
                for line in file:
                    if line.startswith(name):
                        print("Contact:", line.strip())
                        found = True
                if not found:
                    print("Contact not found.")
        except FileNotFoundError:
            print("contacts.txt missing!")

    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        with open("contacts.txt", "a") as file:
            file.write(f"{name} {phone}\n")
        print("Contact added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")


#Custom exception for invalid number
class InvalidNumberError(Exception):
    pass

with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            if not line.isdigit():
                raise InvalidNumberError("Invalid number found!")
            print("Valid:", int(line))
        except InvalidNumberError as e:
            print(e)


#Custom exceptions for marks
class NegativeMarkError(Exception):
    pass

class HighMarkError(Exception):
    pass

with open("marks.txt", "r") as file, open("clean_marks.txt", "w") as clean:
    for line in file:
        line = line.strip()
        try:
            mark = int(line)
            if mark < 0:
                raise NegativeMarkError("Negative mark found!")
            elif mark > 100:
                raise HighMarkError("Mark greater than 100!")
            clean.write(str(mark) + "\n")
        except (NegativeMarkError, HighMarkError, ValueError) as e:
            print("Error:", e)




#Simple calculator with custom exceptions
class OperationError(Exception):
    pass

class InputError(Exception):
    pass

while True:
    op = input("\nEnter operation (+, -, *, /) or 'exit' to stop: ")

    if op == "exit":
        print("Calculator closed.")
        break

    if op not in ["+", "-", "*", "/"]:
        raise OperationError("Invalid operation!")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        raise InputError("Invalid input! Please enter numbers only.")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", a / b)




    

    



        
