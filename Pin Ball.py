#!/usr/bin/env python
# coding: utf-8

# In[13]:



import numpy as np
import math

# A pinball machine has an angle of 6.5 degrees #
class Ball:
    def __init__(
        self,
        position=[0, 0],
        velocity=[0, 0],
        #acceleration=np.array([0, 0], dtype=float),
        name='Ball',
        mass=0.81
    ):
        self.position = position
        self.velocity = velocity
        #self.acceleration = np.copy(acceleration).astype(np.float)
        self.name = name
        self.mass = mass

        
    def downball(self, tstep):
        theta=6.5
        acceleration=(-9.81/np.sin(theta))/self.mass
        
        
        self.velocity[1]=self.velocity[1]+acceleration
        self.position[1]=round(self.position[1]+self.velocity[1]/tstep)
        
        self.velocity[0]=self.velocity[0]
        self.position[0]=round(self.position[0]+self.velocity[0]/tstep)
        
            #print(self.position) 
        
        
            
def board(grid,W,L):       

    for i in range (0,W):
        for j in range (0,L): #putting in the walls
            if j==0 or j==(L-1) or i==0 or i==(W-1):
                grid[i][j]=1
            else:
                grid[i][j]=0
    #coding for the bumper where integer=2
    center=[200,400]
    R=20 #radius of the bumper
    for i in range ((center[0]-R),(center[0]+R)):
        for j in range ((center[1]-R),(center[1]+R)):
            distance=np.sqrt((np.abs(i-center[0]))**2+(np.abs(j-center[1]))**2)
            if distance<=R:
                grid[i][j]=2
    
    
    print(grid)
    

    
                
            
def bounceback(cr): #bounceback for the walls
    #cr=coeffieciant of restitution which depends on the material
    #cr=relative velocity after collision/relative velocity before collision
    #cr for the ball =0.93 so can discount
    initialvelocity=-7  #initial velocity, will need to call a function here at some point
   
    position=[1,1]
    if position[0] or position[1]==1:
        velocity=initialvelocity*cr
    print(velocity)
    
def bumper(self,R,N,V,Res,l): #R is the radius of the bumper, N is the number of windings, V is the voltage, Res is the resistance of the coil
    #l is the length of the solenoid
    if position[0] or position[1]==2:
        #finding the direction that the ball will go. perpendicular to the point on the circle
        if position[0]==2:
            x=abs(position[0]-R)
        elif position[0]!=2:
            x=0
        if position[1]==2:
            y=abs(position[1]-R)
        elif position[1]!=2:
            y=0
        direction=[x,y] #this is the direction vector for the velocity
        
        
        #calculating current
        I=V/Res
        #calculating field of the solenoid
        magconst=(1.2566e-6) #magnetic constant
        B=magconst(N*I)/l
        #calculating force pulling the bumper down
        F=B*I*l
        #defining angle of the bumper as 2 degrees for all bumpers
        theta=2
        Fout=F/np.tan(theta)
        #this is the force with which the ball will be forced out in the direction calculated above
        #calculating the associated acceleration
        a=Fout/self.mass
        #this is the magnitude of acceleration. Need to calculate it with direction
        
        a_x=np.sqrt(xa/x+y)
        a_y=np.sqrt(ya/x+y)
        a=[a_x,a_y]
        return a
        
    
        
    
        
    
#put in an index for the type of object eg. if its a two then its a bumper
#have the length and the width in the main
#for my ball pass the position maybe
#put in a loop to make sure theball is still on the table
    

        
       
        
def main():
    print("hello")
    myball=Ball()
    
    W=560 #width is 560mm
    L=1000 #length is 1000mm
    grid=np.empty([W,L])
    
    board(grid,W,L)
    for t in range (0,1000):
        myball.downball(100)
        if grid[int(myball.position[0]),int(myball.position[1])]!=0:
            #print('it hits something')
            #it hhits something
    
    #bounceback(0.5)


if __name__ == "__main__":
    main()
        


# In[12]:


print(1e-4)
    
    


# In[15]:





# In[ ]:




