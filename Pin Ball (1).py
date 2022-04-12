#!/usr/bin/env python
# coding: utf-8

# In[4]:



        


# In[1]:



    


# In[165]:



import sys
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math
import turtle
import tkinter 
import pytest


class Ball:
    def __init__(
        self,
        position=np.array([550, 20], dtype=float),      #[180, 820]
        intposition=np.array([190, 800],dtype=float),
        velocity=np.array([0, 500], dtype=float),    #[5,0]
        acceleration=np.array([0, 0], dtype=float),
        name='Ball',
        mass=0.81,
        gran=10
    ):
        self.position = np.copy(position)
        self.velocity = np.copy(velocity)
        self.acceleration = np.copy(acceleration).astype(float)
        self.name = name
        self.mass = mass
        self.gran = gran
        self.intposition=intposition

        
    def update(self, tstep,W,L):  #this uses the Euler Cromer method to update the position and velocity
        theta=6.5 #6.5 # A pinball machine has an angle of 6.5 degrees 

        self.acceleration[1]=(-9.81/np.sin(theta))/self.mass
        self.acceleration[0]=0
        
        
        
        self.velocity[0]=np.multiply(self.acceleration[0],tstep)+self.velocity[0]
        self.velocity[1]=np.multiply(self.acceleration[1],tstep)+self.velocity[1]
        
        self.position[0]=np.multiply(self.velocity[0],tstep)+self.position[0]
        self.position[1]=np.multiply(self.velocity[1],tstep)+self.position[1]
        
        if self.position[0]<=0:
            self.position[0]=0
        if self.position[0]>=W:
            self.position[0]=(W-1)
        if self.position[1]<=0:
            self.position[1]=0
        if self.position[1]>=L:
            self.position[1]=(L-1)
        
            
        #self.intposition[0]=int(self.position[0]*self.gran)
        #self.intposition[1]=int(self.position[1]*self.gran)
        
        #self.position[0]=(self.intposition[0]/self.gran)
        #self.intposition[1]=(self.intposition[1]/self.gran)
        
        
    
    def wallbouncex(self,cr):
         #this gives how the ball will bounce off the floor and the wall. cr is high as they are hard and can ignore it  from the ball
        self.velocity[0]=cr*(-self.velocity[0])
    def wallbouncey(self,cr):
        self.velocity[1]=cr*(-self.velocity[1])
        
    def bumper1(self,cr2,center1): #R is the radius of the bumper, N is the number of windings, V is the voltage, Res is the resistance of the coil
        x=np.abs(self.position[0]-center1[0])
        y=np.abs(self.position[1]-center1[1])
        thetax=math.atan(x/y) #angle from the horizontal
        thetay=90-thetax  #angle from the vertical
        
        #angle of the tangent
        tanangley=thetay+90
        tananglex=thetax+90
        
        #angle of the trajectory of the ball
        thetavy=math.atan(self.velocity[0]/self.velocity[1])  #angle of velocity from the vertical
        thetavx=90-thetavy  #angle of velocity from the horizontal
        
        #relative angle of the ball to the tangent
        tan_angley=tanangley-thetavy
        tan_anglex=tananglex-thetavx
        
        #bounce angle
        bounce_x=180-tan_anglex
        bounce_y=180-tan_angley
        
        overall_velocity=np.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))
        
        self.velocity[1]=overall_velocity*(math.cos(bounce_y))
        self.velocity[0]=overall_velocity*(math.sin(bounce_x))
        
        if tan_angley-(bounce_y-tanangley)==0:
            print('For the bumper the angle of incidence is equal to the angle of reflection for the y component')
        print(tan_angley-(bounce_y-tanangley))
        if tan_anglex-(bounce_x-tananglex)==0:
            print('For the bumper the angle of incidence is equal to the angle of reflection for the x component')
        
        #self.velocity[0]=cr2*(self.velocity[0])
        #self.velocity[1]=cr2*((self.velocity[1])
        
    def topleftslantwall(self,cr):
        #angle to the vertical
        thetax=-45
        thetay=-45
        
        #angle of the tangent
        theta_y=thetay-90
        theta_x=theta_y
     
        
        #angle of the trajectory of the ball
        thetavy=-180+math.atan(self.velocity[0]/self.velocity[1])
        thetavx=90-thetavy

        
        #relative angle of the ball to the tangent
        tan_angley=theta_y-thetavy
        tan_anglex=theta_x-thetavx

        #bounce angle
        bounce_y=theta_y+tan_angley

        bounce_x=theta_x+tan_anglex
     
        
        overall_velocity=np.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))
        
        if tan_angley-(bounce_y-theta_y)==0:
            print('For the top left slant wall the angle of incidence is equal to the angle of reflection for the y component')
      
        if tan_anglex-(bounce_x-theta_x)==0:
            print('For the top left slant wall the angle of incidence is equal to the angle of reflection for the x component') 
  
        self.velocity[1]=cr*(overall_velocity*(math.cos(bounce_y)))
        self.velocity[0]=cr*(overall_velocity*(math.sin(bounce_x)))
        
        #print(self.velocity[1])
    
    def toprightslantwall(self,cr):
        #angle to the vertical
        thetax=45
        thetay=45
        
        #angle of the tangent
        theta_y=thetay+90
        theta_x=theta_y
        
        #angle of the trajectory of the ball
        thetavy=math.atan(self.velocity[0]/self.velocity[1])
        thetavx=90-thetavy
        
        #relative angle of the ball to the tangent
        tan_angley=theta_y-thetavy
        tan_anglex=theta_x-thetavx
        
        #bounce angle
        bounce_y=theta_y+tan_angley
        bounce_x=theta_x+tan_anglex
        
        overall_velocity=np.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))
        
        if tan_angley-(bounce_y-theta_y)==0:
            print('For the top right slant wall the angle of incidence is equal to the angle of reflection for the y component')
   
        if tan_anglex-(bounce_x-theta_x)==0:
            print('For the top right slant wall the angle of incidence is equal to the angle of reflection for the x component') 

        self.velocity[1]=cr*(overall_velocity*(math.cos(bounce_y)))
        self.velocity[0]=cr*(overall_velocity*(math.sin(bounce_x)))
        
    def bottomrightslantwall(self,cr):
         #angle to the vertical
        thetax=135
        thetay=135
        
        #angle of the tangent
        theta_y=thetay-90
        theta_x=theta_y
        
        #angle of the trajectory of the ball
        thetavy=math.atan(self.velocity[0]/self.velocity[1])
        thetavx=90-thetavy
        
        #relative angle of the ball to the tangent
        tan_angley=theta_y-thetavy
        tan_anglex=theta_x-thetavx
        
        #bounce angle
        bounce_y=theta_y+tan_angley
        bounce_x=theta_x+tan_anglex
        
        overall_velocity=np.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))
        
        if tan_angley-(bounce_y-theta_y)==0:
            print('For the bottom right slant wall the angle of incidence is equal to the angle of reflection for the y component')
          
        if tan_anglex-(bounce_x-theta_x)==0:
            print('For the bottom right slant wall the angle of incidence is equal to the angle of reflection for the x component') 
        
        self.velocity[1]=cr*(overall_velocity*(math.cos(bounce_y)))
        self.velocity[0]=cr*(overall_velocity*(math.sin(bounce_x)))
        
    def bottomleftslantwall(self,cr):
         #angle to the vertical
        thetax=-135
        thetay=-135
        
        #angle of the tangent
        theta_y=thetay+90
        theta_x=theta_y

        
        #angle of the trajectory of the ball
        thetavy=(math.atan(self.velocity[0]/self.velocity[1]))
        thetavx=90-thetavy

        
        #relative angle of the ball to the tangent
        tan_angley=theta_y-thetavy
        tan_anglex=theta_x-thetavx

        
        #bounce angle
        bounce_y=theta_y+tan_angley
        bounce_x=theta_x+tan_anglex

        
        overall_velocity=np.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))

        

        if tan_angley-(bounce_y-theta_y)==0:
            print('For the bottom left slant wall the angle of incidence is equal to the angle of reflection for the y component')
            
        if tan_anglex-(bounce_x-theta_x)==0:
            print('For the bottom left slant wall the angle of incidence is equal to the angle of reflection for the x component')            
        self.velocity[1]=cr*(overall_velocity*(math.cos(bounce_y)))
        self.velocity[0]=cr*(overall_velocity*(math.sin(bounce_x)))
        
                
        
    
        
    def ballup(self,upvel):
        self.velocity[1]=upvel
        
       

    
            
def board(grid,W,L,center1,center2):       
    for i in range (0,W+1):
        for j in range (0,L): #putting in the walls
            if j==0 or j==(L-1) or i==0 or i==(W-1):
                grid[i][j]=1
            else:
                grid[i][j]=0
                
#left one top
    for i in range(0,51):
        for j in range(0,(i+1)):
            grid[50-i][L-j]=1
      
           
            
#left one bottom
    for i in range(51):
        for j in range(i+1):
            grid[50-i][j]=1
    
#right one bottom
    for i in range(51):
        for j in range(0,(i+1)):
            grid[(W-50)+i][j]=1

#right one top
    for i in range(51):
        for j in range(0,(i+1)):
            grid[(W-50)+i][L-j]=1
  
    
            

    #coding for the bumper where integer=2
    
    R=20 #radius of the bumper
    for i in range ((center1[0]-R),(center1[0]+R)):
        for j in range ((center1[1]-R),(center1[1]+R)):
            distance=np.sqrt((np.abs(i-center1[0]))**2+(np.abs(j-center1[1]))**2)
            if distance<=R:
                grid[i][j]=2
                
    
    #R=20 #radius of the bumper
    #for i in range ((center2[0]-R),(center2[0]+R)):
        #for j in range ((center2[1]-R),(center2[1]+R)):
            #distance=np.sqrt((np.abs(i-center2[0]))**2+(np.abs(j-center2[1]))**2)
           # if distance<=R:
                #grid[i][j]=2
    return grid
    
    
    #print(grid)       


       
        


        


def hit(grid,myball):
    if grid[int(myball.position[0]),int(myball.position[1])]!=0:
        return True
    else:
        return False

def whathit(grid,myball,W,L,cr,cr2,center1,R):
    if grid[int(myball.position[0]),int(myball.position[1])]==1:
        if int(myball.position[0])==0:
            myball.wallbouncex(cr)
        if math.ceil(myball.position[0])==(W-1):
            myball.wallbouncex(cr)
        if int(myball.position[1])==0: 
            myball.wallbouncey(cr)
        if math.ceil(myball.position[1])==(L-1):
            myball.wallbouncey(cr)  
            
        #for the slanted wall 
        #bottom right
        if myball.position[0] in range((W-50),(W+1)) and myball.position[1] in range(0,51):
            myball.bottomrightslantwall(cr)
        #bottom left
        if myball.position[0] in range(0,51) and myball.position[1] in range(0,51):
            myball.bottomleftslantwall(cr)
        #top left
        if myball.position[0] in range(0,51) and myball.position[0] in range((L-50),(L+1)):
            myball.topleftslantwall(cr)
        #top right
        if myball.position[0] in range((W-50),(W+1)) and myball.position[1] in range((L-50),(L+1)):
            myball.toprightslantwall(cr)
    if grid[int(myball.position[0]),int(myball.position[1])]==2:
         myball.bumper1(cr2,center1)
           
        
#pytest part
#
def test_boundaries(myball,tstep,W,L):
    if any(myball.position)<0:
        assert myball.update(tstep,W,L)==0
    if myball.position[0]>W:
        assert myball.update(tstep,W,L)==W
    if myball.position[1]>L:
        assert myball.update(tstep,W,L)==L

def plot(myball,grid,W,L,xpos,ypos):
    x=[]
    y=[]
    t=[]
    k=[]
    h=[]
    q=[]
    for i in range (W+1):
        for j in range(L+1):
            if grid[i][j]==1:
                t.append(i)
                k.append(j)
    plt.scatter(t,k,marker='.',s=1)
    
    for i in range (W+1):
        for j in range(L+1):
            if grid[i][j]==2:
                h.append(i)
                q.append(j)
    plt.scatter(h,q)
            
    plt.plot(xpos,ypos, color='black')
    plt.xlabel('x position (mm)')
    plt.ylabel('y position (mm)')
    plt.title('Motion of the ball across the playing field')
    y=0
    x=W-10
    #plt.scatter(x,y,s=10)
    plt.show()
def kinetic(myball,mass):
    overalvel=np.sqrt(myball.velocity[1]**2+myball.velocity[0]**2)
    EK=(mass*overalvel)/2
    return EK
def mom(myball,mass):
    overalvel=np.sqrt(myball.velocity[1]**2+myball.velocity[0]**2)
    mom=mass*overalvel
    return mom

        
def main():
    print('hello')
    #setting up the interface
    tk=tkinter.Tk()
    
    gran=10
    #setting the dimensions of the board
    W=560 #width is 560mm
    L=1000 #length is 1000mm
    
    # Init parms in Canvas
    canvas_width = W
    canvas_hight = L
    tk.title("Pinball game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = tkinter.Canvas(tk, width=canvas_width, height=canvas_hight, bd=0, highlightthickness=0, bg='#00ffff')
    canvas.pack()
    #tk.update()
    
    #initialising the ball
    myball=Ball()
    
    #defining the parameters
    mass=myball.mass
    velocity=myball.velocity
    
    #setting up the push up of the ball
    upvel=30
    
    #setting up the timevector
    endtime=30
    starttime=0
    tstep=0.1
    timevector=[starttime,endtime,tstep]
            
    #setting the positions of the bumpers
    center1=[280,700]
    center2=[350,800]
    
    #setting up radius of bumpers
    R=20
    
    #initalising the grid
    grid=np.empty([(W+1),(L+1)])
    board(grid,W,L,center1,center2)
    #np.set_printoptions(threshold=sys.maxsize)
    #print(grid)
    
    
    
    #defining the coefficiant of resitution
    cr=0.7
    cr2=1.1
    
    
   
    
    time=starttime
    xpos=[]
    ypos=[]

    while time<endtime:
        #if time==starttime:
             #myball.ballup(upvel)
        myball.update(tstep,W,L)
        xpos.append(myball.position[0])
        ypos.append(myball.position[1])
       
     
      
        #print(myball.position)
        #print(grid[int(myball.position[0]),int(myball.position[1])])
        if hit(grid,myball):
            #what have I hit?
            

            whathit(grid,myball,W,L,cr,cr2,center1,R)

        time=time+tstep

    print(grid[0][559])
    print(grid[math.ceil(myball.position[0])][0])

    plot(myball,grid,W,L,xpos,ypos)
    

    
    t=np.linspace(0,len(xpos),len(xpos))
    #plt.plot(t,ypos)

    plt.show()
   # plt.plot(t,xpos)

    plt.show()
    #plt.plot(xpos,ypos)
    plt.show()
    
    test_boundaries(myball,tstep,W,L)
               
 

  
                
                

   
    



if __name__ == "__main__":
    main()
    #sys.exit(main())
    


# In[166]:



    
    


# In[105]:





# In[ ]:





# In[ ]:




