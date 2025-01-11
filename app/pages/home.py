# pages/home.py
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

import streamlit as st
from components.sidebar import create_sidebar
from functions.functions import config_pages, logged_in

config_pages()
logged_in()
create_sidebar()

st.title("Dashboard")
st.write(f'Welcome *{st.session_state["name"]}*')
