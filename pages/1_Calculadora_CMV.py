import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Calculadora de CMV", page_icon="🧮", layout="wide")

st.title("🧮 Calculadora de CMV (Custo de Mercadoria Vendida)")
st.caption("Monitore e controle a fatia do faturamento consumida pelos insumos.")

tab1, tab2 = st.tabs(["📊 CMV Global Periódico", "🍔 Ficha Técnica por Prato"])

# --- TAB 1: CMV GLOBAL ---
with tab1:
    st.subheader("Cálculo do CMV Real do Período")
    
    col1, col2 = st.columns(2)
    with col1:
        faturamento = st.number_input("Faturamento Bruto Total (R$):", min_value=0.0, value=50000.0, step=1000.0)
        estoque_inicial = st.number_input("Estoque Inicial do Mês (R$):", min_value=0.0, value=8000.0, step=500.0)
        compras = st.number_input("Compras de Insumos no Período (R$):", min_value=0.0, value=17000.0, step=500.0)
        estoque_final = st.number_input("Estoque Final Contado (R$):", min_value=0.0, value=9000.0, step=500.0)

    with col2:
        cmv_reais = (estoque_inicial + compras) - estoque_final
        cmv_percentual = (cmv_reais / faturamento * 100) if faturamento > 0 else 0

        st.markdown("### Resultado do CMV Periódico")
        m1, m2 = st.columns(2)
        m1.metric("CMV Total (R$)", f"R$ {cmv_reais:,.2f}")
        m2.metric("CMV (% do Faturamento)", f"{cmv_percentual:.2f}%")

        # Avaliação do indicador
        if cmv_percentual <= 32:
            st.success("🟢 **CMV Excelente!** Seu custo de insumos está dentro da faixa ideal para delivery (28% a 32%).")
        elif cmv_percentual <= 38:
            st.warning("🟡 **CMV em Alerta.** Atenção com fichas técnicas, porcionamento e desperdícios (33% a 38%).")
        else:
            st.error("🔴 **CMV Crítico!** Acima de 38% o lucro do delivery é gravemente comprometido pelas taxas dos apps.")

        # Gráfico de Rosca
        df_chart = pd.DataFrame({
            "Categoria": ["CMV (Insumos)", "Margem/Outros Custos"],
            "Valor": [cmv_reais, max(0.0, faturamento - cmv_reais)]
        })
        fig = px.pie(df_chart, values="Valor", names="Categoria", hole=0.5, color_discrete_sequence=["#e74c3c", "#2ecc71"])
        fig.update_layout(height=280, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: FICHA TÉCNICA ---
with tab2:
    st.subheader("Engenharia de Cardápio: CMV por Item")
    nome_prato = st.text_input("Nome do Prato/Combo:", value="Burguer Smash Duplo")
    preco_venda_prato = st.number_input("Preço de Venda no App (R$):", min_value=0.1, value=35.0, step=1.0)

    st.markdown("#### Insumos & Embalagens")
    
    # Tabela dinâmica simples
    df_inicial = pd.DataFrame([
        {"Insumo": "Pão Brioche", "Quantidade": 1, "Unidade": "un", "Custo Unitário (R$)": 1.50},
        {"Insumo": "Hambúrguer 100g", "Quantidade": 2, "Unidade": "un", "Custo Unitário (R$)": 3.20},
        {"Insumo": "Queijo Cheddar Fatiado", "Quantidade": 2, "Unidade": "fatia", "Custo Unitário (R$)": 0.80},
        {"Insumo": "Molho Especial", "Quantidade": 30, "Unidade": "g", "Custo Unitário (R$)": 0.03},
        {"Insumo": "Embalagem Hambúrguer", "Quantidade": 1, "Unidade": "un", "Custo Unitário (R$)": 1.20},
    ])

    edited_df = st.data_editor(df_inicial, num_rows="dynamic", use_container_width=True)
    
    # Cálculos da ficha
    edited_df["Custo Total Insumo (R$)"] = edited_df["Quantidade"] * edited_df["Custo Unitário (R$)"]
    custo_total_prato = edited_df["Custo Total Insumo (R$)"].sum()
    cmv_prato_pct = (custo_total_prato / preco_venda_prato) * 100

    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Custo Total de Insumos", f"R$ {custo_total_prato:.2f}")
    col_b.metric("Preço de Venda", f"R$ {preco_venda_prato:.2f}")
    col_c.metric("CMV Direto do Item", f"{cmv_prato_pct:.1f}%")
