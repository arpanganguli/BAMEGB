#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:46:22 2021

@author: arpanganguli
"""
# import packages

import pandas as pd

# import files

url = '/Users/arpanganguli/Documents/Professional/Projects/BAMEUK/Data/tables/data_by_ethnicity_by_utla.csv'
df = pd.read_csv(url, thousands=',')
print(df.head())

# convert data types

df[['Area','Code']] = df[['Area','Code']].astype('string')
print(df.info())

# create main data frame by grouped ethnicities

df_main = df[['Area'
             ,'Code'
             ,'All categories: Ethnic group'
             ,'Mixed/multiple ethnic group: Total'
             ,'Asian/Asian British: Total'
             ,'Black/African/Caribbean/Black British: Total'
             ,'Other ethnic group: Total'
                  ,'Other ethnic group: Arab'
                  ,'Other ethnic group: Any other ethnic group']]
print(df_main.head())