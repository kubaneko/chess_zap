import pygame
import board

pygame.init()

game=1
WIDTH=695
HEGHT=495
FPS=30
COLOUR=(200,200,200)

screen=pygame.display.set_mode((WIDTH,HEGHT))
Clock=pygame.time.Clock()
pygame.display.set_caption("Chess")
icon=pygame.image.load("../chess/Images/K-1.png")
pygame.display.set_icon(icon)
deska=board.Deska(screen)
deska.generatenew()
while game:
	Clock.tick(FPS)

	screen.fill(COLOUR)
	deska.draw()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game=0
		if event.type==pygame.MOUSEBUTTONDOWN:
			mys=pygame.mouse.get_pos()
			if mys[0]<=480 and mys[1]<=480:
				if (mys[0]//60,mys[1]//60) in deska.moves:
				   deska.domove((mys[0]//60, mys[1]//60))
				   deska.updateresult()
				   if deska.result!=None:
					   print(deska.result)
				elif deska.select==None or deska.boardstate[mys[1]//60][mys[0]//60]*deska.turn>0:
					deska.moves.clear()
					deska.selmove(mys)
				else:
					deska.select=None
					deska.moves.clear()
		elif 0:
			for i in range(1,len(deska.History), 2):
				deska.History[i]=deska.History[i][::-1]
			if deska.reverse:
				deska.reverse=0
			else:
				deska.reverse=1
	pygame.display.update()
