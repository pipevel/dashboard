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
st.sidebar.header("🎛️ Simulador de Negocio")
usuarios_activos = st.sidebar.number_input("Usuarios Activos (Seniors)", value=684, step=10)

# Licencias y Suscripciones
precio_b2b_empresa = st.sidebar.number_input("Licencia B2B SaaS Empresas (USD)", value=100, step=10)
mensualidad_senior = st.sidebar.slider("Suscripción Mensual Senior (USD)", min_value=10, max_value=500, value=50, step=5)
suscripcion_jovenes = 0.0  # Entran GRATIS gracias a la IA automatizada

# Costos Operativos y de Adquisición
costo_senior = st.sidebar.slider("Costo de Operación Senior (USD)", min_value=10, max_value=300, value=30, step=5)
cac_senior = st.sidebar.number_input("Costo de Adquisición CAC Senior (USD)", value=1000, step=50)

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
ratio_subsidio_cruzado = 3.5  # Promedio: 1 senior apadrina entre 3 y 4 jóvenes
total_jovenes_impactados = int(usuarios_activos * ratio_subsidio_cruzado)

total_consultas_mes = usuarios_activos * 120  # Promedio de 120 interacciones mensuales por usuario
costo_ia_mensual_usd = int(round(total_consultas_mes * cost_per_inference))

# Cálculo de ratios de valor de vida del cliente (LTV / CAC)
ltv_senior = int(round(cac_senior * 3.0))  # Ratio 3:1
ltv_empresa = 400  # Ratio 4:1 con respecto a la licencia B2B de $100

# ==========================================
# KPIs PRINCIPALES (Métricas Estrella)
# ==========================================
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Seniors Activos", f"{usuarios_activos:,}")
with col2:
    st.metric("Jóvenes Apadrinados", f"{total_jovenes_impactados:,}")
with col3:
    st.metric("Suscripción Senior", f"${mensualidad_senior:,.0f} USD")
with col4:
    st.metric("Precisión Agente IA", f"{accuracy}%")
with col5:
    st.metric("Inferencia IA / Mes", f"${costo_ia_mensual_usd:,.0f} USD")

st.markdown("---")

# ==========================================
# PESTAÑAS DEL DASHBOARD
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Unit Economics", 
    "💚 Impacto Social y Ambiental",
    "🌍 TAM / SAM / SOM",
    "🔥 Burn Rate & Flujo de Caja", 
    "🤖 Rendimiento Detallado IA", 
    "📈 Crecimiento & Pivot Assessment"
])

# PESTAÑA 1: UNIT ECONOMICS COMPLETOS
with tab1:
    st.subheader("Unit Economics & Oferta de Valor (USD)")
    
    data_ue = {
        "Concepto / Métrica": [
            "B2B Empresas (Licencia SaaS ESG / Impacto)",
            "Suscripción Mensual Senior",
            "Suscripción Mensual Jóvenes",
            "Costo de Adquisición (CAC) Seniors",
            "Ratio LTV / CAC Seniors",
            "Ratio LTV / CAC Empresas",
            "Customer Lifetime Value (LTV) Senior Proyectado",
            "Margen Bruto por Senior",
            "Costos Operativos por Senior",
            "Subsidio Cruzado Intergeneracional"
        ],
        "Valor Configurado": [
            f"${precio_b2b_empresa:,.0f} USD",
            f"${mensualidad_senior:,.0f} USD",
            "GRATIS (Automatizado con IA)",
            f"${cac_senior:,.0f} USD",
            "3:1",
            "4:1",
            f"${ltv_senior:,.0f} USD",
            f"${margen_senior:,.0f} USD",
            f"${costo_senior:,.0f} USD",
            "1 Senior financia a 3–4 Jóvenes"
        ],
        "Detalle & Enfoque Estratégico": [
            "SaaS para metas ESG con certificados de impacto auditables por IA.",
            "Cobro mensual recurrente a usuarios mayores por programa integral.",
            "Acceso libre apalancado en infraestructura IA de costo marginal nulo.",
            "Inversión requerida para atraer y convertir a un usuario Senior.",
            "Retorno de inversión sólido en el ciclo de vida del usuario mayor.",
            "Relación de rentabilidad esperada sobre clientes corporativos B2B.",
            "Valor total generado por cliente Senior a lo largo de su retención.",
            "Contribución directa tras deducir costos de atención directa.",
            "Gasto directo de mantenimiento operativo por usuario Senior.",
            "Sostenibilidad social apalancada en mutualismo intergeneracional."
        ]
    }
    st.table(pd.DataFrame(data_ue))

# PESTAÑA 2: IMPACTO SOCIAL Y AMBIENTAL
with tab2:
    st.subheader("❤️ Mutualismo Intergeneracional e Impacto Social/Ambiental")
    st.markdown("Cada **Residente / Senior** financia el proyecto de vida de jóvenes rurales a través del modelo de apoyo mutuo.")

    col_imp1, col_imp2 = st.columns(2)
    
    with col_imp1:
        st.markdown("### 👨‍🎓 Impacto Social y Humano")
        data_social = {
            "Indicador de Impacto": [
                "Planes Padrino Financiados",
                "Alimentación y Alojamiento Garantizado",
                "Relaciones Intergeneracionales Creadas",
                "Propósito y Bienestar Generado"
            ],
            "Impacto Directo (por Residente)": [
                "3–4 jóvenes rurales por Senior",
                "Hasta 4 jóvenes beneficiados",
                "1 mentor Senior por cada 3–4 jóvenes",
                "1 adulto mayor en envejecimiento activo"
            ],
            "Total Consolidado (Comunidad Actual)": [
                f"{usuarios_activos * 3:,} a {usuarios_activos * 4:,} jóvenes",
                f"Hasta {usuarios_activos * 4:,} jóvenes",
                f"{usuarios_activos:,} mentores activos",
                f"{usuarios_activos:,} adultos mayores activos"
            ]
        }
        st.table(pd.DataFrame(data_social))

    with col_imp2:
        st.markdown("### 🌱 Impacto Ambiental y Sostenibilidad")
        
        factor_10 = usuarios_activos / 10.0
        
        data_ambiental = {
            "Métrica Ambiental": [
                "Conservación de Bosque",
                "Captura de Carbono Estimada",
                "Compostaje de Residuos Orgánicos"
            ],
            "Impacto por Base (10 Residentes)": [
                "5 hectáreas de bosque",
                "10 tCO₂ / año",
                "0.4 toneladas / mes"
            ],
            "Proyección Global con Usuarios Activos": [
                f"{int(round(factor_10 * 5)):,} hectáreas",
                f"{int(round(factor_10 * 10)):,} tCO₂ / año",
                f"{factor_10 * 0.4:,.1f} toneladas / mes"
            ]
        }
        st.table(pd.DataFrame(data_ambiental))

# PESTAÑA 3: TAM / SAM / SOM
with tab3:
    st.subheader("🌍 Dimensionamiento del Mercado (TAM / SAM / SOM)")
    
    col_mkt1, col_mkt2 = st.columns([2, 3])
    
    with col_mkt1:
        data_tam = {
            "Nivel de Mercado": ["TAM", "SAM", "SOM"],
            "Monto Total ($ USD)": ["$1,225,000,000 USD", "$191,000,000 USD", "$312,500 USD"],
            "Definición": [
                "Total Addressable Market (Silver Economy Global/Regional)",
                "Serviceable Available Market (Mercado Accesible Target)",
                "Serviceable Obtainable Market (Captura Objetivo Inicial)"
            ]
        }
        st.table(pd.DataFrame(data_tam))
        
    with col_mkt2:
        st.markdown("### 📚 Fuentes y Referencias de Mercado")
        st.info("""
        * **TAM ($1,225M USD / $1.225B USD):** Comisión Europea – *Silver Economy Report*; FMI – *The Rise of the Silver Economy*.
        * **SAM ($191M USD):** DANE (Proyecciones poblacionales Colombia), Ministerio de Comercio, Ministerio de Salud y Estudios del Ecosistema de Economía Plateada.
        * **SOM ($312,500 USD):** Proyección operativa inicial de captura de mercado B2B/B2C en focos urbanos y rurales clave.
        """)

# PESTAÑA 4: BURN RATE & CASHFLOW
with tab4:
    st.subheader("Estructura de Consumo de Caja (Burn Rate en USD)")
    col_burn_act, col_burn_proj = st.columns(2)
    
    with col_burn_act:
        st.markdown("### 🔥 Gross Burn Rate Actual (USD)")
        data_actual = {
            "Concepto": ["Hosting", "Dominio", "Desayunos (Mensual)", "Desayunos Anualizados", "Costos Variables", "Total / Mes"],
            "Valor": [
                f"${int(round(90000.00 / TRM)):,} USD / Año",
                f"${int(round(70000.00 / TRM)):,} USD / Año",
                f"${int(round(30000.00 / TRM)):,} USD",
                f"${int(round(360000.00 / TRM)):,} USD",
                f"${int(round(150000.00 / TRM)):,} USD",
                f"${int(round(193333.33 / TRM)):,} USD"
            ]
        }
        st.table(pd.DataFrame(data_actual))

    with col_burn_proj:
        st.markdown("### 🚀 Gross Burn Rate Proyectado (USD)")
        data_proyectado = {
            "Concepto": [
                "Hosting/Año Proyectado", "Dominio/Año Proyectado", "Desayunos/Mes Proyectado", 
                "Costos Variables Proyectados", "Salario Felipe", "Salario Yoiner", "Salario Jose Berna", "Total Proyectado / Mes"
            ],
            "Valor": [
                f"${int(round(7500.00 / TRM)):,} USD",
                f"${int(round(5833.33 / TRM)):,} USD",
                f"${int(round(30000.00 / TRM)):,} USD",
                f"${int(round(150000.00 / TRM)):,} USD",
                f"${int(round(6000000.00 / TRM)):,} USD",
                f"${int(round(2000000.00 / TRM)):,} USD",
                f"${int(round(4000000.00 / TRM)):,} USD",
                f"${int(round(12193333.33 / TRM)):,} USD"
            ]
        }
        st.table(pd.DataFrame(data_proyectado))

# PESTAÑA 5: RENDIMIENTO DETALLADO IA
with tab5:
    st.subheader("Rendimiento y Sostenibilidad Tecnológica de la IA")
    col_ia_d1, col_ia_d2, col_ia_d3 = st.columns(3)
    
    with col_ia_d1:
        st.markdown("#### ⚡ Latencia y Retención")
        st.metric("Latencia Promedio", f"{latency} seg", delta="-0.3 seg" if latency < 2.0 else "+0.4 seg")
        st.progress(max(0, min(100, int((5.0 - latency) / 4.5 * 100))))
        st.caption("Meta: Menor a 2.0 segundos para evitar tasas de rebote en Senior Users.")

    with col_ia_d2:
        st.markdown("#### 🎯 Resolución Autónoma")
        task_completion = min(100.0, accuracy * 1.05)
        st.metric("Task Completion Rate", f"{task_completion:.1f}%")
        st.caption("Consultas sociales e interacciones resueltas de forma autónoma por Sylver.")

    with col_ia_d3:
        st.markdown("#### 💸 Consumo de Inferencia")
        st.metric("Costo Promedio / Sesión", f"${cost_per_inference * 5:.3f} USD")
        st.metric("Costo Mensual Consolidado", f"${costo_ia_mensual_usd:,.0f} USD")
        st.caption("Infraestructura escalable optimizada para atender a jóvenes con costo incremental cero.")

# PESTAÑA 6: CRECIMIENTO SEMANAL Y PIVOT ASSESSMENT
with tab6:
    st.subheader("Análisis de Crecimiento y Estrategia de Sostenibilidad")
    on_track = growth_rate >= 10.0
    st.write(f"**Tasa de Crecimiento Semanal de la Plataforma:** `{growth_rate}%`")
    
    if on_track:
        st.success("🎉 ¡Felicidades! La Papaya está logrando la meta corporativa del 10% de crecimiento semanal.")
    else:
        st.error("⚠️ Alerta: No estamos alcanzando la meta del 10% de crecimiento semanal. Se requiere análisis estratégico.")
        
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
        ### **Evaluación de Cambio de Rumbo (Pivot B2B2C)**
        Dado que el crecimiento semanal actual (**{growth_rate}%**) está por debajo del objetivo del **10%**:
        
        * **Estrategia B2B SaaS:** Impulsar la venta corporativa de licencias de **$100 USD** para que las empresas cumplan metas de impacto social/ESG y obtengan certificados auditables automáticos creados por la IA.
        * **Escalamiento de Impacto:** Conectar la captación masiva mediante acuerdos corporativos para reducir el CAC de **$1,000 USD** y mantener el acceso gratuito de jóvenes apadrinados mediante la IA.
        """)
    else:
        st.markdown("""
        ### **Evaluación de Persistencia**
        El ritmo de crecimiento actual sostiene la operación. Se recomienda profundizar la tracción del canal B2B SaaS corporativo de $100 USD y mantener la optimización de latencia en la IA.
        """)
