#!/usr/bin/env python
# coding: utf-8

# In[195]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridSpec
get_ipython().run_line_magic('matplotlib', 'notebook')
plt.style.available
plt.style.use('seaborn-colorblind');


# In[196]:


#DATASET 1 - MAPUTO


df3=pd.read_excel(r'C:\Users\bulule\Downloads\IPC_DE_Maputo.xlsx', skiprows=4,index_col=False)
df4=pd.DataFrame(df3)
df4.columns=df4.columns.str.replace(' ','')
df4['Descrição']=df4['Descrição'].str.replace(' ','')
plt.style.use(style='fast')
df4=df4.drop([0,1])


#Slice on the homologous variation
df_var_homologa=df4.loc[19:24,:]
df_var_homologa=df_var_homologa.drop(['Descrição','Unnamed:1'],axis=1)
df_var_homologa=df_var_homologa.set_index([[1,2,3,4,5,6], 'Ano'])
df_var_homologa.index=[2009, 2010, 2011, 2012, 2013, 2014]
df_var_homologaT=df_var_homologa.T
df_var_homologaT['average_inflation_rate']=df_var_homologaT.mean(axis=1)
df_var_homologa=df_var_homologaT.T
df_maputo_homol=df_var_homologaT


#Slice on the annual average rate
df4_variacao_media=df4.loc[25:,:]
df4_variacao_media=df4_variacao_media.drop(['Descrição','Unnamed:1'],axis=1)
df4_variacao_media=df4_variacao_media.set_index([[1,2,3,4,5,6], 'Ano'])
df4_variacao_media.index=[2009,2010,2011,2012,2013,2014]
df4_variacao_mediaT=df4_variacao_media.T
df4_variacao_mediaT=df4_variacao_media.T
df4_variacao_mediaT['avg_rate']=df4_variacao_mediaT.mean(axis=1)
df4_variacao_media=df4_variacao_mediaT.T
df_maputo_media=df4_variacao_mediaT




# In[197]:


#DATASET2 - - BEIRA
df_Beira_2018=pd.read_excel(r'C:\Users\bulule\Downloads\IPCBeira_Quadros_Dezembro18.xls', skiprows=8,skipfooter=42, index_col=False)

#Slicing the average inflation
df_Beira_infl=df_Beira_2018.loc[13:,:]
df_Beira_infl=df_Beira_infl.drop(['Descrição','Unnamed: 1'],axis=1)
df_Beira_infl=df_Beira_infl.set_index([[1,2,3], 'Ano'])
df_Beira_infl.index=[2016,2017,2018]
df_Beira_inflT=df_Beira_infl.T
df_Beira_inflT['avg_inflation']=df_Beira_inflT.mean(axis=1)
df_Beira_infl=df_Beira_inflT.T
df_Beira_media=df_Beira_inflT

#Slicing the homologous
df_Beira_homol=df_Beira_2018.loc[10:12,:]
df_Beira_homol=df_Beira_homol.drop(['Descrição','Unnamed: 1'], axis=1)
df_Beira_homol=df_Beira_homol.set_index([[1,2,3], 'Ano'])
df_Beira_homol.index=[2016,2017,2018]
df_Beira_homolT=df_Beira_homol.T
df_Beira_homolT['avg_homol']=df_Beira_homolT.mean(axis=1)
df_Beira_homol=df_Beira_homolT





# In[200]:


#
plt.figure(figsize=(8,6))
gspec = gridSpec.GridSpec(2,1)
ax_beira=plt.subplot(gspec[0,0])
ax_maputo=plt.subplot(gspec[1,0])
plt.subplots_adjust(hspace=0.9)
months=df_var_homologaT.index.values

#Plot Maputo
ax_maputo.plot(months,df_maputo_homol['average_inflation_rate'],'o-',linewidth=1,alpha=0.75, label='average_homologous_rate')
ax_maputo.plot(months,df_maputo_media['avg_rate'],'o-',linewidth=1,alpha=0.75, label='average_inflation_rate')
ax_maputo.set_title('Homologius variation vs average variation in Maputo Province [2009-2014]\n')
ax_maputo.grid(True)
ax_maputo.set_xticklabels(months)
ax_maputo.set_ylabel('Variation in %')
ax_maputo.set_xlabel('MONTHS')
ax_maputo.legend()

#Plot Beira
ax_beira.plot(months, df_Beira_homol['avg_homol'],'o--',linewidth=1,alpha=0.75, label='average_homologous_rate')
ax_beira.plot(months, df_Beira_media['avg_inflation'],'o--',linewidth=1,alpha=0.75, label='average_inflation_rate')
ax_beira.set_title('Homologius variation vs average variation in Beira Province [2016-2018]\n')
ax_beira.grid(True)
ax_beira.set_xticklabels(months)
ax_beira.set_ylabel('Variation in %')
ax_beira.set_xlabel('MONTHS')
ax_beira.legend()


# In[ ]:





# In[ ]:




