import pygame
import sudoku_generator
import sys

# I hope this works.

board = sudoku_generator.Board(630, 630, 0)
board.start_screen()
board = sudoku_generator.Board(630, 630, board.difficulty)  # displays the board.
board.draw()
previous_click = [0, 0]  # initializes previous value

while True:  # keeps the window open until the user exits.
    # event handler
    for event in pygame.event.get():  # if you exit the window.
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        board.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:  # if you click the mouse.
            board.cells[previous_click[0]][previous_click[1]].selected = False
            x, y = event.pos
            row, col = board.click(x, y)
            previous_click = [row, col]
            board.draw()  # overwrites the box to something else.

        if event.type == pygame.KEYDOWN:  # if you select a key.

            if event.key == pygame.K_DOWN:  # if you select down.
                board.cells[previous_click[0]][previous_click[1]].selected = False  # deselect.
                if previous_click[0] == 8:  # if you reach the end of the board.
                    continue
                else:
                    previous_click = [previous_click[0] + 1, previous_click[1]]  # moves over one cell.
                board.select(previous_click[0], previous_click[1])
                board.draw()

            if event.key == pygame.K_UP:  # up.
                board.cells[previous_click[0]][previous_click[1]].selected = False
                if previous_click[0] == 0:
                    continue
                else:
                    previous_click = [previous_click[0] - 1, previous_click[1]]
                board.select(previous_click[0], previous_click[1])
                board.draw()

            if event.key == pygame.K_RIGHT:  # right.
                board.cells[previous_click[0]][previous_click[1]].selected = False
                if previous_click[1] == 8:
                    continue
                else:
                    previous_click = [previous_click[0], previous_click[1] + 1]
                board.select(previous_click[0], previous_click[1])
                board.draw()

            if event.key == pygame.K_LEFT:  # left.
                board.cells[previous_click[0]][previous_click[1]].selected = False
                if previous_click[1] == 0:
                    continue
                else:
                    previous_click = [previous_click[0], previous_click[1] - 1]
                board.select(previous_click[0], previous_click[1])
                board.draw()

            if event.key == pygame.K_1:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 1
                board.draw()
            if board.is_full():
                board.draw_game_over_screen()

    pygame.display.update()  # updates all changes.
