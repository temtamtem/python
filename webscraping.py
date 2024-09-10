#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')


URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


elo=pd.read_html(URL)
tabela=elo[3]
tabela

tabela.columns = range(tabela.shape[1])
tabela

kury=tabela[[0,2]]
kury
#
bury=kury.iloc[1:11,:]

bury.columns=['Country','GDP (Million USD)']
bury

emo = pd.read_html(URL)
tabela2 = emo[3]

tabela2

import requests
url='https://ibm.com/'
r=requests.get(url)
r.status_code
r.headers['date']
dane={'v':'gUmagAluXpk','t':'120s'}
uerelek=''



# In[ ]:




