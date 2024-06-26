import streamlit as st
import pandas as pd
from components import postprocess
postprocess.initialize()
from main.dclass import DataAdminister

# This has to be here because components.general uses session_state._name_location_dictionary,
# Which is defined in DataAdminister.__init__(), for initialization
st.session_state._DataAdmin = DataAdminister()

from main import general

# Necessary components
main,data,files = st.tabs(['一覧','データ管理','保存'])

# Postprocessing
postprocess.postprocess()

with main:
  st.write('ようこそ一覧へ！ここでは登録されたものの位置の一覧を確認できます')
  input = st.text_input('絞り込み...')
  fullmatch = st.checkbox('完全一致')
  main_df = st.dataframe(general.filter(input,fullmatch))

with data:
  st.write('ようこそデータ管理へ！ここでは登録を変更したり、削除したりできます')

  # Add a data
  st.title('追加')
  st.info('直接書き込めます...')
  edited_df = st.data_editor(pd.DataFrame([[None,None]],columns=['名前','場所']),num_rows='dynamic')
  st.button('追加する',
            on_click = general.broadcast_add,
            args = (edited_df,))

  # Delete data
  st.title('削除')
  name = st.text_input('削除したいものの名前を入力してください')
  st.button('削除する',
            on_click = st.session_state._DataAdmin.delete,
            args = (name,))

  # Edit data
  st.title('編集')
  input = st.text_input('絞り込み...',key='edit_input')
  fullmatch = st.checkbox('完全一致',key='edit_fullmatch')
  st.info('直接書き換えられます！')
  edit_tab_df = st.data_editor(general.filter(input,fullmatch))
  st.button('変更する',
            on_click = general.edit,
            args = (edit_tab_df,))

with files:
  st.write('保存タブへようこそ！ここでは現在のデータをファイルに保存したり、過去に保存したファイルから読み込んだりできます')

  # Save to a file
  st.title('保存')
  st.download_button(label = '保存する',
                     data = st.session_state._DataAdmin.save_to_file())

  # Load from a file
  st.title('アップロード')
  f = st.file_uploader('アップロード',
                       key = 'file',
                       on_change = st.session_state._DataAdmin.load_from_file,
                       args = ('file',))
