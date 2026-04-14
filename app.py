import streamlit as st
from openai import OpenAI
import os

st.set_page_config(
    page_title="AI Internal Communication Generator",
    page_icon="💬",
    layout="centered"
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Internal Communication Generator")
st.markdown("Gere mensagens internas automaticamente utilizando IA generativa.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    tipo = st.selectbox(
        "Tipo de mensagem",
        ["Aviso", "Lembrete", "Motivacional"]
    )

with col2:
    tom = st.selectbox(
        "Tom",
        ["Formal", "Descontraído"]
    )

tema = st.text_input("Tema da mensagem")

# Função com IA real
def gerar_mensagem(tipo, tema, tom):

    prompt = f"""
    Gere uma mensagem interna corporativa.

    Tipo: {tipo}
    Tema: {tema}
    Tom: {tom}

    A mensagem deve ser clara, bem escrita e adequada para colaboradores de uma empresa.
    Não use linguagem genérica demais. Seja específico e natural.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

if st.button("Gerar mensagem", use_container_width=True):

    if not tema.strip():
        st.warning("Por favor, digite um tema.")
    else:
        with st.spinner("Gerando mensagem com IA..."):
            mensagem = gerar_mensagem(tipo, tema, tom)

        st.success("Mensagem gerada com sucesso!")
        st.markdown("### Resultado")
        st.write(mensagem)

        st.download_button(
            "Baixar mensagem",
            mensagem,
            file_name="mensagem.txt"
        )