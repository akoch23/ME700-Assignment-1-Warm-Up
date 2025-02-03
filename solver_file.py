#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('run', 'functions_file.ipynb')

print("Bisection Solver Initiated.")

def float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid integer.")
            
func_select = int(input("Enter an integer value from 1 - 5 to select the function to be used by the solver: "))
try:
    if func_select < 1 or func_select > 5:
            ValueError
    elif func_select == 1:
            base_function = base_function_1
    elif func_select == 2:
            base_function = base_function_2
    elif func_select == 3:
            base_function = base_function_3
    elif func_select == 4:
            base_function = base_function_4
    elif func_select == 5:
            base_function = base_function_5
except ValueError:
    print("Please select a number from 1 to 5.")
    
e = float_input("Enter a value for tolerance (preferably a number close to zero, like 10^-2): ")  

a = float_input("Enter an integer value for a (left coordinate): ")
b = float_input("Enter an integer value for b (right coordinate): ")
c = value_average(a,b)

if a > b:
    raise ValueError("Please enter a value of a that is smaller than b.")

print("If a =", a, "and b =", b, "then c =", c)

func_a = base_function(a)
func_b = base_function(b)
func_c = base_function(c)

print("f(a) =", func_a,", f(b) =", func_b,", f(c) =", func_c)

final_result = convergence_check(a,b,c,e,func_a,func_b,func_c)
print("For the selected inputs, a root of the function is: ", final_result)


# In[ ]:




