import pygame
def getpicture(number):
    if number==0:
        return 0
    elif number<0:
        return slov[abs(number)][1]
    else:
        return slov[abs(number)][0]



p=(pygame.image.load("../chess/Images/P1.png"), pygame.image.load("../chess/Images/P-1.png"),"P")
n=(pygame.image.load("../chess/Images/N1.png"), pygame.image.load("../chess/Images/N-1.png"),"N")
b=(pygame.image.load("../chess/Images/B1.png"), pygame.image.load("../chess/Images/B-1.png"),"B")
q=(pygame.image.load("../chess/Images/Q1.png"), pygame.image.load("../chess/Images/Q-1.png"),"Q")
k=(pygame.image.load("../chess/Images/K1.png"), pygame.image.load("../chess/Images/K-1.png"),"K")
r=(pygame.image.load("../chess/Images/R1.png"), pygame.image.load("../chess/Images/R-1.png"),"R")
slov={1: p, 2: p, 3: n, 4: b, 5: r, 6: r, 9: q, 66: k}
