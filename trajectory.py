#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# In[56]:


cometdata = pd.read_csv('CometData.csv')


# In[57]:


comet_df = pd.DataFrame(cometdata)


# In[58]:


SE = 1


# In[59]:


def sinerule(a, theta, b):
    '''
    calculates the angle alpha using sine rule.
    a : sin theta = b : sin alpha
    '''
    sinalpha = a*np.sin(theta)/b
    alpha = np.arcsin(sinalpha)
    return alpha

def cosrule(a, theta, b=SE):
    '''
    calculates the side c using cosine rule.
    c*c = a*a + b*b - 2*a*b*cos theta
    '''
    costheta = np.cos(theta)
    c = np.sqrt(a**2 + b**2 - 2*a*b*costheta)
    return c


# In[60]:


comet_df['Distance from Sun(AU)'] = cosrule(comet_df['Distance from earth(AU)'], comet_df['Angle between comet and sun(radians)'])


# In[61]:


def calcangle(time):
    k = time - np.floor(time)
    angle = k*2*np.pi
    return angle


# In[62]:


comet_df['Angle made by earth with reference axis(radians)'] = calcangle(comet_df['# Time(in years)'])


# In[63]:


comet_df['Angle between comet and earth(radians)'] = sinerule(comet_df['Distance from earth(AU)'], comet_df['Angle between comet and sun(radians)'], comet_df['Distance from Sun(AU)'])


# In[64]:


comet_df['Angle between comet and reference axis(radians)'] = comet_df['Angle made by earth with reference axis(radians)'] + comet_df['Angle between comet and earth(radians)']


# In[65]:


def polarconic(theta, e, r0, t0):
    exp1 = 1 + e*np.cos(theta - t0)
    return r0/exp1


# In[66]:


r = comet_df['Distance from Sun(AU)']
t = comet_df['Angle between comet and reference axis(radians)']


# In[67]:


from scipy.optimize import curve_fit


# In[68]:


popt, pcov = curve_fit(polarconic, t, r)


# In[69]:


eccentricity = popt[0]
print(eccentricity)


# In[70]:


x = r*np.cos(t)
y = r*np.sin(t)


# In[71]:


plt.plot(x, y, 'r.')
plt.show()


# In[72]:


# The trajectory is elliptical


# In[73]:


time = comet_df['# Time(in years)']


# In[74]:


plt.plot(time, t, 'g.')
plt.show()


# In[75]:


totalangle = t[99] - t[90]
totaltime = time[99] - time[90]

timeperiod = 2*np.pi*totaltime/totalangle


# In[76]:


print(timeperiod*365)

