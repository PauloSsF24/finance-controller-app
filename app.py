import streamlit as st
from models.database import criar_tabelas
from controllers.viagem_controller import obter_dashboard
from views import cadastro_view, dashboard_view

criar_tabelas()

st.sidebar.title("🚛 Menu")
opcao = st.sidebar.radio("Escolha", ["Cadastro de Viagem", "Dashboard Financeiro"])

if opcao == "Cadastro":
    cadastro_view.render()
else:
    df = obter_dashboard()
    if not df.empty:
        dashboard_view.render(df)
    else:
        st.warning("Nenhuma viagem cadastrada ainda.")