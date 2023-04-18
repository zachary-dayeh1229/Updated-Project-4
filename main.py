import pygame
import sudoku_generator
import sys


board = sudoku_generator.Board(630, 630)  # displays the board.
board.draw()
cell = sudoku_generator.Cell(0, 0, 0)  # for testing purposes.
cell.draw()

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



while True:  # keeps the window open until the user exits.
    # event handler
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.QUIT()

            sys.exit()

    pygame.display.update()  # updates all changes.
