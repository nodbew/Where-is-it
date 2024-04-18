'''
Collection of functions that recieve pd.DataFrame as an input and apply 
main function to every element of it.
Used to easen converting input to a correct format in streamlit_app.py
'''
from components.error import raise_error
import streamlit as st

def broadcast_add(df):
  '''
  Base method is main.class.DataAdministor.add
  '''
  # Drop row with None since it might cause an error (Key already exists)
  indexes = (df['名前'] != None)
  items = df[indexes]

  # Add datas
  add = st.session_state._DataAdmin.add
  for name,location in items:
    add(name,location)
  return

def filter(input): 
  '''
  Filters dataframe by whether input is contained in a key of st.session_state._name_location_dictionary
  '''
  df = st.session_state._name_location_dictionary
  return df[df['名前'].isin(input)]

def edit(new_df):
  items = new_df[new_df['名前'] != None]
  df = st.session_state._name_location_dictionary
  for name,location in items:
    if name not in df:
      raise_error(f'{name}は登録されていません')
    else:
      name[df] = location
  return
