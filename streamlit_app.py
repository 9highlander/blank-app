import streamlit as st
import importlib

st.sidebar.title("Navigazione")
pagina = st.sidebar.radio("Seleziona una pagina", ["Home", "Analisi", "Matrix"])

# Mappatura delle pagine
pagine_dict = {
    "Home": "pages.home",
    "Analisi": "pages.analisi",
    "Matrix": "pages.matrix"
}

# Carica la pagina selezionata dinamicamente
if pagina in pagine_dict:
    pagina_modulo = importlib.import_module(pagine_dict[pagina])
    pagina_modulo.show()
