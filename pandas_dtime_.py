# -*- coding: utf-8 -*-
"""pandas-dtime-.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FNrBvkki3Ap8RFnRyi0SBnKlM5FMdIZA
"""

import numpy as np
import pandas as pd
from datetime import datetime

year = 2010
date =  2
month = 3
hour = 20
sec = 19

mydate = datetime(year,date,month,hour,sec)
mydate

pd.to_datetime(mydate)

pd.to_datetime(mydate, dayfirst=True)

mydate = ['2000-31-12']
mydate

pd.to_datetime(mydate,dayfirst=True )

my_c_d = ['13th of October 2020']
pd.to_datetime(my_c_d)

data = pd.read_csv("example.csv")
data

data.to_csv('cade.csv' , index=False)

new = pd.read_csv("cade.csv")
new

url = 'https://en.wikipedia.org/wiki/World_population'

tables = pd.read_html(url)
tables

len(tables)

top_tens =tables[0]

top_tens

top_tens = top_tens.drop(11,axis=0)
top_tens

top_tens = top_tens.drop('#', axis=1)
top_tens

top_tens.columns = ['Countries','2000','2015','2030 Est.']
top_tens

top_tens.to_html("population Est.html")

data =pd.read_excel("my_excel_file.xlsx", sheet_name = 'First_Sheet')
data

from sqlalchemy import create_engine

temp_db = create_engine('sqlite:///:memory:')