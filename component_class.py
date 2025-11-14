# Chess Game is played with a board and a pieces that are pawns, rooks, bishop, king, queen...

# Component class

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


#aggregation example
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
t1=Teacher('Mr.ABC', 'python')
t1=Teacher('Ms.LMN', 'CP')

s1.show_teachers()
s2.show_teachers()

