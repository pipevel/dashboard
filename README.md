import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="La Papaya - Unit Economics", page_icon="🍊", layout="wide")

st.title("🍊 La Papaya - Dashboard de Unit Economics")
st.markdown("### Medición de impacto, subsidio cruzado (Silver/Seniors) y sostenibilidad financiera")

# Barra Lateral para Variables Dinámicas
st.sidebar.header("🎛️ Simulador de Variables")
usuarios_activos = st.sidebar.number_input("Usuarios Activos", value=684, step=10)
mensualidad_senior = st.sidebar.slider("Mensualidad Eco Senior ($)", min_value=5000000, max_value=25000000, value=15000000, step=1000000)
costo_senior = st.sidebar.slider("Costo de Operación Senior ($)", min_value=5000000, max_value=20000000, value=12000000, step=1000000)

# Cálculos dinámicos
margen_senior = mensualidad_senior - costo_senior
costo_joven = 800000 # Costo mes plan padrino
ratio_subsidio_cruzado = margen_senior / costo_joven

# Métricas Principales en Pantalla
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Usuarios Activos", f"{usuarios_activos}")
with col2:
    st.metric("Margen por Senior", f"${margen_senior:,.2f}")
with col3:
    st.metric("Subsidio Cruzado (RSC)", f"{ratio_subsidio_cruzado:.2f}x")
with col4:
    st.metric("ARR (Proyectado Anual)", "$81,200,000.00")

st.markdown("---")

# Secciones del Negocio
tab1, tab2, tab3 = st.tabs(["📊 Unit Economics", "🔥 Burn Rate", "💰 Ingresos Operativos"])

with tab1:
    st.subheader("Métricas de Sostenibilidad (Silver vs Jóvenes)")
    data_ue = {
        "Métrica": ["Mensualidad Eco Senior", "Costos Mes Eco Senior", "Margen Eco Senior", "Costo Plan Padrino Joven", "Ratio de Subsidio Cruzado"],
        "Valor": [f"${mensualidad_senior:,.2f}", f"${costo_senior:,.2f}", f"${margen_senior:,.2f}", f"${costo_joven:,.2f}", f"{ratio_subsidio_cruzado:.2f}"]
    }
    st.table(pd.DataFrame(data_ue))

with tab2:
    st.subheader("Análisis de Consumo de Caja (Burn Rate)")
    col_burn1, col_burn2 = st.columns(2)
    with col_burn1:
        st.write("**Gross Burn Rate Actual (Mensual):** $193,333.00")
    with col_burn2:
        st.write("**Gross Burn Rate Proyectado (Mensual):** $12,193,333.00 (Incluye Nómina)")

with tab3:
    st.subheader("Distribución de Ingresos Operativos")
    ingresos_df = pd.DataFrame({
        "Fuente": ["Grupo Textil", "Calima", "Javeriana", "Icesi", "Comfandi", "Donación Internacional"],
        "Monto ($)": [6000000, 70000000, 700000, 1500000, 3000000, 4000000]
    })
    st.bar_chart(data=ingresos_df, x="Fuente", y="Monto ($)")# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

Prerequisite: install `uv` if you don't already have it.

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. Sync the dependencies

   ```
   $ uv sync
   ```

2. Run the app

   ```
   $ uv run streamlit run streamlit_app.py
   ```
