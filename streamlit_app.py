import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Simulador de Suscripciones & ROI", layout="wide")

st.title("🚀 Simulador SaaS: Proyección de Ingresos, Break-Even y ROI")

# ==========================================
# BARRA LATERAL: PARÁMETROS DE ENTRADA
# ==========================================
st.sidebar.header("💰 1. Inversión Inicial & Costos")
inversion_inicial = st.sidebar.number_input(
    "Inversión Inicial Recibida ($)", 
    min_value=0.0, 
    value=50000.0, 
    step=5000.0,
    help="Capital inyectado hoy para simular el tiempo de retorno (Payback)"
)

costos_fijos_mes = st.sidebar.number_input(
    "Costos Fijos Mensuales ($)", 
    min_value=0.0, 
    value=10000.0, 
    step=500.0,
    help="Nómina, servidores, arriendo, software, etc."
)

margen_bruto_pct = st.sidebar.slider(
    "Margen Bruto (%)", 
    min_value=10, 
    max_value=100, 
    value=80,
    help="Porcentaje del ingreso retenido tras restar los costos directos/variables (COGS)"
) / 100.0

st.sidebar.header("📊 2. Plan y Suscriptores")
precio_suscripcion = st.sidebar.number_input("Precio del Plan Mensual ($)", min_value=1.0, value=50.0)
suscriptores_iniciales = st.sidebar.number_input("Suscriptores Iniciales", min_value=0, value=100)
nuevos_sub_mes = st.sidebar.number_input("Nuevos Suscriptores / Mes", min_value=0, value=30)
churn_rate_pct = st.sidebar.slider("Tasa de Cancelación / Churn Mensual (%)", min_value=0.0, max_value=20.0, value=3.0) / 100.0
meses_simulacion = st.sidebar.slider("Meses a Proyectar", min_value=6, max_value=60, value=24)

# ==========================================
# CÁLCULOS PRINCIPALES (MRR, ARR, BREAK-EVEN)
# ==========================================
# Cálculo de MRR requerido para alcanzar el Punto de Equilibrio
mrr_break_even = costos_fijos_mes / margen_bruto_pct if margen_bruto_pct > 0 else 0
sub_break_even = int(mrr_break_even / precio_suscripcion) if precio_suscripcion > 0 else 0

# Proyección mes a mes
datos_meses = []
subs_actuales = float(suscriptores_iniciales)
caja_acumulada = inversion_inicial
mes_break_even = None
mes_payback = None

for mes in range(1, meses_simulacion + 1):
    # Pérdida de clientes por churn y adición de nuevos
    cancelados = subs_actuales * churn_rate_pct
    subs_fin = max(0.0, subs_actuales - cancelados + nuevos_sub_mes)
    
    mrr = subs_fin * precio_suscripcion
    arr = mrr * 12
    
    # Finanzas del mes
    ingreso_neto_bruto = mrr * margen_bruto_pct
    utilidad_operativa = ingreso_neto_bruto - costos_fijos_mes
    
    # Identificar mes de Break-even
    if utilidad_operativa >= 0 and mes_break_even is None:
        mes_break_even = mes
        
    # Acumulado de caja para calcular retorno de inversión
    caja_acumulada += utilidad_operativa
    
    # Identificar mes de Payback (Retorno de Inversión)
    # Es cuando la utilidad acumulada generada alcanza o supera la inversión inicial recibida
    if (caja_acumulada >= inversion_inicial) and (mes_payback is None) and (utilidad_operativa > 0):
        mes_payback = mes

    datos_meses.append({
        "Mes": mes,
        "Suscriptores": round(subs_fin),
        "MRR": mrr,
        "ARR": arr,
        "Utilidad Mensual": utilidad_operativa,
        "Caja Acumulada": caja_acumulada
    })
    subs_actuales = subs_fin

df = pd.DataFrame(datos_meses)

# Métricas del Mes 1 vs Mes Final
mrr_actual = df.iloc[0]["MRR"]
arr_actual = df.iloc[0]["ARR"]
mrr_final = df.iloc[-1]["MRR"]
arr_final = df.iloc[-1]["ARR"]

# ==========================================
# PANEL DE MÉTRICAS CLAVE
# ==========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="MRR (Fin de Simulación)", 
        value=f"${mrr_final:,.0f}", 
        delta=f"${mrr_final - mrr_actual:,.0f} vs Mes 1"
    )

with col2:
    st.metric(
        label="ARR (Fin de Simulación)", 
        value=f"${arr_final:,.0f}", 
        delta=f"${arr_final - arr_actual:,.0f} vs Mes 1"
    )

with col3:
    st.metric(
        label="MRR para Break-Even", 
        value=f"${mrr_break_even:,.0f}",
        help=f"Necesitas aprox. {sub_break_even} clientes activos para cubrir costos fijos."
    )

with col4:
    if mes_payback:
        st.metric(
            label="Retorno de Inversión (Payback)", 
            value=f"Mes {mes_payback}",
            delta="Inversión recuperada",
            delta_color="normal"
        )
    else:
        st.metric(
            label="Retorno de Inversión (Payback)", 
            value="No alcanzado",
            delta="Amplía el tiempo o sube ventas",
            delta_color="inverse"
        )

st.markdown("---")

# ==========================================
# GRÁFICOS INTERACTIVOS
# ==========================================
tab1, tab2 = st.tabs(["📉 Visualización de MRR & Break-Even", "💵 Retorno de Inversión (Caja Acumulada)"])

with tab1:
    fig_mrr = px.line(
        df, 
        x="Mes", 
        y=["MRR", "ARR"], 
        labels={"value": "Monto ($)", "variable": "Métrica"},
        title="Evolución de Ingresos Recurrentes (MRR vs ARR)"
    )
    # Línea horizontal de Break-Even
    fig_mrr.add_hline(
        y=mrr_break_even, 
        line_dash="dash", 
        line_color="red", 
        annotation_text=f"Break-Even MRR (${mrr_break_even:,.0f})", 
        annotation_position="bottom right"
    )
    st.plotly_chart(fig_mrr, use_container_width=True)

with tab2:
    fig_caja = go.Figure()
    fig_caja.add_trace(go.Scatter(x=df["Mes"], y=df["Caja Acumulada"], mode='lines+markers', name='Caja / Capital Acumulado'))
    
    # Línea de la inversión inicial
    fig_caja.add_hline(
        y=inversion_inicial, 
        line_dash="dot", 
        line_color="green", 
        annotation_text=f"Inversión Inicial (${inversion_inicial:,.0f})", 
        annotation_position="top left"
    )
    
    fig_caja.update_layout(
        title="Recuperación del Capital en el Tiempo",
        xaxis_title="Mes",
        yaxis_title="Dólares ($)"
    )
    st.plotly_chart(fig_caja, use_container_width=True)

# ==========================================
# RESUMEN Y TABLA DE DATOS
# ==========================================
st.subheader("📋 Resumen Financiero")

col_left, col_right = st.columns(2)

with col_left:
    st.info(f"""
    **Estatus del Punto de Equilibrio:**
    * **MRR para cubrir costos:** ${mrr_break_even:,.2f}
    * **Suscriptores requeridos:** {sub_break_even} clientes activos.
    * **Estado:** {'Se alcanza en el **Mes ' + str(mes_break_even) + '**' if mes_break_even else '⚠️ No se alcanza en el periodo simulado.'}
    """)

with col_right:
    st.success(f"""
    **Estatus del Retorno de Inversión (ROI / Payback):**
    * **Capital Inyectado:** ${inversion_inicial:,.2f}
    * **Tiempo estimado de Retorno:** {'**' + str(mes_payback) + ' Meses**' if mes_payback else '⚠️ La inversión no alcanza a recuperarse en este horizonte de tiempo.'}
    """)

with st.expander("Ver tabla completa de proyección mes a mes"):
    st.dataframe(df.style.format({
        "MRR": "${:,.2f}",
        "ARR": "${:,.2f}",
        "Utilidad Mensual": "${:,.2f}",
        "Caja Acumulada": "${:,.2f}"
    }))
