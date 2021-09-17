import pygame
from pygame.locals import *
import time

#初期化
pygame.init()
#画面の高さ
screen_height = 300
#画面の幅
screen_width = 300
line_width = 6
#300 * 300の画面を作る
screen = pygame.display.set_mode((screen_width, screen_height))
#Tic Tac Toeという名前を付ける
pygame.display.set_caption('Tic Tac Toe')

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#define font
font = pygame.font.SysFont(None, 40)

clicked = False
player = 1
pos = (0, 0)
#〇×の初期状態
markers = [ [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0] ]

game_over = False
winner = 0

again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

#盤をつくる
def draw_board():
    bg = (0, 0, 0)
    grid = (255, 255, 255)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, 100*x), (screen_width, 100*x), line_width)
        pygame.draw.line(screen, grid, (100*x, 0), (100*x, screen_height), line_width)

#〇×を書く
def draw_markers():
    y_pos = 0
    for x in markers:
        x_pos = 0
        for y in x:
            if y ==1 :
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            if y == -1:
                pygame.draw.line(screen, blue, (x_pos * 100 + 15, y_pos*100 + 15), (x_pos * 100 + 85, y_pos*100 + 85), line_width)
                pygame.draw.line(screen, blue, (x_pos * 100 + 85, y_pos*100 + 15), (x_pos * 100 + 15, y_pos*100 + 85), line_width)
            x_pos += 1
        y_pos += 1

#ゲーム終了状態か確認する
def check_game_over():
	global game_over
	global winner

	x_pos = 0
	for x in markers:
		#check columns
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True
		#check rows
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			winner = 2
			game_over = True
		x_pos += 1

	#check cross
	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		winner = 2
		game_over = True

	#check for tie
	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		#if it is a tie, then call game over and set winner to 0 (no one)
		if tie == True:
			game_over = True
			winner = 0

#ゲーム終了時の処理
def draw_game_over(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = font.render(end_text, True, (0, 0, 0))
	pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
	screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

	again_text = 'Play Again?'
	again_img = font.render(again_text, True, (0, 0, 0))
	pygame.draw.rect(screen, green, again_rect)
	screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


run = True
while run:
    draw_board()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if markers[cell_y][cell_x] == 0:
                    markers[cell_y][cell_x] = player
                    player *= -1
                    check_game_over()

    if game_over == True:
        draw_game_over(winner)
        #check for mouseclick to see if we clicked on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset variables
                game_over = False
                player = 1
                pos = (0,0)
                markers = []
                winner = 0
                #create empty 3 x 3 list to represent the grid
                for x in range (3):
                    row = [0] * 3
                    markers.append(row)


    pygame.display.update()

pygame.quit()
