import streamlit as st
import pandas as pd
from components import general
from main.class import DataAdminister

# Initializations
st.session_state._DataAdmin = DataAdminister()
# Alias; easier to write
Data = st.session_state._DataAdmin

# Necessary components
main,data,files = st.tabs(['一覧','データ管理','保存'])

with main:
  st.write('ようこそ一覧へ！ここでは登録されたものの位置の一覧を確認できます')
  input = st.text_input('絞り込み...')
  st.dataframe(general.filter(input))

with data:
  st.write('ようこそデータ管理へ！ここでは登録を変更したり、削除したりできます')

  # Add a data
  st.title('追加')
  st.info('直接書き込めます...')
  edited_df = st.data_editor(pd.DataFrame([[None,None]],columns=['名前','場所']))
  if st.button('追加する'):
    general.broadcast_add(edited_df)
    # Reset dataframe for adding
    edited_df = st.data_editor(pd.DataFrame([[None,None]],columns=['名前','場所'])))

  # Delete data
  st.title('削除')
  name = st.text_input('削除したいものの名前を入力してください')
  if st.button('削除する'):
    Data.delete(name)

  # Edit data
  st.info('直接書き換えられます！')
  input = st.text_input('絞り込み...')
  df = st.dataframe(general.filter(input))
  if st.button('変更する'):
    general.edit(df)

with files:
  st.write('')

  # Save to a file
  st.write('保存する')
  st.download_button(Data.save_to_file)

  # Load from a file
  f = st.file_uploader('アップロード')
  Data.load_from_file(f)
