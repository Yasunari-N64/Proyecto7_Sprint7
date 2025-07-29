import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("Análisis de Vehículos Usados")

# Cargar datos
vehicles_df = pd.read_csv('vehicles_us.csv')
vehicles_df = vehicles_df.dropna(
    subset=['price', 'odometer', 'condition', 'fuel', 'model_year', 'type'])

# Menú desplegable
chart_option = st.selectbox("Seleccionar Gráfico",
                            ["Distribución de Precios",
                             "Distribución de Kilometraje",
                             "Precio vs. Kilometraje",
                             "Condición vs. Kilometraje",
                             "Condición vs. Precio",
                             "Año Modelo vs. Kilometraje",
                             "Año Modelo vs. Precio",
                             "Vehículos por Tipo",
                             "Vehículos por Tipo de Combustible"])

# Mostrar gráfico según selección
if chart_option == "Distribución de Precios":
    st.write("Distribución de Precios de Vehículos")
    fig = px.histogram(vehicles_df, x="price", title="Distribución de Precios")
    fig.update_xaxes(title_text="Precio (USD)")
    fig.update_yaxes(title_text="Frecuencia")
elif chart_option == "Distribución de Kilometraje":
    st.write("Distribución de Kilometraje de Vehículos")
    fig = px.histogram(vehicles_df, x="odometer",
                       title="Distribución de Kilometraje")
    fig.update_xaxes(title_text="Kilometraje (millas)")
    fig.update_yaxes(title_text="Frecuencia")
elif chart_option == "Precio vs. Kilometraje":
    st.write("Precio vs. Kilometraje por Modelo")
    fig = px.scatter(vehicles_df, x="odometer", y="price", color="model",
                     title="Precio vs. Kilometraje")
    fig.update_xaxes(title_text="Kilometraje (millas)")
    fig.update_yaxes(title_text="Precio (USD)")
elif chart_option == "Condición vs. Kilometraje":
    st.write("Condición vs. Kilometraje por Condición")
    fig = px.scatter(vehicles_df, x="condition", y="odometer", color="condition",
                     title="Condición vs. Kilometraje")
    fig.update_xaxes(title_text="Condición")
    fig.update_yaxes(title_text="Kilometraje (millas)")
elif chart_option == "Condición vs. Precio":
    st.write("Condición vs. Precio por Condición")
    fig = px.scatter(vehicles_df, x="condition", y="price", color="condition",
                     title="Condición vs. Precio")
    fig.update_xaxes(title_text="Condición")
    fig.update_yaxes(title_text="Precio (USD)")
elif chart_option == "Vehículos por Tipo de Combustible":
    st.write("Cantidad de Vehículos por Tipo de Combustible")
    fuel_counts = vehicles_df['fuel'].value_counts().reset_index()
    fuel_counts.columns = ['fuel', 'count']
    fig = px.bar(fuel_counts, x='fuel', y='count', color='fuel',
                 title="Vehículos por Tipo de Combustible")
    fig.update_xaxes(title_text="Tipo de Combustible")
    fig.update_yaxes(title_text="Cantidad de Vehículos")
elif chart_option == "Año Modelo vs. Kilometraje":
    st.write("Año Modelo vs. Kilometraje por Modelo")
    fig = px.scatter(vehicles_df, x="model_year", y="odometer", color="model",
                     title="Año Modelo vs. Kilometraje")
    fig.update_xaxes(title_text="Año del Modelo")
    fig.update_yaxes(title_text="Kilometraje (millas)")
elif chart_option == "Año Modelo vs. Precio":
    st.write("Año Modelo vs. Precio por Modelo")
    fig = px.scatter(vehicles_df, x="model_year", y="price", color="model",
                     title="Año Modelo vs. Precio")
    fig.update_xaxes(title_text="Año del Modelo")
    fig.update_yaxes(title_text="Precio (USD)")
elif chart_option == "Vehículos por Tipo":
    st.write("Cantidad de Vehículos por Tipo")
    type_counts = vehicles_df['type'].value_counts().reset_index()
    type_counts.columns = ['type', 'count']
    fig = px.bar(type_counts, x='type', y='count', color='type',
                 title="Vehículos por Tipo")
    fig.update_xaxes(title_text="Tipo de Vehículo")
    fig.update_yaxes(title_text="Cantidad de Vehículos")

fig.update_layout(template='plotly_white')
st.plotly_chart(fig, use_container_width=True)

# Mostrar DataFrame completo
st.write("Datos Completos de Vehículos", vehicles_df)
