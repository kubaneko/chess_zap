import pygame
def Bishop(number,x,y,deska):
	# funkce, která upraví set deska.moves, přidáním legálních tahů pro daného střelce
	# Před přidáním tahu se ještě musím přesvědčit, jestli není král pod útokem proto metoda deska.trymove()
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
	# funkce, která upraví set deska.moves, přidáním legálních tahů pro danou věž
	# Před přidáním tahu se ještě musím přesvědčit, jestli není král pod útokem proto metoda deska.trymove()
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
	# funkce, která upraví set deska.moves, přidáním legálních tahů pro danou královnu
	# Před přidáním tahu se ještě musím přesvědčit, jestli není král pod útokem proto metoda deska.trymove()
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
	# funkce, která upraví set deska.moves, přidáním legálních tahů pro daného jezdce
	# Před přidáním tahu se ještě musím přesvědčit, jestli není král pod útokem proto metoda deska.trymove()
	for i in (-2,2):
		for j in (-1,1):
			if 8>x+i>-1 and 8>y+j>-1 and deska.boardstate[y+j][x+i]*deska.turn<=0:
				if deska.trymove(x+i,y+j):
					deska.moves.add((x+i,y+j))
			if 8>x+j>-1 and 8>y+i>-1 and deska.boardstate[y+i][x+j]*deska.turn<=0:
				if deska.trymove(x+j,y+i):
					deska.moves.add((x+j,y+i))
def Pawn(number,x,y,deska):
	# funkce, která upraví set deska.moves, přidáním legálních tahů pro daného jezdce
	# Před přidáním tahu se ještě musím přesvědčit, jestli není král pod útokem proto metoda deska.trymove()
	f=-deska.turn-(deska.reverse-deska.turn*deska.reverse)
	# určuje směr pohybu pěšců pro reverse=1 -1 -1 pro reverse=0 pro černého 1 a pro bílého -1
	if deska.boardstate[y+f][x]==0:
		if deska.trymove(x,y+f):
			deska.moves.add((x,y+f))
		if y==(f*2)%7-f and deska.boardstate[y+f*2][x]==0:
			if deska.trymove(x,y+2*f):
				deska.moves.add((x,y+2*f))
		# skok o 2 pro neoužité pěšce
	for i in (1,-1):
		if 8>x+i>-1 and (deska.boardstate[y+f][x+i]*deska.turn<0 or (-1<y+2*f<8 and deska.boardstate[y][x+i]==-2*deska.turn)):
			if deska.trymove(x+i,y+f):
				deska.moves.add((x+i, y+f))
		# enpassant
	pass
def King(number,x,y,deska):
	# funkce pro krále, který se ještě nehnul, obsahuje rošádu
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
	# Rošáda u krále musím vždy kontrolovat jesli není v šachu, to např. zabranuje rošádě
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
	# Normální pohyb krále
def move(coords,deska,tag=""):
	# tah posunující figuru na coords, parametr tag je použit pro předání, povýšení pěšce, Rošády
	deska.pgn.append(Translatemove1(deska,coords,tag))
	if deska.boardstate[coords[1]][coords[0]]!=0:
		deska.threefold=0
		deska.fiftydraw=0
		# pokud tah je sebrání figury nemůže znovu nastat opakování pozic a pravidlo 50 tahů
	deska.boardstate[coords[1]][coords[0]]=deska.boardstate[deska.select[1]][deska.select[0]]
	deska.boardstate[deska.select[1]][deska.select[0]]=0
	deska.select=None
	deska.moves.clear()
	#pohne figurou, vymaže její zvolení/tahy
	if deska.enpassant!=None and deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]==-deska.turn*2:
		deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]=deska.turn*-1
		deska.enpassant=None
	# aktualizuje stav šachovnice
	deska.threefold+=1
	deska.fiftydraw+=1
	#  zvýší ukazatele podmínky pro remízu
	if deska.reverse:
		deska.rever()
	# popřípadě otočí šachovnici
	deska.pointer+=1
	deska.History.append(deska.boardstate.copy())
	deska.updatepicture()
	deska.turn*=-1
	# posune hru o další tah a přidá aktuální stav do historie
	if deska.turn==-1:
		deska.King=deska.Bing
	else:
		deska.King=deska.Wing
	# změní krále, kterého musím kontrolovat zda není v šachu 
def pove(coords,deska):
	# funkce provádějící komplikovanější tahy pěšců
	tag=""
	deska.fiftydraw=0
	if abs(coords[1]-deska.select[1])==2:
		if deska.enpassant!=None and deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]==-deska.turn*2:
			deska.boardstate[deska.enpassant[1]][deska.enpassant[0]]=deska.turn*-1
			deska.enpassant=None
		# Pokud hraji tah, který není enpassant a musím změnit deska.enpassant změním ho
		deska.enpassant=coords
		deska.boardstate[deska.select[1]][deska.select[0]]=deska.turn*2
	elif coords[1]==0 or coords[1]==7:
		try:
			tag=slov5[deska.text]
		except:
			tag="Q"
		deska.promote(coords)
		# povýší pěšce, pokud má být povýšen, získá pro pgn notaci v co ho vlastně povýšil
	elif abs(coords[0]-deska.select[0])==1 and deska.boardstate[coords[1]][coords[0]]==0:
		deska.boardstate[coords[1]+deska.turn-(deska.reverse)-deska.turn*deska.reverse][coords[0]]=0
		deska.threefold=0
		deska.fiftydraw=0
		# Pokud jde o tah enpassant resetuje remízy a vezme figuru pěšce
	move(coords,deska,tag)
	# všechny podpůrné funkce nakonec "administrativu" nechají na funkci move
def rove(coords,deska):
	# hýbací funkce pro věž, která se ještě nepohla, tímto je pak odebráno právo na rošádu
	deska.boardstate[deska.select[1]][deska.select[0]]=deska.turn*5
	move(coords,deska)
def kove(coords,deska):
	# funkce pro provedení tahu krále, který se ještě nehýbal
	tag=""
	if abs(deska.boardstate[deska.select[1]][deska.select[0]])==66:
		g=coords[0]-deska.select[0]
		deska.boardstate[deska.select[1]][deska.select[0]]=deska.turn*65
		if abs(g)==2:
			deska.boardstate[deska.select[1]][deska.select[0]+g//2]=deska.turn*5
			deska.boardstate[deska.select[1]][int((1+g//2)*3.5)]=0
			if deska.turn*deska.reverse==-1:
				if g<0:
					tag="O-O"
				else:
					tag="O-O-O"
			else:
				if g<0:
					tag="O-O-O"
				else:
					tag="O-O"
			#pokud jde o rošádu ~ skok o dvě pole z pohledu funkce, provedu ji a pgn překladači dám vědět tagem
		if deska.boardstate[deska.select[1]][int((1-g//2)*3.5)]*deska.turn==6:
			deska.boardstate[deska.select[1]][int((1-g//2)*3.5)]=5*deska.turn
		if deska.boardstate[deska.select[1]][int((1+g//2)*3.5)]*deska.turn==6:
			deska.boardstate[deska.select[1]][int((1+g//2)*3.5)]=5*deska.turn
		# "pohne" s věžemi na místě, nutné je to proto, že se pozice liší také podle možností krále na rošádu, důležité pro threefold remízu
	if deska.turn==-1:
		deska.Bing=coords
	else:
		deska.Wing=coords
	# updatuje souřadnice krále
	deska.threefold=0
	# toto ruší právo na rošádu a tedy pozice se už nemůžou opakovat
	move(coords,deska,tag)
def getpicture(number):
	if number==0:
		return 0
	else:
		return slov[number]
	# pro číslo ve slovníku vyhledá obrázek
def getmove(number,x,y,deska):
	slov2[abs(number)](number,x,y,deska)
	# pro číslo ze slovníku zavolá funkci na získání tahů pro dané souřadnice
def domove(coords,deska):
	slov3[abs(deska.boardstate[deska.select[1]][deska.select[0]])](coords, deska)
	# pro číslo ze slovníku zavolá funkci na provedení tahu s danými souřadnicemi
def Playout(moves, deska):
	# funkce dostane tahy zaneřáděné poznámkami atd. ty zahraje a vyhodnotí hru
	c=0
	b=0
	result=None
	resultstr="Game in progress"
	if moves[-1][0]=="0":
		result=-1
		resultstr="Black won by resignation"
	elif moves[-1][1]=="/":
		result=0
		resultstr="Draw by agreement"
	elif moves[-1][0]=="1":
		result=1
		resultstr="White won by resignation"
	# pokud došlo k ukončení hry ne tahem tak si to pro ten případ zapamatuje
	for move in moves:
		of=0
		if move[-1]=="?" or move[-1]=="!":
			of-=1
			if move[-2]=="?" or move[-2]=="!":
				of-=1
		if move[-1]=="+" or move[-1]=="#":
			of=-1
		if len(move)>2:
			if move[-2+of]=="=":
				deska.text=move[-1+of]
				of-=2
		# ?! může být na konci, protože lichess to používá při analýze k značení chyb
		# nastaví posun v daném tahu, protože moje funkce potřebují stejně jen počáteční a finální souřadnice
		if c and move[-1]!="}":
			pass
		elif b and move[-1]!=")":
			pass
		elif move[-1]=="}":
			c=0
		elif move[-1]==")":
			b=0
		else:
			if move[0]=="{":
				c=1
			elif move[0]=="(":
				b=1
		# přeskočí komentáře
			elif ord("A")<=ord(move[0])<=ord("Z"):
				# není zvolen pěšák
				if move[0]=="O":
					deska.select=deska.King
					factor=1
					if deska.turn==-1 and deska.reverse:
						factor=-1
					if len(move)==5:
						domove((deska.King[0]-2*factor,deska.select[1]),deska)
						if deska.result==None:
							deska.updateresult()
					else:
						domove((deska.King[0]+2*factor,deska.select[1]),deska)
						if deska.result==None:
							deska.updateresult()
					deska.select=None
				# řeší rošádu
				elif deska.reverse and deska.turn==-1:
					Playpgn(move, deska,7-ord(move[-2+of])+ord("a"),int(move[-1+of]),of)
				else:
					Playpgn(move, deska,ord(move[-2+of])-ord("a"),8-int(move[-1+of]),of)
			elif ord("a")<=ord(move[0]) and ord(move[0])<=ord("z"):
				if deska.reverse and deska.turn==-1:
					Playpgn(move, deska,7-ord(move[-2+of])+ord("a"),int(move[-1+of])-1,of,"P")
				else:
					Playpgn(move, deska,ord(move[-2+of])-ord("a"),8-int(move[-1+of]),of,"P")
			# jinak přeloží souřadnice z algebraické notace(e5) do souřadnic mého pole
	if deska.result==None:
		deska.result=result
		deska.resultstring=resultstr
	# pokud nebylo dosaženo výsledku na šachovnici výsledek je stejný jako v původní hře
def Playpgn(move, deska,x,y,of,fig=None):
	deska.moves.clear()
	if len(move)>2-of and move[-3+of]=="x":
		of-=1
		# pokud jde o sebrání figury tak zvýší odsazení to je potřeba až ted protože předtím byli potřeba finální souřadnice tahu aneb Ndxe6+ bylo potřeba e6 ted je potřeba to d
	if move[0]=="K":
		deska.select=((deska.King[0],deska.King[1]))
		domove((x,y),deska)
		deska.updateresult()
		deska.select=None
		return
	# Pokud se jedná o krále tak mám jeho počáteční souřadnice a tak tah zahraju
	if fig=="P":
		k=1
	else:
		k=0
	# pokud jde o pěšáka mění se požadovaný ofset, protože se k tahům nepíše P jako pawn
	if abs(of)+3-k-len(move)==2:
		if deska.reverse and deska.turn==-1:
			deska.select((7-ord(move[-3+of])+ord("a"),int(move[-2+of])))
		else:
			deska.select((ord(move[-3+of])-ord("a"),8-int(move[-2+of])))
		domove((x,y),deska)
		deska.updateresult()
		deska.select=None
		return
	# pokud tah má formu Nf3xd4 tak vím kde je figura a tak s ní zahraju
	elif abs(of)+3-k-len(move)==1:
		if deska.reverse and deska.turn==-1:
			yy=7-ord(move[-2+of])+ord("a")
		else:
			yy=ord(move[-2+of])-ord("a")
		for j in range(8):
			if deska.boardstate[yy][j]*deska.turn>0 and (slov4[abs(deska.boardstate[yy][j])]==move[0] or slov4[abs(deska.boardstate[yy][j])]==fig):
				deska.select=(j,yy)
				getmove(deska.boardstate[yy][j],j,yy,deska)
				if (x,y) in deska.moves:
					domove((j,yy),deska)
					deska.moves.clear()
					deska.select=None
					deska.updateresult()
					return
				deska.moves.clear()
				deska.select=None
	# pokud má podobu např. cxd4 tak vím v jakém sloupci se figura nachází, najdu a pokud mezi jejími tahy je aktuální tah zahraju ho
	else:
		for i in range(8):
			for j in range(8):
				if deska.boardstate[i][j]*deska.turn>0 and (slov4[abs(deska.boardstate[i][j])]==move[0] or slov4[abs(deska.boardstate[i][j])]==fig):
					deska.select=(j,i)
					getmove(deska.boardstate[i][j],j,i,deska)
					if (x,y) in deska.moves:
						domove((x,y),deska)
						deska.moves.clear()
						deska.select=None
						deska.updateresult()
						return
					deska.moves.clear()
					deska.select=None
	# jinak např tah Ne6 najdu koně a pokud má mezi jeho tahy aktuální tah tak ten tah zahraju
	deska.text="Invalid game"
	deska.result=0
	deska.resultstring="Who knows its all wrong"
	# Pokud nebyl zahrán žádný tah něco je špatně
def Translatemove1(deska, coords,tags=""):
	move=slov4[abs(deska.boardstate[deska.select[1]][deska.select[0]])]
	# získá figuru s kterou je hráno
	other=[]
	g=deska.select
	if tags!="":
		if tags[0]=="O":
			return tags
			# rošáda je řešena v tagu
		else:	
			tags="="+tags
			move="P"
			# povýšení pěšců upraví tag, aby odpovídal notaci a změní figuru na pěšce, protože ve hře už byla povýšena
	deska.moves.clear()
	for i in range(8):
		for j in range(8):
			if deska.boardstate[i][j]*deska.turn>0 and slov4[abs(deska.boardstate[i][j])]==move[0]:
				deska.select=(j,i)
				getmove(deska.boardstate[i][j],j,i,deska)
				if (coords[0],coords[1]) in deska.moves:
					other.append((j,i))
				deska.moves.clear()
				deska.select=g
			# Najdu všechny možné figury, které mají mezi tahy finální souřadnice pamatuji si aktuálně zvolené pole 
	if deska.boardstate[coords[1]][coords[0]]*deska.turn<0:
		takes="x"
	else:
		takes=""
		# pokud je při tahu sebrána figura zaznačím si to
	for i in other:
		if i==deska.select:
			pass
		elif deska.select[0]==i[0]:
			if deska.reverse and deska.turn==-1:
				move=move+chr(ord("h")-deska.select[0])+str(deska.select[1]+1)+takes+chr(ord("h")-coords[0])+str(coords[1]+1)+tags
				break
			else:
				move=move+chr(ord("a")+deska.select[0])+str(8-deska.select[1])+takes+chr(ord("a")+coords[0])+str(8-coords[1])+tags
				break
	# Pokudd mají dvě figury stejné x tak podle notace musíme zapsat celé souřadnice naší figury, to udělám
	if (len(other)>1 and len(move)==1) or (takes=="x" and move[0]=="P"):
		if deska.reverse and deska.turn==-1:
			move=move+chr(ord("h")-deska.select[0])+takes+chr(ord("h")-coords[0])+str(coords[1]+1)+tags
		else:
			move=move+chr(ord("a")+deska.select[0])+takes+chr(ord("a")+coords[0])+str(8-coords[1])+tags
	# pokud jsou další figury, ale nemá žádná stejné x jako naše figura tak přidáme jen její x v pgn notaci , nebo jde o sebrání figury pěšcem
	elif len(move)==1:
		if deska.reverse and deska.turn==-1:
			move=move+takes+chr(ord("h")-coords[0])+str(coords[1]+1)+tags
		else:
			move=move+takes+chr(ord("a")+coords[0])+str(8-coords[1])+tags
	# jinak víme, že je to jediná možná figura a tak to zahrajem, toho,  že tahy pěšcem vypadají jako Pe6, to vyřeším až v deska.Export()
	return move

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
# obrázky figur
slov={1: p, 2: p, 3: n, 4: b, 5: r,6: r, 9: q, 66: k, 65: k, -1: P, -2: P, -3: N, -4: B, -5: R,-6: R, -9: Q, -66: K, -65: K}
slov3={1: pove, 2: pove, 3: move, 4: move, 5: move, 6: rove, 9: move, 66: kove, 65: kove}
# přiřazuje funkce, které vykonávají tah
slov2={1: Pawn, 2: Pawn, 3: Night, 4: Bishop, 5: Rook, 6: Rook, 9: Queen, 66: King, 65: king}
# přiřazuje funkce přiřazující legální tahy
slov4={1:"P",2:"P",3: "N", 4: "B", 5: "R",6: "R", 9: "Q",65:"K", 66: "K"}
# vrací figuru, kterou reprezentuje ono číslo
slov5={"Q":"Q", "q":"Q", "R":"R", "r":"R", "B":"B", "b":"B", "N":"N", "n":"N", "Queen":"Q", "queen":"Q", "Rook":"R", "rook":"R", "Bishop":"B", "bishop":"B", "Knight":"N", "knight": "N", "Královna":"Q","královna":"Q", "Věž":"R", "věž":"R", "Střelec":"B", "střelec":"B", "Jezdec":"N", "jezdec":"N"}
# Vrací figuru z textového vztupu na povýšení pěšce