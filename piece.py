import pygame
def Bishop(number,x,y,deska):
	for i in (-1,1):
		for j in (-1,1):
			x2=x+i
			y2=y+j
			while x2>=0 and y2>=0 and x2<8 and y2<8: 
				if deska.boardstate[y2][x2]==0:
					if deska.trymove(x2,y2):
						deska.moves.add((x2,y2))
					x2+=i
					y2+=j
				elif deska.boardstate[y2][x2]*deska.turn<0:
					if deska.trymove(x2,y2):
						deska.moves.add((x2,y2))
					break
				else:
					break
def Rook(number,x,y,deska):
	for i in (1,-1):
		x2=x+i
		y2=y+i
		while x2>=0 and x2<8:
			if deska.boardstate[y][x2]==0:
				if deska.trymove(x2,y):
					deska.moves.add((x2,y))
				x2+=i
			elif deska.boardstate[y][x2]*deska.turn<0:
				if deska.trymove(x2,y):
					deska.moves.add((x2,y))
				break
			else:
				break
		while y2>=0 and y2<8:
			if deska.boardstate[y2][x]==0:
				if deska.trymove(x,y2):
					deska.moves.add((x,y2))
				y2+=i
			elif deska.boardstate[y2][x]*deska.turn<0:
				if deska.trymove(x,y2):
					deska.moves.add((x,y2))
				break
			else:
				break
def Queen(number,x,y,deska):
	for i in (1,-1):
		x2=x+i
		y2=y+i
		while x2>=0 and x2<8:
			if deska.boardstate[y][x2]==0:
				if deska.trymove(x2,y):
					deska.moves.add((x2,y))
				x2+=i
			elif deska.boardstate[y][x2]*deska.turn<0:
				if deska.trymove(x2,y):
					deska.moves.add((x2,y))
				break
			else:
				break
		while y2>=0 and y2<8:
			if deska.boardstate[y2][x]==0:
				if deska.trymove(x,y2):
					deska.moves.add((x,y2))
				y2+=i
			elif deska.boardstate[y2][x]*deska.turn<0:
				if deska.trymove(x,y2):
					deska.moves.add((x,y2))
				break
			else:
				break
	for i in (-1,1):
		for j in (-1,1):
			x2=x+i
			y2=y+j
			while x2>=0 and y2>=0 and x2<8 and y2<8: 
				if deska.boardstate[y2][x2]==0:
					if deska.trymove(x2,y2):
						deska.moves.add((x2,y2))
					x2+=i
					y2+=j
				elif deska.boardstate[y2][x2]*deska.turn<0:
					if deska.trymove(x2,y2):
						deska.moves.add((x2,y2))
					break
				else:
					break
def Night(number,x,y,deska):
	for i in (-2,2):
		for j in (-1,1):
			if 8>x+i>-1 and 8>y+j>-1 and deska.boardstate[y+j][x+i]*deska.turn<=0:
				if deska.trymove(x+i,y+j):
					deska.moves.add((x+i,y+j))
			if 8>x+j>-1 and 8>y+i>-1 and deska.boardstate[y+i][x+j]*deska.turn<=0:
				if deska.trymove(x+j,y+i):
					deska.moves.add((x+j,y+i))
def Pawn(number,x,y,deska):
	f=-deska.turn-(deska.reverse-deska.turn*deska.reverse)
	if deska.boardstate[y+f][x]==0:
		if deska.trymove(x,y+f):
			deska.moves.add((x,y+f))
		if y==(f*2)%7-f and deska.boardstate[y+f*2][x]==0:
			if deska.trymove(x,y+2*f):
				deska.moves.add((x,y+2*f))
	for i in (1,-1):
		if 8>x+i>-1 and (deska.boardstate[y+f][x+i]*deska.turn<0 or (-1<y+2*f<8 and deska.boardstate[y][x+i]==-2*deska.turn)):
			if deska.trymove(x+i,y+f):
				deska.moves.add((x+i, y+f))
	pass
def King(number,x,y,deska):
	for i in (1,-1):
		g=8>x+i>-1
		if g and deska.isn_at(x+i,y) and deska.boardstate[y][x+i]*deska.turn<=0:
			deska.moves.add((x+i,y))
		for j in (1,-1):
			if 8>y+j>-1:
				if deska.isn_at(x,y+j) and deska.boardstate[y+j][x]*deska.turn<=0:
					deska.moves.add((x,y+j))
				if g and deska.isn_at(x+i,y+j) and deska.boardstate[y+j][x+i]*deska.turn<=0:
					deska.moves.add((x+i,y+j))
	for i in (1,-1):
		if deska.isn_at(x,y):
			if deska.boardstate[y][0]==6*deska.turn:
				if deska.boardstate[y][1]==0 and deska.boardstate[y][2]==0 and deska.boardstate[y][3]==0:
						if deska.isn_at(2,y) and deska.isn_at(3,y):
							deska.moves.add((2,y))
			if deska.boardstate[y][7]==6*deska.turn:
				if deska.boardstate[y][6]==0 and deska.boardstate[y][5]==0:
						if deska.isn_at(5,y) and deska.isn_at(6,y):
							deska.moves.add((6,y))
def king(number,x,y,deska):
	for i in (1,-1):
		g=8>x+i>-1
		if g and deska.isn_at(x+i,y) and deska.boardstate[y][x+i]*deska.turn<=0:
			deska.moves.add((x+i,y))
		for j in (1,-1):
			if 8>y+j>-1:
				if deska.isn_at(x,y+j) and deska.boardstate[y+j][x]*deska.turn<=0:
					deska.moves.add((x,y+j))
				if g and deska.isn_at(x+i,y+j) and deska.boardstate[y+j][x+i]*deska.turn<=0:
					deska.moves.add((x+i,y+j))
def move(coords,deska):
	if deska.boardstate[coords[1]][coords[0]]!=0:
		deska.threefold=0
		deska.fiftydraw=0
	deska.boardstate[coords[1]][coords[0]]=deska.boardstate[deska.select[1]][deska.select[0]]
	deska.boardstate[deska.select[1]][deska.select[0]]=0
	deska.select=None
	deska.moves.clear()
	if deska.enpassant!=None and deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]==-deska.turn*2:
		deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]=deska.turn*-1
		deska.enpassant=None
	deska.threefold+=1
	deska.fiftydraw+=1
	deska.pointer+=1
	if deska.reverse:
		deska.rever()
	deska.History.append(deska.boardstate.copy())
	deska.updatepicture()
	deska.turn*=-1
	if deska.turn==-1:
		deska.King=deska.Bing
	else:
		deska.King=deska.Wing
def pove(coords,deska):
	deska.fiftydraw=0
	if abs(coords[1]-deska.select[1])==2:
		if deska.enpassant!=None and deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]==-deska.turn*2:
			deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]=deska.turn*-1
			deska.enpassant=None
		deska.enpassant=coords
		deska.boardstate[deska.select[1]][deska.select[0]]=deska.turn*2
	elif coords[1]==0 or coords[1]==7:
		deska.promote(coords)
	elif abs(coords[0]-deska.select[0])==1 and deska.boardstate[coords[1]][coords[0]]==0:
		deska.boardstate[coords[1]+deska.turn-(deska.reverse)-deska.turn*deska.reverse][coords[0]]=0
		deska.threefold=0
	move(coords,deska)
def rove(coords,deska):
	deska.boardstate[coords[1]][coords[0]]=deska.turn*5
	move(coords,deska)
def kove(coords,deska):
	if abs(deska.boardstate[deska.select[1]][deska.select[0]])==66:
		g=coords[0]-deska.select[0]
		deska.boardstate[deska.select[1]][deska.select[0]]=deska.turn*65
		if abs(g)==2:
			if deska.boardstate[deska.select[1]][int((1-g//2)*3.5)]*deska.turn==6:
				deska.boardstate[deska.select[1]][int((1-g//2)*3.5)]=5*deska.turn
			deska.boardstate[deska.select[1]][deska.select[0]+g//2]=deska.turn*5
			deska.boardstate[deska.select[1]][int((1+g//2)*3.5)]=0
	if deska.turn==-1:
		deska.Bing=coords
	else:
		deska.Wing=coords
	move(coords,deska)
def getpicture(number):
	if number==0:
		return 0
	else:
		return slov[number]
def getmove(number,x,y,deska):
	slov2[abs(number)](number,x,y,deska)
def domove(coords,deska):
	slov3[abs(deska.boardstate[deska.select[1]][deska.select[0]])](coords, deska)
def Playout(moves, deska):
	c=0
	for move in moves:
		of=0
		if move[-1]=="+" or move[-1]=="#":
			of=-1
		if c and move[-1]!="}":
			pass
		elif move[-1]=="}":
			c=0
		else:
			if move[0]=="{":
				c=1
			elif ord("A")<=ord(move[0])<=ord("Z"):
				if move[0]=="O":
					deska.select=deska.King
					factor=1
					if deska.turn==-1 and deska.reverse:
						factor=-1
					if len(move)==5:
						domove((deska.King[0]-2*factor,deska.select[1]),deska)
					else:
						domove((deska.King[0]+2*factor,deska.select[1]),deska)
					deska.select=None
				elif deska.reverse and deska.turn==-1:
					Playpgn(move, deska,7-ord(move[-2+of])+ord("a"),int(move[-1+of]),of)
				else:
					Playpgn(move, deska,ord(move[-2+of])-ord("a"),8-int(move[-1+of]),of)
			elif ord("a")<=ord(move[0]) and ord(move[0])<=ord("z"):
				if deska.reverse and deska.turn==-1:
					Playpgn(move, deska,7-ord(move[-2+of])+ord("a"),int(move[-1+of])-1,of,"P")
				else:
					Playpgn(move, deska,ord(move[-2+of])-ord("a"),8-int(move[-1+of]),of,"P")
def Playpgn(move, deska,x,y,of,fig=None):
	if len(move)>2-of and move[-3+of]=="x":
		of-=1
	figs=[]
	deska.moves.clear()
	if move[0]==K:
		fig="K"
	else:
		for i in range(8):
			for j in range(8):
				if deska.boardstate[i][j]*deska.turn>0 and (slov4[abs(deska.boardstate[i][j])]==move[0] or slov4[abs(deska.boardstate[i][j])]==fig):
					deska.select=(j,i)
					getmove(deska.boardstate[i][j],j,i,deska)
					if (x,y) in deska.moves:
						figs.append((j,i))
					deska.moves.clear()
					deska.select=None
	if len(figs)==1:
		deska.select=figs[0]
		domove((x,y),deska)
		return
	elif len(figs)>1:
		p=0
		if ord("a")<=ord(move[-3+of])<=ord("z"):
			p=1
		for i in figs:
			if i[p]==move[-3+of]:
				deska.select=i
				domove((x,y),deska)
	else:
		deska.text="Invalid Game"




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
slov3={1: pove, 2: pove, 3: move, 4: move, 5: move, 6: rove, 9: move, 66: kove, 65: kove}
slov2={1: Pawn, 2: Pawn, 3: Night, 4: Bishop, 5: Rook, 6: Rook, 9: Queen, 66: King, 65: king}
slov4={1:"P",2:"P",3: "N", 4: "B", 5: "R",6: "R", 9: "Q",65:"K", 66: "K"}