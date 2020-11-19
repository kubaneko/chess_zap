import pygame
import board
class piece:
    def __init__(self,typ,colour,x,y,board):
        self.typ=typ
        self.colour=colour
        self.board=board
        self.x=x
        self.y=y
        self.typ=typ
        self.image=pygame.image.load("../chess/Images/"+str(self.typ)+str(self.colour)+".png")
        