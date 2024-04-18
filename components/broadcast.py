'''
Collection of functions that recieve pd.DataFrame as an input and apply 
main function to every element of it.
Used to easen converting input to a correct format in streamlit_app.py
'''
import streamlit as st

def broadcast_add(df):
  indexes = (df['名前'] != None)

