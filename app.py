import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Configurações da página
st.set_page_config(page_title="Homens com Propósito", layout="wide")

st.title("📖 Palavras Diárias - Homens com Propósito")

# Conectar com Google Sheets
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)
client = gspread.authorize(creds)

# Abrir a planilha e aba
planilha_id = "1CxIMciTM6SvcQ3j_BYmgoEwCfqxwQmpg1_5hHoVuSPg"
sheet = client.open_by_key(planilha_id).worksheet("PALAVRA")
dados = sheet.get_all_records()

# Transformar em DataFrame
df = pd.DataFrame(dados)
df = df.astype(str)  # 👈 isso evita os erros de conversão


# Filtros
nomes = df["Nome"].unique()
livros = df["Livro"].unique()

col1, col2 = st.columns(2)
nome_selecionado = col1.selectbox("Filtrar por nome", ["Todos"] + list(nomes))
livro_selecionado = col2.selectbox("Filtrar por livro", ["Todos"] + list(livros))

# Aplicar filtros
if nome_selecionado != "Todos":
    df = df[df["Nome"] == nome_selecionado]
if livro_selecionado != "Todos":
    df = df[df["Livro"] == livro_selecionado]

# Mostrar tabela
st.dataframe(df)

# Mostrar cards
for _, row in df.iterrows():
    with st.expander(f"{row['Data']} - {row['Nome']}"):
        st.write(f"📖 **Livro:** {row['Livro']} - Capítulo {row.get('Capítulo', 'Não informado')}")
        st.write(f"⏱️ **Duração:** {row.get('Duração', 'Não informado')} minutos")

        link = row.get('Link', '').strip()
        if link and "drive.google.com" in link:
            st.markdown(
                f"""
                <a href="{link}" target="_blank">
                    <button style="background-color:#4CAF50;color:white;padding:8px 16px;border:none;border-radius:4px;cursor:pointer;">
                        🔗 Ouvir áudio
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.write("🔇 Sem link disponível")





