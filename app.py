#opcion 1
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Proyecto Sprint 7 - Datos de un Sitio de Venta de Autos 🚗")

# Histograma agrupado por año y marca
selected_brands = st.multiselect(
    "Selecciona una o varias marcas:",
    options=car_data['model'].str.split().str[0].unique(),
    default=["ford", "toyota"]  # puedes poner marcas comunes por defecto
)

if st.button('Cantidad de autos por año y marca'):
    filtered_data = car_data[car_data['brand'].isin(selected_brands)]
    st.write(f'Histograma: cantidad de autos para {", ".join(selected_brands)}')
    fig = px.histogram(
        filtered_data,
        x="model_year",
        color="brand",
        barmode="group",
        title="Cantidad de carros por año y marca"
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
