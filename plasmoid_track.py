# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D


t0=0
tf=1000
N=1000
tarr=np.linspace(t0,tf,N)
theta = np.pi/8.
r0=5
phi0=0

rdot0 = .1 #in units of c, we are using a constant rdot
r0phidot0 = .5 #need to figure out units here



rdot = rdot0

rdotarr = rdot * np.ones(N)

r = r0 + rdot*tarr

phidot = r0phidot0/r

phi=(r0phidot0/rdot)*np.log(r/r0)

'''
fig, (ax0,ax1) = plt.subplots(2,1,sharex=True)
ax0.plot(tarr,r,label='$r$')
ax0.plot(tarr,phi,label='$\phi$')
ax0.legend(frameon=False,prop={'size':14})

ax1.plot(tarr,rdotarr,label='$dr/dt$')
ax1.plot(tarr,phidot,label='$d\phi/dt$')
ax1.legend(frameon=False,prop={'size':14})

ax1.set_xlabel('Time')
'''

x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)