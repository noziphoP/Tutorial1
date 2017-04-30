import numpy as np
import math
from math import pi
x0=0
x1=np.pi/2
    
mydelts=[(x1-x0)/10,(x1-x0)/30,(x1-x0)/100,(x1-x0)/300,(x1-x0)/1000]
for dx in mydelts:
    x=np.arange(x0,x1,dx)
    y=np.sin(x)
    tot=y.sum()*dx
    print('integral is ' + repr(tot) + ' with dx=' + repr(dx))



    
 
    
