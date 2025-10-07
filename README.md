# 🌆 Cidades PE

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicação Django para gerenciamento de municípios de Pernambuco, fornecendo informações detalhadas e uma interface amigável para consulta e administração.

## 📋 Descrição

Este projeto é uma aplicação web desenvolvida em Django que tem como objetivo fornecer informações atualizadas sobre os municípios do estado de Pernambuco, Brasil. A aplicação permite visualizar, adicionar, editar e gerenciar informações dos municípios de forma eficiente, além de oferecer uma API REST para integração com outros sistemas.

## ✨ Funcionalidades

### 🌐 Interface Web
- Listagem completa dos 185 municípios de Pernambuco
- Visualização detalhada de cada município
- Interface responsiva e amigável
- Filtros e busca para fácil localização

### 🛠️ Painel Administrativo
- CRUD completo de municípios
- Gerenciamento de usuários e permissões
- Interface intuitiva baseada no Django Admin

### 🔄 API REST
- Endpoints para consulta de dados
- Suporte a filtros e buscas
- Autenticação via token
- Documentação interativa

## 🚀 Tecnologias Utilizadas

- **Backend:**
  - Python 3.8+
  - Django 5.2.7
  - Django REST Framework 3.16.1
  - SQLite (desenvolvimento) / PostgreSQL (produção)

- **Frontend:**
  - HTML5, CSS3, JavaScript
  - Bootstrap 5
  - jQuery (opcional)

## 🛠️ Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)
- Git (para controle de versão)
- Banco de dados (SQLite incluso, mas recomenda-se PostgreSQL para produção)

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cidades-pe.git
   cd cidades-pe

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   # Linux/MacOS
   python -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   .\venv\Scripts\activate

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Aplique as migrações:
   ```bash
   python manage.py migrate

5. Crie um superusuário para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser

6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver

7. Acesse a aplicação em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Painel administrativo: [http://127.0.0.1:8000/admin/](http://127.0.0.1:800.1/admin/)

## 📚 Estrutura do Projeto

```
cidades_pe/
├── cidades_ibge/          # Configurações do projeto Django
├── municipios/           # Aplicação principal
│   ├── migrations/       # Migrações do banco de dados
│   ├── templates/        # Templates HTML
│   ├── admin.py         # Configurações do painel administrativo
│   ├── models.py        # Modelos de dados
│   ├── urls.py          # URLs da aplicação
│   └── views.py         # Lógica das views
├── .gitignore           # Arquivos ignorados pelo Git
├── manage.py            # Script de gerenciamento do Django
├── README.md            # Este arquivo
└── requirements.txt     # Dependências do projeto
```

## 📝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona alguma feature incrível'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙋‍♂️ Autor

Seu Nome - [@seu-usuario](https://github.com/seu-usuario)

## 📧 Contato

Email: seu.email@exemplo.com

---

<div align="center">
  Feito com ❤️ por você!
</div>
   cd cidades_pe
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: .\venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação em http://127.0.0.1:8000/

## 📊 Estrutura do Projeto

```
cidades_pe/
├── cidades_ibge/         # Configurações do projeto Django
├── municipios/          # Aplicação de municípios
├── manage.py            # Script de gerenciamento do Django
└── requirements.txt     # Dependências do projeto
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
