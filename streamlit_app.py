import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

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

def prediccion_ventas():
    st.title("Predicción de Ventas")
    st.write("Carga un archivo Excel para realizar predicciones")
    archivo_cargado = st.file_uploader("Elige un archivo Excel", type=["xlsx", "xls"], key="3")

    if archivo_cargado is not None:
        df = pd.read_excel(archivo_cargado)
        # Usamos el año y el mes como features (características) y las ventas como target
        df['Periodo'] = df['Año'] + (df['Mes'] - 1) / 12
        X = df[['Periodo']]
        y = df['Ventas']
        
        # Crear y ajustar el modelo de regresión lineal
        modelo = LinearRegression()
        modelo.fit(X, y)
        
        # Predicción para el siguiente año
        ultimo_año = df['Año'].max()
        nuevos_periodos = np.array([[ultimo_año + (i - 1) / 12] for i in range(1, 13)])
        predicciones = modelo.predict(nuevos_periodos)
        
        # Crear dataframe con las predicciones
        df_predicciones = pd.DataFrame({
            'Año': ultimo_año + 1,
            'Mes': range(1, 13),
            'Ventas': predicciones
        })
        
        # Graficar ventas actuales y predicciones
        df_completo = pd.concat([df, df_predicciones], ignore_index=True)
        fig = px.line(df_completo, x='Mes', y='Ventas', color='Año', title='Predicción de Ventas para el Próximo Año')
        st.plotly_chart(fig)
        st.write("Predicciones del próximo año:")
        st.write(df_predicciones)

st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", "Visualización de datos", "Gráficos interactivos", "Predicción de Ventas"])

if pagina == "Página Principal":
    pagina_inicio()
elif pagina == "Visualización de datos":
    visualizar_datos()
elif pagina == "Gráficos interactivos":
    graficos_interactivos()
elif pagina == "Predicción de Ventas":
    prediccion_ventas()
