import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_inicio():
    st.title("Página Principal")
    st.write("Bienvenido a la aplicación de demostración")
    st.write("Usa el menú de la izquierda para navegar")

st.sidebar.title("Navegación")