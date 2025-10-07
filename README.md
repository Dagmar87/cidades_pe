# Cidades PE

Aplicação Django para gerenciamento de municípios de Pernambuco.

## 📋 Descrição

Este projeto tem como objetivo fornecer informações sobre os municípios do estado de Pernambuco, Brasil. A aplicação permite visualizar, adicionar, editar e gerenciar informações dos municípios de forma eficiente.

## 🚀 Funcionalidades

- Listagem de municípios de Pernambuco
- Visualização detalhada de cada município
- Interface administrativa para gerenciamento dos dados
- API REST para integração com outros sistemas

## 🛠️ Pré-requisitos

- Python 3.8+
- Django 4.2+
- Banco de dados (SQLite, PostgreSQL, MySQL, etc.)

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
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
