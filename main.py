import pygame
import sudoku_generator
import sys

# I hope this works.

board = sudoku_generator.Board(630, 630, 0)  # displays the board.
board.start_screen()
board = sudoku_generator.Board(630, 630, board.difficulty)
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
            if board.exit_rect.collidepoint(event.pos):
                sys.exit()
            if board.restart_rect.collidepoint(event.pos):
                board.start_screen()
                board = sudoku_generator.Board(630, 630, board.difficulty)
                break
            if board.reset_rect.collidepoint(event.pos):
                board.clear

            # if board.easy_rect.collidepoint(event.pos):
            #     board.difficulty = 30
            #     print(board.difficulty)
            #
            # elif board.medium_rect.collidepoint(event.pos):
            #     board.difficulty = 40
            #     print(board.difficulty)
            #
            # elif board.hard_rect.collidepoint(event.pos):
            #     board.difficulty = 50
            #     print(board.difficulty)
            #
            # elif board.quit_rect.collidepoint(event.pos):
            #     sys.exit()
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

                    if board.is_full():
                        print()
                        # board.update_board()
                        if board.check_board() is True:
                            print("True")
                        else:
                            print("False") # lose

    pygame.display.update()  # updates all changes.
