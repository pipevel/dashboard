import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="La Papaya - Business, Financial & AI Dashboard", page_icon="🍊", layout="wide")

st.title("🍊 La Papaya - Dashboard Integrado de Negocio, Finanzas e IA")
st.markdown("### Control de Unit Economics, Estructura Financiera (Burn Rate/Ingresos), Métricas de IA y Sostenibilidad Social")

# ==========================================
# BARRA LATERAL: Control de Variables Dinámicas
# ==========================================
st.sidebar.header("🎛️ Simulador de Negocio")
usuarios_activos = st.sidebar.number_input("Usuarios Activos", value=684, step=10)
mensualidad_senior = st.sidebar.slider("Mensualidad Eco Senior ($)", min_value=5000000, max_value=25000000, value=15000000, step=1000000)
costo_senior = st.sidebar.slider("Costo de Operación Senior ($)", min_value=5000000, max_value=20000000, value=12000000, step=1000000)

st.sidebar.markdown("---")
st.sidebar.header("🤖 Configuración del Agente IA (Sylver)")
accuracy = st.sidebar.slider("Precisión del Agente (Accuracy %)", min_value=70.0, max_value=100.0, value=92.5, step=0.5)
latency = st.sidebar.slider("Latencia Promedio (segundos)", min_value=0.5, max_value=5.0, value=1.8, step=0.1)
cost_per_inference = st.sidebar.slider("Costo de Inferencia por Consulta (USD)", min_value=0.001, max_value=0.05, value=0.008, step=0.001, format="%.3f")

st.sidebar.markdown("---")
st.sidebar.header("📈 Escalamiento y Crecimiento")
growth_rate = st.sidebar.slider("Tasa de Crecimiento Semanal Real (%)", min_value=0.0, max_value=20.0, value=6.5, step=0.5)

# ==========================================
# CÁLCULOS DINÁMICOS
# ==========================================
margen_senior = mensualidad_senior - costo_senior
costo_joven = 800000  # Costo mes plan padrino para jóvenes
ratio_subsidio_cruzado = margen_senior / costo_joven
total_consultas_mes = usuarios_activos * 120  # Promedio de 120 interacciones mensuales por usuario
costo_ia_mensual_usd = total_consultas_mes * cost_per_inference

# ==========================================
# KPIs PRINCIPALES (Métricas Estrella)
# ==========================================
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Usuarios Activos", f"{usuarios_activos:,}")
with col2:
    st.metric("Subsidio Cruzado (RSC)", f"{ratio_subsidio_cruzado:.2f}x")
with col3:
    st.metric("Margen por Senior", f"${margen_senior:,.0f} COP")
with col4:
    st.metric("Precisión Agente IA", f"{accuracy}%")
with col5:
    st.metric("Inferencia IA / Mes", f"${costo_ia_mensual_usd:,.2f} USD")

st.markdown("---")

# ==========================================
# PESTAÑAS DEL DASHBOARD (Toda la información)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Unit Economics Completos", 
    "🔥 Burn Rate & Flujo de Caja", 
    "💰 Ingresos Operativos", 
    "🤖 Rendimiento Detallado IA", 
    "📈 Crecimiento Semanal & Pivot Assessment"
])

# PESTAÑA 1: UNIT ECONOMICS COMPLETOS
with tab1:
    st.subheader("Métricas de Sostenibilidad Social y Margen")
    data_ue = {
        "Métrica de Unit Economics": [
            "Mensualidad Eco Senior",
            "Costos Mes Eco Senior",
            "Margen Bruto Eco Senior (Margen directo)",
            "Costo Mes Plan Padrino (Jóvenes)",
            "Ratio de Subsidio Cruzado (RSC)",
            "Active Users: Usuarios activos",
            "Average Revenue Per User (ARPU)",
            "Bookings: Reservas / Facturación contratada",
            "Churn Rate Adultos Mayores",
            "Churn Rate Jóvenes",
            "Customer Acquisition Cost (CAC) Jóvenes",
            "Customer Acquisition Cost (CAC) Senior",
            "Customer Lifetime Value (LTV) Joven",
            "Customer Lifetime Value (LTV) Senior (10 años)",
            "LTV / CAC Jóvenes",
            "LTV / CAC Adultos Mayores",
            "Gross Margin (Margen Bruto %)",
            "Gross Profit: Ganancia bruta mensual",
            "MRR (Mensual recurrente base)",
            "ARR (Anualizado proyectado)",
            "Registered Users: Usuarios registrados",
            "Retention Rate: Tasa de retención global"
        ],
        "Valor": [
            f"${mensualidad_senior:,.0f} COP",
            f"${costo_senior:,.0f} COP",
            f"${margen_senior:,.0f} COP",
            f"${costo_joven:,.0f} COP",
            f"{ratio_subsidio_cruzado:.2f}x",
            f"{usuarios_activos:,}",
            "$14,181.00 COP",
            "2 contratados",
            "0.44% mensual",
            "1.17% mensual",
            "$159,040.00 COP",
            "$1,000,000.00 COP",
            "$12,000,000.00 COP",
            "$1,800,000,000.00 COP",
            "75.0x",
            "1800.0x",
            "98.27%",
            "$11,006,666.67 COP",
            "$6,766,666.67 COP",
            "$81,200,000.00 COP",
            f"{usuarios_activos:,}",
            "100.0%"
        ],
        "Descripción / Enfoque Estratégico": [
            "Cobro mensual por el programa completo de adultos mayores.",
            "Costo de operación/servicios directos por adulto mayor.",
            "Margen de contribución para subsidiar la operación social.",
            "Monto subsidiado/costo del plan padrino para jóvenes.",
            "Cuántos jóvenes cubre el margen neto que deja un solo Senior.",
            "Total de usuarios activos en la plataforma/servicios.",
            "Ingreso promedio mensual por usuario activo.",
            "Contratos o reservas corporativas grandes aseguradas.",
            "Tasa de cancelación / Abandono mensual de clientes senior.",
            "Tasa de cancelación / Abandono mensual de usuarios jóvenes.",
            "Costo de adquisición promedio por cada joven.",
            "Costo de adquisición promedio por cada senior.",
            "Valor de vida financiero del cliente joven.",
            "LTV proyectado del adulto mayor a largo plazo (fidelidad extrema).",
            "Relación de rentabilidad para el segmento joven (75 a 1).",
            "Relación de rentabilidad para el segmento mayor (1800 a 1).",
            "Margen bruto de ganancia porcentual global consolidado.",
            "Ganancia bruta operativa mensual total.",
            "Ingreso mensual recurrente base de operaciones.",
            "Ingreso anualizado proyectado actual.",
            "Total de personas registradas históricamente.",
            "Porcentaje de clientes retenidos en el periodo."
        ]
    }
    st.table(pd.DataFrame(data_ue))

# PESTAÑA 2: BURN RATE & CASHFLOW
with tab2:
    st.subheader("Estructura de Consumo de Caja (Burn Rate)")
    col_burn_act, col_burn_proj = st.columns(2)
    
    with col_burn_act:
        st.markdown("### 🔥 Gross Burn Rate Actual")
        data_actual = {
            "Concepto": ["Hosting", "Dominio", "Desayunos (Mensual)", "Desayunos Anualizados", "Costos Variables", "Total / Mes"],
            "Valor": ["$90,000.00 COP / Año", "$70,000.00 COP / Año", "$30,000.00 COP", "$360,000.00 COP", "$150,000.00 COP", "$193,333.33 COP"]
        }
        st.table(pd.DataFrame(data_actual))
        st.info("**Cashflow Operativo:** $11,006,666.67 COP mensual")

    with col_burn_proj:
        st.markdown("### 🚀 Gross Burn Rate Proyectado")
        data_proyectado = {
            "Concepto": [
                "Hosting/Año Proyectado", "Dominio/Año Proyectado", "Desayunos/Mes Proyectado", 
                "Costos Variables Proyectados", "Salario Felipe", "Salario Yoiner", "Salario Jose Berna", "Total Proyectado / Mes"
            ],
            "Valor": [
                "$7,500.00 COP", "$5,833.33 COP", "$30,000.00 COP", 
                "$150,000.00 COP", "$6,000,000.00 COP", "$2,000,000.00 COP", "$4,000,000.00 COP", "$12,193,333.33 COP"
            ]
        }
        st.table(pd.DataFrame(data_proyectado))

# PESTAÑA 3: INGRESOS OPERATIVOS
with tab3:
    st.subheader("Ingresos Operativos & Convenios")
    data_ingresos = {
        "Fuente de Ingreso": [
            "Grupo Textil", "Calima", "Javeriana", "Icesi", "Comfandi", 
            "Donación Internacional", "Total Sin Donación", "Total Sin Calima", "Total General Consolidado"
        ],
        "Monto ($)": [
            6000000, 70000000, 700000, 1500000, 3000000, 
            4000000, 81200000, 11200000, 4081200000
        ],
        "Tipo": [
            "Operativo", "Convenio", "Educativo", "Educativo", "Alianza", 
            "Filantropía", "Filtro Clave", "Filtro Clave", "Acumulado Consolidado"
        ]
    }
    df_ingresos = pd.DataFrame(data_ingresos)
    
    col_t1, col_t2 = st.columns([2, 3])
    with col_t1:
        st.markdown("#### Detalle Financiero de Canales")
        st.table(df_ingresos)
    with col_t2:
        st.markdown("#### Participación por Fuente de Ingresos")
        df_chart = df_ingresos[~df_ingresos["Fuente de Ingreso"].str.contains("Total")]
        st.bar_chart(data=df_chart, x="Fuente de Ingreso", y="Monto ($)")

# PESTAÑA 4: RENDIMIENTO DETALLADO IA
with tab4:
    st.subheader("Rendimiento y Sostenibilidad Tecnológica de la IA")
    col_ia_d1, col_ia_d2, col_ia_d3 = st.columns(3)
    
    with col_ia_d1:
        st.markdown("#### ⚡ Latencia y Retención")
        st.metric("Latencia Promedio", f"{latency} seg", delta="-0.3 seg" if latency < 2.0 else "+0.4 seg")
        st.progress(max(0, min(100, int((5.0 - latency) / 4.5 * 100))))
        st.caption("Meta: Menor a 2.0 segundos. Los adultos mayores presentan altas tasas de rebote ante latencias elevadas.")

    with col_ia_d2:
        st.markdown("#### 🎯 Tasa de Completado de Tareas (Task Completion Rate)")
        task_completion = min(100.0, accuracy * 1.05)
        st.metric("Resolución Autónoma", f"{task_completion:.1f}%")
        st.caption("Porcentaje de consultas de interacción social y orientación resueltas de manera autónoma por la IA.")

    with col_ia_d3:
        st.markdown("#### 💸 Métricas de Costo y Consumo")
        st.metric("Costo Promedio / Sesión", f"${cost_per_inference * 5:.3f} USD")
        st.metric("Costo Mensual Consolidado (COP)", f"${costo_ia_mensual_usd * 4000:,.0f} COP")
        st.caption("Calculado a una TRM estimada de $4,000 COP por USD.")

# PESTAÑA 5: CRECIMIENTO SEMANAL Y PIVOT ASSESSMENT
with tab5:
    st.subheader("Análisis de Crecimiento y Estrategia de Sostenibilidad")
    on_track = growth_rate >= 10.0
    st.write(f"**Tasa de Crecimiento Semanal de la Plataforma:** `{growth_rate}%`")
    
    if on_track:
        st.success("🎉 ¡Felicidades! La Papaya está logrando la meta corporativa del 10% de crecimiento semanal.")
    else:
        st.error("⚠️ Alerta: No estamos alcanzando la meta del 10% de crecimiento semanal. Se requiere análisis estratégico.")
        
    # Gráfico de Proyecciones
    semanas = [f"Semana {i}" for i in range(1, 7)]
    proyeccion_actual = [usuarios_activos]
    proyeccion_objetivo = [usuarios_activos]

    for i in range(1, 6):
        proyeccion_actual.append(proyeccion_actual[-1] * (1 + growth_rate/100))
        proyeccion_objetivo.append(proyeccion_objetivo[-1] * 1.10)

    df_growth = pd.DataFrame({
        "Semana": semanas,
        "Proyección con Tasa Actual": proyeccion_actual,
        "Objetivo de Crecimiento (10%)": proyeccion_objetivo
    })
    st.line_chart(df_growth.set_index("Semana"))
    
    st.markdown("---")
    st.subheader("🔄 Pivot or Persist Assessment")
    
    if not on_track:
        st.markdown(f"""
        ### **Evaluación de Cambio de Rumbo (Pivot)**
        Dado que el crecimiento semanal actual (**{growth_rate}%**) es menor al objetivo del **10%**, se propone un cambio táctico:
        
        * **El Cuello de Botella:** La combinación del **Churn de jóvenes (1.17% mensual / 117% anual)** y la **latencia de la IA** limita la retención. Cada vez que perdemos un usuario Senior, perdemos el subsidio para {ratio_subsidio_cruzado:.2f} jóvenes.
        * **Cambio Estructural Recomendado (Pivot B2B2C):** Transicionar de un modelo B2C individual a un canal **B2B2C** aliando la plataforma con empresas y cajas de compensación (ej. Comfandi, Calima). 
        * **Modelo de Impacto:** Las empresas apadrinan lotes de licencias de bienestar para sus jubilados y familiares jóvenes de forma anual. Esto reduce el CAC individual a $0, elimina el Churn recurrente bajándolo a un **15% anual** y proyecta elevar la tasa de crecimiento semanal al **12.5%** de inmediato.
        """)
    else:
        st.markdown("""
        ### **Evaluación de Persistencia**
        El crecimiento se encuentra por encima del objetivo. Se aconseja **persistir** en el modelo actual. Las acciones sugeridas son optimizar los tiempos de respuesta del LLM (Latencia) y consolidar el ratio de subsidio cruzado (RSC).
        """)