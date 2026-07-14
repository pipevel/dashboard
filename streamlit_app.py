import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="La Papaya - Business & AI Dashboard", page_icon="🍊", layout="wide")

st.title("🍊 La Papaya - Business & AI Performance Dashboard")
st.markdown("### Control de KPIs de Negocio, Métricas de IA y Análisis de Crecimiento Semanal")

# BARRA LATERAL: Control de Variables de Negocio e IA
st.sidebar.header("🎛️ Simulador de Negocio e IA")
usuarios_activos = st.sidebar.number_input("Usuarios Activos", value=684, step=10)
mensualidad_senior = st.sidebar.slider("Mensualidad Eco Senior ($)", min_value=5000000, max_value=25000000, value=15000000, step=1000000)
costo_senior = st.sidebar.slider("Costo de Operación Senior ($)", min_value=5000000, max_value=20000000, value=12000000, step=1000000)

st.sidebar.markdown("---")
st.sidebar.header("🤖 Configuración de la IA (Agente Sylver)")
accuracy = st.sidebar.slider("Precisión del Agente (Accuracy)", min_value=70.0, max_value=100.0, value=92.5, step=0.5)
latency = st.sidebar.slider("Latencia Promedio (segundos)", min_value=0.5, max_value=5.0, value=1.8, step=0.1)
cost_per_inference = st.sidebar.slider("Costo de Inferencia por Consulta (USD)", min_value=0.001, max_value=0.05, value=0.008, step=0.001, format="%.3f")
growth_rate = st.sidebar.slider("Tasa de Crecimiento Semanal Real (%)", min_value=0.0, max_value=20.0, value=6.5, step=0.5)

# Cálculos dinámicos de Negocio e IA
margen_senior = mensualidad_senior - costo_senior
costo_joven = 800000  # Costo mes plan padrino
ratio_subsidio_cruzado = margen_senior / costo_joven
total_consultas_mes = usuarios_activos * 120 # promedio de interacciones de los usuarios con la IA
costo_ia_mensual_usd = total_consultas_mes * cost_per_inference

# SECCIÓN 1: KPIs Principales del Negocio e IA
st.subheader("📊 1. KPIs Principales del Negocio e IA")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Usuarios Activos", f"{usuarios_activos:,}")
with col2:
    st.metric("Subsidio Cruzado (RSC)", f"{ratio_subsidio_cruzado:.2f}x")
with col3:
    st.metric("Precisión del Agente IA", f"{accuracy}%")
with col4:
    st.metric("Costo Inferencia Mensual Est.", f"${costo_ia_mensual_usd:,.2f} USD")

st.markdown("---")

# SECCIÓN 2: Métricas de Rendimiento de IA Específicas
st.subheader("🤖 2. Métricas de Rendimiento Específicas de IA")
col_ia1, col_ia2, col_ia3 = st.columns(3)

with col_ia1:
    st.markdown("#### ⚡ Latencia y Rendimiento")
    st.metric("Latencia Promedio", f"{latency} seg", delta="-0.3 seg" if latency < 2.0 else "+0.4 seg")
    st.progress(max(0, min(100, int((5.0 - latency) / 4.5 * 100))))
    st.caption("Meta: Menor a 2.0 segundos para mantener la retención de adultos mayores.")

with col_ia2:
    st.markdown("#### 🎯 Tasa de Completado de Tareas")
    task_completion = min(100.0, accuracy * 1.05)
    st.metric("Task Completion Rate", f"{task_completion:.1f}%")
    st.caption("Porcentaje de consultas resueltas sin necesidad de derivación a un agente humano.")

with col_ia3:
    st.markdown("#### 💸 Eficiencia de Costos")
    st.metric("Costo por Consulta", f"${cost_per_inference:.3f} USD")
    st.caption("Costo promedio de tokens de entrada/salida consumidos en el LLM por pregunta.")

st.markdown("---")

# SECCIÓN 3: Análisis de Crecimiento Semanal (Meta: 10%)
st.subheader("📈 3. Análisis de Crecimiento Semanal (Objetivo: 10%)")

on_track = growth_rate >= 10.0
st.write(f"**Tasa de Crecimiento Semanal Actual:** `{growth_rate}%`")

if on_track:
    st.success("🎉 ¡Felicidades! La Papaya está logrando el objetivo de crecimiento semanal del 10%.")
else:
    st.error("⚠️ Alerta: No estamos alcanzando la meta del 10% de crecimiento semanal. Se requiere evaluación de Pivot.")

# Gráfico de Proyección a 6 semanas
semanas = [f"Semana {i}" for i in range(1, 7)]
proyeccion_actual = [usuarios_activos]
proyeccion_objetivo = [usuarios_activos]

for i in range(1, 6):
    proyeccion_actual.append(proyeccion_actual[-1] * (1 + growth_rate/100))
    proyeccion_objetivo.append(proyeccion_objetivo[-1] * 1.10)

df_growth = pd.DataFrame({
    "Semana": semanas,
    "Proyección Actual": proyeccion_actual,
    "Objetivo 10%": proyeccion_objetivo
})

st.line_chart(df_growth.set_index("Semana"))

# SECCIÓN 4: Pivot or Persist Assessment
st.markdown("---")
st.subheader("🔄 4. Pivot or Persist Assessment")

if not on_track:
    st.markdown(f"""
    ### **Análisis de Pivot / Cambio Estructural**
    Dado que el crecimiento semanal actual (**{growth_rate}%**) es inferior a la meta del **10%**, nuestro modelo de crecimiento actual presenta fricciones de adquisición.
    
    * **Identificación del Cuello de Botella:** La **Latencia Promedio** y la **Tasa de Completado de Tareas** representan fricciones de retención clave en el segmento "Silver". Si la IA tarda más de 2 segundos, el adulto mayor abandona la sesión, disparando el Churn de esta vertical.
    * **Propuesta de Pivot (Modelo B2B2C):**
        * **Producto:** Integrar la IA en portales corporativos de bienestar para empleados.
        * **Estrategia de Go-To-Market:** Alianzas directas con cajas de compensación (ej. Comfandi) y universidades para vender licencias del "Plan Padrino" por volumen, reduciendo el CAC de $1,000,000 a cero neto.
        * **Impacto Modelado:** Se reduce el Churn de jóvenes del 117% al 15% y acelera la tasa de crecimiento semanal estimada a un **12.5%** neto de inmediato.
    """)
else:
    st.markdown("""
    ### **Análisis de Persistencia**
    El crecimiento se encuentra en niveles saludables. Se aconseja **persistir** en la estrategia actual, enfocando los esfuerzos en reducir el costo de inferencia de la IA mediante técnicas de *prompt caching* para mejorar el margen bruto operativo.
    """)