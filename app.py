import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Encabezado
st.header("Análisis de Vehículos Usados")

# Cargar datos
vehicles_df = pd.read_csv('vehicles_us.csv')
vehicles_df = vehicles_df.dropna(subset=['price', 'odometer', 'model_year'])

# Botón para mostrar subplots
if st.button("Visualizar Datos de Vehículos Usados"):
    st.write("Análisis de precios, kilometraje, tipo y año de modelo")

    # Crear subplots 2x2
    fig = make_subplots(rows=2, cols=2,
                        subplot_titles=("Distribución de Precios",
                                        "Precio vs. Kilometraje por Modelo",
                                        "Precio Promedio por Tipo",
                                        "Precio Promedio por Año"),
                        column_widths=[0.5, 0.5], row_heights=[0.5, 0.5])

    # Histograma (precio)
    hist_traces = px.histogram(vehicles_df, x="price").data
    for trace in hist_traces:
        fig.add_trace(trace, row=1, col=1)

    # Dispersión (odometer vs. price)
    scatter_traces = px.scatter(
        vehicles_df, x="odometer", y="price", color="model").data
    for trace in scatter_traces:
        fig.add_trace(trace, row=1, col=2)

    # Barras (precio promedio por tipo)
    bar_data = vehicles_df.groupby('type')['price'].mean().reset_index()
    bar_traces = px.bar(bar_data, x='type', y='price', color='type').data
    for trace in bar_traces:
        fig.add_trace(trace, row=2, col=2)

    # Líneas (precio promedio por año)
    line_data = vehicles_df.groupby('model_year')['price'].mean().reset_index()
    line_traces = px.line(line_data, x='model_year',
                          y='price', color_discrete_sequence=['darkgreen']).data
    for trace in line_traces:
        fig.add_trace(trace, row=2, col=1)

    # Etiquetas de ejes
    fig.update_xaxes(title_text="Precio (USD)", row=1, col=1)
    fig.update_yaxes(title_text="Frecuencia", row=1, col=1)
    fig.update_xaxes(title_text="Kilometraje (millas)", row=1, col=2)
    fig.update_yaxes(title_text="Precio (USD)", row=1, col=2)
    fig.update_xaxes(title_text="Tipo de Vehículo", row=2, col=1)
    fig.update_yaxes(title_text="Precio Promedio (USD)", row=2, col=1)
    fig.update_xaxes(title_text="Año del Modelo", row=2, col=2)
    fig.update_yaxes(title_text="Precio Promedio (USD)", row=2, col=2)

    # Actualizar diseño
    fig.update_layout(height=800, width=1000,
                      template='plotly_white', showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

# Mostrar DataFrame completo
st.write("Datos Completos de Vehículos", vehicles_df)
