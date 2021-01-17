from colorama import init
from termcolor import colored
from random import randint
init()
import time
time.sleep(2)
Uzice = [" ", " ", " ", " "," ",25,5,"Uzice"]
Bingo1 = [" ", " ", " ", " ","M",50,0,"Bingo"]
Loznica = [" ", " ", " ", " "," ",35,10,"Loznica"]
PorezNaPrihod = [" ", " ", " ", " ","N",100,0,"Porez Na Prihod"]
PrvaStanica = [" ", " ", " ", " "," ",100,25,"Prva Stanica"]
SremskaMitrovica = [" ", " ", " ", " "," ",50,15,"Sremska Mitrovica"]
Loto1 = [" ", " ", " ", " ","M",100,0,"Loto"]
Vranje = [" ", " ", " ", " "," ",55,17,"Vranje"]
Sombor = [" ", " ", " ", " "," ",60,20,"Sombor"]
PosetaZatvoru = [" "," "," "," ","K",0,0,"Poseta Zatvoru"]
Prizren = [" ", " ", " ", " "," ",75,30,"Prizren"]
ElektroSrbije = [" ", " ", " ", " "," ",250,90,"Elektroprivreda Srbije"]
Valjevo = [" ", " ", " ", " "," ",80,32,"Valjevo"]
NoviPazar = [" ", " ", " ", " "," ",85,35,"Novi Pazar"]
DrugaStanica = [" ", " ", " ", " "," ",250,90,"Druga Stanica"]
Smederevo = [" ", " ", " ", " "," ",100,40,"Smederevo"]
Bingo2 = [" ", " ", " ", " ","M",50,0,"Bingo"]
Cacak = [" ", " ", " ", " "," ",150,50,"Cacak"]
Sabac = [" ", " ", " ", " "," ",175,55,"Sabac"]
BesplatanParking = [" ", " ", " ", " ","K",0,0,"Besplatan Parking"]
Zrenjanin = [" ", " ", " ", " "," ",200,70,"Zrenjanin"]
Loto2 = [" ", " ", " ", " ","M",100,0,"Loto"]
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
Bingo3 = [" ", " ", " ", " ","M",50,0,"Bingo"]
Nis = [" ", " ", " ", " "," ",850,135,"Nis"]
CetvrtaStanica = [" ", " ", " ", " "," ",750,125,"Cetvrta Stanica"]
Loto3 = [" ", " ", " ", " ","M",100,0,"Loto"]
NoviSad = [" ", " ", " ", " "," ",1000,150,"Novi Sad"]
PorezNaLuksuz = [" ", " ", " ", " ","N",250,0,"Porez Na luksuz"]
Beograd = [" ", " ", " ", " "," ",1250,175,"Beograd"]
Pocetak=[colored("X", "red"), colored("X", "blue"),colored("X", "green"),colored("X", "yellow"),"M",0,0,"Pocetak"]
Mesta=[Pocetak,Uzice,Bingo1,Loznica,PorezNaPrihod,PrvaStanica,SremskaMitrovica,Loto1,Vranje,Sombor,PosetaZatvoru,Prizren,ElektroSrbije,Valjevo,NoviPazar,DrugaStanica,Smederevo,Bingo2,Cacak,Sabac,BesplatanParking,Zrenjanin,Loto2,Pancevo,Kraljevo,TrecaStanica,Krusevac,Subotica,NaftnSrbije,Leskovac,OdlazakUZatvor,Pristina,Kragujevac,Bingo3,Nis,CetvrtaStanica,Loto3,NoviSad,PorezNaLuksuz,Beograd]
class Player:
    def __init__(self, name, playercolor, money=2500, locations=[Pocetak], position=0, dice1=0,dice2=0,loste=0,wone=0,j=0):
        self.name = name
        self.playercolor = playercolor
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
    def lost(self):
        self.money -= self.loste
    def won(self):
        self.money+= self.wone
    def roll(self):
        self.dice1=randint(1,6)
        self.dice2=randint(1,6)
        time.sleep(1)
        print("First dice rolled at ",self.dice1)
        time.sleep(1)
        print("Second dice rolled at ", self.dice2)
        time.sleep(1)
    def action(self):
        self.position=self.position+self.dice1+self.dice2
        if self.position<=39:
            print(self.name, "landed on ", Mesta[self.position][7])
            if Mesta[self.position][4]==" ":
                time.sleep(1)
                print("Price of ",Mesta[self.position][7], " is", Mesta[self.position][5], "RSD")
                time.sleep(1)
        if self.position>39:
            self.position=self.position-40
            print(self.name ," made a circle,"  ,self.name," gets 50 RSD bonus")
            print(self.name, "landed on", Mesta[self.position][7])
            if Mesta[self.position][4]==" ":
                time.sleep(1)
                print("Price of ",Mesta[self.position][7], " is", Mesta[self.position][5], "RSD")
                time.sleep(1)
            self.money+=50
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
        elif self.locations[-2][1]==self.figure:
            self.locations[-2][1]=self.locations[-2][2]
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
        elif self.locations[-2][2]==self.figure:
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
        elif self.locations[-2][3]==self.figure:
            self.locations[-2][3]=" "
    def bonus(self):
        if self.locations[-1][4]=="M":
            self.wone=self.locations[-1][5]
            self.won()
            print(self.name, "won ",self.locations[-1][5], " RSD")
        elif self.locations[-1][4]=="J":
            self.j=1
            print(self.name, "is in jail.")
            self.position=10
            self.place()
            self.clear()
        elif self.locations[-1][4]=="N":
            self.loste=self.locations[-1][5]
            self.lost()
            print(self.name, "lost ",self.locations[-1][5], " RSD")
        elif self.locations[-1][4]=="K":
            return 0
        elif self.locations[-1][4]==" ":
            print("Does ", self.name, " want to buy ", self.locations[-1][7], "please answer with Yes or No, if you choose No, place will go to an auction")
            tr=input()
            if tr=="Yes":
                self.loste=self.locations[-1][5]
                self.lost()
                self.locations[-1][4]=self.owner
                print(self.name," bought ", self.locations[-1][7], "for ",self.locations[-1][5]," RSD")
            if tr=="No":
                print("The auction starts, if you have a winner, please type stop")
                tt=""
                while tt!="stop":
                    print("How much does ", Player1.name, " bid ")
                    k1=int(input())
                    print(Player1.name, " bids ", k1, " RSD")
                    print("How much does ", Player2.name, " bid ")
                    k2=int(input())
                    print(Player2.name, " bids ", k2, " RSD")
                    print("How much does ", Player3.name, " bid ")
                    k3=int(input())
                    print(Player3.name, " bids ", k3, " RSD")
                    print("How much does ", Player4.name, " bid ")
                    k4=int(input())
                    print(Player4.name, " bids ", k4, " RSD")
                    print("Would you like to go to another round of an auction, if not type stop")
                    tt=input()
                if max(k1,k2,k3,k4)==k1:
                    self.locations[-1][4]=Player1.owner
                    Player1.money-=k1
                    print(Player1.name, " won an auction and gets the ownership of ", self.locations[-1][7])
                if max(k1, k2, k3, k4) == k2:
                    self.locations[-1][4] = Player2.owner
                    Player2.money -= k2
                    print(Player2.name, " won an auction and gets the ownership of ", self.locations[-1][7])
                if max(k1, k2, k3, k4) == k3:
                    self.locations[-1][4] = Player3.owner
                    Player3.money -= k3
                    print(Player3.name, " won an auction and gets the ownership of ", self.locations[-1][7])
                if max(k1, k2, k3, k4) == k4:
                    self.locations[-1][4] = Player4.owner
                    Player4.money -= k4
                    print(Player4.name, " won an auction and gets the ownership of ", self.locations[-1][7])
            tt=""
            tr=""
        elif self.locations[-1][4]!=self.owner:
            self.loste=self.locations[-1][6]
            self.lost()
            if self.locations[-1][4]==Player1.owner:
                Player1.wone=self.locations[-1][6]
                Player1.won()
                print(self.name, " paid ", int(Player1.wone), " RSD in rent to ", Player1.name)
            if self.locations[-1][4]==Player2.owner:
                Player2.wone=self.locations[-1][6]
                Player2.won()
                print(self.name, " paid ", int(Player2.wone), " RSD in rent to ", Player2.name)
            if self.locations[-1][4]==Player3.owner:
                Player3.wone=self.locations[-1][6]
                Player3.won()
                print(self.name, " paid ", int(Player3.wone), " RSD in rent to ", Player3.name)
            if self.locations[-1][4]==Player4.owner:
                Player4.wone=self.locations[-1][6]
                Player4.won()
                print(self.name, " paid ", int(Player4.wone), " RSD in rent to ", Player4.name)
    def trade(self):
        print("Would ", self.name," like to trade with someone, please answer with Yes or No")
        mm=input()
        if mm == "Yes":
            print("Please enter the name of player you would like to trade with")
            mn=input()
            if mn == Player1.name:
                print("What would you like to trade to ", Player1.name, " ,please enter Money or Place")
                mm=input()
                if mm=="Money":
                    print("How much money do you wish to give to ", Player1.name, ", please enter a number")
                    mm=int(input())
                    self.money-=mm
                    Player1.money+=mm
                if mm=="Place":
                    print("Please enter the name of the place you would like to give to ",Player1.name)
                    mm=input()
                    for x in Mesta:
                        if x[7] == mm:
                            x[4]=Player1.owner
                print("Would you like to trade another thing to ", Player1.name, "please answer with Yes or No")
                u=input()
                while u!="No":
                    if mn == Player1.name:
                        print("What would you like to trade to ", Player1.name, " ,please enter Money or Place")
                        mm = input()
                        if mm == "Money":
                            print("How much money do you wish to give to ", Player1.name, ", please enter a number")
                            mm = int(input())
                            self.money -= mm
                            Player1.money += mm
                        if mm == "Place":
                            print("Please enter the name of the place you would like to give to ", Player1.name)
                            mm = input()
                            for x in Mesta:
                                if x[7] == mm:
                                    x[4] = Player1.owner
                        print("Would you like to trade another thing to ", Player1.name, "please answer with Yes or No")
                        u = input()
                if u=="No":
                    print("What would you like to receive from ", Player1.name, " ,please enter Money or Place")
                    mm = input()
                    if mm == "Money":
                        print("How much money do you wish to receive from ", Player1.name, ", please enter a number")
                        mm = int(input())
                        self.money += mm
                        Player1.money -= mm
                    if mm == "Place":
                        print("Please enter the name of the place you would like to receive from ", Player1.name)
                        mm = input()
                        for x in Mesta:
                            if x[7] == mm:
                                x[4] = self.owner
                    print("Would you like to receive another thing from ", Player1.name, "please answer with Yes or No")
                    u = input()
                    while u != "No":
                        if mn == Player1.name:
                            print("What would you like to receive from ", Player1.name, " ,please enter Money or Place")
                            mm = input()
                            if mm == "Money":
                                print("How much money do you wish to receive from ", Player1.name, ", please enter a number")
                                mm = int(input())
                                self.money += mm
                                Player1.money -= mm
                            if mm == "Place":
                                print("Please enter the name of the place you would like to receive from ", Player1.name)
                                mm = input()
                                for x in Mesta:
                                    if x[7] == mm:
                                        x[4] = self.owner
                            print("Would you like to receive another thing from ", Player1.name,
                                  "please answer with Yes or No")
                            u = input()
            if mn == Player2.name:
                print("What would you like to trade to ", Player2.name, " ,please enter Money or Place")
                mm = input()
                if mm == "Money":
                    print("How much money do you wish to give to ", Player2.name, ", please enter a number")
                    mm = int(input())
                    self.money -= mm
                    Player2.money += mm
                if mm == "Place":
                    print("Please enter the name of the place you would like to give to ", Player2.name)
                    mm = input()
                    for x in Mesta:
                        if x[7] == mm:
                            x[4] = Player2.owner
                print("Would you like to trade another thing to ", Player2.name, "please answer with Yes or No")
                u = input()
                while u != "No":
                    if mn == Player2.name:
                        print("What would you like to trade to ", Player2.name, " ,please enter Money or Place")
                        mm = input()
                        if mm == "Money":
                            print("How much money do you wish to give to ", Player2.name, ", please enter a number")
                            mm = int(input())
                            self.money -= mm
                            Player2.money += mm
                        if mm == "Place":
                            print("Please enter the name of the place you would like to give to ", Player2.name)
                            mm = input()
                            for x in Mesta:
                                if x[7] == mm:
                                    x[4] = Player2.owner
                        print("Would you like to trade another thing to ", Player2.name, "please answer with Yes or No")
                        u = input()
                if u == "No":
                    print("What would you like to receive from ", Player2.name, " ,please enter Money or Place")
                    mm = input()
                    if mm == "Money":
                        print("How much money do you wish to receive from ", Player2.name, ", please enter a number")
                        mm = int(input())
                        self.money += mm
                        Player2.money -= mm
                    if mm == "Place":
                        print("Please enter the name of the place you would like to receive from ", Player2.name)
                        mm = input()
                        for x in Mesta:
                            if x[7] == mm:
                                x[4] = self.owner
                    print("Would you like to receive another thing from ", Player2.name, "please answer with Yes or No")
                    u = input()
                    while u != "No":
                        if mn == Player2.name:
                            print("What would you like to receive from ", Player2.name, " ,please enter Money or Place")
                            mm = input()
                            if mm == "Money":
                                print("How much money do you wish to receive from ", Player2.name,", please enter a number")
                                mm = int(input())
                                self.money += mm
                                Player2.money -= mm
                            if mm == "Place":
                                print("Please enter the name of the place you would like to receive from ", Player2.name)
                                mm = input()
                                for x in Mesta:
                                    if x[7] == mm:
                                        x[4] = self.owner
                            print("Would you like to receive another thing from ", Player2.name,"please answer with Yes or No")
                            u = input()
            if mn == Player3.name:
                print("What would you like to trade to ", Player3.name, " ,please enter Money or Place")
                mm = input()
                if mm == "Money":
                    print("How much money do you wish to give to ", Player3.name, ", please enter a number")
                    mm = int(input())
                    self.money -= mm
                    Player3.money += mm
                if mm == "Place":
                    print("Please enter the name of the place you would like to give to ", Player3.name)
                    mm = input()
                    for x in Mesta:
                        if x[7] == mm:
                            x[4] = Player3.owner
                print("Would you like to trade another thing to ", Player3.name, "please answer with Yes or No")
                u = input()
                while u != "No":
                    if mn == Player3.name:
                        print("What would you like to trade to ", Player3.name, " ,please enter Money or Place")
                        mm = input()
                        if mm == "Money":
                            print("How much money do you wish to give to ", Player3.name, ", please enter a number")
                            mm = int(input())
                            self.money -= mm
                            Player2.money += mm
                        if mm == "Place":
                            print("Please enter the name of the place you would like to give to ", Player3.name)
                            mm = input()
                            for x in Mesta:
                                if x[7] == mm:
                                    x[4] = Player3.owner
                        print("Would you like to trade another thing to ", Player3.name, "please answer with Yes or No")
                        u = input()
                if u == "No":
                    print("What would you like to receive from ", Player3.name, " ,please enter Money or Place")
                    mm = input()
                    if mm == "Money":
                        print("How much money do you wish to receive from ", Player3.name, ", please enter a number")
                        mm = int(input())
                        self.money += mm
                        Player3.money -= mm
                    if mm == "Place":
                        print("Please enter the name of the place you would like to receive from ", Player3.name)
                        mm = input()
                        for x in Mesta:
                            if x[7] == mm:
                                x[4] = self.owner
                    print("Would you like to receive another thing from ", Player3.name, "please answer with Yes or No")
                    u = input()
                    while u != "No":
                        if mn == Player3.name:
                            print("What would you like to receive from ", Player3.name, " ,please enter Money or Place")
                            mm = input()
                            if mm == "Money":
                                print("How much money do you wish to receive from ", Player3.name,", please enter a number")
                                mm = int(input())
                                self.money += mm
                                Player3.money -= mm
                            if mm == "Place":
                                print("Please enter the name of the place you would like to receive from ", Player3.name)
                                mm = input()
                                for x in Mesta:
                                    if x[7] == mm:
                                        x[4] = self.owner
                            print("Would you like to receive another thing from ", Player3.name,"please answer with Yes or No")
                            u = input()
            if mn == Player4.name:
                print("What would you like to trade to ", Player4.name, " ,please enter Money or Place")
                mm = input()
                if mm == "Money":
                    print("How much money do you wish to give to ", Player4.name, ", please enter a number")
                    mm = int(input())
                    self.money -= mm
                    Player4.money += mm
                if mm == "Place":
                    print("Please enter the name of the place you would like to give to ", Player4.name)
                    mm = input()
                    for x in Mesta:
                        if x[7] == mm:
                            x[4] = Player4.owner
                print("Would you like to trade another thing to ", Player4.name, "please answer with Yes or No")
                u = input()
                while u != "No":
                    if mn == Player4.name:
                        print("What would you like to trade to ", Player4.name, " ,please enter Money or Place")
                        mm = input()
                        if mm == "Money":
                            print("How much money do you wish to give to ", Player4.name, ", please enter a number")
                            mm = int(input())
                            self.money -= mm
                            Player4.money += mm
                        if mm == "Place":
                            print("Please enter the name of the place you would like to give to ", Player4.name)
                            mm = input()
                            for x in Mesta:
                                if x[7] == mm:
                                    x[4] = Player4.owner
                        print("Would you like to trade another thing to ", Player4.name, "please answer with Yes or No")
                        u = input()
                if u == "No":
                    print("What would you like to receive from ", Player4.name, " ,please enter Money or Place")
                    mm = input()
                    if mm == "Money":
                        print("How much money do you wish to receive from ", Player4.name, ", please enter a number")
                        mm = int(input())
                        self.money += mm
                        Player4.money -= mm
                    if mm == "Place":
                        print("Please enter the name of the place you would like to receive from ", Player4.name)
                        mm = input()
                        for x in Mesta:
                            if x[7] == mm:
                                x[4] = self.owner
                    print("Would you like to receive another thing from ", Player4.name, "please answer with Yes or No")
                    u = input()
                    while u != "No":
                        if mn == Player4.name:
                            print("What would you like to receive from ", Player4.name, " ,please enter Money or Place")
                            mm = input()
                            if mm == "Money":
                                print("How much money do you wish to receive from ", Player4.name,", please enter a number")
                                mm = int(input())
                                self.money += mm
                                Player4.money -= mm
                            if mm == "Place":
                                print("Please enter the name of the place you would like to receive from ", Player4.name)
                                mm = input()
                                for x in Mesta:
                                    if x[7] == mm:
                                        x[4] = self.owner
                            print("Would you like to receive another thing from ", Player4.name,"please answer with Yes or No")
                            u = input()
        else:
            print(self.name, " decided not to trade with anyone")
    def invest(self):
        if self.locations[-1][4]==self.owner:
            print("Would ", self.name ," like to invest, if you invest,the rent of place that you invested in will raise for 10 percent of your investment, please answer with Yes or No.")
            io=input()
            if io=="Yes":
                print("How much would you like to invest in ", self.locations[-1][7])
                investment=int(input())
                self.money-=investment
                self.locations[-1][6]+=int(investment/10)
                print(self.name, "invested in ", self.locations[-1][7], investment, " RSD,  the rent of ", self.locations[-1][7] ,"raised for ", int(investment/10), "RSD, the rent of ", self.locations[-1][7], "is now ", int(self.locations[-1][6]), "RSD")
            else:
                print(self.name, " decided not to invest in ", self.locations[-1][7] )
    def bankrupt(self):
        if self.money<0:
            for x in Mesta:
                if x[4]==self.owner:
                    x[4]=" "
            print(self.name, " has bankrupted")
    def first_turn(self):
        print()
        if self.j == 1:
            print(print(self.name, " is in jail this turn, he/she can't play"))
            self.j = 0
        else:
            if self.money > 0 and self.j != 1:
                print("It's ", self.name, " turn")
                input("Press ENTER to roll dices")
                print(self.name, " is now rolling dices")
                self.roll()
                self.action()
                self.place()
                self.clear()
                self.bonus()
                time.sleep(1)
                self.trade()
                self.invest()
                self.bankrupt()
                time.sleep(3)
                f1()
    def second_turn(self):
        if self.dice1 == self.dice2:
            print(self.name, " rolled doubles, he/she gets to play again")
            if self.j == 1:
                print(print(self.name, " is in jail this turn, he/she can't play"))
                self.j = 0
                self.dice1 = 1
                self.dice2 = 2
            else:
                if self.money > 0 and self.j != 1:
                    print("It's ", self.name, " turn again")
                    input("Press ENTER to roll dices")
                    print(self.name, " is now rolling dices")
                    self.roll()
                    self.action()
                    self.place()
                    self.clear()
                    self.bonus()
                    time.sleep(1)
                    self.trade()
                    self.invest()
                    self.bankrupt()
                    time.sleep(3)
                    f1()
    def third_turn(self):
        if self.dice1 == self.dice2:
            print(self.name, " rolled doubles for second time, he/she gets to play again")
            if self.j == 1:
                print(print(self.name, " is in jail this turn, he/she can't play"))
                self.j = 0
                self.dice1 = 1
                self.dice2 = 2
            else:
                if self.money > 0 and self.j != 1:
                    print("It's ", self.name, " turn again")
                    input("Press ENTER to roll dices")
                    print(self.name, " is now rolling dices")
                    self.roll()
                    if self.dice1 == self.dice2:
                        print(self.name, " rolled doubles for third time, he/she goes to jail")
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
                        time.sleep(1)
                        self.trade()
                        self.invest()
                        self.bankrupt()
                        time.sleep(3)
                        f1()
    def gameplay(self):
        self.first_turn()
        self.second_turn()
        self.third_turn()
def check_bankrupt():
    if Player1.money < 0:
        print(Player1.name, " has bankrupted he/she can't play anymore")
    if Player2.money < 0:
        print(Player2.name, " has bankrupted he/she can't play anymore")
    if Player3.money < 0:
        print(Player3.name, " has bankrupted he/she can't play anymore")
    if Player4.money < 0:
        print(Player4.name, " has bankrupted he/she can't play anymore")
def winner():
    if max(Player1.money,Player2.money,Player3.money,Player4.money) == Player1.money:
        print("Congratulations ", Player1.name, " won the game")
    if max(Player1.money,Player2.money,Player3.money,Player4.money) == Player2.money:
        print("Congratulations ", Player2.name, " won the game")
    if max(Player1.money,Player2.money,Player3.money,Player4.money) == Player3.money:
        print("Congratulations ", Player3.name, " won the game")
    if max(Player1.money,Player2.money,Player3.money,Player4.money) == Player4.money:
        print("Congratulations ", Player4.name, " won the game")
print("WELCOME TO THE GAME OF MONOPOLY")
print()
Player1 = Player(input("Please enter the name of first player : "), "red")
print("Name of the first player is ", Player1.name, " his/her figure will be of red color")
Player2 = Player(input("Please enter the name of second player : "), "blue")
print("Name of the second player is ", Player2.name, " his/her figure will be of blue color")
Player3 = Player(input("Please enter the name of third player : "), "green")
print("Name of the third player is ", Player3.name, " his/her figure will be of green color")
Player4 = Player(input("Please enter the name of fourth player : "), "yellow")
print("Name of the fourth player is ", Player4.name, " his/her figure will be of yellow color")
#Beograd[4] je vlasnik, Beograd[5] je vrednost, Beograd[6] je porez, Beograd[7] je ime grada
def f1():
    print("\   BESPLATAN   "+BesplatanParking[0]+"  ZRENJANIN    "+Zrenjanin[0]+"    LOTO    "+Loto2[0]+"  PANCEVO    "+Pancevo[0]+"  KRALJEVO   "+Kraljevo[0]+"    TRECA    "+TrecaStanica[0]+"  KRUSEVAC   "+Krusevac[0]+"  SUBOTICA   "+Subotica[0]+"   NAFTN.    "+NaftnSrbije[0]+"  LESKOVAC   "+Leskovac[0]+"  ODLAZAK U  "+OdlazakUZatvor[0]+"  \  "+ "Balance : ")
    print("\    PARKING    "+BesplatanParking[1]+"               "+Zrenjanin[1]+"            "+Loto2[1]+"             "+Pancevo[1]+"             "+Kraljevo[1]+"   STANICA   "+TrecaStanica[1]+"             "+Krusevac[1]+"             "+Subotica[1]+"   SRBIJE    "+NaftnSrbije[1]+"             "+Leskovac[1]+"    ZATVOR   "+OdlazakUZatvor[1]+"  \  "+ Player1.name + " currently has " + str(Player1.money)+ " RSD.")
    print("\               "+BesplatanParking[2]+"  200 RSD      "+Zrenjanin[2]+"  +100 RSD  "+Loto2[2]+"  250 RSD    "+Pancevo[2]+"  300 RSD    "+Kraljevo[2]+"    500 RSD  "+TrecaStanica[2]+"  400 RSD    "+Krusevac[2]+"  450 RSD    "+Subotica[2]+"   750 RSD   "+NaftnSrbije[2]+"  500 RSD    "+Leskovac[2]+"             "+OdlazakUZatvor[2]+"  \  "+ Player2.name + " currently has " + str(Player2.money)+ " RSD.")
    print("\               "+BesplatanParking[3]+"               "+Zrenjanin[3]+"            "+Loto2[3]+"             "+Pancevo[3]+"             "+Kraljevo[3]+"             "+TrecaStanica[3]+"             "+Krusevac[3]+"             "+Subotica[3]+"             "+NaftnSrbije[3]+"             "+Leskovac[3]+"             "+OdlazakUZatvor[3]+"  \  "+ Player3.name + " currently has " + str(Player3.money)+ " RSD.")
    print("\                ",colored("             ","white","on_blue"),"              ",colored("           ","white","on_blue")," ",colored("           ","white","on_blue")," ",colored("            ","white","on_white"),"",colored("           ","white","on_green")," ",colored("           ","white","on_green")," ",colored("           ","white","on_white")," ",colored("           ","white","on_green"),"                 \  "+ Player4.name + " currently has " + str(Player4.money)+ " RSD.")
    print("\                       "+Zrenjanin[4]+"                           "+Pancevo[4]+"             "+Kraljevo[4]+"              "+TrecaStanica[4]+"            "+Krusevac[4]+"             " + Subotica[4]+"             "+NaftnSrbije[4]+"             "+Leskovac[4]+"                       \ ")
    print("\                                                                                                                                                               \ ")
    print("\    SABAC   "+Sabac[0]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Pristina[0]+"  PRISTINA  \ ")
    print("\            "+Sabac[1]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Pristina[1]+"            \ ")
    print("\   175 RSD  "+Sabac[2]+"",colored("  ","white","on_cyan"),Sabac[4],"                                                                                                                        ",Pristina[4], colored("  ","white","on_yellow") ," "+Pristina[2]+"  750 RSD   \ ")
    print("\            "+Sabac[3]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Pristina[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\    CACAK   "+Cacak[0]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Kragujevac[0]+" KRAGUJEVAC \ ")
    print("\            "+Cacak[1]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Kragujevac[1]+"            \ ")
    print("\   150 RSD  "+Cacak[2]+"",colored("  ","white","on_cyan"),Cacak[4],"                                                                                                                        ",Kragujevac[4], colored("  ","white","on_yellow") ," "+Kragujevac[2]+"  800 RSD   \ ")
    print("\            "+Cacak[3]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Kragujevac[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\    BINGO   "+Bingo2[0]+"                                                                                                                                     "+Bingo3[0]+"    BINGO   \ ")
    print("\            "+Bingo2[1]+"                                                                                                                                     "+Bingo3[1]+"            \ ")
    print("\   +50 RSD  "+Bingo2[2]+"                                                                                                                                     "+Bingo3[2]+"   +50 RSD  \ ")
    print("\            "+Bingo2[3]+"                                                                                                                                     "+Bingo3[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\  SMEDEREVO "+Smederevo[0]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Nis[0]+"    NIS     \ ")
    print("\            "+Smederevo[1]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Nis[1]+"            \ ")
    print("\   100 RSD  "+Smederevo[2]+"",colored("  ","white","on_cyan"),Smederevo[4],"                                                                                                                        ",Nis[4], colored("  ","white","on_yellow") ," "+Nis[2]+"  850 RSD   \ ")
    print("\            "+Smederevo[3]+"",colored("  ","white","on_cyan"),"                                                                                                                            ", colored("  ","white","on_yellow") ," "+Nis[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\    DRUGA   "+DrugaStanica[0]+"",colored("  ","white","on_white"),"                                                                                                                            ",colored("  ","white","on_white")," "+CetvrtaStanica[0]+"  CETVRTA   \ ")
    print("\   STANICA  "+DrugaStanica[1]+"",colored("  ","white","on_white"),"                                                                                                                            ",colored("  ","white","on_white")," "+CetvrtaStanica[1]+"  STANICA   \ ")
    print("\   250 RSD  "+DrugaStanica[2]+"",colored("  ","white","on_white"),DrugaStanica[4],"                                                                                                                        ",CetvrtaStanica[4],colored("  ","white","on_white")," "+CetvrtaStanica[2]+"  750 RSD   \ ")
    print("\            "+DrugaStanica[3]+"",colored("  ","white","on_white"),"                                                                                                                            ",colored("  ","white","on_white")," "+CetvrtaStanica[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\    NOVI    "+NoviPazar[0]+"",colored("  ","white","on_yellow"),"                                                                                                                                 "+Loto3[0]+"    LOTO    \ ")
    print("\    PAZAR   "+NoviPazar[1]+"",colored("  ","white","on_yellow"),"                                                                                                                                 "+Loto3[1]+"            \ ")
    print("\    85 RSD  "+NoviPazar[2]+"",colored("  ","white","on_yellow"),NoviPazar[4],"                                                                                                                               "+Loto3[2]+"  +100 RSD  \ ")
    print("\            "+NoviPazar[3]+"",colored("  ","white","on_yellow"),"                                                                                                                                 "+Loto3[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\   VALJEVO  "+Valjevo[0]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+NoviSad[0]+"    NOVI     \ ")
    print("\            "+Valjevo[1]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+NoviSad[1]+"    SAD      \ ")
    print("\   80 RSD   "+Valjevo[2]+"",colored("  ","white","on_yellow"),Valjevo[4],"                                                                                                                        ",NoviSad[4], colored("  ","white","on_red") ,""+NoviSad[2]+"  1000 RSD   \ ")
    print("\            "+Valjevo[3]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+NoviSad[3]+"             \ ")
    print("\                                                                                                                                                               \ ")
    print("\   ELEKTRO. "+ElektroSrbije[0]+"",colored("  ","white","on_white"),"                                                                                                                                 "+PorezNaLuksuz[0]+"  POREZ NA  \ ")
    print("\   SRBIJE   "+ElektroSrbije[1]+"",colored("  ","white","on_white"),"                                                                                                                                 "+PorezNaLuksuz[1]+"  LUKSUZ    \ ")
    print("\   250 RSD  "+ElektroSrbije[2]+"",colored("  ","white","on_white"),ElektroSrbije[4],"                                                                                                                               "+PorezNaLuksuz[2]+"  -200 RSD  \ ")
    print("\            "+ElektroSrbije[3]+"",colored("  ","white","on_white"),"                                                                                                                                 "+PorezNaLuksuz[3]+"            \ ")
    print("\                                                                                                                                                               \ ")
    print("\   PRIZREN  "+Prizren[0]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+Beograd[0]+"   BEOGRAD   \ ")
    print("\            "+Prizren[1]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+Beograd[1]+"             \ ")
    print("\   75 RSD   "+Prizren[2]+"",colored("  ","white","on_yellow"),Prizren[4],"                                                                                                                        ",Beograd[4], colored("  ","white","on_red") ,""+Beograd[2]+"   1250 RSD  \ ")
    print("\            "+Prizren[3]+"",colored("  ","white","on_yellow"),"                                                                                                                            ", colored("  ","white","on_red") ,""+Beograd[3]+"             \ ")
    print("\                                                                                                                                                               \ ")
    print("\                       "+Sombor[4]+"             "+Vranje[4]+"                           "+SremskaMitrovica[4]+"              "+PrvaStanica[4]+"                           "+Loznica[4]+"                           " + Uzice[4]+"                      \ ")
    print("\                ",colored("            ","white","on_magenta")," ",colored("           ","white","on_magenta"),"               ",colored("           ","white","on_magenta"),"  ",colored("           ","white","on_white"),"              ",colored("            ","white","on_blue"),"               ",colored("           ","white","on_blue"),"                \ ")
    print("\ "+PosetaZatvoru[0]+"    POSETA   "+Sombor[0]+"    SOMBOR    "+Vranje[0]+"    VRANJE   "+Loto1[0]+"     LOTO    "+SremskaMitrovica[0]+"   SREMSKA   "+PrvaStanica[0]+"      PRVA   "+PorezNaPrihod[0]+"  POREZ NA   "+Loznica[0]+"    LOZNICA   "+Bingo1[0]+"    BINGO    "+Uzice[0]+"    UZICE    "+Pocetak[0]+"    POCETAK    \ ")
    print("\ "+PosetaZatvoru[1]+"    ZATVORU  "+Sombor[1]+"              "+Vranje[1]+"             "+Loto1[1]+"             "+SremskaMitrovica[1]+"  MITROVICA  "+PrvaStanica[1]+"     STANICA "+PorezNaPrihod[1]+"   PRIHOD    "+Loznica[1]+"              "+Bingo1[1]+"             "+Uzice[1]+"             "+Pocetak[1]+"               \ ")
    print("\ "+PosetaZatvoru[2]+"             "+Sombor[2]+"    60 RSD    "+Vranje[2]+"    55 RSD   "+Loto1[2]+"   +100 RSD  "+SremskaMitrovica[2]+"    50 RSD   "+PrvaStanica[2]+"     100 RSD "+PorezNaPrihod[2]+"  -100 RSD   "+Loznica[2]+"    35 RSD    "+Bingo1[2]+"   +50 RSD   "+Uzice[2]+"    25 RSD   "+Pocetak[2]+"               \ ")
    print("\ "+PosetaZatvoru[3]+"             "+Sombor[3]+"              "+Vranje[3]+"             "+Loto1[3]+"             "+SremskaMitrovica[3]+"             "+PrvaStanica[3]+"             "+PorezNaPrihod[3]+"             "+Loznica[3]+"              "+Bingo1[3]+"             "+Uzice[3]+"             "+Pocetak[3]+"               \ ")
f1()
while True:
    check_bankrupt()
    Player1.gameplay()
    Player2.gameplay()
    Player3.gameplay()
    Player4.gameplay()
    if (Player1.money<0 and Player2.money<0 and Player3.money<0 and Player4.money > 0) or (Player1.money<0 and Player2.money<0 and Player4.money<0 and Player3.money > 0) or (Player1.money<0 and Player3.money<0 and Player4.money<0 and Player2.money > 0) or (Player3.money<0 and Player2.money<0 and Player4.money<0 and Player1.money > 0):
        break
winner()
input("Press ENTER to exit.")
