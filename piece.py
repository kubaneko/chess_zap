import pygame
import numpy as np
def Bishop(number,x,y,tah,sign,deska):
    for i in (-1,1):
        for j in (-1,1):
            x2=x+i
            y2=y+j
            while x2>=0 and y2>=0 and x2<8 and y2<8: 
                if deska.boardstate[y2][x2]==0:
                    tah.add((x2,y2))
                    x2+=i
                    y2+=j
                elif deska.boardstate[y2][x2]*sign<0:
                    tah.add((x2,y2))
                    break
                else:
                    break
    return tah
def Rook(number,x,y,tah,sign,deska):
    for i in (1,-1):
        x2=x+i
        y2=y+i
        while x2>=0 and x2<8:
            if deska.boardstate[y][x2]==0:
                tah.add((x2,y))
                x2+=i
            elif deska.boardstate[y][x2]*sign<0:
                tah.add((x2,y))
                break
            else:
                break
        while y2>=0 and y2<8:
            if deska.boardstate[y2][x]==0:
                tah.add((x,y2))
                y2+=i
            elif deska.boardstate[y2][x]*sign<0:
                tah.add((x,y2))
                break
            else:
                break
    return tah
def Queen(number,x,y,tah,sign,deska):
    for i in (1,-1):
        x2=x+i
        y2=y+i
        while x2>=0 and x2<8:
            if deska.boardstate[y][x2]==0:
                tah.add((x2,y))
                x2+=i
            elif deska.boardstate[y][x2]*sign<0:
                tah.add((x2,y))
                break
            else:
                break
        while y2>=0 and y2<8:
            if deska.boardstate[y2][x]==0:
                tah.add((x,y2))
                y2+=i
            elif deska.boardstate[y2][x]*sign<0:
                tah.add((x,y2))
                break
            else:
                break
    for i in (-1,1):
        for j in (-1,1):
            x2=x+i
            y2=y+j
            while x2>=0 and y2>=0 and x2<8 and y2<8: 
                if deska.boardstate[y2][x2]==0:
                    tah.add((x2,y2))
                    x2+=i
                    y2+=j
                elif deska.boardstate[y2][x2]*sign<0:
                    tah.add((x2,y2))
                    break
                else:
                    break
    return tah
def Pawn(number,x,y,pole,tah,sign,deska):
    f=-tah+(deska.reverse)-tah*deska.rever
    if deska.boardstate[y+f][x]==0:
        tah.add((x,y+f))
        if y==(f*2)%7-f and deska.boardstate[y+f*2][x]==0:
            tah.add((x,y+f))
    for i in (1,-1):
        if 8>x+i>-1 and (np.sign(deska.boardstate[y+f][x+i])==-sign or (-1<y+2*f<8 and deska.boardstate[y+2*f][x+i]==-2*sign)):
            tah.add((x+i, y+f))
    pass
def move(coords,deska):
    deska.boardstate[coords[1]][coords[0]]=deska.boardstate[deska.select[1]][deska.select[0]]
    deska.boardstate[deska.select[1]][deska.select[0]]=0
    deska.updatepicture()
    deska.turn*=-1
    deska.select=None
    deska.moves.clear()
    if deska.reverse:
        deska.rever()
def pove():
    pass
def rove(coords,deska):
    deska.boardstate[coords[1]][coords[0]]=deska.turn*5
    deska.boardstate[deska.select[1]][deska.select[0]]=0
    deska.updatepicture()
    deska.turn*=-1
    deska.select=None
    deska.moves.clear()
    print(deska.boardstate)
def kove():
    pass
def getpicture(number):
    if number==0:
        return 0
    else:
        return slov[number]
def getmove(number,x,y,tah,deska):
    tah=slov2[abs(number)](number,x,y,tah,np.sign(number),deska)
    return tah
def domove(coords,deska):
    slov3[abs(deska.boardstate[deska.select[1]][deska.select[0]])](coords, deska)

P=pygame.image.load("../chess/Images/P-1.png")
N=pygame.image.load("../chess/Images/N-1.png")
B=pygame.image.load("../chess/Images/B-1.png")
Q=pygame.image.load("../chess/Images/Q-1.png")
K=pygame.image.load("../chess/Images/K-1.png")
R=pygame.image.load("../chess/Images/R-1.png")
p=pygame.image.load("../chess/Images/P1.png")
n=pygame.image.load("../chess/Images/N1.png")
b=pygame.image.load("../chess/Images/B1.png")
q=pygame.image.load("../chess/Images/Q1.png")
k=pygame.image.load("../chess/Images/K1.png")
r=pygame.image.load("../chess/Images/R1.png")
slov={1: p, 2: p, 3: n, 4: b, 5: r,6: r, 9: q, 66: k, 65: k, -1: P, -2: P, -3: N, -4: B, -5: R,-6: R, -9: Q, -66: K, -65: K}
slov2={4: Bishop, 5: Rook, 6:Rook, 9: Queen}
slov3={1: pove, 2: pove, 3: move, 4: move, 5: move, 6: rove, 9: move, 66: kove, 65: kove}

#slov2={1: Pawn, 2: Pawn, 3: Night, 4: Bishop, 5: Rook, 6: Rook, 9: Queen, 66: King, 65}