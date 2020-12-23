import pygame
import piece
import numpy as np
class Deska:
	def __init__(self,screen):
		self.dot=pygame.image.load("../chess/Images/Dot.png")
		self.image=pygame.image.load("../chess/Images/Board.png")
		self.normal=self.image
		self.imager=pygame.image.load("../chess/Images/Boardr.png")
		self.screen=screen
		self.abc=pygame.image.load("../chess/Images/Board_abc.png")
		self.num=pygame.image.load("../chess/Images/Board_num.png")
		self.numr=pygame.image.load("../chess/Images/Board_numr.png")
		self.nums=self.num
		self.boardstate=np.zeros((8,8), dtype=np.int8)
		self.turn=1
		self.picture=[[0,0,0,0,0,0,0,0] for x in range(8)]
		self.help=1
		self.select=None
		self.moves=set()
		self.result=None
		self.enpassant=None
		self.reverse=0
	def draw(self):
		self.screen.blit(self.normal,(0,0))
		self.screen.blit(self.abc,(0,480))
		self.screen.blit(self.nums,(480,0))
		if self.help and self.select!=None:
			self.screen.blit(pygame.image.load("../chess/Images/Stress.png"), tuple([60*x for x in self.select]))
		for i in range(8):
			for j in range(8):
				if self.picture[i][j]!=0:
					self.screen.blit(self.picture[i][j],(j*60,i*60))
		if help:
			for i in self.moves:
				self.screen.blit(pygame.image.load("../chess/Images/Dot.png"), tuple([60*x for x in i]))
	def rever(self):
		if self.normal==self.image:
			self.normal=self.imager
			self.nums=self.numr
		else:
			self.normal=self.image
			self.nums=self.num
		self.boardstate=np.flipud(self.boardstate)
		self.enpassant=(self.enpassant[0],7-self.enpassant[1])
		self.updatepicture()
	def generatenew(self, type=0, Hash=None):
		with open("start.txt","r") as f:
			for i in range(0,2):
				v=f.readline().split()
				for j in range(0,len(v)):
					self.boardstate[7-i][j]=np.int8(v[j])
					self.boardstate[i][j]=-np.int8(v[j])
		self.result=None
		self.updatepicture()

	def selmove(self,coords):
		x=coords[0]//60
		y=coords[1]//60
		if self.boardstate[y][x]*self.turn>0:
			piece.getmove(self.boardstate[y][x], x, y, self)    
		self.select=(x,y)
	def updatepicture(self):
		for i in range(8):
			for j in range(8):
				self.picture[i][j]=piece.getpicture(self.boardstate[i][j])
	def domove(self,coords):
		piece.domove(coords,self)
	def promote(self):
		pass
	def isn_at(self,x,y):
		return 1


