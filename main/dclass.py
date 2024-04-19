from components.postprocess import raise_error
import json
import streamlit as st
import pandas as pd

class DataAdminister:
  '''
  Collection of methods to edit datas in st.session_state.name_location_dictionary
  '''
  def __init__(self):
    if "_name_location_dictionary" not in st.session_state:
        st.session_state._name_location_dictionary = dict()
    return

  def add(self,name,location):
      name = name.strip()
      if name in st.session_state._name_location_dictionary:
        raise_error(f'{name}は既に{st.session_state._name_location_dictionary[name]}に存在します')
        return
        
      else:
        st.session_state._name_location_dictionary[name] = location
        st.success('追加しました')
        return

  def delete(self,name):
    try:
      del st.session_state._name_location_dictionary[name]
      st.success('削除しました')
    except KeyError:
      raise_error(f'{name}という名前のものはありません')
    return
    
  def save_to_file(self):
    return json.dumps(st.session_state._name_location_dictionary).encode()

  def load_from_file(self,file):
    data = file.read()

    # Get dictionary from file
    try:
      new_dic = json.loads(data)
    except JSONDecodeError:
      raise_error('無効なファイル形式です')

    # Assert new_dic is a dictionary
    if type(new_dic) != dict:
      raise_error('無効なファイル形式です')

    # Assert all elements in new_dic are str
    if not all(map(isinstance,new_dic.keys(),[str]*len(new_dic))):
      raise_error('無効なファイル形式です')
    if not all(map(isinstance,new_dic.values(),[str]*len(new_dic))):
      raise_error('無効なファイル形式です')

    # Add data
    for key,value in new_dic.items():
      self.add(key,value)

    st.success('保存しました')
    return
