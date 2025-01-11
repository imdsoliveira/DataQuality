# components/sidebar.py
import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

import streamlit as st
from functions.functions import pages_map
from config.config import is_production

PAGES = pages_map()

def create_sidebar():
    # Authenticate only if in production
    if is_production():
        if not st.session_state.get('authentication_status'):
            st.switch_page("/login.py")
            return
    else:
        # If not in production, initialize the necessary session variables
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = True
        if 'name' not in st.session_state:
            st.session_state['name'] = 'Dev User'
    st.markdown("""
    <style>
        /* Esconder elementos padrão do Streamlit */
        [data-testid="stSidebarNav"] {display: none !important;}
        .stDeployButton {display: none !important;}
        section[data-testid="stSidebar"] > div {padding-top: 1rem;}
        
        /* Layout e espaçamento */
        section[data-testid="stSidebar"] {
            background-color: #161B26 !important;
        }
        section[data-testid="stSidebar"] > div {
            padding-top: 1rem;
        }
        
        /* Estilo dos botões */
        section[data-testid="stSidebar"] .stButton button {
            width: 100% !important;
            margin: 0 !important;
            background-color: transparent;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #fff;
            transition: all 0.3s ease;
        }
        section[data-testid="stSidebar"] .stButton button:hover {
            background-color: rgba(151, 166, 195, 0.15);
        }
        
        /* Estilos do selectbox de navegação */
        .stSelectbox [data-baseweb="select"] {
            background-color: transparent;
            border: none;
        }
        .stSelectbox [data-baseweb="select"]:hover {
            background-color: rgba(151, 166, 195, 0.15);
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)
    # Authenticate
    if not st.session_state.get('authentication_status'):
        st.switch_page("/login.py")
        return
    with st.sidebar:
        # Logo
        try:
            st.logo("./app/static/img/logo-azul.png", size="large")
        except:
            #pass
            st.image("./app/static/img/logo-azul.png", width=50)
        # Start current_page
        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = 'Home'
        # Navigation
        st.subheader("Páginas disponíveis")
        pagina = st.selectbox(
            "Selecione a página",
            list(PAGES.keys()),
            index=list(PAGES.keys()).index(st.session_state['current_page']),
            key='navigation_selectbox',
            label_visibility="collapsed"
        )
        
        st.divider()

        st.subheader(f'Welcome *{st.session_state["name"]}*')

        if st.button('Sair'):
            for key in ['authentication_status', 'username', 'name', 'current_page']:
                if key in st.session_state:
                    del st.session_state[key]
            st.switch_page('/login.py')
            return
        if pagina != st.session_state['current_page']:
            st.session_state['current_page'] = pagina
            try:
                arquivo = PAGES[pagina]
                st.switch_page(f"pages/{arquivo}.py")
            except Exception as e:
                st.error(f"Erro ao carregar página: {str(e)}")