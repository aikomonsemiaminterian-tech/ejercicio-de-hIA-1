import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página (Debe ser la primera instrucción de Streamlit)
st.set_page_config(
    page_title="Dashboard de Ventas",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Mi Primer Dashboard en Streamlit")
st.markdown("Este dashboard se despliega automáticamente desde GitHub.")

# Generar datos de prueba
@st.cache_data # Esto hace que la app sea más rápida
def cargar_datos():
    df = pd.DataFrame({
        "Fecha": pd.date_range(start="2024-01-01", periods=100),
        "Ventas": np.random.randint(100, 500, size=100),
        "Categoría": np.random.choice(['Electrónica', 'Hogar', 'Moda'], 100)
    })
    return df

df = cargar_datos()

# Sidebar para filtros
st.sidebar.header("Configuración")
categorias = st.sidebar.multiselect(
    "Filtrar por Categoría:",
    options=df["Categoría"].unique(),
    default=df["Categoría"].unique()
)

# Filtrado de datos
df_filtrado = df[df["Categoría"].isin(categorias)]

# Métricas
col1, col2 = st.columns(2)
with col1:
    st.metric("Ventas Totales", f"${df_filtrado['Ventas'].sum():,}")
with col2:
    st.metric("Promedio de Ventas", f"${df_filtrado['Ventas'].mean():.2f}")

# Gráfico de Plotly
fig = px.line(
    df_filtrado, 
    x="Fecha", 
    y="Ventas", 
    color="Categoría",
    title="Evolución de Ventas",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# Mostrar tabla
st.subheader("Detalle de los datos")
st.dataframe(df_filtrado, use_container_width=True)
