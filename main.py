import pygame
import sudoku_generator
import sys

pygame.init()
pygame.display.set_caption("Sudoku")

black = (0, 0, 0)
width = 630
height = 720
pink = (244, 194, 194)
num_rows = 9
num_cols = 9
cell_length = 70

screen = pygame.display.set_mode((width, height))
screen.fill(pink)

def draw():
    # horizontal lines
    for i in range(0, 10):
        pygame.draw.line(screen,
                         black,
                         (0, i * cell_length),
                         (width, i * cell_length))

    for i in range(0, 10):
        pygame.draw.line(screen, black, (i * cell_length, 0), (i * cell_length, width))

    pygame.draw.line(screen, black, (0, cell_length * 3), (width, cell_length * 3), 4)
    pygame.draw.line(screen, black, (0, cell_length * 6), (width, cell_length * 6), 4)
    pygame.draw.line(screen, black, (cell_length * 3, 0), (cell_length * 3, width), 4)
    pygame.draw.line(screen, black, (cell_length * 6, 0), (cell_length * 6, width), 4)

draw()


while True:
    # event handler
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.QUIT()

            sys.exit()

    pygame.display.update()
