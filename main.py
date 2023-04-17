import pygame
import sudoku_generator
import sys

pygame.init()  # initialize pygame
pygame.display.set_caption("Sudoku")  # give the terminal a title.

black = (0, 0, 0)  # sets variables for later use.
width = 630
height = 720
pink = (244, 194, 194)
num_rows = 9
num_cols = 9
cell_length = 70

screen = pygame.display.set_mode((width, height))  # establishes window size.
screen.fill(pink)  # changes window color.

def draw():

    # horizontal lines
    for i in range(0, 10):
        pygame.draw.line(screen, black, (0, i * cell_length), (width, i * cell_length))

    # vertical lines
    for i in range(0, 10):
        pygame.draw.line(screen, black, (i * cell_length, 0), (i * cell_length, width))

    # bolded lines
    pygame.draw.line(screen, black, (0, cell_length * 3), (width, cell_length * 3), 4)
    pygame.draw.line(screen, black, (0, cell_length * 6), (width, cell_length * 6), 4)
    pygame.draw.line(screen, black, (cell_length * 3, 0), (cell_length * 3, width), 4)
    pygame.draw.line(screen, black, (cell_length * 6, 0), (cell_length * 6, width), 4)

draw()


while True:  # keeps the window open until the user exits.
    # event handler
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.QUIT()

            sys.exit()

    pygame.display.update()  # updates all changes.
