import pygame
#click on the screen
screen = pygame.display.set_mode((30,30))
clock = pygame.time.Clock()
img = pygame.image.load("ball.png").convert_alpha()
click = False
drawing = True
while True:
	screen.fill(120)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:#here is the event u want
			drawing = False
		elif event.type == pygame.MOUSEBUTTONUP:
			drawing = True
	if drawing:
		screen.blit(img,(0,0))
	click = False
	pygame.display.flip()
	clock.tick(60)
