import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis interactivo de anuncios de coches 🚗')

# Histograma por año y marca
hist_button = st.button('Mostrar histograma por año y marca')
if hist_button:
    car_data['brand'] = car_data['model'].str.split().str[0]
    st.write('Histograma: cantidad de autos por año y marca')
    fig = px.histogram(
        car_data,
        x="model_year",
        color="brand",
        barmode="group",
        title="Cantidad de carros por año y marca"
    )
    st.plotly_chart(fig, use_container_width=True)

# Gráfico  dispersión odómetro vs precio
scatter_button = st.button('Mostrar gráfico odómetro vs precio')
if scatter_button:
    st.write('Relación entre kilometraje y precio')
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model",
        title="Relación entre Kilometraje y Precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio en USD"}
    )
    st.plotly_chart(fig, use_container_width=True)
