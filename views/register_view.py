import streamlit as st
from controllers.auth_controller import registrar


def render():
    st.title("📝 Criar Conta")

    username = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    confirmar = st.text_input("Confirmar senha", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Registrar"):
            if not username or not senha:
                st.error("Preencha todos os campos")
                return

            if senha != confirmar:
                st.error("As senhas não coincidem")
                return

            if registrar(username, senha):
                st.success("Conta criada com sucesso! Faça login.")
                st.session_state["tela"] = "login"
                st.rerun()
            else:
                st.error("Usuário já existe")

    with col2:
        if st.button("⬅️ Voltar para Login"):
            st.session_state["tela"] = "login"
            st.rerun()
