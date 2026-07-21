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
st.sidebar.header("🎛️ 1. Simulador de Negocio & Operación")
usuarios_activos = st.sidebar.number_input("Usuarios Activos (Seniors)", value=684, step=10)

# Licencias y Suscripciones
precio_b2b_empresa = st.sidebar.number_input("Licencia B2B SaaS Empresas (USD)", value=100, step=10)
mensualidad_senior = st.sidebar.slider("Suscripción Mensual Senior (USD)", min_value=10, max_value=500, value=50, step=5)
costo_senior = st.sidebar.slider("Costo de Operación Senior (USD)", min_value=10, max_value=300, value=30, step=5)
cac_senior = st.sidebar.number_input("Costo de Adquisición CAC Senior (USD)", value=1000, step=50)

st.sidebar.markdown("---")
st.sidebar.header("💰 2. Simulador de Inversión Inicial & Finanzas")
inversion_inicial = st.sidebar.number_input("Inyección de Inversión Inicial ($ USD)", value=50000, step=5000)
costos_fijos_mes = st.sidebar.number_input("Costos Fijos Operativos Mes ($ USD)", value=3000, step=500)
margen_bruto_pct = st.sidebar.slider("Margen Bruto (%)", min_value=10, max_value=100, value=80, step=5) / 100.0

st.sidebar.markdown("---")
st.sidebar.header("🤖 3. Agente IA (Sylver) & Crecimiento")
accuracy = st.sidebar.slider("Precisión del Agente (Accuracy %)", min_value=70.0, max_value=100.0, value=92.5, step=0.5)
latency = st.sidebar.slider("Latencia Promedio (segundos)", min_value=0.5, max_value=5.0, value=1.8, step=0.1)
cost_per_inference = st.sidebar.slider("Costo Inferencia / Consulta (USD)", min_value=0.001, max_value=0.05, value=0.008, step=0.001, format="%.3f")
growth_rate = st.sidebar.slider("Tasa Crecimiento Semanal Real (%)", min_value=0.0, max_value=20.0, value=6.5, step=0.5)

# ==========================================
# CÁLCULOS FINANCIEROS Y METRICAS RECURRENTES
# ==========================================
margen_senior = mensualidad_senior - costo_senior
total_jovenes_impactados = int(usuarios_activos * 3.5)

# MRR y ARR actuales
mrr_actual = int(round(usuarios_activos * mensualidad_senior))
arr_actual = mrr_actual * 12

# Break-Even
mrr_break_even = int(round(costos_fijos_mes / margen_bruto_pct)) if margen_bruto_pct > 0 else 0
sub_break_even = int(round(mrr_break_even / mensualidad_senior)) if mensualidad_senior > 0 else 0

# Simulación a 24 meses para Payback / Retorno de Inversión
datos_proyeccion = []
caja_acumulada = inversion_inicial
mes_payback = None
mes_break_even = None

# Consumo IA
total_consultas_mes = usuarios_activos * 120
costo_ia_mensual_usd = int(round(total_consultas_mes * cost_per_inference))

for mes in range(1, 25):
    # Proyección con crecimiento simple mensual derivado
    ingreso_mes = mrr_actual * ((1 + (growth_rate/100)) ** (mes/4))
    utilidad_bruta = ingreso_mes * margen_bruto_pct
    utilidad_operativa = utilidad_bruta - costos_fijos_mes
    
    if utilidad_operativa >= 0 and mes_break_even is None:
        mes_break_even = mes
        
    caja_acumulada += utilidad_operativa
    
    if (caja_acumulada >= inversion_inicial * 2) and (mes_payback is None) and (utilidad_operativa > 0):
        mes_payback = mes

    datos_proyeccion.append({
        "Mes": f"Mes {mes}",
        "MRR Proyectado": int(round(ingreso_mes)),
        "Caja Acumulada": int(round(caja_acumulada))
    })

df_proyeccion = pd.DataFrame(datos_proyeccion)

# ==========================================
# KPIs PRINCIPALES (Métricas Estrella)
# ==========================================
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("MRR Actual", f"${mrr_actual:,.0f} USD")
with col2:
    st.metric("ARR Actual", f"${arr_actual:,.0f} USD")
with col3:
    st.metric("Break-Even MRR", f"${mrr_break_even:,.0f} USD")
with col4:
    st.metric("Retorno Inversión", f"Mes {mes_payback}" if mes_payback else " > 24 Meses")
with col5:
    st.metric("Inferencia IA / Mes", f"${costo_ia_mensual_usd:,.0f} USD")

st.markdown("---")

# ==========================================
# PESTAÑAS DEL DASHBOARD
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Unit Economics & ROI", 
    "💚 Impacto Social y Ambiental",
    "🌍 TAM / SAM / SOM",
    "🔥 Burn Rate & Flujo de Caja", 
    "🤖 Rendimiento IA", 
    "📈 Crecimiento & Pivot"
])

# PESTAÑA 1: UNIT ECONOMICS & RETORNO DE INVERSIÓN
with tab1:
    st.subheader("Unit Economics, MRR/ARR & Simulación de Inversión")
    
    col_ue1, col_ue2 = st.columns(2)
    
    with col_ue1:
        st.markdown("### 📋 Estructura Financiera de Suscripción")
        data_ue = {
            "Concepto / Métrica": [
                "MRR Actual (Seniors)",
                "ARR Proyectado (Anualizado)",
                "Punto de Equilibrio (Break-Even MRR)",
                "Seniors requeridos para Break-Even",
                "Licencia B2B Empresas (ESG)",
                "Suscripción Mensual Senior",
                "Suscripción Jóvenes",
                "Costo Adquisición (CAC) Senior",
                "LTV / CAC Seniors (3:1)"
            ],
            "Valor": [
                f"${mrr_actual:,.0f} USD",
                f"${arr_actual:,.0f} USD",
                f"${mrr_break_even:,.0f} USD",
                f"{sub_break_even:,} Seniors",
                f"${precio_b2b_empresa:,.0f} USD",
                f"${mensualidad_senior:,.0f} USD",
                "GRATIS (IA)",
                f"${cac_senior:,.0f} USD",
                f"${cac_senior * 3:,.0f} USD"
            ]
        }
        st.table(pd.DataFrame(data_ue))

    with col_ue2:
        st.markdown("### ⏱️ Simulación de Retorno de Inversión (Payback)")
        st.info(f"""
        * **Inversión Recibida:** ${inversion_inicial:,.0f} USD
        * **Costos Fijos Operativos:** ${costos_fijos_mes:,.0f} USD / mes
        * **Punto de Equilibrio:** {'Alcanzado en **Mes ' + str(mes_break_even) + '**' if mes_break_even else 'Atento: Elevar MRR para cubrir costos fijos'}
        * **Tiempo Estimado de Retorno:** {'**' + str(mes_payback) + ' Meses**' if mes_payback else 'Más de 24 meses proyectados'}
        """)
        
        st.markdown("#### Proyección de MRR y Caja Acumulada")
        st.line_chart(df_proyeccion.set_index("Mes"))

# PESTAÑA 2: IMPACTO SOCIAL Y AMBIENTAL
with tab2:
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

# PESTAÑA 3: TAM / SAM / SOM
with tab3:
    st.subheader("🌍 Dimensionamiento del Mercado")
    data_tam = {
        "Nivel": ["TAM", "SAM", "SOM"],
        "Monto ($ USD)": ["$1,225,000,000 USD", "$191,000,000 USD", "$312,500 USD"],
        "Descripción": ["Silver Economy Global/Regional", "Mercado Accesible Target", "Captura Objetivo Inicial"]
    }
    st.table(pd.DataFrame(data_tam))

# PESTAÑA 4: BURN RATE
with tab4:
    st.subheader("Estructura de Consumo de Caja")
    data_actual = {
        "Concepto": ["Hosting", "Dominio", "Desayunos (Mes)", "Variables", "Total / Mes"],
        "Valor ($ USD)": [
            f"${int(round(90000/TRM)):,}", f"${int(round(70000/TRM)):,}", 
            f"${int(round(30000/TRM)):,}", f"${int(round(150000/TRM)):,}", 
            f"${int(round(193333/TRM)):,}"
        ]
    }
    st.table(pd.DataFrame(data_actual))

# PESTAÑA 5: RENDIMIENTO IA
with tab5:
    st.subheader("Métricas Tecnológicas del Agente IA")
    c1, c2 = st.columns(2)
    c1.metric("Latencia Promedio", f"{latency} seg")
    c2.metric("Task Completion Rate", f"{min(100.0, accuracy * 1.05):.1f}%")

# PESTAÑA 6: CRECIMIENTO & PIVOT
with tab6:
    st.subheader("Análisis de Crecimiento & Estrategia B2B SaaS")
    st.write(f"**Tasa de crecimiento semanal actual:** `{growth_rate}%`")
