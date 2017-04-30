
import numpy as np
import math
from math import pi

from math import cos
def g_of_t(t):
    return (math.cos(t))/t

a=0
b=np.pi/2
N=(10,30,100,300,1000)

import numpy as np
def simpsons_rule (g,a,b,N):
    if N & 1:
        print('Error: N is not a even number.')
    return(0.0)

h= [(b-a)/10,(b-a)/30,(b-a)/100,(b-a)/300,(b-a)/1000]
k= (0.0)

a= float(a)
for i in range (0, N/2):
    k += g(t) + (2.0*g(t+h))
    t += 2*h

k= (2.0*k) - g(a) + g(b)
k= h*k/3.0
return k

print(simpsons_rule(g_of_t, a, b, N))









  

