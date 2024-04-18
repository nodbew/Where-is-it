from setting.parameters import SYSTEM_OPS
from components.error import raise_error
import json
import streamlit as st

class DataAdminister:
  '''
  Holds an object's location with its name.
  '''
  def __init__(self):
    st.session_state.name_location_dictionary = dict()
    self._dic = st.session_state.name_location_dictionary
    return

  def add(self,name,location):
    if name in SYSTEM_OPS:
      raise_error(f'{name}は使用できません')
      return
      
    else:
      if name in self._dic:
        raise_error(f'{name}は既に{self._dic[name]}に存在します')
        return
        
      else:
        self._dic[name] = location
        return

  def delete(self,name):
    try:
      del self._dic[name]
    except KeyError:
      raise_error(f'{name}という名前のものはありません')
    return

  def show_data(self):
    # Create items arra
    items = np.array(self._dic.items(),dtype='U').reshape((-1,2))
    return pd.DataFrame(items,columns=['名前','場所'])

  def save_to_file(self):
    return json.dumps(self._dic).encode()

  def load_from_file(self,file):
    data = file.read()
    
    try:
      new_dic = json.loads(data)
    except JSONDecodeError:
      raise_error('無効なファイル形式です')
      
    if type(new_dic) != dict:
      raise_error('無効なファイル形式です')
      
    if not all(map(isinstance,new_dic.items(),[(str,str)]*len(new_dic))):
      raise_error('無効なファイル形式です')
      
    for invalid in SYSTEM_OPS:
      try:
        del new_dic[invalid]
        raise_error('無効なファイル形式です')
        
      except KeyError:
        continue

    self._dic |= new_dic
    return
