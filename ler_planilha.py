import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 🔐 Conectar com Google Sheets usando credenciais
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

# Substitua pelo nome do seu arquivo de credenciais JSON
creds = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)
client = gspread.authorize(creds)

# 📄 Abrir a planilha usando o ID e acessar a aba "PALAVRA"
planilha_id = "1CxIMciTM6SvcQ3j_BYmgoEwCfqxwQmpg1_5hHoVuSPg"
sheet = client.open_by_key(planilha_id).worksheet("PALAVRA")

# 📊 Ler todos os registros da aba
dados = sheet.get_all_records()

# 🖨️ Mostrar os dados no terminal
for item in dados:
    print(f"📅 Data: {item['Data']}")
    print(f"👤 Nome: {item['Nome']}")
    print(f"📖 Livro: {item['Livro']} - Capítulo: {item['Capítulo']}")
    print(f"🔗 Link do áudio: {item['Link']}")
    print("-" * 50)
