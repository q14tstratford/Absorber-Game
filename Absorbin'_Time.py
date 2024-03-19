#Imports

from pygame_functions import *
import math

#Setup

screenSize(500,500)
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
        if wP:
            xspeed = self.speed * math.cos(self.direction)
            yspeed = self.speed * math.sin(self.direction)
        elif sP:
            xspeed = -self.speed * math.cos(self.direction)
            yspeed = -self.speed * math.sin(self.direction)
        elif aP:
            xspeed = -0.75*self.speed * math.cos(self.direction+math.pi/2)
            yspeed = -0.75*self.speed * math.sin(self.direction+math.pi/2)
        self.x += xspeed
        self.y += yspeed
        moveSprite(self.sprite, self.x, self.y, centre=True)
#Creatures

Player=Creature(150,150,0.5,"Kevin.png")

#e1=Creature(200,200,0.5,"Bob.png",0)
#Main Body
while True:
    Player.move()
    tick(30)

endWait()