import streamlit as st
import subprocess

st.sidebar.title("Navigazione")
pagina = st.sidebar.radio("Seleziona una pagina", ["Home", "Analisi", "Report"])

if pagina == "Home":
    st.title("Benvenuto nella Web App!")
elif pagina == "Analisi":
    st.title("Analisi dei dati")
    subprocess.run(["python", "pages/analisi.py"])
elif pagina == "Matrix":
    st.title("Report dettagliato")
    subprocess.run(["python", "pages/report.py"])
