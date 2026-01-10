# 🚛 FinanceApp – Controle Financeiro para Caminhoneiros

Sistema de controle financeiro desenvolvido em **Python**, com foco em **motoristas de caminhão**, permitindo o acompanhamento detalhado de **despesas**, **fretes**, **lucro por viagem** e **visualização em dashboard interativo**.

Este projeto foi construído com **arquitetura MVC**, banco de dados local e dashboard moderno utilizando **Streamlit + Plotly**.

---

## 📌 Funcionalidades

* ✅ Cadastro de viagens
* 💰 Controle de fretes recebidos
* ⛽ Registro de despesas (diesel, pedágio, manutenção e outros)
* 📈 Cálculo automático de lucro por viagem
* 📊 Dashboard financeiro interativo
* 📋 Histórico completo de viagens
* 🧱 Arquitetura MVC bem definida

---

## 🖥️ Tecnologias Utilizadas

* **Python 3**
* **Streamlit** – Interface web
* **SQLite** – Banco de dados local
* **Pandas** – Manipulação de dados
* **Plotly** – Gráficos interativos

---

## 🏗️ Arquitetura do Projeto (MVC)

```
financeApp/
│
├── app.py
│
├── controllers/
│   ├── __init__.py
│   └── viagem_controller.py
│
├── models/
│   ├── __init__.py
│   ├── database.py
│   └── viagem_model.py
│
├── views/
│   ├── __init__.py
│   ├── cadastro_view.py
│   └── dashboard_view.py
│
├── requirements.txt
└── finance.db
```

### 📂 Responsabilidades

* **Model**: regras de negócio e acesso ao banco de dados
* **Controller**: orquestra a lógica entre View e Model
* **View**: interface gráfica (Streamlit)

---

## 📊 Dashboard

O dashboard apresenta:

* KPIs financeiros (frete, despesas e lucro total)
* Gráfico interativo de **lucro por viagem**
* Gráfico de **despesas por categoria**
* Tabela com histórico completo

Os gráficos são totalmente interativos, permitindo zoom e inspeção de valores.

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/financeApp.git
cd financeApp
```

### 2️⃣ Crie e ative um ambiente virtual (opcional)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute a aplicação

```bash
streamlit run app.py
```

---

## 🧠 Aprendizados

Este projeto reforça conceitos importantes como:

* Arquitetura MVC na prática
* Integração de Python com banco de dados
* Criação de dashboards interativos
* Organização de código para projetos reais

---

## 📌 Próximas Evoluções

* ✏️ Edição e exclusão de viagens
* 📆 Filtro por período
* 📤 Exportação de relatórios (Excel/PDF)
* ☁️ Deploy em nuvem

---

## 👨‍💻 Autor

**Paulo Sérgio**
Full Stack Developer Jr

📎 LinkedIn: [https://www.linkedin.com/](https://www.linkedin.com/in/paulossf/)

---

⭐ Se este projeto te ajudou ou chamou sua atenção, deixe uma estrela no repositório!
