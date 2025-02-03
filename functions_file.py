#!/usr/bin/env python
# coding: utf-8

# In[9]:


def base_function_1(x: float):
    # Parabolic Function
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
    function_1 = (x)**2 + 5*x - 6
    return function_1


# In[ ]:


def base_function_2(x: float):
    # Third-Order Function
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
    function_2 = (x)**3 + x^2 + 2*x + 8
    return function_2


# In[ ]:


def base_function_3(x: float):
    # Linear Function
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
    function_3 = 5*x + 10
    return function_3


# In[ ]:


def base_function_4(x: float):
    # Simple D=VT problem: How far will an object travel (in either the positive or negative direction) in 10 seconds?
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
    function_4 = x*10
    return function_4


# In[ ]:


def base_function_5(x: float):
    # F = u_s*m*g problem: What is the minimum horizontal force required to overcome the static friction coefficient of a chosen mass?
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
    u_s = 0.35
    function_5 = u_s * x * 9.8
    return function_5


# In[11]:


def value_average(x: float, y:float):
    # Given two float values, will return their average. Used to determine the value of c.
    value = (x+y)/2
    return value


# In[ ]:


# Old function that used numpy module to compare the signs of the values of f(a) and f(c)

# import numpy as np
# The numpy function same_sign can directly compare the sign of two values, in this case useful for comparing f(c) to f(a)

# def same_sign(x,y):
   # return np.sign(x)==np.sign(y)


# In[12]:


def convergence_check(x: float, y:float, z:float, w:float, j:float, k:float, l:float):
    # Given the values (in order) of a, b, c, e (convergence), f(a), f(b), and f(c) as floats, this function will:
    # Compare the absolute value of the difference between a and c to convergence and the absolute value of f(c) to convergence
    
    if abs(z-x)<w or abs(l)<w:
        return z
    elif j*l >= 0:
        x = z
    else:
        y = z
    

