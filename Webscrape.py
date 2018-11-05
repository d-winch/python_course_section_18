
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[7]:


r = requests.get("http://pythonhow.com/example.html")
soup = BeautifulSoup(r.content, "html.parser")
all = soup.find_all("div", {"class":"cities"})


# In[6]:


all


# In[10]:


type(all)


# In[11]:


type(all[0])


# In[14]:


all[0].find_all("h2")[0].text


# In[19]:


for tag in all:
    print(tag.find("h2").text)
    print(tag.find("p").text)

