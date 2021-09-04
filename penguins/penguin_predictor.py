#!/usr/bin/env python
# coding: utf-8

# In[2]:
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# In[3]:


penguins = pd.read_csv('penguins.csv')

# In[5]:


penguins.info()

# In[6]:


penguins.dropna(inplace=True)

# In[7]:


penguins

# In[31]:


y = penguins['species']
X = penguins.iloc[:, 1:-1]

# In[40]:


cateogrical_features = X.select_dtypes(object)
numerical_features = X.select_dtypes(float)

# In[33]:


from sklearn.preprocessing import OneHotEncoder

# In[34]:


encoder = OneHotEncoder()
cateogrical_features_one_hot = encoder.fit_transform(cateogrical_features)

# In[35]:


from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# In[44]:


pipeline = ColumnTransformer([
    ('numerical', 'passthrough', numerical_features.columns)
    , ('categorical', OneHotEncoder(), cateogrical_features.columns)
])

# In[45]:


X_prepared = pipeline.fit_transform(X)

# In[46]:


X_prepared

# In[47]:


encoder.categories_

# In[49]:


pipeline.get_feature_names()

# In[50]:


from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# In[52]:


codes, uniques = pd.factorize(y)

# In[55]:


X_train, X_test, y_train, y_test = train_test_split(X_prepared, codes)

# In[56]:


random_forest_classifier = RandomForestClassifier(random_state=15)

# In[57]:


random_forest_classifier.fit(X_train, y_train)

# In[64]:


predictions = random_forest_classifier.predict(X_train)

# In[65]:


score = accuracy_score(y_train, predictions)

# In[66]:


score

# In[67]:


import pickle

# In[68]:


random_forest_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(random_forest_classifier, random_forest_pickle)
random_forest_pickle.close()

# In[70]:


target_pickle = open('penguin_targets.pickle', 'wb')
pickle.dump(uniques, target_pickle)
target_pickle.close()

# In[ ]:

fig, ax = plt.subplots()
sns.barplot(x=random_forest_classifier.feature_importances_, y=pipeline.get_feature_names(), color="salmon")
ax.set(xlabel='Importance'
       , ylabel='Feature'
       , title='Feature importance for Species Predictor')
plt.tight_layout()
fig.savefig('feature_importance.png')