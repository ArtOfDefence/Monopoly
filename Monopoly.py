from colorama import init
from termcolor import colored
from random import randint
init()
import time
def slow():
    time.sleep(0.03)
def text():
    time.sleep(0.9)
Uzice = [" ", " ", " ", " "," ",25,5,"Uzice"]
Bingo1 = [" ", " ", " ", " ","B",50,0,"Bingo I"]
Loznica = [" ", " ", " ", " "," ",35,10,"Loznica"]
PorezNaPrihod = [" ", " ", " ", " ","N",100,0,"Porez Na Prihod"]
PrvaStanica = [" ", " ", " ", " "," ",100,25,"Prva Stanica"]
SremskaMitrovica = [" ", " ", " ", " "," ",50,15,"Sremska Mitrovica"]
Loto1 = [" ", " ", " ", " ","L",100,0,"Loto I"]
Vranje = [" ", " ", " ", " "," ",55,17,"Vranje"]
Sombor = [" ", " ", " ", " "," ",60,20,"Sombor"]
PosetaZatvoru = [" "," "," "," ","K",0,0,"Poseta Zatvoru"]
Prizren = [" ", " ", " ", " "," ",75,30,"Prizren"]
ElektroSrbije = [" ", " ", " ", " "," ",250,90,"Elektroprivreda Srbije"]
Valjevo = [" ", " ", " ", " "," ",80,32,"Valjevo"]
NoviPazar = [" ", " ", " ", " "," ",85,35,"Novi Pazar"]
DrugaStanica = [" ", " ", " ", " "," ",250,90,"Druga Stanica"]
Smederevo = [" ", " ", " ", " "," ",100,40,"Smederevo"]
Bingo2 = [" ", " ", " ", " ","B",50,0,"Bingo II"]
Cacak = [" ", " ", " ", " "," ",150,50,"Cacak"]
Sabac = [" ", " ", " ", " "," ",175,55,"Sabac"]
BesplatanParking = [" ", " ", " ", " ","K",0,0,"Besplatan Parking"]
Zrenjanin = [" ", " ", " ", " "," ",200,70,"Zrenjanin"]
Loto2 = [" ", " ", " ", " ","L",100,0,"Loto II"]
Pancevo = [" ", " ", " ", " "," ",250,90,"Pancevo"]
Kraljevo = [" ", " ", " ", " "," ",300,100,"Kraljevo"]
TrecaStanica = [" ", " ", " ", " "," ",500,125,"Treca Stanica"]
Krusevac = [" ", " ", " ", " "," ",400,110,"Krusevac"]
Subotica = [" ", " ", " ", " "," ",450,115,"Subotica"]
NaftnSrbije = [" ", " ", " ", " "," ",750,125,"Naftna Industrija Srbije"]
Leskovac = [" ", " ", " ", " "," ",500,120,"Leskovac"]
OdlazakUZatvor = [" ", " ", " ", " ","J",0,0,"Odlazak U Zatvor"]
Pristina = [" ", " ", " ", " "," ",750,125,"Pristina"]
Kragujevac = [" ", " ", " ", " "," ",800,130,"Kragujevac"]
Bingo3 = [" ", " ", " ", " ","B",50,0,"Bingo III"]
Nis = [" ", " ", " ", " "," ",850,135,"Nis"]
CetvrtaStanica = [" ", " ", " ", " "," ",750,125,"Cetvrta Stanica"]
Loto3 = [" ", " ", " ", " ","L",100,0,"Loto III"]
NoviSad = [" ", " ", " ", " "," ",1000,150,"Novi Sad"]
PorezNaLuksuz = [" ", " ", " ", " ","N",250,0,"Porez Na luksuz"]
Beograd = [" ", " ", " ", " "," ",1250,175,"Beograd"]
Pocetak=[colored("X", "red"), colored("X", "blue"),colored("X", "green"),colored("X", "yellow"),"K",0,0,"Pocetak"]
Mesta=[Pocetak,Uzice,Bingo1,Loznica,PorezNaPrihod,PrvaStanica,SremskaMitrovica,Loto1,Vranje,Sombor,PosetaZatvoru,Prizren,ElektroSrbije,Valjevo,NoviPazar,DrugaStanica,Smederevo,Bingo2,Cacak,Sabac,BesplatanParking,Zrenjanin,Loto2,Pancevo,Kraljevo,TrecaStanica,Krusevac,Subotica,NaftnSrbije,Leskovac,OdlazakUZatvor,Pristina,Kragujevac,Bingo3,Nis,CetvrtaStanica,Loto3,NoviSad,PorezNaLuksuz,Beograd]
Zone=[[Uzice,Loznica],[SremskaMitrovica,Vranje,Sombor],[Prizren,Valjevo,NoviPazar],[Smederevo,Cacak,Sabac],[Zrenjanin,Pancevo,Kraljevo],[Krusevac,Subotica,Leskovac],[Pristina,Kragujevac,Nis],[NoviSad,Beograd],[PrvaStanica,DrugaStanica,TrecaStanica,CetvrtaStanica],[ElektroSrbije,NaftnSrbije]]
class Player():
    def __init__(self, name, playercolor, coloredname, money=2000, locations=[Pocetak], position=0, dice1=0,dice2=0,loste=0,wone=0,j=0):
        self.property=[]
        self.name = name
        self.playercolor = playercolor
        self.coloredname = coloredname
        self.money = money
        self.figure = colored("X", playercolor)
        self.owner = colored("$",playercolor)
        self.locations = locations
        self.position=position
        self.dice1=dice1
        self.dice2=dice2
        self.loste=loste
        self.wone=wone
        self.j=j
    def append(self, x):
        self.property.append(x)
    def remove(self,x):
        self.property.remove(x)
    def removeall(self):
        self.property=[]
    def lost(self):
        self.money -= self.loste
    def won(self):
        self.money+= self.wone
    def current_money(self):
        text()
        print("You currently have ", self.money, " RSD on your account.")
    def current_properties(self):
        text()
        print("You currently own ", self.property, ".")
    def roll(self):
        self.dice1=randint(1,6)
        self.dice2=randint(1,6)
        text()
        print("First dice rolled at ",self.dice1, ".")
        text()
        print("Second dice rolled at ", self.dice2, ".")
    def work(self):
        if Mesta[self.position][4] == "L":
            self.wone = Mesta[self.position][5]
            self.won()
            text()
            print("You won a lottery, your award is ", Mesta[self.position][5], " RSD.")
            self.current_money()
        if Mesta[self.position][4] == "B":
            self.wone = Mesta[self.position][5]
            self.won()
            text()
            print("You won a Bingo, your award is ", Mesta[self.position][5], " RSD.")
            self.current_money()
        if Mesta[self.position][4] == "N":
            self.loste = Mesta[self.position][5]
            self.lost()
            text()
            print("You paid a ", Mesta[self.position][5], " RSD in taxes.")
            self.current_money()
        if Mesta[self.position][4] != self.owner:
            for x in Igraci:
                if Mesta[self.position][4] == x.owner:
                    self.loste = Mesta[self.position][6]
                    self.lost()
                    x.wone = Mesta[self.position][6]
                    x.won()
                    text()
                    print(Mesta[self.position][7], " is owned by ", x.coloredname,".")
                    text()
                    print(self.coloredname, " paid ", x.wone, " RSD in rent to ", x.coloredname, ".")
                    self.current_money()
                    text()
                    print(x.coloredname, " currently has ", x.money, " RSD on his/her account.")
    def action(self):
        self.position=self.position+self.dice1+self.dice2
        if self.position<=39:
            text()
            print("You landed on", Mesta[self.position][7], ".")
            self.work()
        if self.position>39:
            self.position=self.position-40
            text()
            print("You landed on", Mesta[self.position][7], ".")
            text()
            print(self.coloredname ," made a full circle,"  ,self.coloredname," gets 50 RSD bonus.")
            self.money+=50
            self.current_money()
            self.work()
    def place(self):
        self.locations=[self.locations[-1],Mesta[self.position]]
        if self.locations[-1][0]==" ":
            self.locations[-1][0]=self.figure
        elif self.locations[-1][1]==" ":
            self.locations[-1][1]=self.figure
        elif self.locations[-1][2]==" ":
            self.locations[-1][2]=self.figure
        elif self.locations[-1][3]==" ":
            self.locations[-1][3]=self.figure
    def clear(self):
        if self.locations[-2][0]==self.figure:
            self.locations[-2][0]=self.locations[-2][1]
            self.locations[-2][1]=self.locations[-2][2]
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
            f1()
        elif self.locations[-2][1]==self.figure:
            self.locations[-2][1]=self.locations[-2][2]
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
            f1()
        elif self.locations[-2][2]==self.figure:
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
            f1()
        elif self.locations[-2][3]==self.figure:
            self.locations[-2][3]=" "
            f1()
    def bonus(self):
        if self.locations[-1][4]=="J":
            self.j=1
            text()
            print("You are going to the jail.")
            self.position=10
            self.place()
            self.clear()
        elif self.locations[-1][4]==" ":
            text()
            print("The price of ", Mesta[self.position][7], " is", Mesta[self.position][5], "RSD.")
            self.current_money()
            text()
            print("Would you like to buy ", self.locations[-1][7], "? Please answer with Yes or No, if you choose No, the place will go for an auction.")
            tr=input()
            if tr=="Yes":
                self.loste=self.locations[-1][5]
                self.lost()
                self.locations[-1][4]=self.owner
                text()
                print(self.coloredname," bought ", self.locations[-1][7], "for ",self.locations[-1][5]," RSD.")
                self.current_money()
                self.append(self.locations[-1][7])
                self.current_properties()
                f1()
            if tr=="No":
                text()
                print("The auction starts...")
                tt=""
                m4=0
                won=""
                while tt!="No":
                    for x in Igraci:
                      if x.money >= 0:
                        text()
                        print("How much does ", x.coloredname, " offers this round for ", self.locations[-1][7], "? Please enter the number.")
                        k=int(input())
                        if k >m4:
                            won=x
                            m4=k
                    text()
                    print("Would you like to go for another round of an auction, if not the winner will be announced, please enter Yes or No.")
                    tt=input()
                text()
                print("The winner of this auction is ", won.coloredname, "he/she bought ", self.locations[-1][7], "for ", m4, "RSD .")
                won.append(self.locations[-1][7])
                won.money-=m4
                self.locations[-1][4]=won.owner
                text()
                print(won.coloredname, " currently has ", won.money, " RSD on his/her account.")
                text()
                print(won.coloredname, " currently owns ", won.property, ".")
                f1()
    def trade(self):
        text()
        print("Would you like to trade with someone? Please answer with Yes or No.")
        mm=input()
        if mm == "Yes":
            text()
            print("Please enter the name of the player you would like to trade with.")
            mn=input()
            for t in Igraci:
                if mn == t.name:
                    text()
                    print("What would you like to trade to ", t.coloredname, "? Please enter Money or Place.")
                    mm=input()
                    if mm=="Money":
                        self.current_money()
                        text()
                        print(t.coloredname, " currently has", t.money, " RSD on his/her balance.")
                        text()
                        print("How much money do you wish to give to ", t.coloredname, " ? Please enter a number.")
                        mm = int(input())
                        self.money -= mm
                        t.money += mm
                        text()
                        print("You gave", mm, " RSD to ", t.coloredname, ".")
                        self.current_money()
                        text()
                        print(t.coloredname, " currently has", t.money, " RSD on his/her account.")
                    if mm=="Place":
                        self.current_properties()
                        text()
                        print(t.coloredname, " currently owns ", t.property, ".")
                        text()
                        print("Please enter the name of the place you would like to give to ",t.coloredname, ".")
                        mm=input()
                        for x in Mesta:
                            if x[7] == mm:
                                self.remove(x[7])
                                t.append(x[7])
                                x[4]=t.owner
                                text()
                                print(t.coloredname, " received ", x[7], "from ", self.coloredname)
                                self.current_properties()
                                text()
                                print(t.coloredname, " currently owns ", t.property, ".")
                                f1()
                    text()
                    print("Would you like to trade another thing to ", t.coloredname, " ? Please answer with Yes or No.")
                    u=input()
                    while u!="No":
                        text()
                        print("What would you like to trade to ", t.coloredname, " ,please enter Money or Place.")
                        mm = input()
                        if mm == "Money":
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has", t.money, " RSD on his/her account.")
                            text()
                            print("How much money do you wish to give to ", t.coloredname, " ? Please enter a number.")
                            mm = int(input())
                            self.money -= mm
                            t.money += mm
                            text()
                            print("You gave", mm, " RSD to ", t.coloredname, ".")
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has", t.money, " RSD on his/her account.")
                        if mm == "Place":
                            self.current_properties()
                            text()
                            print(t.coloredname, " currently owns ", t.property, ".")
                            text()
                            print("Please enter the name of the place you would like to give to ", t.coloredname, ".")
                            mm = input()
                            for x in Mesta:
                                if x[7] == mm:
                                    self.remove(x[7])
                                    t.append(x[7])
                                    x[4] = t.owner
                                    text()
                                    print(t.coloredname, " received ", x[7], "from ", self.coloredname, ".")
                                    self.current_properties()
                                    text()
                                    print(t.coloredname, " currently owns ", t.property, ".")
                                    f1()
                    if u=="No":
                        text()
                        print("What would you like to receive from ", t.coloredname, " ? Please enter Money or Place.")
                        mm = input()
                        if mm == "Money":
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has ", t.money, " on his account.")
                            text()
                            print("How much money do you wish to receive from ", t.coloredname, "? Please enter a number.")
                            mm = int(input())
                            self.money += mm
                            t.money -= mm
                            text()
                            print(self.coloredname, " received ", mm, " RSD from", t.coloredname, "." )
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has", t.money, " RSD on his/her account.")
                        if mm == "Place":
                            self.current_properties()
                            text()
                            print(t.coloredname, " currently owns ", t.property, ".")
                            text()
                            print("Please enter the name of the place you would like to receive from ", t.coloredname)
                            mm = input()
                            for x in Mesta:
                                if x[7] == mm:
                                    self.append(x[7])
                                    t.remove(x[7])
                                    x[4] = self.owner
                                    text()
                                    print(self.coloredname, " received ", x[7], "from ", t.coloredname)
                                    self.current_properties()
                                    text()
                                    print(t.coloredname, " currently owns ", t.property, ".")
                                    f1()
                        text()
                        print("Would you like to receive another thing from ", t.coloredname, "? Please answer with Yes or No.")
                        u = input()
                        while u != "No":
                            if mn == t.name:
                                text()
                                print("What would you like to receive from ", t.coloredname, " ? Please enter Money or Place.")
                                mm = input()
                                if mm == "Money":
                                    self.current_money()
                                    text()
                                    print(t.coloredname, " currently has ", t.money, " on his account.")
                                    text()
                                    print("How much money do you wish to receive from ", t.coloredname,"? Please enter a number.")
                                    mm = int(input())
                                    self.money += mm
                                    t.money -= mm
                                    text()
                                    print(self.coloredname, " received ", mm, " RSD from", t.coloredname, ".")
                                    self.current_money()
                                    text()
                                    print(t.coloredname, " currently has", t.money, " RSD on his/her account.")
                                if mm == "Place":
                                    self.current_properties()
                                    text()
                                    print(t.coloredname, " currently owns ", t.property, ".")
                                    text()
                                    print("Please enter the name of the place you would like to receive from ",t.coloredname)
                                    mm = input()
                                    for x in Mesta:
                                        if x[7] == mm:
                                            self.append(x[7])
                                            t.remove(x[7])
                                            x[4] = self.owner
                                            text()
                                            print(self.coloredname, " received ", x[7], "from ", t.coloredname)
                                            self.current_properties()
                                            text()
                                            print(t.coloredname, " currently owns ", t.property, ".")
                                            f1()
                                text()
                                print("Would you like to receive another thing from ", t.coloredname,"? Please answer with Yes or No.")
                                u = input()
        else:
            text()
            print("You decided not to trade with anyone.")
    def invest(self):
        tray=0
        for k in Zone:
            if self.locations[-1] in k:
                for n in k:
                    if n[7] in self.property:
                        tray+=1
                if tray == len(k):
                    if self.locations[-1][4]==self.owner:
                        text()
                        print("Would you like to invest in ",self.locations[-1][7], ", if you invest,the rent of place that you invested in will raise for 10 percent of your investment, please answer with Yes or No.")
                        io=input()
                        if io=="Yes":
                            self.current_money()
                            text()
                            print("How much would you like to invest in ", self.locations[-1][7], ", please enter the number that ends with zero, for example 250.")
                            investment=int(input())
                            self.money-=investment
                            self.locations[-1][6]+=int(investment/10)
                            text()
                            print(self.coloredname, "invested in ", self.locations[-1][7], investment, " RSD,  the rent of ", self.locations[-1][7] ,"raised for ", int(investment/10), "RSD, the rent of ", self.locations[-1][7], "is now ", int(self.locations[-1][6]), "RSD.")
                        else:
                            text()
                            print(self.coloredname, " decided not to invest in ", self.locations[-1][7] )
        if self.dice1 != self.dice2:
            text()
            print(self.coloredname, " ends his/her turn.")
    def bankrupt(self):
        if self.money<0:
            for x in Mesta:
                if x[4]==self.owner:
                    x[4]=" "
            for u in self.locations[-1]:
                if u==self.figure:
                    u=" "
            self.removeall()
            text()
            print(self.coloredname, " has bankrupted.")
            self.dice1=1
            self.dice2=2
            f1()
    def first_turn(self):
        if self.j == 1:
            text()
            print(self.coloredname, " is in jail this turn, he/she can't play.")
            self.j = 0
        else:
            if self.money > 0 and self.j != 1:
                text()
                print(self.coloredname, " is on the turn.")
                self.trade()
                text()
                input("Press ENTER to roll dices.")
                text()
                print(self.coloredname, " is now rolling dices.")
                self.roll()
                self.action()
                self.place()
                self.clear()
                self.bonus()
                self.invest()
                self.bankrupt()
    def second_turn(self):
        if self.dice1 == self.dice2:
            text()
            print(self.coloredname, " rolled doubles, he/she gets to play again.")
            if self.j == 1:
                text()
                print(print(self.coloredname, " is in jail this turn, he/she can't play."))
                self.j = 0
                self.dice1 = 1
                self.dice2 = 2
            else:
                if self.money > 0 and self.j != 1:
                    text()
                    print(self.coloredname, " is on the turn again.")
                    self.trade()
                    text()
                    input("Press ENTER to roll dices.")
                    text()
                    print(self.coloredname, " is now rolling dices.")
                    self.roll()
                    self.action()
                    self.place()
                    self.clear()
                    self.bonus()
                    time.sleep(1)
                    self.invest()
                    self.bankrupt()
                    time.sleep(3)
    def third_turn(self):
        if self.dice1 == self.dice2:
            text()
            print(self.coloredname, " rolled doubles for second time, he/she gets to play again.")
            if self.j == 1:
                text()
                print(print(self.coloredname, " is in jail this turn, he/she can't play."))
                self.j = 0
                self.dice1 = 1
                self.dice2 = 2
            else:
                if self.money > 0 and self.j != 1:
                    text()
                    print(self.coloredname, " is on the turn again.")
                    self.trade()
                    text()
                    input("Press ENTER to roll dices")
                    text()
                    print(self.coloredname, " is now rolling dices.")
                    self.roll()
                    if self.dice1 == self.dice2:
                        text()
                        print(self.coloredname, " rolled doubles for the third time, he/she is going to the jail.")
                        self.j = 1
                        self.position = 10
                        self.place()
                        self.clear()
                        self.dice1 = 1
                        self.dice2 = 2
                    else:
                        self.action()
                        self.place()
                        self.clear()
                        self.bonus()
                        self.invest()
                        self.bankrupt()
    def gameplay(self):
        self.first_turn()
        self.second_turn()
        self.third_turn()
def check_bankrupt():
    for x in Igraci:
        if x.money < 0:
            text()
            print(x.coloredname, " has bankrupted he/she can't play anymore")
def winner():
    tre=0
    tru=""
    for x in Igraci:
        if x.money > tre:
            tru=x.coloredname
    text()
    print("The winner of the game is", tru, "CONGRATULATIONS !!!")
text()
print("WELCOME TO THE GAME OF MONOPOLY")
print()
text()
print("Please enter the name of the first player.")
a1= input()
Player1 = Player(a1, "red", colored(a1,"red"))
text()
print("Please enter the name of the second player.")
a2=input()
Player2 = Player(a2, "blue", colored(a2,"blue"))
text()
print("Please enter the name of the third player.")
a3 = input()
Player3 = Player(a3, "green", colored(a3,"green"))
text()
print("Please enter the name of the fourth player.")
a4 = input()
Player4 = Player(a4, "yellow", colored(a4,"yellow"))
text()
print("Name of the first player is ", Player1.coloredname, " his/her figure will be of red color.")
text()
print("Name of the second player is ", Player2.coloredname, " his/her figure will be of blue color.")
text()
print("Name of the third player is ", Player3.coloredname, " his/her figure will be of green color.")
text()
print("Name of the fourth player is ", Player4.coloredname, " his/her figure will be of yellow color.")
Igraci=[Player1,Player2,Player3,Player4]
#Beograd[0:4] su pozicije,Beograd[4] je vlasnik, Beograd[5] je vrednost, Beograd[6] je porez, Beograd[7] je ime grada
def f1():
    time.sleep(3.5)
    print("\   BESPLATAN   "+BesplatanParking[0]+"  ZRENJANIN    "+Zrenjanin[0]+" LOTO II    "+Loto2[0]+"  PANCEVO    "+Pancevo[0]+"  KRALJEVO   "+Kraljevo[0]+"    TRECA    "+TrecaStanica[0]+"  KRUSEVAC   "+Krusevac[0]+"  SUBOTICA   "+Subotica[0]+"   NAFTN.    "+NaftnSrbije[0]+"  LESKOVAC   "+Leskovac[0]+"  ODLAZAK U  "+OdlazakUZatvor[0]+"  \  "+ "Balance : ")
    slow()
    print("\    PARKING    "+BesplatanParking[1]+"               "+Zrenjanin[1]+"            "+Loto2[1]+"             "+Pancevo[1]+"             "+Kraljevo[1]+"   STANICA   "+TrecaStanica[1]+"             "+Krusevac[1]+"             "+Subotica[1]+"   SRBIJE    "+NaftnSrbije[1]+"             "+Leskovac[1]+"    ZATVOR   "+OdlazakUZatvor[1]+"  \  "+ Player1.coloredname + " currently has " + str(Player1.money)+ " RSD.")
    slow()
    print("\               "+BesplatanParking[2]+"  200 RSD      "+Zrenjanin[2]+" +100 RSD   "+Loto2[2]+"  250 RSD    "+Pancevo[2]+"  300 RSD    "+Kraljevo[2]+"    500 RSD  "+TrecaStanica[2]+"  400 RSD    "+Krusevac[2]+"  450 RSD    "+Subotica[2]+"   750 RSD   "+NaftnSrbije[2]+"  500 RSD    "+Leskovac[2]+"             "+OdlazakUZatvor[2]+"  \  "+ Player2.coloredname + " currently has " + str(Player2.money)+ " RSD.")
    slow()
    print("\               "+BesplatanParking[3]+"               "+Zrenjanin[3]+"            "+Loto2[3]+"             "+Pancevo[3]+"             "+Kraljevo[3]+"             "+TrecaStanica[3]+"             "+Krusevac[3]+"             "+Subotica[3]+"             "+NaftnSrbije[3]+"             "+Leskovac[3]+"             "+OdlazakUZatvor[3]+"  \  "+ Player3.coloredname + " currently has " + str(Player3.money)+ " RSD.")
    slow()
    print("\                ",colored("             ","white","on_blue"),"              ",colored("           ","white","on_blue")," ",colored("           ","white","on_blue")," ",colored("            ","white","on_white"),"",colored("           ","white","on_green")," ",colored("           ","white","on_green")," ",colored("           ","white","on_white")," ",colored("           ","white","on_green"),"                 \  "+ Player4.coloredname + " currently has " + str(Player4.money)+ " RSD.")
    slow()
    print("\                       "+Zrenjanin[4]+"                           "+Pancevo[4]+"             "+Kraljevo[4]+"              "+TrecaStanica[4]+"            "+Krusevac[4]+"             " + Subotica[4]+"             "+NaftnSrbije[4]+"             "+Leskovac[4]+"                       \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\    SABAC   "+Sabac[0]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Pristina[0]+"  PRISTINA  \ ")
    slow()
    print("\            "+Sabac[1]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Pristina[1]+"            \ ")
    slow()
    print("\   175 RSD  "+Sabac[2]+"",colored("  ","white","on_cyan"),Sabac[4],"                                                                                                                        ",Pristina[4], colored("  ","white","on_yellow") ," "+Pristina[2]+"  750 RSD   \ ")
    slow()
    print("\            "+Sabac[3]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Pristina[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\    CACAK   "+Cacak[0]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Kragujevac[0]+" KRAGUJEVAC \ ")
    slow()
    print("\            "+Cacak[1]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Kragujevac[1]+"            \ ")
    slow()
    print("\   150 RSD  "+Cacak[2]+"",colored("  ","white","on_cyan"),Cacak[4],"                                                                                                                        ",Kragujevac[4], colored("  ","white","on_yellow") ," "+Kragujevac[2]+"  800 RSD   \ ")
    slow()
    print("\            "+Cacak[3]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Kragujevac[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\  BINGO II  "+Bingo2[0]+"                                                                                                                                     "+Bingo3[0]+"  BINGO III \ ")
    slow()
    print("\            "+Bingo2[1]+"                                                                                                                                     "+Bingo3[1]+"            \ ")
    slow()
    print("\  +50 RSD   "+Bingo2[2]+"                                                                                                                                     "+Bingo3[2]+"  +50 RSD   \ ")
    slow()
    print("\            "+Bingo2[3]+"                                                                                                                                     "+Bingo3[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\  SMEDEREVO "+Smederevo[0]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Nis[0]+"    NIS     \ ")
    slow()
    print("\            "+Smederevo[1]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Nis[1]+"            \ ")
    slow()
    print("\   100 RSD  "+Smederevo[2]+"",colored("  ","white","on_cyan"),Smederevo[4],"                                                                                                                        ",Nis[4], colored("  ","white","on_yellow") ," "+Nis[2]+"  850 RSD   \ ")
    slow()
    print("\            "+Smederevo[3]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Nis[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\    DRUGA   "+DrugaStanica[0]+"",colored("  ","white","on_white"),"                                                                                                                            ",colored("  ","white","on_white")," "+CetvrtaStanica[0]+"  CETVRTA   \ ")
    slow()
    print("\   STANICA  "+DrugaStanica[1]+"",colored("  ","white","on_white"),"                                                                                                                            ",colored("  ","white","on_white")," "+CetvrtaStanica[1]+"  STANICA   \ ")
    slow()
    print("\   250 RSD  "+DrugaStanica[2]+"",colored("  ","white","on_white"),DrugaStanica[4],"                                                                                                                        ",CetvrtaStanica[4],colored("  ","white","on_white")," "+CetvrtaStanica[2]+"  750 RSD   \ ")
    slow()
    print("\            "+DrugaStanica[3]+"",colored("  ","white","on_white"),"                                                                                                                            ",colored("  ","white","on_white")," "+CetvrtaStanica[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\    NOVI    "+NoviPazar[0]+"",colored("  ","white","on_yellow"),"                                                                                                                                 "+Loto3[0]+"  LOTO III  \ ")
    slow()
    print("\    PAZAR   "+NoviPazar[1]+"",colored("  ","white","on_yellow"),"                                                                                                                                 "+Loto3[1]+"            \ ")
    slow()
    print("\    85 RSD  "+NoviPazar[2]+"",colored("  ","white","on_yellow"),NoviPazar[4],"                                                                                                                               "+Loto3[2]+"  +100 RSD  \ ")
    slow()
    print("\            "+NoviPazar[3]+"",colored("  ","white","on_yellow"),"                                                                                                                                 "+Loto3[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\   VALJEVO  "+Valjevo[0]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+NoviSad[0]+"    NOVI     \ ")
    slow()
    print("\            "+Valjevo[1]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+NoviSad[1]+"    SAD      \ ")
    slow()
    print("\   80 RSD   "+Valjevo[2]+"",colored("  ","white","on_yellow"),Valjevo[4],"                                                                                                                        ",NoviSad[4], colored("  ","white","on_red") ,""+NoviSad[2]+"  1000 RSD   \ ")
    slow()
    print("\            "+Valjevo[3]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+NoviSad[3]+"             \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\   ELEKTRO. "+ElektroSrbije[0]+"",colored("  ","white","on_white"),"                                                                                                                                 "+PorezNaLuksuz[0]+"  POREZ NA  \ ")
    slow()
    print("\   SRBIJE   "+ElektroSrbije[1]+"",colored("  ","white","on_white"),"                                                                                                                                 "+PorezNaLuksuz[1]+"  LUKSUZ    \ ")
    slow()
    print("\   250 RSD  "+ElektroSrbije[2]+"",colored("  ","white","on_white"),ElektroSrbije[4],"                                                                                                                               "+PorezNaLuksuz[2]+"  -200 RSD  \ ")
    slow()
    print("\            "+ElektroSrbije[3]+"",colored("  ","white","on_white"),"                                                                                                                                 "+PorezNaLuksuz[3]+"            \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\   PRIZREN  "+Prizren[0]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+Beograd[0]+"   BEOGRAD   \ ")
    slow()
    print("\            "+Prizren[1]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+Beograd[1]+"             \ ")
    slow()
    print("\   75 RSD   "+Prizren[2]+"",colored("  ","white","on_yellow"),Prizren[4],"                                                                                                                        ",Beograd[4], colored("  ","white","on_red") ,""+Beograd[2]+"   1250 RSD  \ ")
    slow()
    print("\            "+Prizren[3]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+Beograd[3]+"             \ ")
    slow()
    print("\                                                                                                                                                               \ ")
    slow()
    print("\                       "+Sombor[4]+"             "+Vranje[4]+"                           "+SremskaMitrovica[4]+"              "+PrvaStanica[4]+"                           "+Loznica[4]+"                           " + Uzice[4]+"                      \ ")
    slow()
    print("\                ",colored("            ","white","on_magenta")," ",colored("           ","white","on_magenta"),"               ",colored("           ","white","on_magenta"),"  ",colored("           ","white","on_white"),"              ",colored("            ","white","on_blue"),"               ",colored("           ","white","on_blue"),"                \ ")
    slow()
    print("\  "+PosetaZatvoru[0]+"   POSETA    "+Sombor[0]+"   SOMBOR     "+Vranje[0]+"   VRANJE    "+Loto1[0]+"  LOTO I     "+SremskaMitrovica[0]+"  SREMSKA    "+PrvaStanica[0]+"    PRVA     "+PorezNaPrihod[0]+"  POREZ NA   "+Loznica[0]+"   LOZNICA    "+Bingo1[0]+"  BINGO I    "+Uzice[0]+"   UZICE     "+Pocetak[0]+"   POCETAK    \ ")
    slow()
    print("\  "+PosetaZatvoru[1]+"   ZATVORU   "+Sombor[1]+"              "+Vranje[1]+"             "+Loto1[1]+"             "+SremskaMitrovica[1]+" MITROVICA   "+PrvaStanica[1]+"   STANICA   "+PorezNaPrihod[1]+"   PRIHOD    "+Loznica[1]+"              "+Bingo1[1]+"             "+Uzice[1]+"             "+Pocetak[1]+"              \ ")
    slow()
    print("\  "+PosetaZatvoru[2]+"             "+Sombor[2]+"   60 RSD     "+Vranje[2]+"   55 RSD    "+Loto1[2]+"  +100 RSD   "+SremskaMitrovica[2]+"   50 RSD    "+PrvaStanica[2]+"   100 RSD   "+PorezNaPrihod[2]+"  -100 RSD   "+Loznica[2]+"   35 RSD     "+Bingo1[2]+"  +50 RSD    "+Uzice[2]+"   25 RSD    "+Pocetak[2]+"              \ ")
    slow()
    print("\  "+PosetaZatvoru[3]+"             "+Sombor[3]+"              "+Vranje[3]+"             "+Loto1[3]+"             "+SremskaMitrovica[3]+"             "+PrvaStanica[3]+"             "+PorezNaPrihod[3]+"             "+Loznica[3]+"              "+Bingo1[3]+"             "+Uzice[3]+"             "+Pocetak[3]+"              \ ")
f1()
ios = 1
def endgame():
    if (Player1.money<0 and Player2.money<0 and Player3.money<0 and Player4.money > 0) or (Player1.money<0 and Player2.money<0 and Player4.money<0 and Player3.money > 0) or (Player1.money<0 and Player3.money<0 and Player4.money<0 and Player2.money > 0) or (Player3.money<0 and Player2.money<0 and Player4.money<0 and Player1.money > 0):
        global ios
        ios=0
while ios!=0:
    check_bankrupt()
    Player1.gameplay()
    endgame()
    Player2.gameplay()
    endgame()
    Player3.gameplay()
    endgame()
    Player4.gameplay()
    endgame()
winner()
text()
input("Press ENTER to exit.")
