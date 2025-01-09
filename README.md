**Gerador de Senhas Seguras**
- Este projeto é um aplicativo de interface gráfica para gerar senhas seguras e personalizadas.Ele permite que os usuários configurem características específicas das senhas,
como números, símbolos, letras maiúsculas e minúsculas, além de escolher o tamanho da senha. O sistema também oferece integraçãopara envio de feedback via e-mail.


**Finalidade**
- Desenvolvimento de interfaces gráficas com Custom Tkinter.
- Uso de bibliotecas adicionais para funcionalidades específicas.
- Implementação de lógica para geração de conteúdo dinâmico.
- Integração de sistemas externos, como o Outlook, para envio de e-mails.
- Documentação e organização de código Python.

**Tecnologias Usadas**
- **Python 3.12.3**
- **Custom Tkinter**
- **Pillow** (para manipulação de imagens)
- **Win32com** (para integração com o Outlook)
- **Pyperclip** (para copiar informações para a área de transferência)
  
**Estrutura do Repositório**
- **/imagens**: Contém os ícones e imagens utilizados na interface gráfica.
- **main.py**: Arquivo principal com a lógica e interface do gerador de senhas.
- **requirements.txt**: Lista de dependências para instalação.

**Funcionalidades Principais**
- Geração de senhas seguras personalizáveis.
- Interface amigável para selecionar características das senhas.
- Integração com o Outlook para envio de feedback.
- Opção de copiar a senha gerada diretamente para a área de transferência.

**Como Rodar o Projeto**
Siga as instruções abaixo para rodar o projeto em sistemas operacionais Windows:

**Crie um ambiente virtual:**
- python -m venv venv
  
**Ative o ambiente virtual:**
- venv\Scripts\activate
  
**Instale as dependências:**
- pip install -r requirements.txt

**Clone o repositório:**
- git clone https://github.com/delciocruzs2/Gerador_de_Senhas.git

**Execute o projeto:**
- python main.py
  
Versão 1.0.0
