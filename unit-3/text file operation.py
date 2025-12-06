#Text file handling
#opening a file
f=open('file1.txt', 'r')

#Attributes of file object
print(type(f))          #prints the type of file object
print(f.name)          #prints the name of the file
print(f.mode)          #prints the mode in which file is opened
print(f.closed)        #prints whether the file is closed or not

#Read the file
str=f.read()
print(str)

#Close the file
f.close()

print(f.closed)        #prints whether the file is closed or not


f=open('file1.txt', 'r')
#Read multiple lines of the file
s=f.readlines()
print(s)
print(type(s))

f.close()


#write a file
with open('file2.txt', 'w') as f1:
    c=f1.write("This is the first line.\n")
    c=f1.write("This is the second line.\n")
    c=f1.write("This is the third line.\n")
    
    print(f"The file is written with {c} number of characters.")
    
    
#write multiple lines to a file
lines=["Line 1: Hello World!\n", "Line 2: Welcome to Python file handling.\n", "Line 3: This is the third line.\n"]

with open('file3.txt', 'w') as f2:
    c=f2.writelines(lines)
    print(f"The file is written with {c} number of characters.")
    
    f2.close()
    
    
#append to a file
with open('file3.txt', 'a') as f3:
    c=f3.write("Line 4: This line is appended.\n")
    print(f"The file is appended with {c} number of characters.")
    
    f3.close()
    
    
#File pointer movement
f=open('File1.txt', 'r')
f.seek(10,0)
'''first parameter is offset and second is position from where offset is calculated. it can be 0-start of file,
1-current position, 2-end of file'''

s=f.readline()
print(s)

print(f.tell()) #prints current position of file pointer



#Assume taht u have a text file and do the following operations:
#1. find out the number of words in the even lines
with open('file1.txt', 'r') as f:
    lines=f.readlines()
    even_line_word_count=0
    for i in range(len(lines)):
        if i%2==1: #even lines (considering first line as line 0)
            words=lines[i].split()
            even_line_word_count+=len(words)
    print(f"Number of words in even lines: {even_line_word_count}")

#2. find out the number of words that contains more than 2 bubbles
with open('file1.txt', 'r') as f:
    content=f.read()
    words=content.split()
    count=0
    for word in words:
        if len(word)>2:
            count+=1
    print(f"Number of words with more than 2 bubbles: {count}")
#3. number of words which starts with capital letter
with open('file1.txt', 'r') as f:
    content=f.read()
    words=content.split()
    count=0
    for word in words:
        if word[0].isupper():
            count+=1
    print(f"Number of words starting with capital letter: {count}")      
    


