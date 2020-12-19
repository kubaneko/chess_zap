import pygame
import piece as p
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
    def draw(self):
        self.screen.blit(self.normal,(0,0))
        self.screen.blit(self.abc,(0,480))
        self.screen.blit(self.nums,(480,0))
        for i in range(8):
            for j in range(8):
                if self.picture[i][j]!=0:
                    self.screen.blit(self.picture[i][j],(j*60,i*60))
    def rever(self):
        if self.normal==self.image:
            self.normal=self.imager
            self.nums=self.numr
        else:
            self.normal=self.image
            self.nums=self.num
        self.boardstate=self.boardstate[::-1]
    def generatenew(self, type=0, Hash=None):
        with open("start.txt","r") as f:
            for i in range(0,2):
                v=f.readline().split()
                for j in range(0,len(v)):
                    self.boardstate[7-i][j]=np.int8(v[j])
                    self.boardstate[i][j]=-np.int8(v[j])
        self.updatepicture()

    def move(self,coords):
        #if self.boardstate[coords[0]//60][coords[1]//60]!=0:
            #getattr(self.boardstate[coords[0]//60][coords[1]//60], "stress" + self.boardstate[coords[0]//60][coords[1]//60].typ
        pass
    def updatepicture(self):
        for i in range(8):
            for j in range(8):
                self.picture[i][j]=p.getpicture(self.boardstate[i][j])

