import streamlit as st
st.session_state._errors = {}

def raise_error(message,execution=2):
  postprocess = st.session_state._postprocess

  # Command to execute while postprocess
  command = 'st.error(' + message + ')'

  # Have to raise 2 times because 1 will be executed when button is true
  # If only once, error will disappear due to a rerun after a button is released
  if command  in postprocess:
    postprocess[command] += execution
  else:
    postprocess[command] = execution

  return

def success(message,execution=2):
  postprocess = st.session_state._postprocess

  # Command to execute while postprocess
  command = 'st.success(' + message + ')'

  if command in postprocess:
    postprocess[command] += execution
  else:
    postprocess[command] = execution

  return

# postprocess
for key in st.session_state._postprocess.keys():
  st.session_state._errors[key] -= 1

  # Raise error
  exec(key)

  # Stop raising error when there is no execution count remaining
  if st.session_state._errors[key] == 0:
    del st.session_state._errors[key]
