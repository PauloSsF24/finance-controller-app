import streamlit as st
import plotly.express as px
from controllers.viagem_controller import editar_viagem, deletar_viagem


def render(df):
    st.title("📊 Dashboard Financeiro")

    # ================= KPIs =================
    total_frete = df["frete"].sum()
    total_despesas = (
        df["diesel"].sum()
        + df["pedagio"].sum()
        + df["manutencao"].sum()
        + df["outros"].sum()
    )
    lucro_total = df["lucro"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total em Fretes", f"R$ {total_frete:,.2f}")
    col2.metric("🧾 Total em Despesas", f"R$ {total_despesas:,.2f}")
    col3.metric("📈 Lucro Total", f"R$ {lucro_total:,.2f}")

    st.divider()

    # ================= GRÁFICO LUCRO =================
    st.subheader("📈 Lucro por Viagem")

    fig_lucro = px.line(
        df,
        x="data",
        y="lucro",
        markers=True,
        labels={"data": "Data", "lucro": "Lucro (R$)"}
    )

    st.plotly_chart(fig_lucro, use_container_width=True)

    st.divider()

    # ================= GRÁFICO DESPESAS =================
    st.subheader("🧾 Despesas por Categoria")

    despesas_df = df[["diesel", "pedagio", "manutencao", "outros"]].sum().reset_index()
    despesas_df.columns = ["Categoria", "Valor"]

    fig_despesas = px.bar(
        despesas_df,
        x="Categoria",
        y="Valor",
        labels={"Valor": "Valor (R$)"}
    )

    st.plotly_chart(fig_despesas, use_container_width=True)

    st.divider()

    # ================= TABELA =================
    st.subheader("📋 Histórico de Viagens")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # ================= CRUD =================
    st.subheader("✏️ Editar / 🗑️ Excluir Viagem")

    viagem_ids = df["id"].tolist()
    viagem_id = st.selectbox("Selecione a viagem pelo ID", viagem_ids)

    viagem = df[df["id"] == viagem_id].iloc[0]

    with st.form("form_edicao"):
        col1, col2 = st.columns(2)

        with col1:
            data = st.text_input("Data", viagem["data"])
            origem = st.text_input("Origem", viagem["origem"])
            destino = st.text_input("Destino", viagem["destino"])

        with col2:
            frete = st.number_input("Frete (R$)", value=float(viagem["frete"]))
            diesel = st.number_input("Diesel (R$)", value=float(viagem["diesel"]))
            pedagio = st.number_input("Pedágio (R$)", value=float(viagem["pedagio"]))
            manutencao = st.number_input("Manutenção (R$)", value=float(viagem["manutencao"]))
            outros = st.number_input("Outros (R$)", value=float(viagem["outros"]))

        lucro = frete - (diesel + pedagio + manutencao + outros)
        st.info(f"💰 Lucro atualizado: R$ {lucro:,.2f}")

        salvar = st.form_submit_button("💾 Salvar Alterações")

    if salvar:
        editar_viagem(
            viagem_id,
            data,
            origem,
            destino,
            frete,
            diesel,
            pedagio,
            manutencao,
            outros,
            lucro
        )
        st.success("✅ Viagem atualizada com sucesso!")
        st.experimental_rerun()

    st.divider()

    if st.button("❌ Excluir Viagem Selecionada"):
        deletar_viagem(viagem_id)
        st.warning("🗑️ Viagem excluída com sucesso!")
        st.experimental_rerun()
