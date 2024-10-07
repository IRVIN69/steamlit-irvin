import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_inicio():
    st.title("Página Principal")
    st.write("Bienvenido")
    st.write("Podrás leer tu archivo excel y generar gráficos")
    st.image("imagen/torta.gif", caption="Gráficos estadísticos", use_column_width=True)

def visualizar_datos():
    st.title("Visualización de datos")
    st.write("Carga un archivo Excel para visualizar los datos")
    archivo_cargado = st.file_uploader("Elige un archivo Excel", type=["xlsx", "xls"])

    if archivo_cargado is not None:
        df = pd.read_excel(archivo_cargado)
        st.write("Datos del archivo Excel:")
        st.write(df)
        st.write("Estadísticas descriptivas:")
        st.write(df.describe())

def graficos_interactivos():
    st.title("Gráficos interactivos")
    st.write("Carga un archivo Excel para crear gráficos interactivos")
    archivo_cargado = st.file_uploader("Elige un archivo Excel", type=["xlsx", "xls"], key="2")

    if archivo_cargado is not None:
        df = pd.read_excel(archivo_cargado)
        st.write("Elige una columna para el eje X:")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Elige una columna para el eje Y:")
        eje_y = st.selectbox("Eje Y", df.columns)
        
        if st.button("Crear Gráficos"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)


st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", "Visualización de datos", "Gráficos interactivos"])

if pagina == "Página Principal":
    pagina_inicio()
elif pagina == "Visualización de datos":
    visualizar_datos()
elif pagina == "Gráficos interactivos":
    graficos_interactivos()
