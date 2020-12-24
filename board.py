import pygame
import piece
import numpy as np
class Deska:
	def __init__(self,screen):
		self.dot=pygame.image.load("../chess/Images/Dot.png")
		self.image=pygame.image.load("../chess/Images/Board.png")
		self.imager=pygame.image.load("../chess/Images/Boardr.png")
		self.abc=pygame.image.load("../chess/Images/Board_abc.png")
		self.abcr=pygame.image.load("../chess/Images/Boardr_abc.png")
		self.abcn=self.abc
		self.num=pygame.image.load("../chess/Images/Board_num.png")
		self.numr=pygame.image.load("../chess/Images/Board_numr.png")
		self.normal=self.image
		self.screen=screen
		self.nums=self.num
		self.boardstate=np.zeros((8,8), dtype=np.int8)
		self.turn=1
		self.picture=[[0,0,0,0,0,0,0,0] for x in range(8)]
		self.help=1
		self.select=None
		self.moves=set()
		self.result=None
		self.enpassant=None
		self.reverse=1
	def draw(self):
		self.screen.blit(self.normal,(0,0))
		self.screen.blit(self.abcn,(0,480))
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
			self.abcn=self.abcr
		else:
			self.normal=self.image
			self.nums=self.num
			self.abcn=self.abc
		self.boardstate=self.boardstate[::-1]
		self.boardstate=np.fliplr(self.boardstate)
		if self.enpassant!=None:
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
		for i in (-2,2):
			for j in (-1,1):
				if 8>x+i>-1 and 8>y+j>-1 and self.boardstate[y+j][x+i]*self.turn==-3:
					return 0
				if 8>x+j>-1 and 8>y+i>-1 and self.boardstate[y+i][x+j]*self.turn==-3:
					return 0
		for i in (1,-1):
			x2=x+i
			y2=y+i
			while x2>=0 and x2<8:
				if self.boardstate[y][x2]==0:
					x2+=i
				elif self.boardstate[y][x2]*self.turn in {-6,-5,-9}:
					return 0
					break
				else:
					break
			while y2>=0 and y2<8:
				if self.boardstate[y2][x]==0:
					y2+=i
				elif self.boardstate[y2][x]*self.turn in {-6,-5,-9}:
					return 0
					break
				else:
					break
		for i in (-1,1):
			for j in (-1,1):
				x2=x+i
				y2=y+j
				while x2>=0 and y2>=0 and x2<8 and y2<8: 
					if self.boardstate[y2][x2]==0:
						x2+=i
						y2+=j
					elif self.boardstate[y2][x2]*self.turn==-4 or self.boardstate[y2][x2]*self.turn==-9:
						return 0
						break
					else:
						break
		f=-self.turn-(self.reverse-self.turn*self.reverse)
		for i in (1,-1):
			if 8>x+i>-1 and 8>y+f>-1 and self.boardstate[y+f][x+i]*self.turn==-1 or self.boardstate[y+f][x+i]*self.turn==-2:
				return 0
		for i in (1,-1):
			g=8>x+i>-1
			if g and self.boardstate[y][x+i]*self.turn==-66 or self.boardstate[y][x+i]*self.turn==-65:
				return 0
			for j in (1,-1):
				if 8>y+j>-1:
					if self.boardstate[y+j][x]*self.turn==-66 or self.boardstate[y+j][x]*self.turn==-65:
						return 0
					if g and self.boardstate[y+j][x+i]*self.turn==-66 or self.boardstate[y+j][x+i]*self.turn==-65:
						return 0
		return 1
