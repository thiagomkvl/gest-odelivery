import streamlit as st

st.set_page_config(page_title="Mini Curso: Precificação", page_icon="🎓", layout="wide")

st.title("🎓 Mini Curso: Precificação Inteligente para Delivery")
st.caption("Domine os conceitos fundamentais para nunca mais pagar para vender nos aplicativos.")

modulo = st.radio("Selecione o Módulo:", [
    "Módulo 1: O Triângulo da Precificação",
    "Módulo 2: O Perigo da Regra dos 3x",
    "Módulo 3: O Método do Markup Divisor",
    "Simulador Interativo de Preço"
], horizontal=True)

st.divider()

if modulo == "Módulo 1: O Triângulo da Precificação":
    st.subheader("📐 O Triângulo da Precificação para Delivery")
    st.write("""
    Para precificar um prato no delivery, seu preço final precisa cobrir exatamente **4 pilares básicos**:
    
    1. **CMV (Custo do Prato + Embalagem):** Insumos diretos utilizados no preparo.
    2. **Custos Variáveis de Venda:** Taxa do iFood, imposto (Simples) e taxa de cartão.
    3. **Contribuição para Custos Fixos:** Fatia para pagar aluguel, equipe e sistemas.
    4. **Lucro Líquido Desejado:** A recompensa do sócio pelo risco do negócio.
    """)
    st.info("💡 **Regra Ouro:** No delivery, o canal de venda altera o custo do produto. O mesmo hambúrguer DEVE ter preços diferentes no Balcão e no iFood.")

elif modulo == "Módulo 2: O Perigo da Regra dos 3x":
    st.subheader("⚠️ Por que multiplicar o custo por 3 quebra o seu Delivery?")
    st.write("""
    Muitos donos de restaurantes usam a regra antiga: *'Se o produto custa R$ 10, multiplico por 3 e vendo por R$ 30'*.
    
    **Veja o que acontece no iFood:**
    * **Custo do Insumo:** R$ 10,00
    * **Preço de Venda:** R$ 30,00
    * **(-) Comissão iFood (23%):** R$ 6,90
    * **(-) Imposto (6%):** R$ 1,80
    * **(-) Custo do Insumo:** R$ 10,00
    * **Sobram:** R$ 11,30 (Margem bruta de 37,6%)
    
    Depois de pagar aluguel, funcionários e energia, **o lucro desaparece**. A regra dos 3x ignora as taxas abusivas dos marketplaces.
    """)

elif modulo == "Módulo 3: O Método do Markup Divisor":
    st.subheader("🧮 A Fórmula Exata: Markup Divisor")
    st.markdown("""
    A forma matemática correta de precificar é usando o **Markup Divisor**:

    $$\\text{Preço de Venda} = \\frac{\\text{Custo dos Insumos + Embalagem}}{1 - \\frac{\\sum \\% \\text{Custos Variáveis e Lucro}}{100}}$$

    #### Exemplo Prático:
    * **Custo do Insumo + Embalagem:** R$ 12,00
    * **Comissão App:** 21%
    * **Imposto:** 6%
    * **Margem Desejada (Fixo + Lucro):** 35%
    * **Soma das Porcentagens:** 21 + 6 + 35 = **62%**

    $$\\text{Preço de Venda} = \\frac{12,00}{1 - 0,62} = \\frac{12,00}{0,38} = \\mathbf{R\\$ 31,58}$$
    """)

elif modulo == "Simulador Interativo de Preço":
    st.subheader("🛠️ Simulador de Precificação por Markup Divisor")
    
    col1, col2 = st.columns(2)
    with col1:
        custo_insumos = st.number_input("Custo de Insumos + Embalagem (R$):", value=12.00, step=0.50)
        taxa_canal = st.number_input("Taxa do Canal / iFood (%):", value=23.00, step=0.50)
        imposto_simples = st.number_input("Imposto Simples Nacional (%):", value=6.00, step=0.50)
        outros_custos_var = st.number_input("Outros Custos Variáveis (Cartão/Mkt %):", value=3.00, step=0.50)
        margem_lucro_desejada = st.number_input("Margem Bruta Alvo (Para Cobrir Fixos + Lucro %):", value=35.00, step=1.00)

    sum_pct = taxa_canal + imposto_simples + outros_custos_var + margem_lucro_desejada
    
    with col2:
        st.markdown("### Resultado da Precificação")
        if sum_pct >= 100:
            st.error("🚨 A soma das porcentagens é maior ou igual a 100%. É impossível precificar com estes parâmetros.")
        else:
            divisor = 1 - (sum_pct / 100)
            preco_sugerido = custo_insumos / divisor
            lucro_bruto_reais = preco_sugerido * (margem_lucro_desejada / 100)

            st.metric("Preço de Venda Sugerido", f"R$ {preco_sugerido:.2f}")
            st.metric("Margem Bruta em Reais", f"R$ {lucro_bruto_reais:.2f}")

            st.markdown(f"""
            **Detalhamento de onde vai cada real do preço (R$ {preco_sugerido:.2f}):**
            * 🔴 **Canal de Venda ({taxa_canal}%):** R$ {preco_sugerido * (taxa_canal/100):.2f}
            * 🟡 **Insumos e Embalagem:** R$ {custo_insumos:.2f}
            * 🔵 **Impostos ({imposto_simples}%):** R$ {preco_sugerido * (imposto_simples/100):.2f}
            * 🟢 **Margem Contribuição ({margem_lucro_desejada}%):** R$ {lucro_bruto_reais:.2f}
            """)
