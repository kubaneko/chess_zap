import pygame
import board
class piece:
    def __init__(self,x,y,board,typ=None,colour=None):
        self.typ=typ
        self.colour=colour
        self.board=board
        self.x=x
        self.y=y
        self.typ=typ
        if self.typ!=None:
            self.image=pygame.image.load("../chess/Images/"+str(self.typ)+str(self.colour)+".png")
class P(piece):
    def getmove():
        pass
    def move():
        pass
class B(piece):
    def getmove():
        pass
    def move():
        pass
class R(piece):
    def getmove():
        pass
    def move():
        pass
class Q(piece):
    def getmove():
        pass
    def move():
        pass
class N(piece):
    def getmove():
        pass
    def move():
        pass
class K(piece):
    def getmove():
        pass
    def move():
        pass
        