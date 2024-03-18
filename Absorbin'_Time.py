#Imports

from pygame_functions import *

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
        moveSprite(self.sprite,self.x,self.y)
        showSprite(self.sprite)
#Creatures

c1=Creature(0,0,1,"SweetBabyKevin.png")

#Main Body


endWait()