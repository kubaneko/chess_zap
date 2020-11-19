import pygame
import piece
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
        self.pieces=[]
        self.BK=1
        self.WK=1
        self.boardstate=[]
        for _ in range(0,8):
            self.boardstate.append([0,0,0,0,0,0,0,0])
    def draw(self):
        self.screen.blit(self.normal,(0,0))
        self.screen.blit(self.abc,(0,480))
        self.screen.blit(self.nums,(480,0))
        for i in self.pieces:
            self.screen.blit(i.image,(i.x,i.y))
    def rever(self):
        if self.normal==self.image:
            self.normal=self.imager
            self.nums=self.numr
        else:
            self.normal=self.image
            self.nums=self.num
        for i in self.pieces:
            i.y=420-i.y
    def addpiece(self,typ,colour,x,y,board):
        self.boardstate[x//60][y//60]=piece.piece(typ,colour,x,y,self)
        self.pieces.append(self.boardstate[x//60][y//60])
    def generatenew(self, type=0, Hash=None):
        with open("start.txt","r") as f:
            for i in range(0,2):
                v=f.readline().split()
                for j in range(0,len(v)):
                    x=j*60
                    y=i*60
                    self.addpiece(v[j],"2",x,y,self)
                    y2=(420-y)
                    self.addpiece(v[j],"1",x,y2,self)
    def move(self,coords):
        #if self.boardstate[coords[0]//60][coords[1]//60]!=0:
            #getattr(self.boardstate[coords[0]//60][coords[1]//60], "stress" + self.boardstate[coords[0]//60][coords[1]//60].typ
        pass


