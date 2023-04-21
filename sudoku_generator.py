import math, random  # imports every file we need to make the project.
import sys
import pygame


# hopefully this works.

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

    def initialize_board(self):  # Zack: generates 2D list.
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
    sudoku = SudokuGenerator(size, removed)  # develops the board for us.
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.print_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    # sudoku.print_board() # for testing purposes
    return board


class Cell:
    black = (0, 0, 0)  # sets variables for later use.
    width = 630
    board_height = 720
    game_height = 630
    pink = (244, 194, 194)
    num_rows = 9
    num_cols = 9
    cell_length = 70
    purple = (193, 105, 225)
    red = (255, 0, 0)
    grey = (128, 128, 128)

    def __init__(self, value, row, col, screen=pygame.display.set_mode((width, board_height))):  # initialize.
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0

    def set_cell_value(self, value):  # basic setter.
        self.value = value

    def set_sketched_value(self, value):  # basic setter.
        self.sketched_value = value

    def draw(self):  # draws all the values in the cells.
        font = pygame.font.Font(None, 50)
        if self.value != 0:  # if not == 0.
            empty_board = font.render(str(self.value), True, self.black)  # render text of element.
            cell_rect = empty_board.get_rect(center=(
            self.row * self.cell_length + self.cell_length // 2, self.col * self.cell_length + self.cell_length // 2))
            self.screen.blit(empty_board, cell_rect)

        elif self.sketched_value != 0 and self.value == 0:  # if not == 0.
            empty_board = font.render(str(self.sketched_value), True, self.grey)  # render text of element.
            self.screen.blit(empty_board, (self.row * self.cell_length + 5, self.col * self.cell_length + 5))

        if self.selected:  # draws a red box around the selected cell.
            pygame.draw.rect(self.screen, self.red,
                             pygame.Rect((self.row * self.cell_length, self.col * self.cell_length),
                                         (self.cell_length, self.cell_length)), 2)


class Board:
    black = (0, 0, 0)  # sets variables for later use.
    width = 630
    board_height = 720
    game_height = 630
    pink = (251,224,231)
    num_rows = 9
    num_cols = 9
    cell_length = 70
    red = (255, 0, 0)

    pygame.init()  # initialize pygame
    pygame.display.set_caption("Sudoku")  # give the terminal a title.

    def __init__(self, width, height, difficulty, screen=pygame.display.set_mode((width, board_height))):  # initializes.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, self.difficulty)
        # for row in board: #for testing purposes
        #     for col in row:
        #         print(col, end=" ")
        #     print()
        self.cells = []
        self.reset_rect = ""
        self.restart_rect = ""
        self.exit_rect = ""

        for i in range(9):
            row = []
            for j in range(9):
                row.append(Cell(self.board[i][j], j, i, self.screen))
            self.cells.append(row)

    def draw(self):  # draws lines for the game.

        self.screen.fill(self.pink)  # changes window color.

        # horizontal lines
        for i in range(0, 10):
            pygame.draw.line(self.screen, self.black, (0, i * self.cell_length), (self.width, i * self.cell_length))

        # vertical lines
        for i in range(0, 10):
            pygame.draw.line(self.screen, self.black, (i * self.cell_length, 0), (i * self.cell_length, self.width))

        # bolded lines
        pygame.draw.line(self.screen, self.black, (0, 0), (self.width, 0), 4)
        pygame.draw.line(self.screen, self.black, (0, self.cell_length * 3), (self.width, self.cell_length * 3), 4)
        pygame.draw.line(self.screen, self.black, (0, self.cell_length * 6), (self.width, self.cell_length * 6), 4)
        pygame.draw.line(self.screen, self.black, (0, self.cell_length * 9), (self.width, self.cell_length * 9), 4)
        pygame.draw.line(self.screen, self.black, (0, 0), (0, self.width), 4)
        pygame.draw.line(self.screen, self.black, (self.cell_length * 3, 0), (self.cell_length * 3, self.width), 4)
        pygame.draw.line(self.screen, self.black, (self.cell_length * 6, 0), (self.cell_length * 6, self.width), 4)
        pygame.draw.line(self.screen, self.black, (self.cell_length * 9, 0), (self.cell_length * 9, self.width), 4)

        for row in self.cells:
            for cell in row:  # iterates over every item in board.
                cell.draw()

        # creates buttons
        self.button_font = pygame.font.Font(None, 40)  # button font
        self.reset_text = self.button_font.render("Reset", 0, (255, 255, 240))
        self.restart_text = self.button_font.render("Restart", 0, (255, 255, 240))
        self.exit_text = self.button_font.render("Exit", 0, (255, 255, 240))

        # button background color and text
        # creates reset button
        self.reset_surface = pygame.Surface((self.reset_text.get_size()[0] + 20, self.reset_text.get_size()[1] + 20))
        self.reset_surface.fill((181, 229, 200))
        self.reset_surface.blit(self.reset_text, (10, 10))


        # creates restart button
        restart_surface = pygame.Surface((self.restart_text.get_size()[0] + 20, self.restart_text.get_size()[1] + 20))
        restart_surface.fill((176, 224, 230))
        restart_surface.blit(self.restart_text, (10, 10))
        # creates exit button
        exit_surface = pygame.Surface((self.exit_text.get_size()[0] + 20, self.exit_text.get_size()[1] + 20))
        exit_surface.fill((255, 204, 153))
        exit_surface.blit(self.exit_text, (10, 10))
        # button rectangles
        self.reset_rect = self.reset_surface.get_rect(center=(170, 680))
        self.restart_rect = restart_surface.get_rect(center=(320, 680))
        self.exit_rect = exit_surface.get_rect(center=(455, 680))

        # draw the buttons on the screen
        self.screen.blit(self.reset_surface, self.reset_rect)
        self.screen.blit(restart_surface, self.restart_rect)
        self.screen.blit(exit_surface, self.exit_rect)

        # draw the buttons on the screen
        self.screen.blit(self.reset_surface, self.reset_rect)
        self.screen.blit(restart_surface, self.restart_rect)
        self.screen.blit(exit_surface, self.exit_rect)

        # while True:  # keeps the window open until the user exits.
        #     # event handler
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.QUIT
        #             sys.exit()
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if exit_rect.collidepoint(event.pos):
        #                 sys.exit()
        #             if restart_rect.collidepoint(event.pos):
        #                 self.start_screen()
        #                 return
        #             if reset_rect.collidepoint(event.pos):
        #                 self.clear
        #     pygame.display.update()
    def select(self, row, col):
        self.cells[row][col].selected = True

    def check_avaialable(self, board, row, col):
        return board[row][col] == 0

    def click(self, x, y):
        row = y // self.cell_length
        col = x // self.cell_length
        self.select(row, col)
        return row, col

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].value = self.board[i][j]
                self.cells[i][j].sketched_value = self.board[i][j]

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        for row in self.cells:
            for col in row:
                if col.value == 0:
                    return False
        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    def find_empty(self):
        pass

    def is_valid(self, numbers):
        numbers.sort()
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return numbers == nums

    def check_board(self):
        # Check each row
        for row in self.cells:
            cell_val = []
            for cell in row:
                cell_val.append(cell.value)
            if not self.is_valid(cell_val):
                print("row false")
                return False

        # Check each column
        for i in range(9):
            column = [self.cells[j][i].value for j in range(9)]
            if not self.is_valid(column):
                print("col false")
                return False

        # Check each square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.cells[x][y].value for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid(square):
                    return False

        # If we get here, the board is valid
        return True


        '''
        our_list = []
        #
        # for row in completed_board:
        #     for cell in row:
        #         print(cell, end=" ")
        #     print()
        # print()

        for row in self.cells:
            row_list = []
            for cell in row:
                row_list.append(cell.value)
            our_list.append(row_list)

        for row in our_list:
            for cell in row:
                print(cell, end=" ")
            print()
        print()

        # for i in range(9):
        #     for j in range(9):
        #         our_value = our_list[i][j]
        #         print(our_value, end=" ")
        #         completed_value = completed_board[i][j]
        #         print(completed_value)
        #         if our_value != completed_value:
        #             print(False)
        #             return False
        # return True
        '''
    def start_screen(self):

        title_font = pygame.font.Font(None, 150)  # title font
        button_font = pygame.font.Font(None, 40)  # button font

        background_image = pygame.image.load('sudoku_background_image.png')
        #self.screen.fill((220, 220, 220))  # background color
        title_surface = title_font.render("Sudoku", 0, (199, 75, 120))
        title_rectangle = title_surface.get_rect(center=(305, 230))
        self.screen.blit(background_image, (0,0))
        self.screen.blit(title_surface, title_rectangle)  # render title

        easy_text = button_font.render("Easy", 0, (255, 255, 240))
        medium_text = button_font.render("Medium", 0, (255, 255, 240))
        hard_text = button_font.render("Hard", 0, (255, 255, 240))
        quit_text = button_font.render("Quit", 0, (255, 255, 240))

        # button background color and text
        easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
        easy_surface.fill((255, 188, 217))
        easy_surface.blit(easy_text, (10, 10))

        medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
        medium_surface.fill((255, 188, 217))
        medium_surface.blit(medium_text, (10, 10))

        hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
        hard_surface.fill((255, 188, 217))
        hard_surface.blit(hard_text, (10, 10))

        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
        quit_surface.fill((255, 188, 217))
        quit_surface.blit(quit_text, (10, 10))

        # button rectangle
        self.easy_rect = easy_surface.get_rect(center=(175, 330))
        self.medium_rect = medium_surface.get_rect(center=(300, 330))
        self.hard_rect = hard_surface.get_rect(center=(425, 330))
        self.quit_rect = quit_surface.get_rect(center=(300, 400))

        # draw the buttons
        self.screen.blit(easy_surface, self.easy_rect)
        self.screen.blit(medium_surface, self.medium_rect)
        self.screen.blit(hard_surface, self.hard_rect)
        self.screen.blit(quit_surface, self.quit_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board = Board(630, 630, self.difficulty)
                    if self.easy_rect.collidepoint(event.pos):
                        self.difficulty = 30
                        print(self.difficulty)
                        return
                    elif self.medium_rect.collidepoint(event.pos):
                        self.difficulty = 40
                        print(self.difficulty)
                        return
                    elif self.hard_rect.collidepoint(event.pos):
                        self.difficulty = 50
                        print(self.difficulty)
                        return
                    elif self.quit_rect.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()

    def draw_game_over_screen(self):
        self.screen.fill((220, 220, 220))
        if self.check_board():
            end_text = "You Win"
        else:
            end_text = "You lose :("
        game_over_font = pygame.font.Font(None, 100)
        button_font = pygame.font.Font(None, 40)  # button font

        end_surf = game_over_font.render(end_text, 0, (199, 75, 120))
        end_rect = end_surf.get_rect(center=(305, 230))
        self.screen.blit(end_surf, end_rect)

        restart_text = button_font.render("Restart", 0, (255, 255, 240))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill((255, 188, 217))
        restart_surface.blit(restart_text, (10, 10))
        restart_rect = restart_surface.get_rect(center=(300, 330))
        self.screen.blit(restart_surface, restart_rect)

        while True:  # keeps the window open until the user exits.
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        self.start_screen()

                        return
            pygame.display.update()
