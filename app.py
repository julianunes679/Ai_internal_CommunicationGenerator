import streamlit as st

# Configuração da página (mais profissional)
st.set_page_config(
    page_title="AI Internal Communication Generator",
    page_icon="💬"
)

# Título e descrição
st.title("💬 AI Internal Communication Generator")
st.write("Gere mensagens corporativas automaticamente de forma rápida e eficiente.")

# Entradas do usuário
tipo = st.selectbox(
    "Tipo de mensagem",
    ["Aviso", "Lembrete", "Motivacional"]
)

tema = st.text_input("Tema da mensagem")

tom = st.selectbox(
    "Tom da mensagem",
    ["Formal", "Descontraído"]
)

# Função que gera a mensagem (simulação de IA)
def gerar_mensagem(tipo, tema, tom):

    if tom == "Formal":
        return f"""
Prezados colaboradores,

Gostaríamos de informar um {tipo.lower()} relacionado a {tema}.

Pedimos a atenção de todos para garantir o cumprimento das orientações.

Atenciosamente,  
Equipe
"""
    else:
        return f"""
Fala, pessoal! 

Passando aqui para lembrar sobre {tema}.

Contamos com vocês! Qualquer dúvida, estamos por aqui. 
"""

# Botão de ação
if st.button("Gerar mensagem"):

    if tema.strip() == "":
        st.warning("Por favor, digite um tema antes de gerar a mensagem.")
    else:
        mensagem = gerar_mensagem(tipo, tema, tom)

        st.success("Mensagem gerada com sucesso!")
        st.markdown("### 📄 Resultado:")
        st.write(mensagem)