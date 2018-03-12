import pygame
import time
import random
from Overlap_rect_rect import *

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 255)
peach = (255, 255, 128)
gray = (128, 128, 128)
orange = (255, 128, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
aqua = (51, 255, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_gray = (200, 200, 200)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dodgee!')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')

def car(x,y):
	gameDisplay.blit(carImg, (x,y))

def obstacle(x, y, width, height, color):
	pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def text_objects(text, font):
 	textSurface = font.render(text, True, black)
 	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	message_display('Game Over')

def button(pos, color, text):
	x = pos[0]
	y = pos[1]
	width = pos[2]
	height = pos[3]
	obstacle(x - width/2, y - height/2, width, height, color)
	smallText = pygame.font.Font('freesansbold.ttf', 30)
	TextSurf, TextRect = text_objects(text, smallText)
	TextRect.center = (x, y)
	gameDisplay.blit(TextSurf, TextRect)

def pause_menu():

	mouse_pos = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	pause_button1_pos = (300, 200, 200, 50)
	pause_button2_pos = (300, 200, 200, 50)
	pause_button3_pos = (300, 200, 200, 50)
	
	pause = True

	button(pause_button1_pos, green, 'Resume Game')
	button(pause_button2_pos, gray, 'Main Menu')
	button(pause_button3_pos, red, 'Quit')

	while not pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if point_in_rect(mouse_pos, pause_button1_pos):
				button(pause_button1_pos, bright_green, 'Resume Game')
				if click[0] == 1:
					game_loop()
			if point_in_rect(mouse_pos, pause_button2_pos):
				button(pause_button2_pos, bright_gray, 'Main Menu')
				if click[0] == 1:
					game_loop()
			if point_in_rect(mouse_pos, pause_button3_pos):
				button(pause_button3_pos, bright_red, 'Quit')
				if click[0] == 1:
					game_loop()
	
def game_intro():

	intro = True

	button1_pos = [300, 400, 100, 50]
	button2_pos = [500, 400, 100, 50]

	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(aqua)
		largeText = pygame.font.Font('freesansbold.ttf', 100)
		TextSurf, TextRect = text_objects("Dodgee!", largeText)
		TextRect.center = ((display_width/2), (display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		
		mouse_pos = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if point_in_rect(mouse_pos, button1_pos):
				#Change color
				button(button1_pos, bright_green, 'Start')
				#Go to game
				if click[0] == 1:
					intro = False
		else: button(button1_pos, green, 'Start')

		if point_in_rect(mouse_pos, button2_pos):
			#Change color
			button(button2_pos, bright_red, 'Quit')
			#Go to game
			if click[0] == 1:
				pygame.quit()
				quit()
		else: button(button2_pos, red, 'Quit')
		
		pygame.display.update()
		clock.tick(15)
def game_loop():

	x = (display_width * 0.45)
	y = (display_height * 0.8)

	car_width = 73
	car_height = 82

	x_change = 0
	y_change = 0

	obstacle_1_width = random.randrange(50, 200)
	obstacle_1_height = 50
	obstacle_1_x = random.randrange(0, display_width - obstacle_1_width)
	obstacle_1_y = 1
	obstacle_1_color = red	
	obstacle_1_y_change = 400/obstacle_1_width

	obstacle_2_width = random.randrange(50, 200)
	obstacle_2_height = 50
	obstacle_2_x = random.randrange(0, display_width - obstacle_2_width)
	obstacle_2_y = 1
	obstacle_2_color = blue
	obstacle_2_y_change = 400/obstacle_2_width

	pause_button_pos = (700, 50, 100, 50)

	counter = 0

	gameExit = False
	pause = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pause = True
					pause_menu()
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					pause = False
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		x += x_change
		y += y_change

		if x > display_width:
			#x = 1
			crash()
			
		elif y > display_height:
			#y = 1
			crash()
			
		elif x < 0:
			#x = display_width - 1
			crash()
			
		elif y < 0:
			#y = display_height - 1
			crash()

		gameDisplay.fill(white)
		car(x,y)

		obstacle_1_y += obstacle_1_y_change
		if obstacle_1_y > display_height:
			obstacle_1_width = random.randrange(50, 200)
			obstacle_1_x = random.randrange(0, display_width - obstacle_1_width)
			obstacle_1_y = 1
			counter += 1
			obstacle_1_y_change = 400/obstacle_1_width + 0.1 * counter

		obstacle_2_y += obstacle_2_y_change
		if obstacle_2_y > display_height:
			obstacle_2_width = random.randrange(50, 200)
			obstacle_2_x = random.randrange(0, display_width - obstacle_2_width)
			obstacle_2_y = 1
			counter += 1
			obstacle_2_y_change = 400/obstacle_2_width + 0.1 * counter

		normalText = pygame.font.Font('freesansbold.ttf', 50)
		TextSurf, TextRect = text_objects('Points:  ' + str(counter), normalText)
		TextRect.center = (150, 50)
		
		if pause:
			button(pause_button_pos, bright_gray, 'Pause')
		else:
			button(pause_button_pos, gray, 'Pause')

		gameDisplay.blit(TextSurf, TextRect)
		obstacle(obstacle_1_x, obstacle_1_y, obstacle_1_width, obstacle_1_height, obstacle_1_color)
		obstacle(obstacle_2_x, obstacle_2_y, obstacle_2_width, obstacle_2_height, obstacle_2_color)

		if 20 > counter > 10:
			time.sleep(5)
			obstacle_1_color = black
			obstacle_2_color = gray
		if 30 > counter > 20:
			time.sleep(5)
			obstacle_1_color = peach
			obstacle_2_color = green
		if 50 > counter > 30:
			time.sleep(5)
			obstacle_1_color = purple
			obstacle_2_color = orange
		if counter > 50:
			time.sleep(5)
			obstacle_1_color = yellow
			obstacle_2_color = aqua
		if overlap_rect_rect([x, y, car_width, car_height], [obstacle_1_x, obstacle_1_y, obstacle_1_width, obstacle_1_height]):
			crash()
		if overlap_rect_rect([x, y, car_width, car_height], [obstacle_2_x, obstacle_2_y, obstacle_2_width, obstacle_2_height]):
			crash()
		pygame.display.update()
		if pause:
			time.sleep(2)
		clock.tick(100)
game_intro()
game_loop()
pygame.quit()
quit()



