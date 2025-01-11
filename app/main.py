import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

import streamlit as st
import pandas as pd
from src.schema import ContratoFuncionarios

def validar(csv):
    try:
        df = pd.read_csv(csv)
        erros = []
        dados_validos = []
        
        for idx, row in df.iterrows():
            try:
                ContratoFuncionarios(**row.to_dict())
            except Exception as e: # Captura a exceção
                erros.append(f"Erro na linha {idx+2}: {e}")
        if erros:
            st.error(f"Ocorreram erros ao validar o CSV")
            for erro in erros:
                st.error(erro)
        else:
            st.success("CSV validado com sucesso!")
            return True

    except Exception as e:
        st.error(f"Error ao ler o arquivo CSV: {e}")
    
def main():
    st.set_page_config(page_title="Validador de CSV", page_icon=":bar_chart:", layout="wide")
    st.title("Validador de CSV")
    csv = st.file_uploader("Upload CSV", type=["csv"])
    btn = st.button("Validar CSV")
    
    if btn and csv is not None:
        validar(csv)

if __name__ == "__main__":
        main()
