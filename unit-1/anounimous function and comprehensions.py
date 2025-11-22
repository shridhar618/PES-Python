def is_even(n):
    if n%2==0:
        return n
    
l=list(filter(is_even, range(20)))
print(l)


def is_even(n):
    if n%2==0:
        return n
    
l=list(filter(lambda x: x%2==0, range(20)))
print(l)

#--------------------reduce function---------------------
from functools import reduce
l=reduce(lambda a,b:a+b, [1,2,3,4,5,6,7,8,9,10])
print(l)

#---------------------zip function------------------------
print(list(zip([1,2,3,4,5],['a','b','c','d','e'])))
print(list(zip([1,2,3,4,5,6,7,8,9],['a','b','c','d','e'])))

# -----------------------max()---------------------------
print(max('a','A','aa','AA'))
print((max([1,2,3,4],[1,2,3,4],[1,2,4,5],[1,2,6])))

#------------------------min()---------------------------
print(min('a','A','aa','AA'))
print((min([1,2,3,4],[1,2,3,4],[1,2,4,5],[1,2,6])))



#---------------------list comprehension-------------------
l=[a for a in range(20)]
print(l)

l=[a*2 for a in range(20) if a%2==0]
print(l)


#-------------------conditional comprehension--------------------
l=[a*2 if a%2==0 else a+3 for a in range(20)]
print(l)

#---------------------nested comprehension----------------------
l=[a*b for a in range(1,5) for b in range(1,3)]
print(l)

#nested comprehension with condition
l=[a*b for a in range(1,10) for b in range(1,5) if (a+b)%2==0 ]
print(l)

#set comprehension
s={a for a in range(20)}
print(s)

#conditional set comprehension
s={a for a in range(20) if a%2==0}
print(s)

#nested set comprehension
s={a+b for a in range(1,5) for b in range(1,5)}
print(s)

#nested conditional comprehension
s={(a,b) for a in [1,2,3,4] for b in [4,5] if (a+b)%2==0}
print(s)

#dictionary comprehension
d={a:a*a for a in range(1,6)}
print(d)

#conditional dictionary comprehension
d={a:a*a for a in range(1,11) if a%2==0}
print(d)

#nested dictionary comprehension
d={a:{b:b*b for b in range(1,4)} for a in range(1,4)}
print(d)

#nested conditional dictionary comprehension
d={a:{b:b*b for b in range(1,6) if b%2==0} for a in range(1,6) if a%2!=0}
print(d)



#create a list of all upper case words from a given list.
words = ['hello', 'world', 'python', 'programming']
upper_case_words = [word.upper() for word in words]
print(upper_case_words)

#given a list of words, create a list with words that start with a vowel.
words = ['apple', 'banana', 'orange', 'grape', 'umbrella', 'kiwi']
vowel_words = [word for word in words if word[0].lower() in 'aeiou']
print(vowel_words)              

#given a list of string, create a new string that contains the string and its length
words = ['apple', 'banana', 'orange']
lengthened_words = [f"{word} - {len(word)}" for word in words]
print(lengthened_words)

#extract all lower case letters from a given string into a set.
input_string = "Hello World! Welcome to Python Programming."
lower_case_letters = {char for char in input_string if char.islower()}
print(lower_case_letters)

#given a sentence, create a set of all words that have more than four characters.
sentence = "This is a sample sentence for testing set comprehension."
long_words = {word for word in sentence.split() if len(word) > 4}
print(long_words)

#create a set of firstn letter of each word from a given paragraph.
paragraph = "Python is a powerful programming language."
first_letters = {word[0] for word in paragraph.split()} 
print(first_letters)


#given a string, create a dictionary that maps each character to its frequency in the string.
input_string = "hello world"
char_frequency = {char: input_string.count(char) for char in set(input_string)}
print(char_frequency)

#from a dictionary of student scores, create a new dictionary with students who scored more than 70 marks.
student_scores = {'Alice': 85, 'Bob': 65, 'Charlie': 90, 'David': 55}
high_scorers = {student: score for student, score in student_scores.items() if score > 70}
print(high_scorers)

#given a list of student records, create a new dict, that has students and total marks.
student_records = [
    {'name': 'Alice', 'marks': 85},
    {'name': 'Bob', 'marks': 65},
    {'name': 'Charlie', 'marks': 90},
    {'name': 'David', 'marks': 55}
]
total_marks = sum(student['marks'] for student in student_records)
average_marks = total_marks / len(student_records)
print(average_marks)



