import pygame
import piece
import numpy as np
class Deska:
	def __init__(self,screen):
		self.image=pygame.image.load("../chess/Images/Board.png")
		self.imager=pygame.image.load("../chess/Images/Boardr.png")
		self.abc=pygame.image.load("../chess/Images/Board_abc.png")
		self.abcr=pygame.image.load("../chess/Images/Boardr_abc.png")
		self.abcn=self.abc
		self.num=pygame.image.load("../chess/Images/Board_num.png")
		self.numr=pygame.image.load("../chess/Images/Board_numr.png")
		self.Texti2=pygame.image.load("../chess/Images/Tex_Input2.png")
		self.Texti=pygame.image.load("../chess/Images/Tex_Input.png")
		self.nums=self.num
		self.Textin=self.Texti
		self.normal=self.image
		# Načtení obrázků měnících se na základě interakce + určení defaultního
		self.screen=screen
		# grafické okno
		self.turn=1
		#aktuální tah 1 bílý, -1 černý hráč
		self.picture=[[0,0,0,0,0,0,0,0] for x in range(8)]
		# obraz šachovnice
		self.help=1
		self.reverse=0
		# uživatelské nastavení (otáčení šachovnice a značení možných tahů)
		self.select=None
		self.moves=set()
		# aktuálně zvolená figura a její možné tahy
		self.result=None
		self.resultstring="Game in progress"
		# Výsledek a jeho důvod
		self.enpassant=None
		self.Bing=(4,0)
		self.Wing=(4,7)
		self.King=self.Wing
		# pozice figur, které musí být známy
		self.text=""
		# textový input
	def draw(self):
		self.screen.blit(self.normal,(0,0))
		self.screen.blit(self.abcn,(0,480))
		self.screen.blit(self.nums,(480,0))
		self.screen.blit(self.Textin, (495,435))
		self.screen.blit(pygame.image.load("../chess/Images/I_E.png"), (495,465))
		self.screen.blit(pygame.image.load("../chess/Images/Result.png"), (495,0))
		self.screen.blit(pygame.image.load("../chess/Images/Arrows.png"), (495,345))
		self.screen.blit(pygame.image.load("../chess/Images/New.png"), (495,315))
		self.screen.blit(pygame.image.load("../chess/Images/Text.png"), (495,30))
		self.screen.blit(pygame.image.load("../chess/Images/Gamebutton.png"), (495,295))
		if self.reverse:
			self.screen.blit(pygame.image.load("../chess/Images/Reverse1.png"), (495,405))
		else:
			self.screen.blit(pygame.image.load("../chess/Images/Reverse0.png"), (495,405))
		# načtení šachovnice tlačítek a ostatní grafiky
		if self.help and self.select!=None:
			self.screen.blit(pygame.image.load("../chess/Images/Stress.png"), tuple([60*x for x in self.select]))
		# načtení zvýraznění zvolené figury
		for i in range(8):
			for j in range(8):
				if self.picture[i][j]!=0:
					self.screen.blit(self.picture[i][j],(j*60,i*60))
		# načtení figur
		if self.help:
			self.screen.blit(pygame.image.load("../chess/Images/Description1.png"), (495,375))
			for i in self.moves:
				self.screen.blit(pygame.image.load("../chess/Images/Dot.png"), tuple([60*x for x in i]))
		else:
			self.screen.blit(pygame.image.load("../chess/Images/Description0.png"), (495,375))
		# načtení možných tahů a tlačítka pro jejich zvýraznění (musí být po načtení figur)
		self.Font=pygame.font.Font(None,20).render(self.resultstring, True, (0,0,0))
		self.Text=pygame.font.Font(None,30).render(self.text, True, (0,0,0))
		self.screen.blit(self.Text, (500,440))
		self.screen.blit(self.Font, (500,8))
		# načtení textu-výsledku hry a textového vztupu
	def rever(self):
		if self.normal==self.image:
			self.normal=self.imager
			self.nums=self.numr
			self.abcn=self.abcr
		else:
			self.normal=self.image
			self.nums=self.num
			self.abcn=self.abc
		# Otočení grafických prvků
		self.boardstate=self.boardstate[::-1]
		self.boardstate=np.fliplr(self.boardstate)
		# Otočení figur
		if self.enpassant!=None:
			self.enpassant=(7-self.enpassant[0],7-self.enpassant[1])
		self.Wing=(7-self.Wing[0],7-self.Wing[1])
		self.Bing=(7-self.Bing[0],7-self.Bing[1])
		self.King=(7-self.King[0],7-self.King[1])
		# aktualizace dat o figurách
	def generatenew(self, type=0):
		self.boardstate=np.zeros((8,8), dtype=np.int8)
		# prázdná šachovnice
		if self.reverse and self.turn==-1:
			self.rever()
		# vrácení šachovnice do původní polohy
		with open("start.txt","r") as f:
			for i in range(0,2):
				v=f.readline().split()
				for j in range(0,len(v)):
					self.boardstate[7-i][j]=np.int8(v[j])
					self.boardstate[i][j]=-np.int8(v[j])
		# načtení figur
		self.Bing=(4,0)
		self.Wing=(4,7)
		self.King=self.Wing
		# základní informace o figurách
		self.History=[self.boardstate.copy()]
		self.pointer=0
		# historie hry, pointer ukazuje počet tahů (principielně půltahů)
		self.turn=1
		self.threefold=1
		self.fiftydraw=0
		self.result=None
		# metriky pro výsledek hry (self.result 1 vyhrál bílý 0 remíza -1 vyhrál černý)
		self.updatepicture()
		# aktualizace grafické šachovnice
		self.pgn=[]
		# tahy převedené do pgn notace
	def updatepicture(self):
		for i in range(8):
			for j in range(8):
				self.picture[i][j]=piece.getpicture(self.History[self.pointer][i][j])
		# z aktuálně prohlíženého tahu vrátí grafiku figur (modul piece)
	def selmove(self,coords):
		# funkce dostane souřadnice myši a aktualizuje proměnnou self.moves s možnými tahy
		x=coords[0]//60
		y=coords[1]//60
		self.select=(x,y)
		if self.boardstate[y][x]*self.turn>0 and self.pointer==len(self.History)-1:
			piece.getmove(self.boardstate[y][x], x, y, self)
		# pokud je zvolená figura správné barvy zavolá pro tahy (modul piece)
	def domove(self,coords):
		piece.domove(coords,self)
		# provede tah (modul piece)
	def promote(self,coords):
		slov={"Q":9, "q":9, "R":5, "r":5, "B":4, "b":4, "N":3, "n":3, "Queen":9, "queen":9, "Rook":5, "rook":5, "Bishop":4, "bishop":4, "Knight":3, "knight": 3, "Královna":9,"královna":9, "Věž":5, "věž":5, "Střelec":4, "střelec":4, "Jezdec":3, "jezdec":3}
		# vrací číslo povyšovanné figury
		try:
			fig=slov[self.text]
			self.text=""
		except KeyError:
			fig=9
		self.boardstate[self.select[1]][self.select[0]]=fig*self.turn
		# povýší pěšáka defaultně na královnu pokud není řečeno jinak
	def isn_at(self,x,y):
		# zjištuje jestli je zadané pole pod útokem, implementace hledání figur tam kde by na dané pole mohly útočit.
		# pro útoky neskákajících figur jsem musel nastavit, že nejsou zastaveny králem
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
				if self.boardstate[y][x2]==0 or self.boardstate[y][x2]*self.turn==65 or self.boardstate[y][x2]*self.turn==66:
					x2+=i
				elif self.boardstate[y][x2]*self.turn in {-6,-5,-9}:
					return 0
					break
				else:
					break
			while y2>=0 and y2<8:
				if self.boardstate[y2][x]==0 or self.boardstate[y2][x]*self.turn==65 or self.boardstate[y2][x]*self.turn==66:
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
					if self.boardstate[y2][x2]==0 or self.boardstate[y2][x2]*self.turn==65 or self.boardstate[y2][x2]*self.turn==66:
						x2+=i
						y2+=j
					elif self.boardstate[y2][x2]*self.turn==-4 or self.boardstate[y2][x2]*self.turn==-9:
						return 0
						break
					else:
						break
		f=-self.turn-(self.reverse-self.turn*self.reverse)
		for i in (1,-1):
			if 8>x+i>-1 and 8>y+f>-1 and (self.boardstate[y+f][x+i]*self.turn==-1 or self.boardstate[y+f][x+i]*self.turn==-2):
				return 0
		for i in (1,-1):
			g=8>x+i>-1
			if g and (self.boardstate[y][x+i]*self.turn==-66 or self.boardstate[y][x+i]*self.turn==-65):
				return 0
			for j in (1,-1):
				if 8>y+j>-1:
					if self.boardstate[y+j][x]*self.turn==-66 or self.boardstate[y+j][x]*self.turn==-65:
						return 0
					if g and (self.boardstate[y+j][x+i]*self.turn==-66 or self.boardstate[y+j][x+i]*self.turn==-65):
						return 0
		return 1
	def trymove(self,x,y):
		# zahraje tah vrátí jestli je král pod útokem a vrátí šachovnici do původního stavu
		memor=self.boardstate[y][x]
		self.boardstate[y][x]=self.boardstate[self.select[1]][self.select[0]]
		self.boardstate[self.select[1]][self.select[0]]=0
		if self.isn_at(self.King[0],self.King[1]):
			i=1
		else:
			i=0
		self.boardstate[self.select[1]][self.select[0]]=self.boardstate[y][x]
		self.boardstate[y][x]=memor
		return i
	def Threefold(self):
		# Hledá zda se aktuální pozice už 3. nezopakovala, to je považováno za remízu.
		# self. threefold je ukazate, kdy je ještě možné mluvit o stejné pozici
		counter=0
		i=-1
		while -self.threefold<=i and counter<3:
			if (self.boardstate==self.History[i]).all():
				counter+=1
			i-=2
		if counter==3:
			return 1
		else:
			return 0
	def Dead_position(self):
		# pokud není možné dát v dané pozici mat tak to prohlásí za remízu (zachytí jen primitivní případy blokády ne)
		minor=0
		for i in range(8):
			for j in range(8):
				if abs(self.boardstate[j][i]) in {9,5,6,1,2}:
					return 0
				elif abs(self.boardstate[j][i])==3 or abs(self.boardstate[j][i])==4:
					minor+=1
		if minor<2:
			return 1
		return 0
	def trystalemate(self):
		# Zjistí zda strana na tahu má legální tahy, použita heuristika, že je pravděpodobnější, že figury budou na straně na které začínají.
		piece.getmove(self.boardstate[self.King[1]][self.King[0]], self.King[0], self.King[1], self)
		if len(self.moves)!=0:
			self.moves.clear()
			return 0
		heur=-self.turn-(self.reverse-self.turn*self.reverse)
		for i in range(heur%7-heur,(-heur)%7+2*heur,heur):
			for j in range(8):
				if self.boardstate[i][j]*self.turn>0:
					self.select=(j,i)
					piece.getmove(self.boardstate[i][j], j, i, self)
					self.select=None
					if len(self.moves)!=0:
						self.moves.clear()
						return 0
		return 1
	def updateresult(self):
		if self.isn_at(self.King[0],self.King[1])==0:
			k=0
		else:
			k=1
		# K poslednímu tahu v pgn notaci přidá značku matu nebo šachu. Toto je zde, proto, že zbytek tahu se generuje před jeho zahráním, aby se mohlo odhalit braní figur.
		# zjistí zda se nezměnil výsledek hry, mat je detekován jako pat, kdy je král pod útokem, ještě je možnost se vzdát a nebo domluvit na remíze to tato funkce neřeší.
		if self.result==None:
			if self.trystalemate():
				if k:
					self.result=0
					self.resultstring="Draw by stalemate"
				else:
					self.result=self.turn*-1
					if self.result==1:
						self.resultstring="White won by checkmate"
					else:
						self.resultstring="Black won by checkmate"
			else:
				# tato forma remízy nastane, kdy 50 tahů není posunuto pěšcem a není sebrána figura
				if self.fiftydraw>=100:
					self.result=0
					self.resultstring="Draw by 50 move rule"
				elif self.Threefold():
					self.result=0
					self.resultstring="Draw by threefold repetition"
				elif self.Dead_position():
					self.result=0
					self.resultstring="Draw by insufficient material"
		if k==0:
			if self.result!=None and abs(self.result)==1:
				self.pgn[-1]+="#"
			else:
				self.pgn[-1]+="+"
	def Import(self):
		# funkce se pokusí importovat šachovou hru a předá ji funkci v lepší podobě popřípadě nahlásí chybu
		if len(self.text.split("."))==2:
			pass
		elif len(self.text.split("."))==1:
			self.text=self.text+".txt"
		else:
			self.text="Invalid format"
			return
		try:
			with open(self.text,"r") as f:
				try:
					while 1:
						g=f.readline()
						if g[0]=="1":
							break
				except EOFError:
					pass
				g=g+f.read()
				g=g.strip().split()
				self.generatenew()
				piece.Playout(g,self)
		except:
			self.text="file not found"
			if self.resultstring=="Who knows its all wrong":
				self.text="Invalid game"
	def Export(self):
		# Načte jméno souboru, který bud vytvoří nebo do nějž zapíše
		if len(self.text.split("."))==2:
			pass
		elif len(self.text.split("."))==1:
			self.text=self.text+".txt"
		else:
			self.text="Invalid format"
			return
		f=open(self.text,"w")
		if self.result==None:
			result="*"
		elif self.result==0:
			result="1/2-1/2"
		elif self.result==1:
			result="1-0"
		else:
			result="0-1"
		f.write("[Event \"Zapoctovy program test hra\"]\n[Site \"https://github.com/kubaneko/chess_zap\"]\n[Date \"??\"]\n[White \"Player 1\"]\n[Black \"Player 2\"]\n[Result \""+result+"\"]\n\n")
		# Zapíše povinný úvod ten jsem zvolil spíše okrasně až na výsledek hry
		i=1
		for j in range(len(self.pgn)-1):
			if self.pgn[j][0]=="P":
				self.pgn[j]=self.pgn[j][1:]
		for j in range(0,len(self.pgn),2):
			if j+1<len(self.pgn):
				b=self.pgn[j+1]+" " 
			else:
				b=""
			f.write(str(i)+". "+self.pgn[j]+"   "+b)
			i+=1
			if i%7==0:
				f.write("\n")
		if result!="*":
			f.write(result)
		f.close()
		# Zapíše tahy převedené do pgn notace z self.pgn podle formátu.

