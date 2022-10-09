#to run this pen terminal and enter the commonds
#1. cd data_app1
#2. streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Data app 1",
    page_icon=" ",
    layout="wide")

st.title(' Data Analytics App')
st.info('this is a simple data analytics app')

@st.cache
def load_data():
    data=pd.read_csv('cps_85_wages.csv')
    return data
data=load_data()
st.dataframe(data,use_container_width=True)


c1,c2=st.columns(2)
c1.header("Data information(numeric")
c2.header("Data columns")
if c1.checkbox('view data information'):
    c1.dataframe(data.describe(),use_container_width=True)
if c2.checkbox('view data columns'):
    c2.dataframe(data.columns,use_container_width=True)

st.header(" Data Summery")
c1,c2=st.columns([1,3])

numerical_columns=data.select_dtypes(include=np.number).columns
categorical_columns=data.select_dtypes(exclude=np.object).columns
index_col=c1.selectbox('select column for index(categorical)',categorical_columns)
values_col=c1.multiselect('select column for values(numerical)',numerical_columns)
agg_func=c1.selectbox('select aggregation function',['mean','sum','count','min','max'])
out=pd.pivot_table(data,index='index_col',values='values_col',aggfunc=agg_func)
st.dataframe(out,use_container_width=True)
