'''
Collection of functions that recieve pd.DataFrame as an input and apply 
main function to every element of it.
Used to easen converting input to a correct format in streamlit_app.py
'''
from components.postprocess import raise_error
import streamlit as st
import numpy as np
import pandas as pd
from time import time

def broadcast_add(df):
  '''
  Base method is main.class.DataAdministor.add
  '''
  # Drop row with None since it might cause an error (Key already exists)
  indexes = (df['名前'] != None)
  items = df[indexes].to_numpy()
  
  # Add datas
  add = st.session_state._DataAdmin.add
  for name,location in items:
    add(name,location)
  return

def _name_location_dic_to_df():
  dic = st.session_state._name_location_dictionary
  names,locations = np.array([dic.keys()]),np.array([dic.values()])
  return pd.DataFrame(np.stack([names,locations]).transpose(),columns=['名前','場所'])

def filter(input,fullmatch): 
  '''
  Filters dataframe by whether input is contained in a key of st.session_state._name_location_dictionary
  '''
  st.success(f"debug info:{st.session_state._name_location_dictionary}")
  if fullmatch:
    try:
      return pd.DataFrame([[input,st.session_state._name_location_dictionary[input]]],
                          columns = ['名前','場所'])
    except KeyError:
      return pd.DataFrame([[None,None]],columns = ['名前','場所'])

  else:
    names = np.array(
      [name for name in st.session_state._name_location_dictionary.keys() 
       if name.find(input) != -1]
    )
    values = np.array(
      [st.session_state._name_location_dictionary[name] for name in names]
    )

    result = pd.DataFrame(np.stack([names,values]).transpose(),
                          columns=['名前','場所'])
    st.success(f'filter function successfully called on {time()}, returned {result}')
    return result

def edit(new_df):
  items = new_df[new_df['名前'] != None]
  df = _name_location_dic_to_df()
  for name,location in items:
    if name not in df:
      raise_error(f'{name}は登録されていません')
    else:
      name[df] = location
  st.success('変更しました')
  return
