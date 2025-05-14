import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Dati di esempio: etichette reali e previste
y_true = [0, 1, 0, 2, 2, 1, 0, 1, 2, 2]
y_pred = [0, 1, 0, 2, 1, 1, 0, 2, 2, 2]

# Creazione della matrice di confusione
cm = confusion_matrix(y_true, y_pred)
labels = ["Classe 0", "Classe 1", "Classe 2"]

# Funzione per visualizzare la matrice di confusione
def plot_confusion_matrix(cm, labels):
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    ax.set_xlabel("Predizioni")
    ax.set_ylabel("Valori reali")
    ax.set_title("Matrice di Confusione")
    return fig

# Creazione dell'app Streamlit
st.title("Esempio di Matrice di Confusione con Streamlit e Matplotlib")

fig = plot_confusion_matrix(cm, labels)
st.pyplot(fig)
