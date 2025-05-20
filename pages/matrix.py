import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def show():
    st.title("Matrice di Confusione")
    
    y_true = [0, 2, 2, 1, 0, 1, 2, 2]
    y_pred = [0, 2, 1, 1, 0, 2, 2, 2]
    
    cm = confusion_matrix(y_true, y_pred)
    
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Predizioni")
    ax.set_ylabel("Valori reali")
    ax.set_title("Matrice di Confusione")
    
    st.pyplot(fig)
