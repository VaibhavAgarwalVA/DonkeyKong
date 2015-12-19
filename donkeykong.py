from random import *
import sys
from time import sleep

BLACK=0
RED=1
GREEN=2
YELLOW=3
BLUE=4
MAGENTA=5
CYAN=6
WHITE=7

def printf(text,colour):
    seq="\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
    v=sys.stdout
    v.write(seq)


def getchar():

  	import tty, termios, sys
   	fd = sys.stdin.fileno()
  	old_settings = termios.tcgetattr(fd)
   	try:
      		tty.setraw(sys.stdin.fileno())
      		ch = sys.stdin.read(1)
   	finally:
      		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   	return ch


class Person():

    def __init(self):
        pass

    def getPosition(self):
        pass

    def move(self):
        pass

    def updatePositon(self):
        pass


class Player(Person):

    def __init__(self):
        self.__score=0
        self.__position=(20,1)
        self.__live=3
        self.__var=' '

    def setscore(self,x):
        self.__score=x

    def setlive(self,x):
        self.__live=x

    def getscore(self):
        return self.__score

    def finaldestination(self):
        if self.__position==(1,8):
            return 1
        else:
            return 0

    def incrementscore(self):
        self.__score=self.__score+5

    def hit(self):
        self.__score=self.__score-25
        b.set_board(self.__position[0],self.__position[1],' ')
        self.__position=(20,1)
        b.set_board(self.__position[0],self.__position[1],'P')
        self.__live=self.__live-1
        self.__var=' '

    def getlive(self):
        return self.__live

    def getPosition(self):
        return self.__position

    def CheckCollision(self):
        for fireball in F:
            if fireball.getFireballPosition()==self.getPosition():
                return 1
        return 0

    def updatePosition(self,x,y,c):
        self.__position=(self.__position[0]+x,self.__position[1]+y)
        b.set_board(self.__position[0]-x,self.__position[1]-y,c)
        b.set_board(self.__position[0],self.__position[1],'P')


    def checkJump(self,direction):
        if direction=='d':
            for i in range(1,3):
                if b.checkWall(self.__position[0]-i,self.__position[1]+i)!=0:
                    return 0
                if b.checkWall(self.__position[0]+1,self.__position[1]+i)!='X':
                    return 0
            for i in range(1,3):
                if b.checkWall(self.__position[0]-2+i,self.__position[1]+2+i)!=0:
                    return 0
                if b.checkWall(self.__position[0]+1,self.__position[1]+i)!='X':
                    return 0
            return 1
        
        elif direction=='a':
            for i in range(1,3):
                if b.checkWall(self.__position[0]-i,self.__position[1]-i)!=0:
                    return 0
                if b.checkWall(self.__position[0]+1,self.__position[1]-i)!='X':
                    return 0
            for i in range(1,3):
                if b.checkWall(self.__position[0]-2+i,self.__position[1]-2-i)!=0:
                    return 0
                if b.checkWall(self.__position[0]+1,self.__position[1]-i)!='X':
                    return 0
            return 1
    
    
    def jumpright(self):
        for i in range(1,3):
            for fireball in F:
                fireball.move()
            c1=b.getelement(self.__position[0]-1,self.__position[1]+1)
            if c1=='C':
                c1=' '
                self.incrementscore()
            if c1=='F':
                for fireball in F:
                    if fireball.getFireballPosition()==(self.__position[0]-1,self.__position[1]+1):
                        c1=fireball.getelementofboard()
                        F.remove(fireball)
                        self.hit()
            else:
                self.updatePosition(-1,1,self.__var)
                self.__var=c1
            b.print_board()
            print "Your Score: %d       LIVES LEFT: %d      LEVEL: %d"%(P.getscore(),P.getlive(),lev)
            if P.getlive()==0:
                print "                                     GAME    OVER                                 "
                break;
            sleep(.25)
        for i in range(1,3):
                for fireball in F:
                    fireball.move()
                c1=b.getelement(self.__position[0]+1,self.__position[1]+1)
                if c1=='C':
                    c1=' '
                    self.incrementscore()
                if c1=='F':
                    for fireball in F:
                        if fireball.getFireballPosition()==(self.__position[0]+1,self.__position[1]+1):
                            c1=fireball.getelementofboard()
                            F.remove(fireball)
                            self.hit()
                else:
                    self.updatePosition(1,1,self.__var)
                    self.__var=c1
                b.print_board()
                print "Your Score: %d       LIVES LEFT: %d      LEVEL: %d"%(P.getscore(),P.getlive(),lev)
                if P.getlive()==0:
                    print "                                     GAME    OVER                                 "
                    break;
                sleep(.25)


    def jumpleft(self):
        for i in range(1,3):
            for fireball in F:
                fireball.move()
            c1=b.getelement(self.__position[0]-1,self.__position[1]-1)
            if c1=='C':
                c1=' '
                self.incrementscore()
            if c1=='F':
                for fireball in F:
                    if fireball.getFireballPosition()==(self.__position[0]-1,self.__position[1]-1):
                        c1=fireball.getelementofboard()
                        F.remove(fireball)
                        self.hit()
            else:
                self.updatePosition(-1,-1,self.__var)
                self.__var=c1
            b.print_board()
            print "Your Score: %d       LIVES LEFT: %d      LEVEL: %d"%(P.getscore(),P.getlive(),lev)
            if P.getlive()==0:
                print "                                     GAME    OVER                                 "
                break;
            sleep(.25)
        for i in range(1,3):
            for fireball in F:
                fireball.move()
            c1=b.getelement(self.__position[0]+1,self.__position[1]-1)
            if c1=='C':
                c1=' '
                self.incrementscore()
            if c1=='F':
                for fireball in F:
                    if fireball.getFireballPosition()==(self.__position[0]+1,self.__position[1]-1):
                        c1=fireball.getelementofboard()
                        F.remove(fireball)
                        self.hit()
            else:
                self.updatePosition(1,-1,self.__var)
                self.__var=c1
            b.print_board()
            print "Your Score: %d       LIVES LEFT: %d      LEVEL: %d"%(P.getscore(),P.getlive(),lev)
            if P.getlive()==0:
                print "                                     GAME    OVER                                 "
                break;
            sleep(.25)



    def jump(self,direction):
        if direction=='d':
            if self.checkJump(direction)==1:
                self.jumpright()
            else:
                print "You can't jump due to presence of wall"
        
        elif direction=='a':
            if self.checkJump(direction)==1:
                self.jumpleft()
            else:
                print "You can't jump due to presence of wall"
            
            
    def moveup(self):
        
        c1=b.getelement(self.__position[0]-1,self.__position[1])
        if c1=='C':
            c1=' '
            self.incrementscore()
        if self.__var=='H':
            if c1=='F':
                for fireball in F:
                    if fireball.getFireballPosition()==(self.__position[0]-1,self.__position[1]):
                        c1=fireball.getelementofboard()
                        b.set_board(self.__position[0]-1,self.__position[1],' ')
                        F.remove(fireball)
                        self.hit()
            else:                 
                self.updatePosition(-1,0,self.__var)
                self.__var=c1


    def moveleft(self):
        
        c1=b.getelement(self.__position[0],self.__position[1]-1)
        if c1=='C':
            c1=' '
            self.incrementscore()
        if b.checkWall(self.__position[0]+1,self.__position[1]-1)!=0:
            if b.checkWall(self.__position[0],self.__position[1]-1)=='H':  
                self.updatePosition(0,-1,self.__var)
                self.__var=c1
            elif b.checkWall(self.__position[0],self.__position[1]-1)==0:
                if c1=='F':
                    for fireball in F:
                        if fireball.getFireballPosition()==(self.__position[0],self.__position[1]-1):
                            c1=fireball.getelementofboard()
                            b.set_board(self.__position[0],self.__position[1]-1,' ')
                            F.remove(fireball)
                            self.hit()
                else:
                    self.updatePosition(0,-1,self.__var)
                    self.__var=c1
            
            
    def movedown(self):
        
        c1=b.getelement(self.__position[0]+1,self.__position[1])
        if c1=='C':
            c1=' '
            self.incrementscore()
        if b.checkWall(self.__position[0]+1,self.__position[1])=='H':
            self.updatePosition(1,0,self.__var)
            self.__var=c1
        elif b.checkWall(self.__position[0]+1,self.__position[1])==0:
            if c1=='F':
                for fireball in F:
                    if fireball.getFireballPosition()==(self.__position[0]+1,self.__position[1]):
                        if fireball.getelementofboard()=='H':
                            c1=fireball.getelementofboard()
                            b.set_board(self.__position[0]+1,self.__position[1],'H')
                            F.remove(fireball)
                            self.hit()


    def moveright(self):

        if self.__position==(20,1):
                self.__var=' '
        if b.checkWall(self.__position[0]+1,self.__position[1]+1)!=0:
            if b.checkWall(self.__position[0],self.__position[1]+1)=='H':
                c1=b.getelement(self.__position[0],self.__position[1]+1)
                if c1=='C':
                    c1=' '
                    self.incrementscore()
                else:
                    self.updatePosition(0,1,self.__var)
                    self.__var=c1
            elif b.checkWall(self.__position[0],self.__position[1]+1)==0:
                c1=b.getelement(self.__position[0],self.__position[1]+1)
                if c1=='C':
                    c1=' '
                    self.incrementscore()
                if c1=='F':
                    for fireball in F:
                        if fireball.getFireballPosition()==(self.__position[0],self.__position[1]+1):
                            c1=fireball.getelementofboard()
                            b.set_board(self.__position[0],self.__position[1]+1,' ')
                            F.remove(fireball)
                            self.hit()
                else:
                    self.updatePosition(0,1,self.__var)
                    self.__var=c1




    def move(self,inp):

        if inp=='w':
            self.moveup()

        elif inp=='a':
            self.moveleft()

        elif inp=='s':
            self.movedown()

        elif inp=='d':
            self.moveright()



class Donkey(Person):

    def __init__(self):
        self.__position=(4,1)


    def getGhostPosition(self):
        return self.__position




class Fireball():

    def __init__(self):
        self.__position=(4,2)
        self.__direction=randint(0,1)
        self.__var=' '
        b.set_board(self.__position[0],self.__position[1],'F')

    def getelementofboard(self):
        return self.__var
        
    def getFireballPosition(self):
        return self.__position

    
    def deleteFireball(self):
        b.set_board(self.__position[0],self.__position[1],' ')
        F.remove(self)




    def updateFireballPosition(self,x,y):
        c1=b.getelement(self.__position[0]+x,self.__position[1]+y)
        if x==4:
            if c1=='F':
                c1='H'
        self.__position=(self.__position[0]+x,self.__position[1]+y)
        b.set_board(self.__position[0]-x,self.__position[1]-y,self.__var)
        b.set_board(self.__position[0],self.__position[1],'F')
        self.__var=c1
    


    def move(self):
        if self.__position==(20,1):
            self.deleteFireball()
        else:
            if self.__position[0]==4:
                if b.checkWall(self.__position[0]+1,self.__position[1])=='X':
                    if b.getelement(self.__position[0],self.__position[1]+1)=='P':
                        P.hit()
                        self.deleteFireball()
                    else:
                        self.updateFireballPosition(0,1)
                else:
                    if b.getelement(self.__position[0]+4,self.__position[1])=='P':
                        P.hit()
                        self.deleteFireball()
                    else:
                        self.updateFireballPosition(4,0)
            
            else:
                if self.__direction==0:
                    if b.checkWall(self.__position[0]+1,self.__position[1])=='X':
                        if b.checkWall(self.__position[0],self.__position[1]+1)=='X':
                            self.__direction=1
                        else:
                            if b.getelement(self.__position[0],self.__position[1]+1)=='F':
                                self.__direction=1
                            else:
                                if b.getelement(self.__position[0],self.__position[1]+1)=='P':
                                    P.hit()
                                    self.deleteFireball()
                                else:
                                    self.updateFireballPosition(0,1)
                    else:
                        if b.getelement(self.__position[0]+4,self.__position[1])=='P':
                            P.hit()
                            self.deleteFireball()
                        else:
                            self.updateFireballPosition(4,0)
                else:
                    if b.checkWall(self.__position[0]+1,self.__position[1])=='X':
                        if b.checkWall(self.__position[0],self.__position[1]-1)=='X':
                            self.__direction=0
                        else:
                            if b.getelement(self.__position[0],self.__position[1]-1)=='F':
                                self.__direction=0
                            else:
                                if b.getelement(self.__position[0],self.__position[1]+1)=='P':
                                    P.hit()
                                    self.deleteFireball()
                                else:
                                    self.updateFireballPosition(0,-1)
                    else:
                        if b.getelement(self.__position[0]+4,self.__position[1])=='P':
                            P.hit()
                            self.deleteFireball()
                        else:
                            self.updateFireballPosition(4,0)





class Board():

    def __init__(self,r,c,level):
        self.__row=r
        self.__column=c
        self.__gameboard=[]
        self.__gamelevel=level

    def generate_board(self):
        self.__gameboard=[
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ','X',' ','Q',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ','X','X','X','X','H','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','D',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]


    def print_board(self):
        sys.stderr.write("\x1b[2J\x1b[H")
        #for row in range(22):
         #   for col in range(70):
          #      print self.__gameboard[row][col],
           # print
        for row in range(22):
            for col in range(70):
                if self.__gameboard[row][col]=='C':
                    printf("C ",YELLOW)
                elif self.__gameboard[row][col]=='X':
                    printf("X ",MAGENTA)
                elif self.__gameboard[row][col]=='D':
                    printf("D ",GREEN)
                elif self.__gameboard[row][col]=='P':
                    printf("P ",BLUE)
                elif self.__gameboard[row][col]=='H':
                    printf("H ",CYAN)
                elif self.__gameboard[row][col]=='F':
                    printf("O ",RED)
                elif self.__gameboard[row][col]=='Q':
                    printf("Q ",WHITE)
                else:
                    printf("  ", BLACK)
            print ""



    def checkWall(self,row,col):
        if self.__gameboard[row][col]=='X':
            return 'X'
        elif self.__gameboard[row][col]=='H':
            return 'H'
        else:
            return 0


    def getelement(self,row,col):
        return self.__gameboard[row][col]


    def set_board(self,row,col,val):
        self.__gameboard[row][col]=val

    def __setcoins(self,count):
        for row in range(4,22,8):
            x=count/5
            while(x!=0):
                y=randint(2,44)
                if self.checkWall(row,y)==0:
                    self.__gameboard[row][y]='C'
                    x=x-1

        for row in range(8,22,8):
            x=count/5
            while(x!=0):
                y=randint(35,69)
                if self.checkWall(row,y)==0:
                    self.__gameboard[row][y]='C'
                    x=x-1
    
    def setboard(self):
        self.generate_board()
        self.__setcoins(25*(self.__gamelevel))

    def reloadboard(self):
        self.__setcoins(25*(self.__gamelevel))



def main(flag):
    global P,b,lev,direction,c,k,F,inp,fscore,flive 
    lev=(int)(raw_input("Enter the stage which u want to play(1/2/3):\n"))
    b=Board(22,70,lev)
    b.setboard()
    b.print_board()
    if flag==0:
        P=Player()
    else:
        P=Player()
        P.setscore(fscore)
        P.setlive(flive)
    direction='d'
    c=0
    k=6
    F=[]
    print "Your Score: %d       LIVES LEFT: %d      LEVEL: %d"%(P.getscore(),P.getlive(),lev)
    while True:
        inp=getchar()
        inp=inp.lower()
        c=c+1
        if(inp=='q'):
            break
        elif inp==' ':
            P.jump(direction)
        else:
            if inp=='d':
                direction=inp
            elif inp=='a':
                direction=inp
            if c%(k/lev)==0:
                F.append(Fireball())
                if c>=20:
                    c=0
                    if k<=25:
                        k=k+3 
            P.move(inp)
            for fireball in F:
                fireball.move()
            b.print_board()
            print "Your Score: %d       LIVES LEFT: %d      LEVEL: %d"%(P.getscore(),P.getlive(),lev)
            if P.getlive()==0:
                print "                                     GAME    OVER                                 "
                break
            if P.finaldestination()==1:
                print "Congo You have completed the level"
                lev=lev+1
                flag=1
                fscore=P.getscore()
                fscore=fscore+50
                flive=P.getlive()
                main(flag)


if __name__=="__main__":
    main(0)
