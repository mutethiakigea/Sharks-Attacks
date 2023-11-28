#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing library
import pandas as pd


# In[2]:


# loading the CSV file
file_path = 'SharkAttack.csv' 
data = pd.read_csv(file_path)


# In[3]:


# data summary
print("Initial data summary:")
print(data.head())


# In[4]:


# Identifying duplicate records based on 'Case Number'
duplicate_records = data[data.duplicated(subset='Case Number', keep=False)]


# In[5]:


# Displaying duplicate records found
print("\nDuplicate records:")
print(duplicate_records)


# In[6]:


# Removing duplicates and keep the first occurrence
cleaned_data = data.drop_duplicates(subset='Case Number', keep='first')


# In[7]:


# cleaned data summary
print("\nCleaned data summary:")
print(cleaned_data.head())


# In[8]:


# a new file
output_file_path = 'cleaned_shark_attack_data.csv'  
cleaned_data.to_csv(output_file_path, index=False)
print(f"\nCleaned data saved to {output_file_path}")

