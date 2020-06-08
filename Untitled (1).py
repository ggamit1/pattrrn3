#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[12]:


num = int(input())
row_num = num+num//2+1
space_handler=0
star_handler=0
if num%2!=0:
    
    for i in range(1,row_num+1):
        if i<=num//2+1:
            for j in range(num//2):
                print(' ',end='')
            for j in range(space_handler):
                print(" ",end='')
            space_handler+=1
            for j in range(num-star_handler):
                print('@',end='')
            star_handler+=2
        else:
            if i==num//2+2:
                for j in range(num):
                    print('*',end='')
            else:
                 for j in range(num):
                        if j==0 or j==num-1:
                                print('*',end='')
                        else:
                           print(' ',end='')

        print()


# In[ ]:





# In[ ]:




