import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Proyecto Sprint 7 - Datos de un Sitio de Venta de Autos 🚗')

#histograma
build_histogram = st.checkbox('Mostrar histograma por año y marca')
if build_histogram:
    car_data['brand'] = car_data['model'].str.split().str[0]
    fig = px.histogram(
        car_data,
        x="model_year",
        color="brand",
        barmode="group",
        title="Cantidad de carros por año y marca"
    )
    st.plotly_chart(fig, use_container_width=True)

# dispersión
build_scatter = st.checkbox('Mostrar gráfico odómetro vs precio')
if build_scatter:
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model",
        title="Relación entre Millaje y Precio",
        labels={"odometer": "Millaje (millas)", "price": "Precio en USD"}
    )
    st.plotly_chart(fig, use_container_width=True)
