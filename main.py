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


def start_screen(screen):
    title_font = pygame.font.Font(None, 100)  # title font
    button_font = pygame.font.Font(None, 70)  # button font

    screen.fill((197, 161, 196))  # background color
    title_surface = title_font.render("Sudoku", 0, (0, 0, 0))
    screen.blit(title_surface)  # render title
    start_text = button_font.render("Start", 0, (255, 255, 240))
    quit_text = button_font.render("Quit", 0, (255, 255, 240))

    # button background color and text
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill((0, 0, 0))
    start_surface.blit(start_text, (10, 10))

    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(0, 0, 0)
    quit_surface.blit(quit_text, (10, 10))

    # button rectangle
    start_rect = start_surface.get_rect(center=(35, 70))
    quit_rect = quit_surface.get_rect(center=(35, 70))

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

# def game_over(screen):
#     game_over_font = pygame.font.Font(None, 40)
#     screen.fill(197, 161, 196)

start_screen(screen)  # FIXME

while True:  # keeps the window open until the user exits.
    # event handler
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.QUIT()

            sys.exit()

    pygame.display.update()  # updates all changes.
