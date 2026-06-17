# 👗 Fashion Inventory System

Bem-vindo ao sistema de gestão de estoque para lojas de vestuário. Este software foi desenvolvido como projeto prático para a disciplina de **Backend**, com o objetivo de centralizar o controle de peças, marcas e tamanhos através de uma interface programável (API).

## 🛠️ Sobre o Projeto
A aplicação utiliza as tecnologias mais modernas do ecossistema Python: **FastAPI** para alta performance, **SQLAlchemy** para manipulação de dados e **PostgreSQL** como banco de dados relacional. A estrutura foi pensada para ser escalável e de fácil manutenção.

### O que o sistema faz:
- **Catálogo Completo:** Visualiza todo o acervo de roupas disponíveis.
- **Busca Direta:** Localiza qualquer peça instantaneamente através do seu código identificador.
- **Entrada de Estoque:** Adiciona novas peças ao inventário com detalhes de marca, tamanho e preço.
- **Gestão de Itens:** Permite editar informações de peças existentes ou removê-las do sistema.
- **Destaque:** Acesso rápido à última peça adicionada ao estoque.
- **Monitoramento:** Endpoint simplificado para validar se o servidor está operante.

## 🌐 Guia de Endpoints

### Status do Servidor
| Método | Rota | Função |
| :--- | :--- | :--- |
| `GET` | `/` | Valida a conexão com a API |

### Controle de Vestuário
| Método | Rota | Ação |
| :--- | :--- | :--- |
| `GET` | `/roupas/` | Retorna a lista total de itens |
| `GET` | `/roupas/{id}` | Exibe os detalhes de uma peça específica |
| `POST` | `/roupas/` | Insere uma nova peça no banco de dados |
| `PATCH` | `/roupas/{id}` | Atualiza dados específicos de um item |
| `DELETE` | `/roupas/{id}` | Exclui permanentemente uma peça |
| `GET` | `/roupas/latest` | Recupera o item mais recente do catálogo |

## ⚙️ Como Colocar para Rodar

### Dependências
- Docker & Docker Compose

### Passo a Passo
1. **Obtendo o código:**
   ```bash
   git clone <url-do-repositorio>
   cd p2-t2-fastapi
   ```

2. **Configurações:**
   Crie seu arquivo de ambiente baseado no exemplo:
   ```bash
   cp .env.EXAMPLE .env
   ```
   Edite o `.env` com as credenciais do seu banco. Lembre-se de usar `db` como host para a conexão interna do Docker.

3. **Inicialização:**
   ```bash
   docker compose up --build
   ```

Acesse a API em `http://127.0.0.1:8000` e explore a documentação automática via Swagger em `http://127.0.0.1:8000/docs`.

---

## 🧪 Testes Automatizados

Para garantir a estabilidade do sistema, utilizamos o `pytest`. Você pode disparar a suíte de testes diretamente pelo Docker:
```bash
docker compose exec backend pytest
```

---

## ✍️ Desenvolvedor
**Raissa Oliveira da Rosa**