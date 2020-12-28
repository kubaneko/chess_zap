import pygame
import board
import numpy as np

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
select="else"
while game:
	Clock.tick(FPS)
	screen.fill(COLOUR)
	deska.draw()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game=0
		if event.type==pygame.MOUSEBUTTONDOWN:
			if select=="text":
				select="else"
				deska.Textin=deska.Texti
			else:
				mys=pygame.mouse.get_pos()
				if mys[0]<=480 and mys[1]<=480:
					if (mys[0]//60,mys[1]//60) in deska.moves:
						deska.domove((mys[0]//60, mys[1]//60))
						if deska.result==None:
							deska.updateresult()
					elif deska.select==None or deska.boardstate[mys[1]//60][mys[0]//60]*deska.turn>0:
						deska.moves.clear()
						deska.selmove(mys)
					else:
						deska.select=None
						deska.moves.clear()
				elif mys[0]>495:
					deska.select=None
					deska.moves.clear()
					if mys[1]>295:
						if mys[1]<405:
							if mys[1]>375:
								if deska.help:
									deska.help=0
								else:
									deska.help=1
							elif mys[1]>345:
								if mys[0]<545:
									deska.pointer=0
								elif mys[0]<595:
									if deska.pointer!=0:
										deska.pointer-=1
								elif mys[0]<645:
									if deska.pointer!=len(deska.History)-1:
										deska.pointer+=1
								else:
									deska.pointer=len(deska.History)-1
								deska.updatepicture()
							elif mys[1]>315:
								deska.generatenew()
							else:
								if deska.result==None:
									if mys[0]>595:
										deska.result=0
										deska.resultstring="Draw by agreement"
									else:
										deska.result=deska.turn*-1
										if deska.result==-1:
											deska.resultstring="Black won by resignation"
										else:
											deska.resultstring="White eon by resignation"
						else: 
							if mys[1]<435:
								for i in range(1,len(deska.History), 2):
									deska.History[i]=deska.History[i][::-1]
									deska.History[i]=np.fliplr(deska.History[i])
								if deska.turn==-1:
									deska.rever()
									deska.updatepicture()
								if deska.reverse:
									deska.reverse=0
								else:
									deska.reverse=1
							elif mys[1]<465:
								deska.Textin=deska.Texti2
								select="text"
							else:
								if mys[0]>594:
									deska.Export()
								else:
									deska.Import()
				else:
					deska.select=None
					deska.moves.clear()
		if event.type==pygame.KEYDOWN and select=="text":
			if event.key==pygame.K_BACKSPACE:
				deska.text=deska.text[0:-1]
			else:
				deska.text+=event.unicode

	pygame.display.update()
