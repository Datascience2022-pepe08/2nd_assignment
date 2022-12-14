#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/corazzon/boostcourse-ds-510/master/data/medical_201909.csv.zip", low_memory=False)
df.shape


# ### π Q1. μ κ΅­ μλλ³ μ½κ΅­μλ₯Ό κ΅¬ν΄μ£ΌμΈμ! 
# * μκΆμμ’μλΆλ₯λͺμ΄ μ½κ΅­μΈ κ²μ μ°Ύμ λΉλμλ₯Ό κ΅¬ν΄μ£ΌμΈμ.
# * μ΄ λ, value_counts, groupby, pivot_table λ± λ€μν μ§κ³ λ°©λ²μ ν΅ν΄ κ΅¬ν΄λ³Ό μ μμ΅λλ€.
# * κ°μ κ΅¬νκΈ° νΈν λ°©λ²μ ν΅ν΄ λΉλμλ₯Ό κ΅¬ν©λλ€.

# In[4]:


drug =  df[df["μκΆμμ’μλΆλ₯λͺ"] == "μ½κ΅­"]
drug
drug["μλλͺ"].value_counts()


# ### π Q2. μ¬λ¬λΆμ λ°λ €λλ¬Όκ³Ό κ΄λ ¨λ μ¬μμ νλ μ€ννΈμμ μ·¨μμ νμ¬ μκΆλΆμμ ν΄λ¬λΌλ μμ²­μ λ°μμ΅λλ€. λ³μμ΄λ μ½κ΅­μ μΈκ΅¬λ μ λμΈκ΅¬κ° λ§μ μ§μ­μ μ£Όλ‘ μμΉνκ³  μμ΅λλ€. κ·Έλ λ€λ©΄ λλ¬Όλ³μλ λ³μμ΄λ μ½κ΅­μ΄ λ§μ κ³³μ λ λ§μ΄ μμκΉμ?
# 
# * λΉλμλ₯Ό κ΅¬νκ³  μκ°ν νμ¬ λλ¬Όλ³μμ΄ μ΄λ μ§μ­μ λ§μμ§ λΆμν΄ μ£ΌμΈμ!
# 

# In[39]:


# λ³μ, μ½κ΅­, λλ¬Όλ³μμ μλλ³ λΉμ¨μ value_count λ‘ κ΅¬ν ν data frameμΌλ‘ λ§λ€μ΄μ£ΌκΈ°
animal_hos_df = df[df['μκΆμμ’μλΆλ₯λͺ']=='λλ¬Όλ³μ']['μλλͺ'].value_counts().reset_index()
hospital_df = df[df['μκΆμμ’μ€λΆλ₯λͺ'] == 'λ³μ']['μλλͺ'].value_counts().reset_index()
pharmacy_df = df[df['μκΆμμ’μλΆλ₯λͺ'] == 'μ½κ΅­']['μλλͺ'].value_counts().reset_index()
# column μ΄λ¦μ λ³΄κΈ° μ’κ² λ³κ²½νκ³  indexλ₯Ό μλλͺμΌλ‘ μΌμΉμν€κΈ°
animal_hos_df.columns = ['μλλͺ', 'λλ¬Όλ³μ']
animal_hos_df.set_index('μλλͺ',inplace=True)
hospital_df.columns = ['μλλͺ', 'λ³μ']
hospital_df.set_index('μλλͺ',inplace=True)
pharmacy_df.columns = ['μλλͺ', 'μ½κ΅­']
pharmacy_df.set_index('μλλͺ',inplace=True)
# μΈ κ°μ DataFrameμ λ³ν©μν€κΈ°
total_df = animal_hos_df.join(hospital_df)
total_df = total_df.join(pharmacy_df)
total_df.head()
# κ° column μ μλλ³ μ§μ μλ₯Ό μ΅λκ°μΌλ‘ λλ μ£ΌκΈ°
target_col = ['λλ¬Όλ³μ','λ³μ','μ½κ΅­']
weight_col = total_df[target_col].max()
total_rate_df = total_df / weight_col
total_rate_df.head()

weight_col

# λͺ κ°μ§ μ΅μμΌλ‘ λ λ΄μ©μ νμΈνκΈ° νΈνλλ‘ μμ νκΈ°
# μ μ²΄ figure μ μ¬μ΄μ¦λ₯Ό μ‘°μ 
plt.figure(figsize = (8,8))
sns.heatmap(total_rate_df.sort_values(by='λ³μ', ascending=False), annot=True, fmt='f', linewidths=1.5, cmap='Reds')
plt.title('μλλ³μλ£κΈ°κ΄μ\nλ³μμΌλ‘ μ λ ¬. κ° ν­λͺ©λ³ μ΅λκ°μΌλ‘ λλ  μ κ·ν ν¨')
plt.show()


# ### πQ3. κ°λ¨μ§μ­μλ λ€λ₯Έ μ§μ­μ λΉν΄ νΌλΆκ³Όλ μ±νμΈκ³Όκ° λ§μ λ³΄μλλ€. μ€μ λ‘ ν΄λΉ μ§μ­μ νΌλΆκ³Όλ μ±νμΈκ³Όκ° λ€λ₯Έ μ§μ­μ λΉν΄ μ μ²΄ λ³μ μ μ€μμ μ΄λ μ λμ λΉμ¨μ μ°¨μ§νκ³  μλμ§ μμλ³΄κ² μ΅λλ€.
# 
# * μμΈμ μμ¬ν λ³μ μ€ μκΆμμ’μλΆλ₯λͺμ "νΌλΆ" λ "μ±ν"μ΄ λ€μ΄κ° λΆλ₯λͺμ μ°Ύμ κ΅¬ν΄μ£ΌμΈμ!
# * νΌλΆκ³Ό μ±νμΈκ³Ό μ / μ μ²΄λ³μ μ λ‘ λΉμ¨μ κ΅¬ν΄μ£ΌμΈμ!
# * λΉμ¨μ΄ λμ μμλλ‘ μ λ ¬λκ² κ΅¬ν΄μ£ΌμΈμ!
# * μμμμ μ¬μ©ν κ°μ CSV νμΌμ μ¬μ©νλ©° λ€μμ κ²°κ³Όκ° λμ€λλ‘ κ΅¬ν©λλ€.
# * μμ«μ  λ λ²μ§Έμ§λ¦¬κΉμ§ μΆλ ₯νλ λ°©λ²μ pandas round λ‘ κ²μν΄μ μ¬μ©λ²μ μμλ³΄μΈμ!

# In[35]:


seoul_hos_df = df[(df['μκΆμμ’μ€λΆλ₯λͺ']=='λ³μ') & (df['μλλͺ']=='μμΈνΉλ³μ')]
seoul_total_hos = seoul_hos_df.value_counts('μκ΅°κ΅¬λͺ')
beauty_hos_df = seoul_hos_df[seoul_hos_df['μκΆμμ’μλΆλ₯λͺ'].str.contains('νΌλΆ|μ±ν')].value_counts('μκ΅°κ΅¬λͺ').reset_index()
beauty_hos_df.set_index('μκ΅°κ΅¬λͺ',inplace=True)
beauty_hos_df.columns = ['νΌλΆ|μ±ν']
beauty_hos_df = beauty_hos_df.div(seoul_total_hos, axis='index')
beauty_hos_df.round(2).sort_values(by='νΌλΆ|μ±ν',ascending=False)


# ### πQ4. νκ·  κΈ°λμλͺμ΄ μ μ  κΈΈμ΄μ§λ©΄μ μ€λ² μλ£ μ°μλ μ£Όλͺ©λ°κ³  μμ΅λλ€. μ¬λ¬λΆμ μ€λ² μλ£ μ°μκ³Ό κ΄λ ¨λ μ€ννΈμμ μ·¨μνμ΅λλ€. μ§λλ₯Ό μκ°ννμ¬ 'λΈμΈ/μΉλ§€λ³μ'μ΄ μ£Όλ‘ μ΄λμ μμΉνκ³  μλμ§λ₯Ό μ°Ύμλ³΄κ³ μ ν©λλ€.
# 
# * folium μ ν΅ν΄ μ§λμ μ κ΅­μ 'λΈμΈ/μΉλ§€λ³μ'μ νμν΄ μ£ΌμΈμ!
# * λ€μκ³Ό κ°μ΄ μκ°ν νλ©°, folium μ λ¬Έμλ₯Ό μ°Έκ³ νμ¬ λ€λ₯Έ κΈ°λ₯μ μ¬μ©νμ¬ μ’ λ λ©μ§κ² μ§λλ₯Ό κΎΈλ©°λ μ’μ΅λλ€.
# * folium λ¬Έμ : https://python-visualization.github.io/folium/quickstart.html

# In[ ]:


import folium
df_korea_elder = df[df["μκΆμμ’μλΆλ₯λͺ"] =="λΈμΈ/μΉλ§€λ³μ"]
df_korea_elder
df_korea_elder["μλ"].mean()
df_korea_elder["κ²½λ"].mean()
map = folium.Map(location=[df_korea_elder["μλ"].mean(),df_korea_elder["κ²½λ"].mean()], zoom_start=12)

for n in df_korea_elder.index:
    name = df_korea_elder.loc[n,"μνΈλͺ"]
    address = df_korea_elder.loc[n,"λλ‘λͺμ£Όμ"]
    popup = f"{name}-{address}"
    location = [df_korea_elder.loc[n,"μλ"], df_korea_elder.loc[n,"κ²½λ"]]
    print(popup)
    folium.Marker(
        location = location,
        popup = popup,
    ).add_to(map)
map

