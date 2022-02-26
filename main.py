import pygame, random

pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("Tic-Tac-Toe.png")
pygame.display.set_icon(icon)

running = True

sunnySpells = pygame.font.Font("assets/font/SunnyspellsRegular.otf", 50)

X = pygame.image.load("assets/img/X.png").convert_alpha()
X = pygame.transform.scale(X, (50, 50))
O = pygame.image.load("assets/img/O.png").convert_alpha()
O = pygame.transform.scale(O, (50, 50))

box = ["", "", "", "", "", "", "", "", ""]

playerwin = 0
playerturn = 1

# Define the colors we will use in RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (50, 190, 50)
YELLOW = (255, 170, 0)
BORDER = (85, 85, 85)
X_LINE = (255, 0, 0)
O_LINE = (51, 130, 177)

game_over = sunnySpells.render("Game Over", False, RED)
game_over_rect = game_over.get_rect()
game_over_rect.center = (200, 330)

win_game = sunnySpells.render("You Win!", False, GREEN)
win_game_rect = win_game.get_rect()
win_game_rect.center = (200, 330)

draw = sunnySpells.render("Draw!", False, YELLOW)
draw_rect = draw.get_rect()
draw_rect.center = (200, 330)

try_again_bg = pygame.Surface((200, 50))
try_again_bg.fill(GREEN)
try_again_bg.set_alpha(80)

try_again = sunnySpells.render("Try Again", False, BLACK)
try_again_rect = try_again.get_rect()
try_again_rect.center = (200, 400)

while running:
    screen.fill(WHITE)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Board
    pygame.draw.line(screen, BORDER, (80, 50), (80, 290), 2)
    pygame.draw.line(screen, BORDER, (80, 50), (320, 50), 2)
    pygame.draw.line(screen, BORDER, (80, 290), (320, 290), 2)
    pygame.draw.line(screen, BORDER, (320, 290), (320, 50), 2)

    # Board - border
    # Horizontal border
    pygame.draw.line(screen, BORDER, (80, 130), (320, 130), 2)
    pygame.draw.line(screen, BORDER, (80, 210), (320, 210), 2)

    # Vertical border
    pygame.draw.line(screen, BORDER, (160, 50), (160, 290), 2)
    pygame.draw.line(screen, BORDER, (240, 50), (240, 290), 2)

    if playerwin != 0:
        screen.blit(try_again_bg, (100, 373))
        screen.blit(try_again, try_again_rect)

    # When player win or lose
    if playerwin == 1:
        screen.blit(win_game, win_game_rect)
    elif playerwin == 2:
        screen.blit(game_over, game_over_rect)
    elif playerwin == 3:
        screen.blit(draw, draw_rect)

    # Show X in box
    def show_X(index, x, y):
        if box[index] and box[index] == "X":
            screen.blit(X, (x, y))

    def show_O(index, x, y):
        if box[index] and box[index] == "O":
            screen.blit(O, (x, y))

    # row 1
    show_X(0, 96, 65)
    show_X(1, 176, 65)
    show_X(2, 256, 65)

    # row 2
    show_X(3, 96, 145)
    show_X(4, 176, 145)
    show_X(5, 256, 145)

    # row 3
    show_X(6, 96, 225)
    show_X(7, 176, 225)
    show_X(8, 256, 225)

    # Show O in box
    # row 1
    show_O(0, 96, 65)
    show_O(1, 176, 65)
    show_O(2, 256, 65)

    # row 2
    show_O(3, 96, 145)
    show_O(4, 176, 145)
    show_O(5, 256, 145)

    # row 3
    show_O(6, 96, 225)
    show_O(7, 176, 225)
    show_O(8, 256, 225)

    if playerturn == 2:
        if box[0] == "O" and box[1] == "O" and box[2] == "":
            box[2] = "O"
            playerturn = 1
        elif box[0] == "O" and box[2] == "O" and box[1] == "":
            box[1] = "O"
            playerturn = 1
        elif box[1] == "O" and box[2] == "O" and box[0] == "":
            box[0] = "O"
            playerturn = 1
        elif box[3] == "O" and box[4] == "O" and box[5] == "":
            box[5] = "O"
            playerturn = 1
        elif box[3] == "O" and box[5] == "O" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "O" and box[5] == "O" and box[3] == "":
            box[3] = "O"
            playerturn = 1
        elif box[6] == "O" and box[7] == "O" and box[8] == "":
            box[8] = "O"
            playerturn = 1
        elif box[6] == "O" and box[8] == "O" and box[7] == "":
            box[7] = "O"
            playerturn = 1
        elif box[7] == "O" and box[8] == "O" and box[6] == "":
            box[6] = "O"
            playerturn = 1
        elif box[0] == "O" and box[3] == "O" and box[6] == "":
            box[6] = "O"
            playerturn = 1
        elif box[0] == "O" and box[6] == "O" and box[3] == "":
            box[3] = "O"
            playerturn = 1
        elif box[3] == "O" and box[6] == "O" and box[0] == "":
            box[0] = "O"
            playerturn = 1
        elif box[1] == "O" and box[4] == "O" and box[7] == "":
            box[7] = "O"
            playerturn = 1
        elif box[1] == "O" and box[7] == "O" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "O" and box[7] == "O" and box[1] == "":
            box[1] = "O"
            playerturn = 1
        elif box[2] == "O" and box[5] == "O" and box[8] == "":
            box[8] = "O"
            playerturn = 1
        elif box[2] == "O" and box[8] == "O" and box[5] == "":
            box[5] = "O"
            playerturn = 1
        elif box[5] == "O" and box[8] == "O" and box[2] == "":
            box[2] = "O"
            playerturn = 1
        elif box[0] == "O" and box[4] == "O" and box[8] == "":
            box[8] = "O"
            playerturn = 1
        elif box[0] == "O" and box[8] == "O" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "O" and box[8] == "O" and box[0] == "":
            box[0] = "O"
            playerturn = 1
        elif box[2] == "O" and box[4] == "O" and box[6] == "":
            box[6] = "O"
            playerturn = 1
        elif box[2] == "O" and box[6] == "O" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "O" and box[6] == "O" and box[2] == "":
            box[2] = "O"
            playerturn = 1
        elif box[0] == "X" and box[1] == "X" and box[2] == "":
            box[2] = "O"
            playerturn = 1
        elif box[0] == "X" and box[2] == "X" and box[1] == "":
            box[1] = "O"
            playerturn = 1
        elif box[1] == "X" and box[2] == "X" and box[0] == "":
            box[0] = "O"
            playerturn = 1
        elif box[3] == "X" and box[4] == "X" and box[5] == "":
            box[5] = "O"
            playerturn = 1
        elif box[3] == "X" and box[5] == "X" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "X" and box[5] == "X" and box[3] == "":
            box[3] = "O"
            playerturn = 1
        elif box[6] == "X" and box[7] == "X" and box[8] == "":
            box[8] = "O"
            playerturn = 1
        elif box[6] == "X" and box[8] == "X" and box[7] == "":
            box[7] = "O"
            playerturn = 1
        elif box[7] == "X" and box[8] == "X" and box[6] == "":
            box[6] = "O"
            playerturn = 1
        elif box[0] == "X" and box[3] == "X" and box[6] == "":
            box[6] = "O"
            playerturn = 1
        elif box[0] == "X" and box[6] == "X" and box[3] == "":
            box[3] = "O"
            playerturn = 1
        elif box[3] == "X" and box[6] == "X" and box[0] == "":
            box[0] = "O"
            playerturn = 1
        elif box[1] == "X" and box[4] == "X" and box[7] == "":
            box[7] = "O"
            playerturn = 1
        elif box[1] == "X" and box[7] == "X" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "X" and box[7] == "X" and box[1] == "":
            box[1] = "O"
            playerturn = 1
        elif box[2] == "X" and box[5] == "X" and box[8] == "":
            box[8] = "O"
            playerturn = 1
        elif box[2] == "X" and box[8] == "X" and box[5] == "":
            box[5] = "O"
            playerturn = 1
        elif box[5] == "X" and box[8] == "X" and box[2] == "":
            box[2] = "O"
            playerturn = 1
        elif box[0] == "X" and box[4] == "X" and box[8] == "":
            box[8] = "O"
            playerturn = 1
        elif box[0] == "X" and box[8] == "X" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "X" and box[8] == "X" and box[0] == "":
            box[0] = "O"
            playerturn = 1
        elif box[2] == "X" and box[4] == "X" and box[6] == "":
            box[6] = "O"
            playerturn = 1
        elif box[2] == "X" and box[6] == "X" and box[4] == "":
            box[4] = "O"
            playerturn = 1
        elif box[4] == "X" and box[6] == "X" and box[2] == "":
            box[2] = "O"
            playerturn = 1
        else:
            index = random.randint(0, 8)
            if box[index] == "":
                box[index] = "O"
                playerturn = 1

    def check_result(index1, index2, index3, char, pos_start, pos_end, size):
        if box[index1] == char and box[index2] == char and box[index3] == char:
            global playerwin
            if char == "X":
                pygame.draw.line(screen, X_LINE, pos_start, pos_end, size)
                playerwin = 1
            else:
                pygame.draw.line(screen, O_LINE, pos_start, pos_end, size)
                playerwin = 2

    # Char X
    # type 1
    check_result(0, 1, 2, "X", (100, 90), (300, 90), 5)
    check_result(3, 4, 5, "X", (100, 170), (300, 170), 5)
    check_result(6, 7, 8, "X", (100, 250), (300, 250), 5)

    # type 2
    check_result(0, 3, 6, "X", (121, 70), (121, 270), 5)
    check_result(1, 4, 7, "X", (201, 70), (201, 270), 5)
    check_result(2, 5, 8, "X", (281, 70), (281, 270), 5)

    # type 3
    check_result(0, 4, 8, "X", (100, 70), (300, 270), 10)
    check_result(2, 4, 6, "X", (300, 70), (100, 270), 10)

    # Char O
    # type 1
    check_result(0, 1, 2, "O", (100, 90), (300, 90), 5)
    check_result(3, 4, 5, "O", (100, 170), (300, 170), 5)
    check_result(6, 7, 8, "O", (100, 250), (300, 250), 5)

    # # type 2
    check_result(0, 3, 6, "O", (121, 70), (121, 270), 5)
    check_result(1, 4, 7, "O", (201, 70), (201, 270), 5)
    check_result(2, 5, 8, "O", (281, 70), (281, 270), 5)

    # type 3
    check_result(0, 4, 8, "O", (100, 70), (300, 270), 10)
    check_result(2, 4, 6, "O", (300, 70), (100, 270), 10)

    # type 4
    if (
        box[0] != ""
        and box[1] != ""
        and box[2] != ""
        and box[3] != ""
        and box[4] != ""
        and box[5] != ""
        and box[6] != ""
        and box[7] != ""
        and box[8] != ""
        and playerwin == 0
    ):
        playerwin = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if playerwin == 0:

                    def set_choose(index):
                        global playerturn
                        if box[index] == "":
                            if playerturn == 1:
                                box[index] = "X"
                                playerturn = 2
                            # else:
                            #     box[index] = "O"
                            #     playerturn = 1

                    # row 1
                    if 82 < mouse_x < 160 and 52 < mouse_y < 130:
                        set_choose(0)
                    if 162 < mouse_x < 240 and 52 < mouse_y < 130:
                        set_choose(1)
                    if 242 < mouse_x < 320 and 52 < mouse_y < 130:
                        set_choose(2)

                    # row 2
                    if 82 < mouse_x < 160 and 132 < mouse_y < 210:
                        set_choose(3)
                    if 162 < mouse_x < 240 and 132 < mouse_y < 210:
                        set_choose(4)
                    if 242 < mouse_x < 320 and 132 < mouse_y < 210:
                        set_choose(5)

                    # row 3
                    if 82 < mouse_x < 160 and 212 < mouse_y < 290:
                        set_choose(6)
                    if 162 < mouse_x < 240 and 212 < mouse_y < 290:
                        set_choose(7)
                    if 242 < mouse_x < 320 and 212 < mouse_y < 290:
                        set_choose(8)

                if 100 < mouse_x < 300 and 373 < mouse_y < 473:

                    def reset_game():
                        global box
                        global playerwin
                        global playerturn

                        if playerwin == 1:
                            playerturn = 1
                        elif playerwin == 2:
                            playerturn = 2

                        box = ["", "", "", "", "", "", "", "", ""]
                        playerwin = 0

                    if playerwin != 0:
                        reset_game()
    pygame.display.flip()

pygame.quit()
