import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

import streamlit as st
import streamlit_authenticator as stauth
from config.config import is_production
from functions.functions import remove_sidebar

# If not in production, go straight to home
if not is_production():
    st.session_state["authentication_status"] = True
    st.session_state["name"] = "Dev User"
    st.switch_page("pages/home.py")
# If in production, continue with the normal login flow

remove_sidebar()

import yaml
from yaml.loader import SafeLoader

with open("./app/auth/auth.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

url_logo = "https://s3.quadrodenegocios.com.br/img/a8z-logo-horizontal.png"

st.markdown(
    f"<img src='{url_logo}' width='200' style='display: block; margin: 0 auto; padding-bottom: 80px'>",
    unsafe_allow_html=True,
)

authenticator.login()

if st.session_state["authentication_status"]:
    st.switch_page("pages/home.py")
elif st.session_state["authentication_status"] == False:
    st.error("Usuario ou senha incorretos")
elif st.session_state["authentication_status"] == None:
    st.warning("Informe seu login e senha")
