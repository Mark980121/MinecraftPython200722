# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:01:44 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def plantTree(x,y,z):
    
     mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,46)
     
     mc.setBlocks(x,y,z,x,y+4,z,41)
   
x,y,z=mc.player.getTilePos()
plantTree(x,y,z)
for i in range(10):
    for j in range(5):
        for k in range(5):
            plantTree(x+i*10,y+j*10,z+k*10)
        
        

    