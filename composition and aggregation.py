# Chess Game is played with a board and a pieces that are pawns, rooks, bishop, king, queen...

# Component class

#-----------------------------------------------Composition----------------------------------------------------

class Piece:
    def _init_(self, color):
        self.color = color

# Pawn is a type of piece
class Pawn(Piece):
    def __init__(self, color):
        super()._init_(color)
        self.type = 'Pawn'

# Board has eight Pawns of each color. (has is used so composition)
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] 
                     for _ in range(8)]
        
    def initialize_board(self):
        '''Creating pawns to be placed on second and last but 
           second row'''
        self.grid[1] = [Pawn('White') for _ in range(8)]
        self.grid[6] = [Pawn('Black') for _ in range(8)]

    def print_board(self):
        for row in self.grid:
            print([piece.type if piece else '----' for piece in row])

# Composite Class - Game
class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_board()

    def play(self):
        print('Initial Board Arrangement')
        self.board.print_board()

# Begin the game
Game().play()


#-----------------------------------------aggregation example-------------------------------------------------
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        
    def teach(self):
        print(f'{self.name} is teaching {self.subject}')
        
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []  # list to hold teacher objects
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def conduct_classes(self):
        print(f'Classes at {self.name} are being conducted:')
        for teacher in self.teachers:
            teacher.teach()
            
    def show_teachers(self):
        print(f'Teachers at {self.name}:')
        for teacher in self.teachers:
            print(f'- {teacher.name}, Subject: {teacher.subject}')
            
            
s1=School('ABC school')
s2=School('PQR High school')
t1=Teacher('Mr.XYZ', 'maths')
t2=Teacher('Mr.ABC', 'python')
t3=Teacher('Ms.LMN', 'CP')

s1.show_teachers()
s2.show_teachers()

s1.add_teacher(t1)
s1.add_teacher(t2)
s2.add_teacher(t3)

s1.show_teachers()
s2.show_teachers()




#a user creates folders. folders has files. files have paragraphs. paragraphs have words. each word is madseup of characters.
# -----------------------------
# USER → FOLDER (AGGREGATION)
# -----------------------------

class User:
    def __init__(self, name):
        self.name = name
        self.folders = []   # user aggregates folders

    def add_folder(self, folder):
        self.folders.append(folder)

    def __repr__(self):
        return f"User({self.name})"


# -----------------------------
# FOLDER → FILE (COMPOSITION)
# -----------------------------

class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []  # folder OWNS files (composition)

    def create_file(self, filename):
        new_file = File(filename)
        self.files.append(new_file)
        return new_file

    def __repr__(self):
        return f"Folder({self.name})"


# -----------------------------
# FILE → PARAGRAPH (COMPOSITION)
# -----------------------------

class File:
    def __init__(self, name):
        self.name = name
        self.paragraphs = []

    def add_paragraph(self, text):
        p = Paragraph(text)
        self.paragraphs.append(p)
        return p

    def __repr__(self):
        return f"File({self.name})"


# -----------------------------
# PARAGRAPH → WORD (COMPOSITION)
# -----------------------------

class Paragraph:
    def __init__(self, text):
        self.words = [Word(w) for w in text.split()]

    def __repr__(self):
        return "Paragraph(" + " ".join([w.text for w in self.words]) + ")"


# -----------------------------
# WORD → CHARACTER (COMPOSITION)
# -----------------------------

class Word:
    def __init__(self, text):
        self.text = text
        self.characters = list(text)  # characters are part of the word

    def __repr__(self):
        return f"Word({self.text})"


# -----------------------------
# DEMO
# -----------------------------
if __name__ == "__main__":
    user = User("Shridhar")

    # Aggregation: User has folders
    folder1 = Folder("Projects")
    user.add_folder(folder1)

    # Composition: Folder owns files
    file1 = folder1.create_file("notes.txt")

    # Composition: File owns paragraphs
    p1 = file1.add_paragraph("This is the first paragraph")
    p2 = file1.add_paragraph("Composition represents strong ownership")

    print("\nUser:", user)
    print("Folders:", user.folders)
    print("Files in Folder:", folder1.files)
    print("Paragraphs in File:", file1.paragraphs)

    # Showing words and characters
    print("Words in first paragraph:", [w.text for w in p1.words])
    print("Characters of first word:", p1.words[0].characters)



# A library has books. users use library. a smartphone has a camera and display. user uses a smartphone.
# ------------------------------------------------
# USER → LIBRARY (AGGREGATION)
# USER → SMARTPHONE (AGGREGATION)
# ------------------------------------------------

class User:
    def __init__(self, name):
        self.name = name
        self.library = None      # user uses a library (aggregation)
        self.smartphone = None   # user uses smartphone (aggregation)

    def use_library(self, library):
        self.library = library

    def use_smartphone(self, phone):
        self.smartphone = phone

    def __repr__(self):
        return f"User({self.name})"


# ------------------------------------------------
# LIBRARY → BOOK (COMPOSITION)
# ------------------------------------------------

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # library OWNS books (composition)

    def add_book(self, title):
        new_book = Book(title)
        self.books.append(new_book)
        return new_book

    def __repr__(self):
        return f"Library({self.name})"


class Book:
    def __init__(self, title):
        self.title = title   # book exists only as part of library (composition)

    def __repr__(self):
        return f"Book({self.title})"


# ------------------------------------------------
# SMARTPHONE → CAMERA + DISPLAY (COMPOSITION)
# ------------------------------------------------

class Smartphone:
    def __init__(self, model):
        self.model = model
        self.camera = Camera()     # composition
        self.display = Display()   # composition

    def __repr__(self):
        return f"Smartphone({self.model})"


class Camera:
    def __init__(self):
        self.megapixels = 48

    def __repr__(self):
        return "Camera(48MP)"


class Display:
    def __init__(self):
        self.size_inches = 6.5

    def __repr__(self):
        return "Display(6.5 inch)"


# ------------------------------------------------
# DEMO
# ------------------------------------------------

if __name__ == "__main__":
    # Create a user
    user = User("Shridhar")

    # Aggregation: User uses Library
    lib = Library("City Library")
    user.use_library(lib)

    # Composition: Library owns books
    lib.add_book("Data Structures in Python")
    lib.add_book("Operating System Concepts")

    # Aggregation: User uses Smartphone
    phone = Smartphone("Samsung S24")
    user.use_smartphone(phone)

    print("\nUser:", user)
    print("Library used by user:", user.library)
    print("Books in library:", user.library.books)

    print("\nSmartphone used by user:", user.smartphone)
    print("Camera:", user.smartphone.camera)
    print("Display:", user.smartphone.display)







