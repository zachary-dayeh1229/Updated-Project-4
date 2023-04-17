import math, random  # imports every file we need to make the project.
import sys
import pygame


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):  # Zack: initialize - default is 9 as sudoku is always 9x9
        self.row_length = int(row_length)
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(self.row_length))  # Zack: per instructions
        self.col_length = 9
        self.board = []
        for row in range(9):  # initializes the board
            row = []
            for column in range(9):  # similar to connect 4.
                row.append(0)
            self.board.append(row)


    def initialize_board(self): # Zack: generates 2D list.
      self.board = []  
      for row in range(9):
        row = []
        for column in range(9):  # similar to connect 4.
          row.append(0)
        self.board.append(row)
      return self.board


    def get_board(self):  # Zack - basic get function
        return self.board

    def print_board(self):  # Sanjana - prints the board properly
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    '''
      Determines if num is contained in the specified row (horizontal) of the board
      If num is already in the specified row, return False. Otherwise, return True
  
      Parameters:
      row is the index of the row we are checking
      num is the value we are looking for in the row
  
      Return: boolean
      '''

    def valid_in_row(self, row, num):
        for i in range(self.col_length):
            if self.board[row][i] == num:  # iterates over every row value to check num.
                return False
        return True

    '''
      Determines if num is contained in the specified column (vertical) of the board
      If num is already in the specified col, return False. Otherwise, return True
  
      Parameters:
      col is the index of the column we are checking
      num is the value we are looking for in the column
  
      Return: boolean
      '''

    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][col] == int(num):  # iterates over every col to check num.
                return False
        return True

    '''
      Determines if num is contained in the 3x3 box specified on the board
      If num is in the specified box starting at (row_start, col_start), return False.
      Otherwise, return True
  
      Parameters:
      row_start and col_start are the starting indices of the box to check
      i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
      num is the value we are looking for in the box
  
      Return: boolean
      '''

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):  # iterates over box to check for num.
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    '''
      Determines if it is valid to enter num at (row, col) in the board
      This is done by checking that num is unused in the appropriate, row, column, and box
  
      Parameters:
      row and col are the row index and col index of the cell to check in the board
      num is the value to test if it is safe to enter in this cell
  
      Return: boolean
      '''

    def is_valid(self, row, col, num):
        '''
        row_start = 0
        col_start = 0
        for i in range(1, 4):
          for j in range(1, 4):
            if row < i*3:
              if col < j*3:
                if self.valid_in_box(row_start, col_start, num) is True:
                  break
                row_start += 3
                col_start  += 3
        '''
        # initialise row_start and col_start
        row_start = 0
        col_start = 0
        if row < 3 and col < 3:  # defines box 1 row_start and col_start
            row_start = 0
            col_start = 0
        elif row < 3 and 3 <= col < 6:  # defines box 2
            row_start = 0
            col_start = 3
        elif row < 3 and 6 <= col < 9:  # box 3
            row_start = 0
            col_start = 6
        elif 3 <= row < 6 and col < 3:  # box 4
            row_start = 3
            col_start = 0
        elif 3 <= row < 6 and 3 <= col < 6:  # box 5
            row_start = 3
            col_start = 3
        elif 3 <= row < 6 and 6 <= col < 9:  # box 6
            row_start = 3
            col_start = 6
        elif 6 <= row < 9 and col < 3:  # box 7
            row_start = 6
            col_start = 0
        elif 6 <= row < 9 and 3 <= col < 6:  # box 8
            row_start = 6
            col_start = 3
        elif 6 <= row < 9 and 6 <= col < 9:  # box 9
            row_start = 6
            col_start = 6

            # run through each of the 3 functions, check if true, else false
        if self.valid_in_box(row_start, col_start, num):
            if self.valid_in_row(row, num):
                if self.valid_in_col(col, num):
                    return True
        return False

    '''
      Fills the specified 3x3 box with values
      For each position, generates a random digit which has not yet been used in the box
  
      Parameters:
      row_start and col_start are the starting indices of the box to check
      i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
  
      Return: None
  
    See below
      '''

    def fill_box(self, row_start, col_start):  # chloe - fills a 3x3 box of 9 random numbers
        random_list = []
        random_list = list(range(1, 10))  # creates a list of 9 elements.
        random.shuffle(random_list)  # randomizes order.
        random_list_index = 0
        for i in range(3):
            for j in range(3):  # iterates over every row and column in 3x3 box.
                self.board[row_start + i][col_start + j] = random_list[random_list_index]  # fills in random list value.
                random_list_index += 1

    '''
      Fills the three boxes along the main diagonal of the board
      These are the boxes which start at (0,0), (3,3), and (6,6)
  
      Parameters: None
      Return: None
    See below
      '''

    def fill_diagonal(self):  # repeats fill box 3 times.
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
      DO NOT CHANGE
      Provided for students
      Fills the remaining cells of the board
      Should be called after the diagonal boxes have been filled
  
      Parameters:
      row, col specify the coordinates of the first empty (0) cell
  
      Return:
      boolean (whether or not we could solve the board)
      '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
      DO NOT CHANGE
      Provided for students
      Constructs a solution by calling fill_diagonal and fill_remaining
  
      Parameters: None
      Return: None
      '''

    def fill_values(self):  # fills the whole box.
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
      Removes the appropriate number of cells from the board
      This is done by setting some values to 0
      Should be called after the entire solution has been constructed
      i.e. after fill_values has been called
  
      NOTE: Be careful not to 'remove' the same cell multiple times
      i.e. if a cell is already 0, it cannot be removed again
  
      Parameters: None
      Return: None
      '''

    def remove_cells(self):
        empty_boxes = 0
        while empty_boxes < self.removed_cells:
            row = random.randint(0, 8)  # inclusive parameters.
            col = random.randint(0, 8)
            if self.board[row][col] == 0:
                continue
            else:
                self.board[row][col] = 0
                empty_boxes += 1


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    sudoku.print_board() # for testing purposes
    return board


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        font = pygame.font.Font(None, 300)
        number_one = font.render('1', 0, (193, 105, 225))
        number_two = font.render('2', 0, (193, 105, 225))
        number_three = font.render('3', 0, (193, 105, 225))
        number_four = font.render('4', 0, (193, 105, 225))
        number_five = font.render('5', 0, (193, 105, 225))
        number_six = font.render('6', 0, (193, 105, 225))
        number_seven = font.render('7', 0, (193, 105, 225))
        number_eight = font.render('8', 0, (193, 105, 225))
        number_nine = font.render('9', 0, (193, 105, 225))
        number_list = [number_one, number_two, number_three, number_four, number_five, number_six, number_seven,
                       number_eight, number_nine]
        for i in number_list:
            if self.selected == False:
                number_rect = i.get_rect(
                    center=(self.width // 2 + self.width * self.col, self.height // 2 + self.height * self.row))
                screen.blit(number_rect, i)
            if self.selected == True:
                continue


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, row, col):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

    
def start_screen(screen):
  title_font = pygame.font.Font(None, 100) # title font
  button_font = pygame.font.Font(None, 70) # button font
  
  screen.fill(197, 161, 196) # background color
  title_surface = title_font.render("Sudoku", 0, (0,0,0))
  screen.blit(title_surface) # render title
  start_text = button_font.render("Start", 0, (255, 255, 240))
  quit_text = button_font.render("Quit", 0, (255, 255, 240))
                                  
  # button background color and text
  start_surface = pygame.Surface((start_text.get_size()[0] + 20,  start_text.get_size()[1] +20))
  start_surface.fill(0, 0, 0)
  start_surface.blit(start_text, (10, 10))

  quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] +20))
  quit_surface.fill(0, 0, 0)
  quit_surface.blit(quit_text, (10, 10))


  # button rectangle 
  start_rect = start_surface.get_rect(center = (35, 70))
  quit_rect = quit_surface.get_rect(center=(35,70))

  # draw the buttons 
  screen.blit(start_surface, start_rect)
  screen.blit(quit_surface, quit_rect)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT():
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if start_rect.collidepoint(event.pos):
          return 
        elif quit_rect.collidepoint(event.pos):
          sys.exit()
    pygame.display.update()

  def game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(197, 161, 196)
        

generate_sudoku(9, 40)
