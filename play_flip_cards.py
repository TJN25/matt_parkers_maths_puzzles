
import pygame
import sys
import time
import random


pygame.init()


white = (255,255,255)
bg = (180,230,255)

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
border_col = (50,100,155)

blue = (0,0,100)

clock = pygame.time.Clock()

display_width = 1200
display_height = 800
block_size = 30
wall_size = 10
FPS = 15


matt_parker = pygame.image.load("/Users/thomasnicholson/bin/mpmp/matt_parker.png")

smallfont = pygame.font.SysFont("helvetica", 25)
smallfontbold = pygame.font.SysFont("helvetica", 25,  bold=True)
medfont = pygame.font.SysFont("helvetica", 50)
largefont = pygame.font.SysFont("helvetica", 80)


def show_method(b_string, i, score_counter):
    card_1_fliped = False
    card_2_fliped = False
    card_3_fliped = False
    card_4_fliped = False
    click_counter = 2
    #print(b_string)
    if b_string[0] == "1":
        card_1_col = red
    else:
        card_1_col = black
    if b_string[1] == "1":
        card_2_col = red
    else:
        card_2_col = black
    if b_string[2] == "1":
        card_3_col = red
    else:
        card_3_col = black
    if b_string[3] == "1":
        card_4_col = red
    else:
        card_4_col = black

    if i == 0:
        card_1_fliped = True
    if i == 1:
        card_2_fliped = True
    if i == 2:
        card_3_fliped = True
    if i == 3:
        card_4_fliped = True

    #print(card_1_col)

    gameDisplay.fill(bg)
    pygame.draw.rect(gameDisplay, border_col, [0, 0, wall_size, display_height])
    pygame.draw.rect(gameDisplay, border_col, [0, 0, display_width, wall_size])
    pygame.draw.rect(gameDisplay, border_col, [0, display_height - wall_size, display_width, wall_size])
    pygame.draw.rect(gameDisplay, border_col, [display_width - wall_size, 0, wall_size, display_height])

    if card_1_fliped == True:
        pygame.draw.rect(gameDisplay, card_1_col,
                         [16, display_height / 4 - 4, display_width / 4 - 32, display_height / 2 + 8])
        if card_1_col == red:
            gameDisplay.blit(matt_parker, (16 + 20, display_height / 4 + 70))
        card_1_fliped = False
    else:
        pygame.draw.rect(gameDisplay, card_1_col, [20, display_height / 4, display_width / 4 - 40, display_height / 2])
        if card_1_col == red:
            gameDisplay.blit(matt_parker, (16 + 20, display_height / 4 + 70))

    if card_2_fliped == True:
        pygame.draw.rect(gameDisplay, card_2_col,
                         [display_width / 4 - 4, display_height / 4 - 4, display_width / 4 - 12,
                          display_height / 2 + 8])
        card_2_fliped = False
        if card_2_col == red:
            gameDisplay.blit(matt_parker, (display_width / 4 + 20, display_height / 4 + 70))
    else:
        pygame.draw.rect(gameDisplay, card_2_col,
                         [display_width / 4, display_height / 4, display_width / 4 - 20, display_height / 2])
        if card_2_col == red:
            gameDisplay.blit(matt_parker, (display_width / 4 + 20, display_height / 4 + 70))

    if card_3_fliped == True:
        pygame.draw.rect(gameDisplay, card_3_col,
                         [2 * display_width / 4 - 4, display_height / 4 - 4, display_width / 4 - 12,
                          display_height / 2 + 8])
        if card_3_col == red:
            gameDisplay.blit(matt_parker, (2 * display_width / 4 + 20, display_height / 4 + 70))
        card_3_fliped = False
    else:
        pygame.draw.rect(gameDisplay, card_3_col,
                         [2 * display_width / 4, display_height / 4, display_width / 4 - 20, display_height / 2])
        if card_3_col == red:
            gameDisplay.blit(matt_parker, (2 * display_width / 4 + 20, display_height / 4 + 70))

    if card_4_fliped == True:
        pygame.draw.rect(gameDisplay, card_4_col,
                         [3 * display_width / 4 - 4, display_height / 4 - 4, display_width / 4 - 12,
                          display_height / 2 + 8])
        if card_4_col == red:
            gameDisplay.blit(matt_parker, (3 * display_width / 4 + 20, display_height / 4 + 70))
        card_4_fliped = False
    else:
        pygame.draw.rect(gameDisplay, card_4_col,
                         [3 * display_width / 4, display_height / 4, display_width / 4 - 20, display_height / 2])
        if card_4_col == red:
            gameDisplay.blit(matt_parker, (3 * display_width / 4 + 20, display_height / 4 + 70))

    if click_counter > 1:
        pygame.draw.rect(gameDisplay, border_col,
                         [3 * display_width / 4 + 100, display_height - 100, display_width / 4 - 130, 50])
        text = smallfont.render("Run Method", True, black)
        gameDisplay.blit(text, [3 * display_width / 4 + 115, display_height - 85])
    else:
        pygame.draw.rect(gameDisplay, border_col,
                         [3 * display_width / 4 + 98, display_height - 98, display_width / 4 - 126, 54])
        text = smallfontbold.render("Run Method", True, black)
        gameDisplay.blit(text, [3 * display_width / 4 + 108, display_height - 85])
    score(score_counter)
    pygame.display.update()




def change_single_pos(b_string, i):
    pos_1 = b_string[0]
    pos_2 = b_string[1]
    pos_3 = b_string[2]
    pos_4 = b_string[3]
    all_pos = [pos_1, pos_2, pos_3, pos_4]
    if all_pos[i] == "1":
        all_pos[i] = "0"
    else:
        all_pos[i] = "1"
    new_string = all_pos[0] + all_pos[1] + all_pos[2] + all_pos[3]
    return(new_string)
def swap_pos(b_string, swap, counter, print_val, changes_list = []):

    for i in range(0, 4):
        b_string = change_single_pos(b_string, i)
        changes_list.append(b_string)
        counter += 1
        if print_val == "T":
            print(b_string)
        if b_string == "1111":
            print("Number of turns: " + str(counter))
            return(changes_list)
    b_string = swap_pos_minus_1(b_string, swap, counter, print_val, changes_list)
    return(b_string)
def swap_pos_minus_1(b_string, swap, counter, print_val, changes_list):
    for i in range(0, 3):
        b_string = change_single_pos(b_string, i)
        changes_list.append(b_string)

        counter += 1
        if print_val == "T":
            print(b_string)
        if b_string == "1111":
            print("Number of turns: " + str(counter))
            return(changes_list)
    pos_1 = b_string[0]
    pos_2 = b_string[1]
    pos_3 = b_string[2]
    pos_4 = b_string[3]
    if swap == 1:
        swap = 2
        b_string = pos_2 + pos_1 + pos_3 + pos_4
        changes_list.append(b_string)
    else:
        swap = 1
        b_string = pos_1 + pos_3 + pos_2 + pos_4
        changes_list.append(b_string)
    b_string = swap_pos(b_string, swap, counter, print_val, changes_list)
    return(changes_list)

def solve_pattern(card_1_col, card_2_col, card_3_col, card_4_col):
    if card_1_col == red:
        b_1 = "1"
    else:
        b_1 = "0"
    if card_2_col == red:
        b_2 = "1"
    else:
        b_2 = "0"
    if card_3_col == red:
        b_3 = "1"
    else:
        b_3 = "0"
    if card_4_col == red:
        b_4 = "1"
    else:
        b_4 = "0"
    counter = 0
    swap = 1
    b_string = b_1 + b_2 + b_3 + b_4
    b_string = swap_pos(b_string, swap, counter, "F", [b_string])
    return(b_string)



def text_objects(text, colour, size):

    if size == "small":
        textSurface = smallfont.render(text, True, colour)
    elif size == "medium":
        textSurface = medfont.render(text, True, colour)
    elif size == "large":
        textSurface = largefont.render(text, True, colour)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, colour, y_adjust=0, size = "small"):
    textSurf, textRect = text_objects(msg, colour, size)
    textRect.center = (display_width/2), (display_height/2) - y_adjust
    gameDisplay.blit(textSurf, textRect)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Face Down Cards")
pygame.display.set_icon(matt_parker)


def rand_dot():
    rand_dot_x = random.randrange(block_size, display_width - rand_size - block_size)#/block_size - 2)*block_size
    rand_dot_y = random.randrange(block_size, display_height - rand_size - block_size)#/block_size - 2)*block_size
    return rand_dot_x, rand_dot_y

def score(score):
    text = smallfont.render("Counter: "+str(score), True, black)
    gameDisplay.blit(text, [block_size, block_size])


def game_intro():
    lead_colour = "black"
    gameExit = False
    gameOver = False
    gamePause = False
    gameStart = True

    while gameStart:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  ##quit game
                gamePause = False
                gameExit = True
                gameStart = False

                gameDisplay.fill(bg)
                pygame.draw.rect(gameDisplay, border_col, [0, 0, wall_size, display_height])
                pygame.draw.rect(gameDisplay, border_col, [0, 0, display_width, wall_size])
                pygame.draw.rect(gameDisplay, border_col, [0, display_height - wall_size, display_width, wall_size])
                pygame.draw.rect(gameDisplay, border_col, [display_width - wall_size, 0, wall_size, display_height])
                message_to_screen("Quiting game", black)
                pygame.display.update()

                time.sleep(2)

                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
                    gamePause = False
                    gameStart = False
                    gameDisplay.fill(bg)
                    pygame.draw.rect(gameDisplay, border_col, [0, 0, wall_size, display_height])
                    pygame.draw.rect(gameDisplay, border_col, [0, 0, display_width, wall_size])
                    pygame.draw.rect(gameDisplay, border_col, [0, display_height - wall_size, display_width, wall_size])
                    pygame.draw.rect(gameDisplay, border_col, [display_width - wall_size, 0, wall_size, display_height])
                    message_to_screen("Quiting game", black)
                    pygame.display.update()

                    time.sleep(2)

                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    gamePause = False
                    gameStart = False
                elif event.key == pygame.K_SPACE:
                    gamePause = False
                    gameStart = False

                elif event.key == pygame.K_ESCAPE:
                    gameStart = False
                    gamePause = False
                    gameExit = True
                    gameDisplay.fill(bg)
                    pygame.draw.rect(gameDisplay, border_col, [0, 0, wall_size, display_height])
                    pygame.draw.rect(gameDisplay, border_col, [0, 0, display_width, wall_size])
                    pygame.draw.rect(gameDisplay, border_col, [0, display_height - wall_size, display_width, wall_size])
                    pygame.draw.rect(gameDisplay, border_col, [display_width - wall_size, 0, wall_size, display_height])
                    message_to_screen("Quiting game", black)

                    pygame.display.update()

                    time.sleep(2)

                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gamePause = False
                gameStart = False
        gameDisplay.fill(bg)
        pygame.draw.rect(gameDisplay, border_col, [0, 0, wall_size, display_height])
        pygame.draw.rect(gameDisplay, border_col, [0, 0, display_width, wall_size])
        pygame.draw.rect(gameDisplay, border_col, [0, display_height - wall_size, display_width, wall_size])
        pygame.draw.rect(gameDisplay, border_col, [display_width - wall_size, 0, wall_size, display_height])
        message_to_screen("Welcome!", blue, y_adjust = 100, size="large")
        message_to_screen("Click on a card to filp it", black, y_adjust = -40)
        message_to_screen("Click anywhere to start", black, y_adjust = -80)
        pygame.display.update()

        clock.tick(5)

def gameLoop():
    gameExit = False
    gameOver = False
    gamePause = False
    gameStart = True
    run_method = False
    loop_counter = 0
    score_counter = 0
    FPS = 15
    card_1_col = black
    card_2_col = black
    card_3_col = black
    card_4_col = black
    card_1_fliped = False
    card_2_fliped = False
    card_3_fliped = False
    card_4_fliped = False
    click_counter = 2

    while not gameExit:
        if run_method == True:
            FPS = 1

            if loop_counter == 0:
                score_counter = 0
                changes_list = solve_pattern(card_1_col, card_2_col, card_3_col, card_4_col)
                print(changes_list)
            b_string = changes_list[loop_counter]
            show_method(b_string, loop_counter, score_counter)
            loop_counter +=1
            if loop_counter % 8 != 0:
                score_counter += 1
            if loop_counter == len(changes_list) - 1:
                run_method = False
                card_1_col = red
                card_2_col = red
                card_3_col = red
                card_4_col = red
                loop_counter = 0
                score("Done")
        else:
            FPS = 15
            changes_list = []
        click_counter += 1
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:##quit game
                gameOver = False
                gameExit = True
            elif event.type == pygame.KEYDOWN:##start movements
                if event.key == pygame.K_ESCAPE:
                    gameOver = False
                    gameExit = True
                elif event.key == pygame.K_SPACE:
                    gamePause = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_accel = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_accel = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #print(pos)
                if pos[0] < display_width/4 - 40 and pos[0] > 20 and pos[1] < display_height/4 + display_height/2 and pos[1] > display_height/4:
                    if card_1_col == red:
                        card_1_col = black
                        card_1_fliped = True

                    else:
                        card_1_col = red
                        card_1_fliped = True

                if pos[0] < display_width/4 + display_width/4 - 20 and pos[0] > display_width/4 and pos[1] < display_height/4 + display_height/2 and pos[1] > display_height/4:
                    if card_2_col == red:
                        card_2_col = black
                        card_2_fliped = True

                    else:
                        card_2_col = red
                        card_2_fliped = True
                if pos[0] < 3*display_width/4 - 20 and pos[0] > 2*display_width/4 and pos[1] < display_height/4 + display_height/2 and pos[1] > display_height/4:
                    if card_3_col == red:
                        card_3_col = black
                        card_3_fliped = True

                    else:
                        card_3_col = red
                        card_3_fliped = True

                if pos[0] < 4*display_width/4 - 20 and pos[0] > 3*display_width/4 and pos[1] < display_height/4 + display_height/2 and pos[1] > display_height/4:
                    if card_4_col == red:
                        card_4_col = black
                        card_4_fliped = True

                    else:
                        card_4_col = red
                        card_4_fliped = True

                if pos[0] < 3*display_width/4 + 100 + display_width/4 - 130 and pos[0] > 3*display_width/4 + 100 and pos[1] < display_height - 50 and pos[1] > display_height - 100:
                    run_method = True
                    loop_counter = 0
                    click_counter = 1
                    #print("Run method")

        gameDisplay.fill(bg)
        pygame.draw.rect(gameDisplay, border_col, [0, 0, wall_size, display_height])
        pygame.draw.rect(gameDisplay, border_col, [0, 0, display_width, wall_size])
        pygame.draw.rect(gameDisplay, border_col, [0, display_height - wall_size, display_width, wall_size])
        pygame.draw.rect(gameDisplay, border_col, [display_width - wall_size, 0, wall_size, display_height])


        if card_1_fliped == True:
            pygame.draw.rect(gameDisplay, card_1_col, [16, display_height/4 - 4, display_width/4 - 32, display_height/2 + 8])
            card_1_fliped = False
        else:
            pygame.draw.rect(gameDisplay, card_1_col, [20, display_height/4, display_width/4 - 40, display_height/2])
            if card_1_col == red:
                gameDisplay.blit(matt_parker, (16 + 20, display_height / 4 + 70))

        if card_2_fliped == True:
            pygame.draw.rect(gameDisplay, card_2_col,
                             [display_width / 4 - 4, display_height / 4 - 4, display_width / 4 - 12, display_height / 2 + 8])
            card_2_fliped = False
        else:
            pygame.draw.rect(gameDisplay, card_2_col,
                             [display_width / 4, display_height / 4,  display_width / 4 - 20, display_height / 2])
            if card_2_col == red:
                gameDisplay.blit(matt_parker, (display_width / 4 + 20, display_height / 4 + 70))

        if card_3_fliped == True:
            pygame.draw.rect(gameDisplay, card_3_col,
                             [2 * display_width / 4 - 4, display_height / 4 - 4, display_width / 4 - 12, display_height / 2 + 8])
            card_3_fliped = False
        else:
            pygame.draw.rect(gameDisplay, card_3_col,
                             [2 * display_width / 4, display_height / 4, display_width / 4 - 20, display_height / 2])
            if card_3_col == red:
                gameDisplay.blit(matt_parker, (2 * display_width / 4 + 20, display_height / 4 + 70))

        if card_4_fliped == True:
            pygame.draw.rect(gameDisplay, card_4_col,
                             [3 * display_width / 4 - 4, display_height / 4 - 4, display_width / 4 - 12, display_height / 2 + 8])
            card_4_fliped = False
        else:
            pygame.draw.rect(gameDisplay, card_4_col,
                             [3 * display_width / 4, display_height / 4, display_width / 4 - 20, display_height / 2])
            if card_4_col == red:
                gameDisplay.blit(matt_parker, (3 * display_width / 4 + 20, display_height / 4 + 70))

        if click_counter > 1:
            pygame.draw.rect(gameDisplay, border_col, [3*display_width/4 + 100, display_height - 100, display_width/4 - 130, 50])
            text = smallfont.render("Run Method", True, black)
            gameDisplay.blit(text, [3*display_width/4 + 115, display_height - 85])
        else:
            pygame.draw.rect(gameDisplay, border_col, [3*display_width/4 + 98, display_height - 98, display_width/4 - 126, 54])
            text = smallfontbold.render("Run Method", True, black)
            gameDisplay.blit(text, [3*display_width/4 + 108, display_height - 85])
        score(score_counter)
        pygame.display.update()

        clock.tick(FPS)

game_intro()
gameLoop()

message_to_screen("Quiting game", black)
pygame.display.update()

time.sleep(0.5)

pygame.quit()
sys.exit()