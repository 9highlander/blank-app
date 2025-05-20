import streamlit as st

def show():
    st.title("Analisi dei Dati")
    st.write("Qui puoi caricare e analizzare i tuoi dati.")

# Caricamento file CSV
uploaded_file = st.file_uploader("Carica un file CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Anteprima dei dati:")
    st.dataframe(df)

    # Esegui un'analisi esterna (ipotizziamo un altro script Python)
    if st.button("Esegui Analisi"):
        subprocess.run(["python", "scripts/analisi_esterna.py"])
        st.success("Analisi completata!")