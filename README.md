# Proyecto Sprint 7

Este proyecto forma parte del Sprint 7 del curso de Data Analyst.  
La aplicación web permite visualizar información de un data set de anuncios de vehículos de manera interactiva.

## Funcionalidades

- Un histograma de la cantidad de autos disponibles por año y marca.
- Un diagrama de dispersión entre kilometraje y precio.


## Archivos

- app.py → código de la aplicación web en Streamlit
- requirements.txt → librerías para ejecutar la app
- vehicles_us.csv → dataset
- notebooks/EDA.ipynb → análisis exploratorio de datos (realizado en google colab)

## Cómo ejecutar la app en local

Instalar dependencias:
pip install -r requirements.txt

Ejecutar la aplicación:
streamlit run app.py

La aplicación se abrirá automáticamente en tu navegador en http://localhost:8501/
