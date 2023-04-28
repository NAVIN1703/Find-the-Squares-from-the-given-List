#!/usr/bin/env python
# coding: utf-8

# In[8]:


def square_list(nums):
    squared_nums = map(lambda x: x**2, nums)
    return list(squared_nums)
my_list =[4, 5, 2, 9]
result = square_list(my_list)
print(result)  # Output: [1, 4, 9, 16, 25]


# In[ ]:




