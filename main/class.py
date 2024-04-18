from setting.system_use_variables import SYSTEM_OPS
from components.error import raise_error

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

  def save_to_file(self):
    return bytes(json.dumps(self._dic))

  def load_from_file(self,file):
    data = file.read
    new_dic = json.loads(data)
