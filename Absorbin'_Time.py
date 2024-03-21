#Imports

from pygame_functions import *
import math
import random
#Setup

screenSize(1000,800)
setBackgroundColour("blue")

#Globals

#Constants

#Subprograms

#Classes

class Creature:
    def __init__(self,x,y,size,image):
        self.x=x
        self.y=y
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
                xspeed = self.speed * math.cos(self.direction)*speedScalar
                yspeed = self.speed * math.sin(self.direction)*speedScalar
            elif sP:
                xspeed = -self.speed * math.cos(self.direction)*speedScalar
                yspeed = -self.speed * math.sin(self.direction)*speedScalar
            elif aP:
                xspeed = -1.05*self.speed * math.cos(self.direction+math.pi/2)
                yspeed = -1.05*self.speed * math.sin(self.direction+math.pi/2)
            elif dP:
                xspeed = 1.05*self.speed * math.cos(self.direction+math.pi/2)
                yspeed = 1.05*self.speed * math.sin(self.direction+math.pi/2)
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
        if ((dX**2+dY**2)**0.5)<350 and self.size>Player.size:
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
#e1=Creature(200,200,0.5,"Bob.png",0)
#Main Body
while True:
    Player.move()
    tick(30)
    for e in enemies:
        e.move()
endWait()