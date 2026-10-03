import streamlit as st

st.set_page_config(
    page_title="Gestão & Precificação para Delivery",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS GLOBAL ---
st.markdown("""
<style>
    /* Estilo principal de cards e métricas */
    .metric-card {
        background-color: #1E222D;
        border: 1px solid #2B313E;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .status-healthy { color: #2ecc71; font-weight: bold; }
    .status-warning { color: #f1c40f; font-weight: bold; }
    .status-danger { color: #e74c3c; font-weight: bold; }
    
    /* Customização dos títulos */
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #8B949E;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- SISTEMA DE AUTENTICAÇÃO ---
def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.markdown("<h2 style='text-align: center;'>🔐 Acesso Restrito ao Gestor</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password_input = st.text_input("Digite a Senha Mestre de Acesso:", type="password")
        if st.button("Entrar no Painel", use_container_width=True):
            # Obtém senha do secrets.toml ou usa padrão de fallback
            correct_password = st.secrets.get("auth", {}).get("master_password", "delivery123")
            
            if password_input == correct_password:
                st.session_state.authenticated = True
                st.rerun()
                return True
            else:
                st.error("❌ Senha incorreta. Verifique suas credenciais.")
        return False

if check_password():
    # --- INTERFACE INICIAL / HUB ---
    st.markdown("<div class='main-header'>🍔 Hub de Inteligência Financeira para Delivery</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Aumente sua margem, domine seus custos e precifique com precisão matemática.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>🧮 1. Calculadora de CMV</h3>
            <p>Descubra o Custo de Mercadoria Vendida do seu restaurante, analise fichas técnicas e identifique desperdícios.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='metric-card'>
            <h3>📈 2. Ponto de Equilíbrio</h3>
            <p>Calcule exatamente quantos pedidos e qual faturamento mínimo você precisa atingir por dia para não ter prejuízo.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>🩺 3. Raio-X Financeiro</h3>
            <p>Diagnóstico completo do seu DRE Operacional. Visualize o impacto das taxas de apps e margem de lucro real.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='metric-card'>
            <h3>🎓 4. Mini Curso: Precificação</h3>
            <p>Aprenda a aplicar o <b>Markup Divisor</b> e pare de perder dinheiro usando regras ultrapassadas como multiplicar por 3.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("👈 Use o menu lateral para navegar entre os módulos do sistema.")
