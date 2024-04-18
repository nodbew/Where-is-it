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

  # Stop raising error when there is no execution count remaining
  if st.session_state._errors[key] == 0:
    del st.session_state._errors[key]

  # Raise error
  st.error(st.session_state._errors[key])
