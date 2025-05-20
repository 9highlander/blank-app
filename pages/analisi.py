import streamlit as st
import pandas as pd

def show():
    st.title("Analisi del Dataset CSV 📊")

    # Caricamento del file CSV
    uploaded_file = st.file_uploader("Carica un file CSV", type=["csv"])

    if uploaded_file is not None:
        # Lettura del dataset
        df = pd.read_csv(uploaded_file)

        # Mostrare una panoramica dei dati
        st.subheader("Anteprima del Dataset")
        st.write(df.head())

        # Informazioni generali
        st.subheader("Informazioni sul Dataset")
        st.write(df.describe())

        # Visualizzazione delle colonne
        st.subheader("Colonne disponibili")
        st.write(df.columns)

        # Analisi interattiva
        col_selezionata = st.selectbox("Seleziona una colonna per la distribuzione", df.columns)
        if col_selezionata:
            st.subheader(f"Distribuzione dei valori - {col_selezionata}")
            st.hist_chart(df[col_selezionata])

