import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Justicia Algorítmica",
    page_icon="⚖️",
    layout="wide"
)

# Título
st.title("⚖️ Justicia Algorítmica: ¿Puede un software decidir quién va a prisión?")

# Frase motivadora
st.markdown(
    """
> **“En un mundo donde incluso los algoritmos buscan decidir nuestro destino, recordemos que la verdadera justicia nace de la conciencia humana y el compromiso de construir un futuro más justo”.**
"""
)

st.divider()

# Introducción
st.header("📖 Introducción")
st.write(
"""
En la era de la transformación digital, la Inteligencia Artificial (IA) ha dejado de ser ciencia ficción para convertirse en una herramienta presente en distintos ámbitos de la sociedad. 
Su llegada al sistema judicial plantea preguntas importantes: ¿puede una máquina ayudar a decidir sobre la libertad de una persona? ¿Es posible que un algoritmo prediga el comportamiento humano?

La tecnología está comenzando a utilizarse para analizar grandes volúmenes de datos, apoyar la valoración de pruebas y prevenir delitos. Sin embargo, su uso también plantea retos éticos, legales y sociales.
"""
)

# Sección 1
st.header("1️⃣ El robot en el estrado")
st.write(
"""
La inteligencia artificial ya se utiliza en algunos sistemas judiciales para apoyar decisiones relacionadas con la prisión provisional, la evaluación de riesgos y el análisis de testimonios.

Investigaciones indican que los algoritmos pueden ayudar a identificar patrones que los humanos podrían pasar por alto. Sin embargo, los especialistas advierten que estas herramientas deben ser supervisadas para evitar errores o violaciones de derechos fundamentales.
"""
)

# Sección 2
st.header("2️⃣ ¿Cómo piensa la justicia artificial?")
st.write(
"""
El uso de IA en el derecho se basa en tres pilares principales:

- **Apoyo, no reemplazo:** la IA funciona como asistente del juez.
- **Ética vs eficiencia:** los sistemas pueden priorizar el beneficio social o los derechos individuales.
- **Problema de la caja negra:** algunos algoritmos no explican cómo llegan a sus conclusiones.
"""
)

# Sección 3
st.header("3️⃣ Predicción de violencia de género")
st.write(
"""
Uno de los usos más prometedores de la IA es la prevención de la violencia de género. 
Sistemas de análisis de datos pueden identificar patrones de riesgo y ayudar a las autoridades a actuar antes de que ocurra un delito grave.
"""
)

# Sección 4
st.header("4️⃣ El futuro de la justicia")
st.write(
"""
El principal desafío es garantizar que la tecnología respete los derechos humanos y las garantías legales. 
La inteligencia artificial puede mejorar la eficiencia del sistema judicial, pero la decisión final siempre debe recaer en los jueces y operadores de justicia.
"""
)

st.divider()

# Conceptos clave
st.header("📚 Conceptos clave")

conceptos = {
    "Concepto": [
        "Algoritmo de predicción",
        "Sesgo algorítmico",
        "Sistemas expertos"
    ],
    "Descripción": [
        "Software que analiza datos del pasado para estimar eventos futuros.",
        "Decisiones injustas producidas por datos con prejuicios.",
        "Programas diseñados para ayudar a resolver problemas jurídicos complejos."
    ]
}

df_conceptos = pd.DataFrame(conceptos)

st.table(df_conceptos)

st.divider()

# Resúmenes de artículos
st.header("📑 Resumen de investigaciones")

resumenes = {
    "Artículo": [
        "Altamirano-Yupanqui & Bernuy-Alva (2022)",
        "Carrasco Cabezas (2025)",
        "Espinosa & Clemente (2023)",
        "Neira Pena (2021)",
        "Pérez Castellano & Caterini (2021)",
        "Roa Avella et al. (2023)"
    ],
    "Tema principal": [
        "IA para detectar declaraciones falsas en psicología forense",
        "Uso de IA en la valoración de pruebas judiciales",
        "Percepción social de decisiones tomadas por IA",
        "IA en decisiones sobre prisión provisional",
        "Desafíos de la IA para el sistema penal",
        "Predicción de violencia de género con IA"
    ]
}

df_articulos = pd.DataFrame(resumenes)

st.dataframe(df_articulos, use_container_width=True)

# Gráfico simple
st.header("📊 Áreas de aplicación de la IA en justicia")

datos_grafico = pd.DataFrame({
    "Área": [
        "Análisis de pruebas",
        "Detección de mentiras",
        "Predicción de reincidencia",
        "Prevención de violencia"
    ],
    "Nivel de investigación": [4, 3, 4, 5]
})

st.bar_chart(datos_grafico.set_index("Área"))

st.divider()

st.success("La inteligencia artificial puede ser una herramienta poderosa para la justicia, siempre que exista supervisión humana, transparencia y respeto por los derechos fundamentales.")
