import streamlit as st

def render(df):
    st.header("📊 Dashboard Financeiro")

    col1, col2, col3 = st.columns(3)
    col1.metric("Fretes", f"R$ {df['frete'].sum():.2f}")
    col2.metric("Despesas", f"R$ {df[['diesel', 'pedagio', 'manutencao', 'outros']].sum().sum():.2f}")
    col3.metric("Lucro", f"R$ {df['lucro'].sum():,.2f}")

    st.line_chart(df.set_index("id")["lucro"])
    st.dataframe(df)