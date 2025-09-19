import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Proyecto Sprint 7 - Datos de un Sitio de Venta de Autos 🚗")

car_data['brand'] = car_data['model'].str.split().str[0]

# Histograma
selected_brands = st.multiselect(
    "Selecciona una marca para visualizar:",
    options=car_data['brand'].unique(),
    default=car_data['brand'].unique()[:3]
)

filtered_data_brand = car_data[car_data['brand'].isin(selected_brands)]

if st.button('Cantidad de autos por año y marca'):

    fig = px.histogram(
        filtered_data_brand,
        x="model_year",
        color="brand",
        barmode="group",
        title="Cantidad de carros por año y marca"
    )
    st.plotly_chart(fig, use_container_width=True)

selected_models = st.multiselect(
    "Selecciona un modelo para visualizar:",
    options=car_data['model'].unique(),
    default=car_data['model'].unique()[:3]
)

filtered_data_model = car_data[car_data['model'].isin(selected_models)]

# Gráfico de dispersión
if st.button('Relación entre Millaje y precio'):
    fig = px.scatter(
        filtered_data_model,
        x="odometer",
        y="price",
        color="model",
        title="Relación entre Millaje y Precio",
        labels={"odometer": "Millaje", "price": "Precio en USD"}
    )
    st.plotly_chart(fig, use_container_width=True)
