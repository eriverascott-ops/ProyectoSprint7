#opcion 1
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Proyecto Sprint 7 - Datos de un Sitio de Venta de Autos 🚗")

# Histograma agrupado por año y marca
hist_button = st.button('Cantidad de autos por año y marca')
if hist_button:
    car_data['brand'] = car_data['model'].str.split().str[0]
    st.write('Histograma: cantidad de autos por año y marca')
    fig = px.histogram(
        car_data,
        x="model_year",
        color="brand",
        barmode="group",
        title="Cantidad de carros por año y marca",
        labels={"brand": "Marca", "model_year": "Año"}
    )
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión odómetro vs precio
scatter_button = st.button('Relación entre Millaje y precio')
if scatter_button:
    st.write('Relación entre Millaje y precio')
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model",
        title="Relación entre Millaje y Precio",
        labels={"odometer": "Millaje", "price": "Precio en USD"}
    )
    st.plotly_chart(fig, use_container_width=True)
