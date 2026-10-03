import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Ponto de Equilíbrio", page_icon="📈", layout="wide")

st.title("📈 Calculadora de Ponto de Equilíbrio (Break-even)")
st.caption("Determine o faturamento mínimo necessário para cobrir 100% das despesas fixas e variáveis.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Custos Fixos Mensais (R$)")
    aluguel = st.number_input("Aluguel + Condomínio + IPTU:", value=3500.0, step=100.0)
    folha_pagamento = st.number_input("Folha / Pró-labore / Encargos:", value=8500.0, step=500.0)
    sistemas_sistemas = st.number_input("Sistemas / Automações / Internet:", value=600.0, step=50.0)
    contabilidade_mkt = st.number_input("Contabilidade + Tráfego Pago Fixo:", value=1500.0, step=100.0)
    outros_fixos = st.number_input("Outros Custos Fixos (Água, Luz, etc.):", value=1400.0, step=100.0)

    total_custos_fixos = aluguel + folha_pagamento + sistemas_sistemas + contabilidade_mkt + outros_fixos

with col2:
    st.subheader("2. Margem de Contribuição Média (%)")
    cmv_medio = st.slider("CMV Médio (%):", 15.0, 50.0, 32.0, 0.5)
    taxa_apps = st.slider("Taxa Média de Comissão de Apps (%):", 0.0, 30.0, 18.0, 0.5)
    impostos = st.slider("Impostos (% Simples Nacional):", 0.0, 20.0, 6.0, 0.5)
    outros_variaveis = st.slider("Outros Variáveis (% Taxa Cartão, Embalagens extra):", 0.0, 15.0, 4.0, 0.5)

    margem_contrib_pct = 100.0 - (cmv_medio + taxa_apps + impostos + outros_variaveis)
    ticket_medio = st.number_input("Ticket Médio por Pedido (R$):", value=45.0, step=1.0)

st.divider()

# --- CÁLCULOS E RESULTADOS ---
if margem_contrib_pct <= 0:
    st.error("🚨 SUA MARGEM DE CONTRIBUIÇÃO É MENOR OU IGUAL A ZERO! Você perde dinheiro em cada venda feita.")
else:
    ponto_equilibrio_reais = total_custos_fixos / (margem_contrib_pct / 100)
    pedidos_necessarios = ponto_equilibrio_reais / ticket_medio
    pedidos_dia = pedidos_necessarios / 30

    res1, res2, res3, res4 = st.columns(4)
    res1.metric("Custos Fixos Totais", f"R$ {total_custos_fixos:,.2f}")
    res2.metric("Margem Contribuição", f"{margem_contrib_pct:.1f}%")
    res3.metric("Faturamento Mínimo", f"R$ {ponto_equilibrio_reais:,.2f}")
    res4.metric("Pedidos / Mês (Dia)", f"{int(pedidos_necessarios)} ({pedidos_dia:.1f}/dia)")

    # Gráfico de Ponto de Equilíbrio
    faturamento_simulado = [i * (ponto_equilibrio_reais * 2 / 20) for i in range(21)]
    custos_totais_simulados = [total_custos_fixos + (f * (1 - margem_contrib_pct/100)) for f in faturamento_simulado]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=faturamento_simulado, y=faturamento_simulado, mode='lines', name='Faturamento (Receita)', line=dict(color='#2ecc71', width=3)))
    fig.add_trace(go.Scatter(x=faturamento_simulado, y=custos_totais_simulados, mode='lines', name='Custos Totais', line=dict(color='#e74c3c', width=3)))
    fig.add_trace(go.Scatter(x=faturamento_simulado, y=[total_custos_fixos]*len(faturamento_simulado), mode='lines', name='Custos Fixos', line=dict(color='#f39c12', dash='dash')))

    fig.add_vline(x=ponto_equilibrio_reais, line_dash="dash", line_color="white", annotation_text=f"Breakeven: R$ {ponto_equilibrio_reais:,.0f}")

    fig.update_layout(
        title="Gráfico do Ponto de Equilíbrio",
        xaxis_title="Faturamento Mensal (R$)",
        yaxis_title="Valores (R$)",
        height=400,
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)
