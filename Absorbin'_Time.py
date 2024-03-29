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
    for creature1 in allCreatures:
        for creature2 in allCreatures:
            if creature1==creature2:
                break
            elif touching(creature1.sprite,creature2.sprite):
                if creature1.size > creature2.size :
                    print("{} eats {}".format(creature1,creature2))
                elif creature1.size <= creature2.size :
                    print("{} eats {}".format(creature2,creature1))

def findNearest():
    pass

#Classes

class Creature:
    def __init__(self,x,y,size,image):
        self.x=x
        self.y=y
        if self.x>=width:
            self.x=10
        if self.x<=0:
            self.x=990
        self.sprite=makeSprite(image)
        self.direction=0
        self.size=size
        self.speed = 10
        moveSprite(self.sprite,self.x,self.y, centre=True)
        showSprite(self.sprite)
        transformSprite(self.sprite,self.direction,self.size)
        
    def move(self):
        mX=mouseX()
        mY=mouseY()
        wP=keyPressed("W")
        aP=keyPressed("A")
        sP=keyPressed("S")
        dP=keyPressed("D")
        dX=mX-self.x
        dY=mY-self.y
        self.direction=math.atan2(dY,dX)
        transformSprite(self.sprite,self.direction/math.pi*180+90,self.size)
        xspeed = 0
        yspeed = 0
        speedScalar=((dX**2+dY**2)**0.5)/100
        if speedScalar>1.25:
            speedScalar==1.25
        if abs(dX)>5 or abs(dY)>5:
            if wP:
                xspeed = (xspeed*0.75)+self.speed * math.cos(self.direction)*speedScalar
                yspeed = (yspeed*0.75)+self.speed * math.sin(self.direction)*speedScalar
            #elif sP:
                #xspeed = -self.speed * math.cos(self.direction)*speedScalar
                #yspeed = -self.speed * math.sin(self.direction)*speedScalar
            if aP:
                xspeed = (xspeed*0.75)-1.05*self.speed * math.cos(self.direction+math.pi/2)
                yspeed = (yspeed*0.75)-1.05*self.speed * math.sin(self.direction+math.pi/2)
            if dP:
                xspeed = (xspeed*0.75)+1.05*self.speed * math.cos(self.direction+math.pi/2)
                yspeed = (yspeed*0.75)+1.05*self.speed * math.sin(self.direction+math.pi/2)
        self.x += xspeed
        self.y += yspeed
        moveSprite(self.sprite, self.x, self.y, centre=True)


class Enemy(Creature):
    def move(self):
        global Player
        dX=Player.x-self.x
        dY=Player.y-self.y
        xspeed=0
        yspeed=0
        if((dX**2+dY**2)**0.5)<10:
            self.direction=math.atan2(dY,dX)
            transformSprite(self.sprite,self.direction/math.pi*180+90,self.size)
            xspeed=0
            yspeed=0
        elif ((dX**2+dY**2)**0.5)<350 and self.size>Player.size:
            self.direction=math.atan2(dY,dX)
            transformSprite(self.sprite,self.direction/math.pi*180+90,self.size)
            xspeed = self.speed * math.cos(self.direction)
            yspeed = self.speed * math.sin(self.direction)
        elif ((dX**2+dY**2)**0.5)<350 and self.size<=Player.size:
            self.direction=math.atan2(-dY,-dX)
            transformSprite(self.sprite,self.direction/math.pi*180+90,self.size)
            xspeed = self.speed * math.cos(self.direction)
            yspeed = self.speed * math.sin(self.direction)
        
        self.x += xspeed
        self.y += yspeed
        moveSprite(self.sprite, self.x, self.y, centre=True)
#Creatures

Player=Creature(150,150,0.5,"Kevin.png")

enemies=[]
for i in range(5):
    enemies.append(Enemy(random.randint(0,1000),random.randint(0,800),random.randint(0,10)/10,"Bob.png"))
allCreatures=enemies
allCreatures.append(Player)
#Main Body
while True:
    Player.move()
    tick(30)
    for e in enemies:
        e.move()
    updateDisplay()
    colDetect()
endWait()