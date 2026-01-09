import streamlit as st
from controllers.viagem_controller import salvar_viagem

def render():
    st.header("📋 Cadastro de Viagem")

    dados = {
        "data": st.date_input("Data da Viagem"),
        "origem": st.text_input("Origem"),
        "destino": st.text_input("Destino"),
        "frete": st.number_input("Frete", min_value=0.0, format="%.2f"),
        "diesel": st.number_input("Custo com Diesel", min_value=0.0, format="%.2f"),
        "pedagio": st.number_input("Custo com Pedágio", min_value=0.0, format="%.2f"),
        "manutencao": st.number_input("Custo com Manutenção", min_value=0.0, format="%.2f"),
        "outros": st.number_input("Outros Custos", min_value=0.0, format="%.2f"),
    }

    if st.button("Salvar Viagem"):
        salvar_viagem(dados)
        st.success("Viagem cadastrada com sucesso!")