import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from views.login_view import render as login_view
from views.register_view import render as register_view


import streamlit as st
from models.database import criar_tabelas
from controllers.viagem_controller import obter_dashboard
from views import cadastro_view, dashboard_view

criar_tabelas()

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if "tela" not in st.session_state:
    st.session_state["tela"] = "login"

if not st.session_state["logado"]:
    if st.session_state["tela"] == "login":
        login_view()
    else:
        register_view()
    st.stop()



st.sidebar.title("📊 Menu")
opcao = st.sidebar.radio("Escolha", ["Cadastro de Viagem", "Dashboard Financeiro"])

if opcao == "Cadastro de Viagem":
    cadastro_view.render()

elif opcao == "Dashboard Financeiro":
    df = obter_dashboard()
    if not df.empty:
        dashboard_view.render(df)
    else:
        st.warning("Nenhuma viagem cadastrada ainda.")

st.sidebar.write(f"👤 {st.session_state['usuario']}")

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()
