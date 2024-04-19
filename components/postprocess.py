import streamlit as st
from copy import copy

def initialize():
  if "_postprocess" not in st.session_state:
    st.session_state["_postprocess"] = dict()
  return

def raise_error(message,execution=2):
  # Command to execute while postprocess
  command = 'st.error("' + message + '")'

  # Have to raise 2 times because 1 will be executed when button is true
  # If only once, error will disappear due to a rerun after a button is released
  st.session_state._postprocess[command] = execution

  return

def success(message,execution=2):
  postprocess = st.session_state._postprocess

  # Command to execute while postprocess
  command = 'st.success("' + message + '")'

  if command in postprocess:
    postprocess[command] += execution
  else:
    postprocess[command] = execution

  return

def postprocess():
  # postprocess
  keys_to_delete = set()
  for key in st.session_state._postprocess.keys():
    st.session_state._postprocess[key] -= 1
    # Execute command
    exec(key)

    # Stop raising error when there is no execution count remaining
    if st.session_state._postprocess[key] == 0:
      keys_to_delete.add(key)

    # Delete unneeded keys
    for key in keys_to_delete:
      del st.session_state._postprocess[key]
  return
