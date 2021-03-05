#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:37:20 2021

@author: arpanganguli
"""
import sys
sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages')

import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, NVARCHAR
import os

# create SQL database
# sqlite:////absolute/path/to/file.db

engine_asian = create_engine('sqlite:////Users/arpanganguli/Documents/Professional/Projects/BAMEUK/Data/SQL/GB_Asian.db', echo = True) 
engine_black = create_engine('sqlite:////Users/arpanganguli/Documents/Professional/Projects/BAMEUK/Data/SQL/GB_Black.db', echo = True)
engine_minority_ethnic = create_engine('sqlite:////Users/arpanganguli/Documents/Professional/Projects/BAMEUK/Data/SQL/GB_Minority_Ethnic.db', echo = True)  
engine_white = create_engine('sqlite:////Users/arpanganguli/Documents/Professional/Projects/BAMEUK/Data/SQL/GB_White.db', echo = True) 

meta = MetaData()

table = Table(
    'table', meta
    ,Column('Geography_name', NVARCHAR)
    ,Column('Geography_code', NVARCHAR)
    ,Column('Value',Float))

meta.create_all(engine_asian)
meta.create_all(engine_black)
meta.create_all(engine_minority_ethnic)
meta.create_all(engine_white)

# create SQL files from existing Excel files

root = r'/Users/arpanganguli/Documents/Professional/Projects/BAMEUK/Data/Excel'


df_asian = pd.read_excel(os.path.join(root, 'GB_Asian.xlsx'))
df_asian.to_sql('table', con=engine_asian, if_exists='replace')

df_black = pd.read_excel(os.path.join(root, 'GB_Black.xlsx'))
df_black.to_sql('table', con=engine_black, if_exists='replace')

df_minority_ethnic = pd.read_excel(os.path.join(root, 'GB_Minority_Ethnic.xlsx'))
df_minority_ethnic.to_sql('table', con=engine_minority_ethnic, if_exists='replace')

df_white = pd.read_excel(os.path.join(root, 'GB_White.xlsx'))
df_white.to_sql('table', con=engine_white, if_exists='replace')