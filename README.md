# Zápočtový program pro Programování 1.
Jde o pygame zpracování šachů člověk proti člověku. Co se týče funkčnosti tak zvládne exportovat a importovat hry PGN notaci, otáčet šachovnici k aktuálnímu hráči, prohlížet aktuální partii a ukazovat schovávat možné tahy a zvolené pole.

Co se týče struktury programu program je rozdělen na 3 části main.py zpravuje hlavně input/output hráčů, soubor board.py řeší zaznamenávání stavu šachovnice, komunikaci s main a grafické znázornění, nakonec piece.py řeší pohyb figur a další logiku jako překlad do pgn a překlad z něho.

Program funguje přibližně takto: main dostane input ten předá board, ta ho předá piece ta ho zpracuje a aktualizuje stav board.

Podrobnosti jsou v programu jakožto komentáře.

Použité knihovny jsou pygame pro grafické rozhraní a input/output a numpy, který používám na zefektivnění uložení stavů šachovnic (deska.boarsstate je 8x8 8int array).

# Zdroje
Obrázky jsou ze zdrojů: https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent a https://commons.wikimedia.org/wiki/File:Chessboard480.png, nebyly změněny, zbytek jak by z kvality mělo být zřejmé je vlastní výroby v Malování.

# Licence
Toto dílo podléhá licenci Creative Commons Uveďte původ-Zachovejte licenci 3.0 Česká republika. Pro získání kopie plného znění licenčních podmínek navštivte http://creativecommons.org/licenses/by-sa/3.0/cz/ nebo požádejte písemně na adrese Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

