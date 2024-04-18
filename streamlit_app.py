import streamlit as st
from main.dclass import DataAdminister
# This has to be here because components.general uses session_state._name_location_dictionaru
# Which is defined in DataAdminister.__init__()
st.session_state._DataAdmin = DataAdminister()

import pandas as pd
from main import general

# Initializations
# Alias; easier to write
Data = st.session_state._DataAdmin

# Necessary components
main,data,files = st.tabs(['一覧','データ管理','保存'])

with main:
  st.write(st.session_state._name_location_dictionary)
  st.write('ようこそ一覧へ！ここでは登録されたものの位置の一覧を確認できます')
  input = st.text_input('絞り込み...')
  fullmatch = st.checkbox('完全一致')
  st.dataframe(general.filter(input,fullmatch))

with data:
  st.write('ようこそデータ管理へ！ここでは登録を変更したり、削除したりできます')

  # Add a data
  st.title('追加')
  st.info('直接書き込めます...')
  edited_df = st.data_editor(pd.DataFrame([[None,None]],columns=['名前','場所']),num_rows='dynamic')
  if st.button('追加する'):
    general.broadcast_add(edited_df)

  # Delete data
  st.title('削除')
  name = st.text_input('削除したいものの名前を入力してください')
  if st.button('削除する'):
    Data.delete(name)

  # Edit data
  st.info('直接書き換えられます！')
  input = st.text_input('絞り込み...',key='edit_input')
  fullmatch = st.checkbox('完全一致',key='edit_fullmatch')
  df = st.dataframe(general.filter(input,fullmatch))
  if st.button('変更する'):
    general.edit(df)

with files:
  st.write('保存タブへようこそ！ここでは現在のデータをファイルに保存したり、過去に保存したファイルから読み込んだりできます')

  # Save to a file
  st.title('保存')
  st.download_button(label = '保存する',
                     data = Data.save_to_file())

  # Load from a file
  st.title('アップロード')
  f = st.file_uploader('アップロード')
  if f != None:
    Data.load_from_file(f)
