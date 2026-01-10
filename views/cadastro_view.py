import streamlit as st
from controllers.viagem_controller import cadastrar_viagem


def render():
    st.title("🚛 Cadastro de Viagem")

    with st.form("form_viagem"):
        st.subheader("📍 Informações da Viagem")

        col1, col2 = st.columns(2)

        with col1:
            data = st.date_input("📅 Data da Viagem")
            origem = st.text_input("📌 Origem")
            destino = st.text_input("🏁 Destino")

        with col2:
            frete = st.number_input("💰 Valor do Frete (R$)", min_value=0.0, step=100.0)

        st.divider()
        st.subheader("🧾 Despesas")

        col3, col4, col5 = st.columns(3)

        with col3:
            diesel = st.number_input("⛽ Diesel (R$)", min_value=0.0, step=10.0)

        with col4:
            pedagio = st.number_input("🛣️ Pedágios (R$)", min_value=0.0, step=5.0)

        with col5:
            manutencao = st.number_input("🔧 Manutenção (R$)", min_value=0.0, step=10.0)

        outros = st.number_input("📦 Outras Despesas (R$)", min_value=0.0, step=10.0)

        lucro = frete - (diesel + pedagio + manutencao + outros)

        st.info(f"💵 **Lucro estimado:** R$ {lucro:,.2f}")

        submitted = st.form_submit_button("✅ Cadastrar Viagem")

        if submitted:
            if not origem or not destino:
                st.error("⚠️ Origem e destino são obrigatórios.")
                return

            cadastrar_viagem(
                data=str(data),
                origem=origem,
                destino=destino,
                frete=frete,
                diesel=diesel,
                pedagio=pedagio,
                manutencao=manutencao,
                outros=outros,
                lucro=lucro
            )

            st.success("🚚 Viagem cadastrada com sucesso!")
            st.balloons()
