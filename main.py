import pygame
import sudoku_generator
import sys


board = sudoku_generator.Board(630, 630, 0)  # creates a full board to run start_screen
board.start_screen() # start screen
board = sudoku_generator.Board(630, 630, board.difficulty)  # creates board with desired difficulty and draws it
board.draw()
previous_click = [0, 0]  # initializes previous value


while True:  # keeps the window open until the user exits.
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if you exit the window
            pygame.QUIT()
            sys.exit()
        board.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:  # if you click the mouse.
            if board.exit_rect.collidepoint(event.pos):  # exit button
                sys.exit()
            if board.restart_rect.collidepoint(event.pos):  # restart button - brings back to start and new board
                board.start_screen()
                board = sudoku_generator.Board(630, 630, board.difficulty)
                break
            if board.reset_rect.collidepoint(event.pos):  # resets user's changes to the board
                board.clear()
            x, y = event.pos # click position
            if y <= 630: # when board is clicked, bc the board is 630 x 630
                board.cells[previous_click[0]][previous_click[1]].selected = False
                row, col = board.click(x, y)
                previous_click = [row, col]
                board.draw()  # overwrites the box to something else.

        if event.type == pygame.KEYDOWN:  # if you select a key.
            # sets up key functions down, up, right, and left
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

            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 1
                board.draw()

            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 2
                board.draw()

            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 3
                board.draw()

            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 4
                board.draw()

            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 5
                board.draw()

            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 6
                board.draw()

            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 7
                board.draw()

            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 8
                board.draw()

            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                board.cells[previous_click[0]][previous_click[1]].sketched_value = 9
                board.draw()

            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                if board.cells[previous_click[0]][previous_click[1]].value == 0:
                    board.cells[previous_click[0]][previous_click[1]].value = board.cells[previous_click[0]][previous_click[1]].sketched_value
                    board.draw()
            # if the user has finished the game by filling all the boxes
            if board.is_full():
                board.draw_game_over_screen()  # calls the ending screen
                board = sudoku_generator.Board(630, 630, board.difficulty)  # generates a new board with the difficulty

    pygame.display.update()  # updates all changes.
