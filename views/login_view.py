import streamlit as st
from controllers.auth_controller import autenticar


def render():
    st.title("🔐 Login")

    username = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if autenticar(username, senha):
            st.session_state["logado"] = True
            st.session_state["usuario"] = username
            st.session_state["tela"] = "dashboard"
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.divider()

    if st.button("Criar conta"):
        st.session_state["tela"] = "registro"
        st.rerun()
