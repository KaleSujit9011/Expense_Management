import os
import sys
import streamlit as st
try:
    project_root = os.path.join(os.path.dirname(__file__), '..')
    sys.path.insert(0,project_root)
except NameError:
    project_root = os.getcwd()  # fallback when __file__ isn't defined


st.write("Current working directory:", os.getcwd())
st.write("Current sys.path:", sys.path)
