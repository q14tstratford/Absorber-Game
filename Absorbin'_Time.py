#Imports

from pygame_functions import *
import math
import random
#Setup
width=1000
height=800
screenSize(width,height)
setBackgroundColour("blue")
setAutoUpdate(False)
#Globals

#Constants

#Subprograms
def colDetect():
    global allCreatures
    global Player
    for creature1 in allCreatures:
        for creature2 in allCreatures:
            if creature1==creature2:
                break
            elif touching(creature1.sprite,creature2.sprite):
                if creature1.size > creature2.size :
                    print("{} eats {}".format(creature1,creature2))
                    allCreatures.remove(creature2)
                    creature1.size+=creature2.Die()
                    if creature2==Player:
                        setBackgroundColour("red")
                        while True:
                            pass
                    enemies.append(Enemy(random.randint(-2000,2000)+Player.x,random.randint(-2000,2000)+Player.y,random.randint(0,(10000+(15*Player.size)))/10,"Bob.png"))
                    
                elif creature1.size <= creature2.size :
                    print("{} eats {}".format(creature2,creature1))
                    allCreatures.remove(creature1)
                    creature2.size+=creature1.Die()
                    if creature1==Player:
                        setBackgroundColour("red")
                        while True:
                            pass
                    enemies.append(Enemy(random.randint(-2000,2000)+Player.x,random.randint(0,10000)+Player.y,random.randint(0,(10000+(15*Player.size)))/10,"Bob.png"))


#Classes

class Creature:
    def __init__(self,x,y,size,image):
        self.x=x
        self.y=y
        self.sprite=makeSprite(image)
        self.direction=0
        self.size=size
        self.speed = 10
        self.trailPos=[]
        moveSprite(self.sprite,500,400, centre=True)
        showSprite(self.sprite)
        transformSprite(self.sprite,self.direction,(self.size**0.3)/25)
        
    def move(self):
        mX=mouseX()
        mY=mouseY()
        wP=keyPressed("W")
        aP=keyPressed("A")
        sP=keyPressed("S")
        dP=keyPressed("D")
        dX=mX-500
        dY=mY-400
        self.direction=math.atan2(dY,dX)
        transformSprite(self.sprite,self.direction/math.pi*180+90,((self.size**0.3))/25)
        xspeed = 0
        yspeed = 0
        speedScalar=((dX**2+dY**2)**0.5)/100
        self.trailPos.append([int(self.x),int(self.y)])
        if len(self.trailPos) > 20:
            self.trailPos.pop(0)
        if speedScalar>1.25:
            speedScalar==1.25
        if abs(dX)>5 or abs(dY)>5:
            if wP:
                xspeed = (xspeed*0.99)+self.speed * math.cos(self.direction)*speedScalar
                yspeed = (yspeed*0.99)+self.speed * math.sin(self.direction)*speedScalar
            #elif sP:
                #xspeed = -self.speed * math.cos(self.direction)*speedScalar
                #yspeed = -self.speed * math.sin(self.direction)*speedScalar
            if aP:
                xspeed = (xspeed*0.75)-1.05*self.speed * math.cos(self.direction+math.pi/2)
                yspeed = (yspeed*0.75)-1.05*self.speed * math.sin(self.direction+math.pi/2)
            if dP:
                xspeed = (xspeed*0.75)+1.05*self.speed * math.cos(self.direction+math.pi/2)
                yspeed = (yspeed*0.75)+1.05*self.speed * math.sin(self.direction+math.pi/2)
        self.x = (self.x+xspeed)%5000
        self.y = (self.y+yspeed)%5000
        for tElement in self.trailPos:
            drawEllipse(500+tElement[0]-self.x,400+tElement[1]-self.y,(self.size**0.3),(self.size**0.3),"green")
    
    def Die(self):
        hideSprite(self.sprite)
        return self.size
    
class Enemy(Creature):
    def __init__(self,x,y,size,image):
        self.x=x
        self.y=y
        self.sprite=makeSprite(image)
        self.direction=0
        self.size=size
        self.speed = 10
        showSprite(self.sprite)
        transformSprite(self.sprite,self.direction,(self.size**0.3)/25)
        
    def move(self):
        global Player
        dX=(Player.x-self.x)
        dY=(Player.y-self.y)
        xspeed=0
        yspeed=0
        if((dX**2+dY**2)**0.5)<10:
            self.direction=math.atan2(dY,dX)
            xspeed=0
            yspeed=0
        elif ((dX**2+dY**2)**0.5)<350 and self.size>Player.size:
            self.direction=math.atan2(dY,dX)
            xspeed = self.speed * math.cos(self.direction)
            yspeed = self.speed * math.sin(self.direction)
        elif ((dX**2+dY**2)**0.5)<350 and self.size<=Player.size:
            self.direction=math.atan2(-dY,-dX)
            xspeed = self.speed * math.cos(self.direction)
            yspeed = self.speed * math.sin(self.direction)
        
        self.x = (self.x + xspeed)%5000
        self.y = (self.y + yspeed)%5000
        if (dX**2+dY**2)**0.5 <(2000):
            transformSprite(self.sprite,self.direction/math.pi*180+90,((self.size**0.3))/25)
        moveSprite(self.sprite, 500+(self.x-Player.x),400+(self.y-Player.y), centre=True)
        
        
#Creatures

Player=Creature(2500,2500,200,"Kevin.png")
enemies=[]
for i in range(200):
    enemies.append(Enemy(random.randint(0,10000),random.randint(0,10000),random.randint(0,10000)/10,"Bob.png"))
allCreatures=enemies
allCreatures.append(Player)
#Main Body
while True:
    clearShapes()
    Player.move()
    tick(30)
    for e in enemies:
        e.move()
    updateDisplay()
    try:
        colDetect()
    except:
        pass

endWait()