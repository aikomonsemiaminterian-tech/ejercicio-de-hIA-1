import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(page_title="Mi Dashboard Pro", layout="wide")

# 2. Simulación de datos
def load_data():
    df = pd.DataFrame({
        "Fecha": pd.date_range(start="2023-01-01", periods=100),
        "Ventas": np.random.randint(100, 500, size=100),
        "Categoría": np.random.choice(['Electrónica', 'Hogar', 'Moda'], 100)
    })
    return df

df = load_data()

# 3. Barra Lateral (Filtros)
st.sidebar.header("Filtros de Usuario")
categoria_seleccionada = st.sidebar.multiselect(
    "Selecciona Categoría:",
    options=df["Categoría"].unique(),
    default=df["Categoría"].unique()
)

df_filtrado = df[df["Categoría"].isin(categoria_seleccionada)]

# 4. Título y Métricas Principales
st.title("📊 Dashboard de Rendimiento Comercial")
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales", f"${df_filtrado['Ventas'].sum():,}")
col2.metric("Promedio Diario", f"${df_filtrado['Ventas'].mean():.2f}")
col3.metric("Registros", len(df_filtrado))

# 5. Visualización de Gráficos
st.subheader("Tendencia de Ventas en el Tiempo")
fig = px.line(df_filtrado, x="Fecha", y="Ventas", color="Categoría", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# 6. Tabla de Datos Detallada
with st.expander("Ver base de datos completa"):
    st.dataframe(df_filtrado, use_container_width=True)
