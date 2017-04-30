import numpy as np 
from matplotlib import pyplot as plt 
N = (1.0,1.0,1.0,1.0,1.0)
n = (10,30,100,300,1000)

#area for simpson's rule
A1 = (1.05236326978,1.01745333429,1.00523598809,1.00174532926,1.00052359878)

#the area for standard sum
A2 = (1.0764828026941022, 1.025951465275319, 1.0078334198735821, 
1.0026157092462991, 1.0007851925466307)

E_simpson = abs(np.subtract(A1,N))
E_std = abs(np.subtract(A2,N))

plt.figure()
plt.semilogy(n, E_simpson,
             color = 'blue',
             linewidth = 2)
plt.semilogy(n, E_std,
             color = 'red',
             linewidth = 2)
plt.title('semilog y-axis')
plt.grid(True)