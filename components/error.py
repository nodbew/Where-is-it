import streamlit as st
st.session_state._errors = {}

def raise_error(message,execution=2):
  errors = st.session_state._errors

  # Have to raise 2 times because 1 will be executed when button is true
  # If only once, error will disappear due to a rerun after a button is released
  if mesage in errors:
    errors[message] += execution
  else:
    errors[command] = execution

  return

# postprocess
for key in st.session_state._errors.keys():
  st.session_state._errors[key] -= 1
  st.error(st.session_state._errors[key])
