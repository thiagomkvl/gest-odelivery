import streamlit as st
import pandas as pd

st.set_page_config(page_title="Raio-X Financeiro", page_icon="🩺", layout="wide")

st.title("🩺 Raio-X Financeiro & Diagnóstico DRE Operacional")
st.caption("Entenda o fluxo completo do dinheiro: do faturamento bruto ao lucro líquido que entra no bolso.")

# --- ENTRADA DE DADOS ---
with st.sidebar:
    st.header("⚙️ Parâmetros Operacionais")
    faturamento = st.number_input("Faturamento Mensal Bruto (R$):", value=60000.0, step=2000.0)
    
    st.subheader("Participação por Canal")
    pct_ifood = st.slider("% Faturamento iFood:", 0, 100, 60)
    pct_proprio = st.slider("% Faturamento Canal Próprio:", 0, 100 - pct_ifood, 40)
    
    st.subheader("Custos Variáveis (%)")
    taxa_ifood = st.number_input("Taxa Média iFood (%):", value=21.5, step=0.5)
    taxa_proprio = st.number_input("Taxa Pagamento Próprio/Gateway (%):", value=3.2, step=0.1)
    cmv = st.number_input("CMV Média Global (%):", value=32.0, step=0.5)
    imposto = st.number_input("Imposto Simples Nacional (%):", value=6.0, step=0.5)
    embalagens = st.number_input("Embalagens / Insumos de Entrega (%):", value=4.5, step=0.5)
    
    st.subheader("Despesas Fixas e Mkt")
    custos_fixos = st.number_input("Custos Fixos Totais (R$):", value=14000.0, step=500.0)
    investimento_mkt = st.number_input("Investimento em Anúncios (R$):", value=1500.0, step=100.0)

# --- CONSTRUÇÃO DA DRE ---
comissao_apps_reais = (faturamento * (pct_ifood/100) * (taxa_ifood/100)) + (faturamento * (pct_proprio/100) * (taxa_proprio/100))
cmv_reais = faturamento * (cmv / 100)
imposto_reais = faturamento * (imposto / 100)
embalagens_reais = faturamento * (embalagens / 100)

total_variaveis_reais = comissao_apps_reais + cmv_reais + imposto_reais + embalagens_reais
margem_bruta_reais = faturamento - total_variaveis_reais

lucro_operacional_reais = margem_bruta_reais - custos_fixos - investimento_mkt
margem_liquida_pct = (lucro_operacional_reais / faturamento * 100) if faturamento > 0 else 0

# --- APRESENTAÇÃO DOS RESULTADOS ---
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("📊 Demonstrativo de Resultado Operacional (DRE)")
    
    dre_data = [
        {"Linha": "1. Faturamento Bruto", "Valor (R$)": faturamento, "% Faturamento": 100.0},
        {"Linha": "(-) Comissões de Apps & Taxas", "Valor (R$)": -comissao_apps_reais, "% Faturamento": - (comissao_apps_reais/faturamento*100)},
        {"Linha": "(-) CMV (Insumos/Ingredientes)", "Valor (R$)": -cmv_reais, "% Faturamento": -cmv},
        {"Linha": "(-) Impostos", "Valor (R$)": -imposto_reais, "% Faturamento": -imposto},
        {"Linha": "(-) Embalagens", "Valor (R$)": -embalagens_reais, "% Faturamento": -embalagens},
        {"Linha": "= Margem de Contribuição Bruta", "Valor (R$)": margem_bruta_reais, "% Faturamento": (margem_bruta_reais/faturamento*100)},
        {"Linha": "(-) Custos Fixos Operacionais", "Valor (R$)": -custos_fixos, "% Faturamento": -(custos_fixos/faturamento*100)},
        {"Linha": "(-) Marketing & Tráfego Pago", "Valor (R$)": -investimento_mkt, "% Faturamento": -(investimento_mkt/faturamento*100)},
        {"Linha": "= LUCRO LÍQUIDO OPERACIONAL", "Valor (R$)": lucro_operacional_reais, "% Faturamento": margem_liquida_pct}
    ]

    df_dre = pd.DataFrame(dre_data)
    
    def highlight_rows(row):
        if "LUCRO" in row["Linha"]:
            return ['background-color: #1e3799; font-weight: bold'] * len(row)
        elif "=" in row["Linha"]:
            return ['background-color: #2c3e50; font-weight: bold'] * len(row)
        return [''] * len(row)

    st.dataframe(
        df_dre.style.apply(highlight_rows, axis=1).format({"Valor (R$)": "R$ {:,.2f}", "% Faturamento": "{:.1f}%"}),
        use_container_width=True,
        hide_index=True
    )

with col2:
    st.subheader("🩺 Diagnóstico do Especialista")
    
    st.metric("Lucro Líquido Final", f"R$ {lucro_operacional_reais:,.2f}", f"{margem_liquida_pct:.1f}% de Margem")

    if margem_liquida_pct >= 15:
        st.markdown("<div class='metric-card'><h4 class='status-healthy'>🟢 Saúde Financeira Excelente</h4>Seu delivery está gerando um resultado altamente lucrativo (acima de 15%). Foco em escala.</div>", unsafe_allow_html=True)
    elif margem_liquida_pct >= 8:
        st.markdown("<div class='metric-card'><h4 class='status-warning'>🟡 Operação Estável, mas Vulnerável</h4>Margem entre 8% e 14%. Qualquer oscilação em vendas ou alta em insumos pode zerar seu resultado.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='metric-card'><h4 class='status-danger'>🔴 Alerta Crítico de Rentabilidade</h4>Margem abaixo de 8%. Você está trabalhando duro para pagar apps e fornecedores.</div>", unsafe_allow_html=True)

    st.markdown("#### 💡 Plano de Ação Recomendado:")
    
    if pct_ifood > 70:
        st.warning("⚠️ **Alta Dependência do iFood:** Mais de 70% das suas vendas estão no iFood. Fortaleça seu Canal Próprio (WhatsApp/App) para economizar em comissões.")
    if cmv > 35:
        st.error("⚠️ **CMV Elevado:** Seu custo de insumos está acima de 35%. Recalcule fichas técnicas ou renegocie com fornecedores imediatamente.")
