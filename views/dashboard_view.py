import streamlit as st
import plotly.express as px


def render(df):
    st.title("📊 Dashboard Financeiro")

    # ===== KPIs =====
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

    # ===== Gráfico: Lucro por Viagem =====
    st.subheader("📈 Lucro por Viagem")

    fig_lucro = px.line(
        df,
        x="data",
        y="lucro",
        markers=True,
        title="Lucro por Viagem",
        labels={"data": "Data", "lucro": "Lucro (R$)"}
    )

    st.plotly_chart(fig_lucro, use_container_width=True)

    st.divider()

    # ===== Gráfico: Despesas =====
    st.subheader("🧾 Distribuição de Despesas")

    despesas_df = df[["diesel", "pedagio", "manutencao", "outros"]].sum().reset_index()
    despesas_df.columns = ["Categoria", "Valor"]

    fig_despesas = px.bar(
        despesas_df,
        x="Categoria",
        y="Valor",
        title="Despesas Totais por Categoria",
        labels={"Valor": "Valor (R$)"}
    )

    st.plotly_chart(fig_despesas, use_container_width=True)

    st.divider()

    # ===== Tabela =====
    st.subheader("📋 Histórico de Viagens")
    st.dataframe(df, use_container_width=True)
