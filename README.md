# Data Project Starter Kit

Bem-vindo ao repositório do **Data Project Starter Kit**, que tem como objetivo estudos para estruturação de projetos de dados do 0 até o deploy, passando por estruturação dos arquivos, testes unitários, automação de formatação de padrões pep8 até CI/CD.

---

## 🎯 Objetivos do Workshop

- ✅ Compreender a **estrutura padrão de projetos** de dados: organização de diretórios, separação de código-fonte, testes, documentação e muito mais.
- ✅ Aplicar boas práticas de desenvolvimento usando **ETL com classes e módulos**.
- ✅ Implementar **testes automatizados** com Pytest.
- ✅ Trabalhar com **versionamento de código** usando Git e GitHub.
- ✅ Configurar **CI/CD** para manter a qualidade e integridade do projeto.

---

### ✅ Pré-requisitos

- [Git](https://git-scm.com/): Ferramenta de versionamento.
- [Conta no GitHub](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account): Para colaboração e publicação.
- [Pyenv](https://github.com/pyenv/pyenv): Gerenciador de versões Python (usaremos Python 3.11.5).
- [Poetry](https://python-poetry.org/docs/#installation): Para gerenciamento de dependências.

> 💡 **Dica para usuários Windows:**  
> - [Instalação do Pyenv para Windows](https://github.com/pyenv-win/pyenv-win)  
> - Instalação do Poetry através do comando: `pip install poetry`

---

## 🛠️ Instalação e Configuração

### 1. Clone o repositório

- Rode no bash os comandos : 
  - git clone https://github.com/luizfernandoOliveiraa/Starterkit
  - cd dataprojectstarterkit 

### 2. Configure a versão do Python com Pyenv

- Novamente no bash rode os comandos:
  - pyenv install 3.11.5
  - pyenv local 3.11.5
  
### 3. Configure o ambiente virtual com Poetry

- No bash rode:
  - poetry env use 3.11.5
  - poetry shell
  - poetry install
  
### 🧪 Testes

Para rodar os testes automatizados com Pytest:
  - task test

### ⚙️ Executando a Pipeline (ETL)

Para executar o pipeline ETL:
  - task run

Os dados ficaram salvos em data/output/.
