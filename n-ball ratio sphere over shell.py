
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
import math
from mpmath import mp
N = np.arange(3, 400, 1)
Ratio = np.zeros(N.size)
VRe = np.zeros(N.size)
Vr = np.zeros(N.size)
Re = np.zeros(N.size)
epsilon = np.zeros(N.size)
RoverRe=0.01

for i, n in enumerate(N):
    radius = ((1 / np.pi**(n/2)) * mp.gamma((n/2) + 1))**(1/n)
    Re[i] = radius    
    
for i, n in enumerate(N):
    epsilon[i] = Re[i]-Re[i]*RoverRe

def calculate_sphere_volume(radius, dimensions):
    mp.dps = 50  # Set the desired precision
    numerator = mp.pi**(dimensions/2) * radius**dimensions
    denominator = mp.gamma((dimensions/2) + 1)
    volume = numerator / denominator
    return volume

for i, n in enumerate(N):
    VRe[i] = calculate_sphere_volume(Re[i], n)
    Vr[i] = VRe[i]-calculate_sphere_volume(epsilon[i], n)
    Ratio[i] = VRe[i] / (Vr[i])
    
#plt.plot(N,VRe,'b+',label='VRe')
#plt.plot(N,Vr,'g+',label='Vr')
plt.loglog(N, Ratio, 'r+')
plt.xlabel('Number of Dimensions')
plt.ylabel('Ratio R / (R - epsilon)')
plt.title('Ratio R / (R - epsilon) vs. Number of Dimensions')
plt.show()
