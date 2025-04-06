# Flask Pets API

Este é um projeto de exemplo de uma API REST para gerenciar informações de pets, desenvolvido utilizando Flask e Flask-RESTx. O projeto foi criado como primeira tarefa da disciplina **"Desenvolvimento de APIs e Microsserviços"**.

## Tecnologias

As principais tecnologias utilizadas neste projeto são:

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para criação de APIs.
- **Flask-RESTx**: Extensão para facilitar o desenvolvimento de APIs RESTful.
- **Pytest**: Ferramenta para criação e execução de testes automatizados.

## Funcionalidades

- Cadastro de pets.
- Consulta de pets cadastrados.
- Atualização de informações de pets.
- Exclusão de pets.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.8 ou superior.
- Pip (gerenciador de pacotes do Python).
- Virtualenv (opcional, mas recomendado).

## Como executar

Siga os passos abaixo para executar o projeto:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/ygorsg/dams-api-flask-pets.git
   cd dams-api-flask-pets
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No Linux/Mac
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto e adicione as variáveis necessárias. Exemplo:

   ```plaintext
   SERVER_HOST=localhost
   SERVER_PORT=5500
   ENV=DEVELOPMENT
   ```

5. **Execute o servidor**:

   ```bash
   python run.py
   ```

6. **Acesse a API**:
   A API estará disponível em: [http://localhost:5000](http://localhost:5000)

## Testes

Para executar os testes automatizados, utilize o comando:

```bash
pytest
```
