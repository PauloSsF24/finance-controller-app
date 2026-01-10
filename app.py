import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from models.database import criar_tabelas
from controllers.viagem_controller import obter_dashboard
from views import cadastro_view, dashboard_view

criar_tabelas()

st.sidebar.title("📊 Menu")
opcao = st.sidebar.radio("Escolha", ["Cadastro de Viagem", "Dashboard Financeiro"])

if opcao == "Cadastro de Viagem":
    cadastro_view.render()

elif opcao == "Dashboard Financeiro":
    df = obter_dashboard()

    if df.empty:
        st.warning("Nenhuma viagem cadastrada ainda.")
    else:
        dashboard_view.render(df)
