#Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Datos 
df = pd.read_csv('https://raw.githubusercontent.com/jsaraujott/datos/refs/heads/main/iris.csv')
df["type"] = df["type"].astype(str)

#Titulo 
st.header("Relacion entre variables de iris",divider="gray")

# Boton para descargar los datos 
st.download_button(
    label="Descargar datos",
    data=df.to_csv(index = False),
    file_name='iris.csv',
)

st.divider()

# Seleccionador de variables
opciones = list(df.columns)[0:4]

v = st. multiselect(
    label = "Seleccione máximo 2 variables",
    options = opciones,
    max_selections = 2,
)

# Boton para ejecutar graficos
analisis_b = st.button(
    label = "Analizar"
    )

st.divider()

#Analisis de datos 
if analisis_b:
    col1, col2 = st.columns(2)
    with col1:

        hist_plot01 = px.histogram(
            data_frame = df,
            x = v[0],
            color = "type",
            title = f"Histograma de {v[0]}",
            #marginal = "box",
        )
        st.plotly_chart(hist_plot01, use_container_width=True)
        prom1 = np.mean(df[v[0]])
        


        c1,c2,c3 = st.columns(3)
        with c1:
            prom1 = np.mean(df[v[0]])
            st.metric(
                label = f"Media de {v[0]}",
                value = round(prom1,2),
                delta = round(prom1 - np.mean(df[v[0]]),2),
                delta_color = "inverse"
            )
        with c2:
            med1 = np.median(df[v[0]])
            st.metric(
                label = f"Mediana de {v[0]}",
                value = round(med1,2),
                delta = round(med1 - np.mean(df[v[0]]),2),
                delta_color = "inverse"
            )
        with c3:
            std1 = np.std(df[v[0]])
            st.metric(
                label = f"Desviación estandar de {v[0]}",
                value = round(std1,2),
                delta = round(std1 - np.mean(df[v[0]]),2),
                delta_color = "inverse"
            )


    with col2:
        
        hist_plot02 = px.histogram(
            data_frame = df,
            x = v[1],
            color = "type",
            title = f"Histograma de {v[1]}",
            #marginal = "box",
        )
        st.plotly_chart(hist_plot02, use_container_width=True)

        c4,c5,c6 = st.columns(3)
        with c4:
            prom2 = np.mean(df[v[1]])
            st.metric(
                label = f"Media de {v[1]}",
                value = round(prom2,2),
                delta = round(prom2 - np.mean(df[v[1]]),2),
                delta_color = "inverse"
            )
        with c5:
            med2 = np.median(df[v[1]])
            st.metric(
                label = f"Mediana de {v[1]}",
                value = round(med2,2),
                delta = round(med2 - np.mean(df[v[1]]),2),
                delta_color = "inverse"
            )
        with c6:
            std2 = np.std(df[v[1]])
            st.metric(
                label = f"Desviación estandar de {v[1]}",
                value = round(std2,2),
                delta = round(std2 - np.mean(df[v[1]]),2),
                delta_color = "inverse"
            )
        
#Grafico de dispersión

if analisis_b and len(v) == 2:

    #Grafico de dispersión
    st.divider()
    dis_plot = px.scatter(
        data_frame = df,
        x = v[0],
        y = v[1],
        color = "type",
        title = f"Grafico de dispersión entre {v[0]} y {v[1]}",
    )
    st.plotly_chart(dis_plot, use_container_width=True)
    correl = np.corrcoef(df[v[0]], df[v[1]])[0,1]
    st.metric(
        label = f"Correlación entre {v[0]} y {v[1]}",
        value = round(correl,2),
        delta = round(correl - np.mean(df[v[0]]),2),
        delta_color = "inverse"
    )

