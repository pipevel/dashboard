import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="La Papaya - Business, Financial & AI Dashboard", 
    page_icon="🍊", 
    layout="wide"
)

st.title("🍊 La Papaya - Dashboard Integrado de Negocio, Finanzas e IA")
st.markdown("### Control de Unit Economics, Estructura Financiera (Burn Rate/Ingresos), Métricas de IA y Sostenibilidad Social")

# Tasa de cambio de referencia (COP a USD)
TRM = 4000.0

# ==========================================
# BARRA LATERAL: Control de Variables Dinámicas
# ==========================================
st.sidebar.header("🎛️ 1. Simulador de Negocio & Precios")
usuarios_activos = st.sidebar.number_input("Seniors Activos Actuales", value=684, step=10)

# Licencias y Suscripciones
precio_b2b_empresa = st.sidebar.number_input("Licencia B2B SaaS Empresas ($ USD/mes)", value=100, step=10)
mensualidad_senior = st.sidebar.slider("Suscripción Mensual Senior ($ USD/mes)", min_value=10, max_value=500, value=50, step=5)
costo_senior = st.sidebar.slider("Costo Directo Operación Senior ($ USD/mes)", min_value=0, max_value=200, value=10, step=5)
cac_senior = st.sidebar.number_input("Costo de Adquisición CAC Senior ($ USD)", value=1000, step=50)

st.sidebar.markdown("---")
st.sidebar.header("💰 2. Salarios Full y Costos Fijos Mensuales (USD)")
salario_felipe = st.sidebar.number_input("Salario Full Felipe ($ USD/mes)", value=1500, step=100)
salario_yoiner = st.sidebar.number_input("Salario Full Yoiner ($ USD/mes)", value=500, step=50)
salario_jose_berna = st.sidebar.number_input("Salario Full José Berna ($ USD/mes)", value=1000, step=100)
otros_costos_fijos = st.sidebar.number_input("Otros Costos Fijos Operativos ($ USD/mes)", value=100, step=50)

st.sidebar.markdown("---")
st.sidebar.header("🤖 3. Agente IA (Sylver) & Crecimiento")
accuracy = st.sidebar.slider("Precisión del Agente (Accuracy %)", min_value=70.0, max_value=100.0, value=92.5, step=0.5)
latency = st.sidebar.slider("Latencia Promedio (segundos)", min_value=0.5, max_value=5.0, value=1.8, step=0.1)
cost_per_inference = st.sidebar.slider("Costo Inferencia / Consulta (USD)", min_value=0.001, max_value=0.05, value=0.008, step=0.001, format="%.3f")
growth_rate = st.sidebar.slider("Tasa Crecimiento Semanal Real (%)", min_value=0.0, max_value=20.0, value=6.5, step=0.5)

# ==========================================
# CÁLCULOS DE BURN RATE Y SALARIOS FULL
# ==========================================
total_salarios_mes = salario_felipe + salario_yoiner + salario_jose_berna
burn_rate_fijo_mes = total_salarios_mes + otros_costos_fijos
burn_rate_anual = burn_rate_fijo_mes * 12

# Margen de contribución por suscripción senior
margen_contribucion_senior = mensualidad_senior - costo_senior

# Cálculo de Break-Even (Suscripciones necesarias)
seniors_para_break_even = int(np.ceil(burn_rate_fijo_mes / margen_contribucion_senior)) if margen_contribucion_senior > 0 else 0
empresas_b2b_para_break_even = int(np.ceil(burn_rate_fijo_mes / precio_b2b_empresa)) if precio_b2b_empresa > 0 else 0

# ARR Mínimo de Equilibrio
arr_break_even = burn_rate_anual

# Métricas Actuales de la Plataforma
mrr_actual = int(round(usuarios_activos * mensualidad_senior))
arr_actual = mrr_actual * 12
margen_total_actual = int(round(usuarios_activos * margen_contribucion_senior))
flujo_caja_neto_actual = margen_total_actual - burn_rate_fijo_mes

# Consumo IA
total_consultas_mes = usuarios_activos * 120
costo_ia_mensual_usd = int(round(total_consultas_mes * cost_per_inference))

# ==========================================
# KPIs PRINCIPALES (Métricas Estrella)
# ==========================================
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("ARR Mínimo Break-Even", f"${arr_break_even:,.0f} USD")
with col2:
    st.metric("Suscripciones Senior Equilibrio", f"{seniors_para_break_even:,}")
with col3:
    st.metric("Ó Licencias B2B Equilibrio", f"{empresas_b2b_para_break_even:,}")
with col4:
    st.metric("Burn Rate Mensual (Full)", f"${burn_rate_fijo_mes:,.0f} USD")
with col5:
    st.metric("Flujo de Caja Neto Actual", f"${flujo_caja_neto_actual:,.0f} USD", 
              delta="Superávit" if flujo_caja_neto_actual >= 0 else "Déficit",
              delta_color="normal" if flujo_caja_neto_actual >= 0 else "inverse")

st.markdown("---")

# ==========================================
# PESTAÑAS DEL DASHBOARD
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔥 Burn Rate & Flujo de Caja", 
    "📊 Unit Economics", 
    "💚 Impacto Social y Ambiental",
    "🌍 TAM / SAM / SOM",
    "🤖 Rendimiento IA", 
    "📈 Crecimiento & Pivot"
])

# PESTAÑA 1: BURN RATE, SALARIOS FULL Y PUNTO DE EQUILIBRIO
with tab1:
    st.subheader("🔥 Estructura de Salarios Full, Burn Rate y Punto de Equilibrio (ARR)")
    
    col_br1, col_br2 = st.columns(2)
    
    with col_br1:
        st.markdown("### 💼 Gastos Fijos Operativos y Salarios Full")
        data_salarios = {
            "Concepto / Cargo": [
                "Salario Full - Felipe",
                "Salario Full - Yoiner",
                "Salario Full - José Berna",
                "Total Salarios Mensual",
                "Otros Costos Fijos (Hosting, Dominio, Infraestructura)",
                "Gross Burn Rate Total / Mes",
                "Gross Burn Rate Total / Año"
            ],
            "Monto ($ USD)": [
                f"${salario_felipe:,.0f} USD",
                f"${salario_yoiner:,.0f} USD",
                f"${salario_jose_berna:,.0f} USD",
                f"${total_salarios_mes:,.0f} USD",
                f"${otros_costos_fijos:,.0f} USD",
                f"${burn_rate_fijo_mes:,.0f} USD",
                f"${burn_rate_anual:,.0f} USD"
            ]
        }
        st.table(pd.DataFrame(data_salarios))

    with col_br2:
        st.markdown("### ⚖️ Meta Mínima para Punto de Equilibrio (Break-Even)")
        
        st.info(f"""
        Para cubrir el **Burn Rate mensual full de ${burn_rate_fijo_mes:,.0f} USD** (${burn_rate_anual:,.0f} USD/año), la empresa requiere alcanzar **un ARR mínimo de ${arr_break_even:,.0f} USD**.
        """)
        
        data_break_even = {
            "Modelo / Canal de Ventas": [
                "Canal B2C: Suscripciones Senior ($50 USD/mes)",
                "Canal B2B: Licencias SaaS Empresas ($100 USD/mes)",
                "Modelo Mixto (Ejemplo: 50% Seniors + 50% B2B)"
            ],
            "Mínimo Requerido para Equilibrio": [
                f"{seniors_para_break_even:,} suscriptores Senior activos",
                f"{empresas_b2b_para_break_even:,} licencias B2B corporativas",
                f"{int(seniors_para_break_even/2):,} Seniors + {int(empresas_b2b_para_break_even/2):,} Empresas"
            ],
            "Ingreso Recurrente Generado (MRR)": [
                f"${seniors_para_break_even * mensualidad_senior:,.0f} USD / mes",
                f"${empresas_b2b_para_break_even * precio_b2b_empresa:,.0f} USD / mes",
                f"${burn_rate_fijo_mes:,.0f} USD / mes"
            ]
        }
        st.table(pd.DataFrame(data_break_even))
        
        st.markdown("#### Estado Actual vs. Meta de Equilibrio")
        diferencia_seniors = usuarios_activos - seniors_para_break_even
        if diferencia_seniors >= 0:
            st.success(f"🎉 **Superávit:** Tu base actual de {usuarios_activos:,} Seniors supera la meta por {diferencia_seniors:,} suscripciones.")
        else:
            st.warning(f"⚠️ **Faltante:** Faltan {abs(diferencia_seniors):,} suscripciones Senior (o {empresas_b2b_para_break_even:,} licencias B2B) para cubrir los salarios full y costos operativos.")

# PESTAÑA 2: UNIT ECONOMICS
with tab2:
    st.subheader("Unit Economics & Oferta de Valor (USD)")
    data_ue = {
        "Concepto / Métrica": [
            "B2B Empresas (Licencia SaaS ESG / Impacto)",
            "Suscripción Mensual Senior",
            "Suscripción Mensual Jóvenes",
            "Costo de Adquisición (CAC) Seniors",
            "Ratio LTV / CAC Seniors",
            "Customer Lifetime Value (LTV) Senior Proyectado",
            "Margen Bruto por Senior",
            "Costos Operativos por Senior"
        ],
        "Valor Configurado": [
            f"${precio_b2b_empresa:,.0f} USD",
            f"${mensualidad_senior:,.0f} USD",
            "GRATIS (Automatizado con IA)",
            f"${cac_senior:,.0f} USD",
            "3:1",
            f"${cac_senior * 3:,.0f} USD",
            f"${margen_contribucion_senior:,.0f} USD",
            f"${costo_senior:,.0f} USD"
        ]
    }
    st.table(pd.DataFrame(data_ue))

# PESTAÑA 3: IMPACTO SOCIAL Y AMBIENTAL
with tab3:
    st.subheader("❤️ Mutualismo Intergeneracional e Impacto Social/Ambiental")
    col_imp1, col_imp2 = st.columns(2)
    
    with col_imp1:
        st.markdown("### 👨‍🎓 Impacto Social")
        data_social = {
            "Indicador": ["Planes Padrino Financiados", "Jóvenes Beneficiados", "Mentores Activos"],
            "Por Senior": ["3–4 jóvenes", "Hasta 4 jóvenes", "1 mentor"],
            "Total Comunidad": [f"{usuarios_activos*3:,} - {usuarios_activos*4:,}", f"{usuarios_activos*4:,}", f"{usuarios_activos:,}"]
        }
        st.table(pd.DataFrame(data_social))

    with col_imp2:
        st.markdown("### 🌱 Impacto Ambiental")
        f10 = usuarios_activos / 10.0
        data_amb = {
            "Métrica": ["Conservación Bosque", "Captura Carbono", "Compostaje Residuos"],
            "Proyección Global": [f"{int(round(f10*5)):,} ha", f"{int(round(f10*10)):,} tCO₂/año", f"{f10*0.4:,.1f} ton/mes"]
        }
        st.table(pd.DataFrame(data_amb))

# PESTAÑA 4: TAM / SAM / SOM
with tab4:
    st.subheader("🌍 Dimensionamiento del Mercado")
    data_tam = {
        "Nivel": ["TAM", "SAM", "SOM"],
        "Monto ($ USD)": ["$1,225,000,000 USD", "$191,000,000 USD", "$312,500 USD"],
        "Descripción": ["Silver Economy Global/Regional", "Mercado Accesible Target", "Captura Objetivo Inicial"]
    }
    st.table(pd.DataFrame(data_tam))

# PESTAÑA 5: RENDIMIENTO IA
with tab5:
    st.subheader("Métricas Tecnológicas del Agente IA")
    c1, c2, c3 = st.columns(3)
    c1.metric("Latencia Promedio", f"{latency} seg")
    c2.metric("Task Completion Rate", f"{min(100.0, accuracy * 1.05):.1f}%")
    c3.metric("Inferencia Mensual", f"${costo_ia_mensual_usd:,.0f} USD")

# PESTAÑA 6: CRECIMIENTO & PIVOT
with tab6:
    st.subheader("Análisis de Crecimiento & Estrategia B2B SaaS")
    st.write(f"**Tasa de crecimiento semanal actual:** `{growth_rate}%`")
    st.markdown(f"""
    * **Meta para salarios full:** Se requiere mantener un MRR de **${burn_rate_fijo_mes:,.0f} USD** para cubrir la nómina full de Felipe (${salario_felipe:,.0f}), Yoiner (${salario_yoiner:,.0f}) y José Berna (${salario_jose_berna:,.0f}).
    * **Apalancamiento B2B:** Capturar **{empresas_b2b_para_break_even:,} empresas B2B** a $100 USD/mes permite cubrir el 100% de la nómina full de forma recurrente.
    """)
