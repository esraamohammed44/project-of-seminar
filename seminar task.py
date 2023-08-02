#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gspan-mining


# In[2]:


from gspan_mining.config import parser
from gspan_mining.main import main


# In[3]:


get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


f=open("Chemical_340.txt","r")
print(f.read())


# In[5]:


args_str = '-s 2 -d True -l 5 -p True -w True output3.txt'
FLAGS, _ = parser.parse_known_args(args=args_str.split())


# In[6]:


print(FLAGS)


# In[7]:


gs = main(FLAGS)


# In[ ]:




