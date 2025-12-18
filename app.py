import streamlit as st
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="FinanceScope",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 FinanceScope")
st.subheader("Análise Inteligente de Documentos Financeiros")

# Verifica se a API key está configurada
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("⚠️ Configure sua OPENAI_API_KEY no arquivo .env")
    st.stop()

st.success("✅ Sistema configurado e pronto!")

# Placeholder para próximos passos
st.info("🚀 Projeto iniciado. Próximo passo: Upload de PDFs")