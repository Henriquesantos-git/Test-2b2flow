# b2bflow - Desafio Estágio Python

Projeto desenvolvido como parte do processo seletivo para Estágio em Desenvolvimento Python na **b2bflow**.

## Descrição

Script Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API (WhatsApp), com a mensagem:

```
Olá, <nome_contato> tudo bem com você?
```

## Tecnologias

- Python 3
- Supabase — banco de dados PostgreSQL gerenciado
- Z-API — integração com WhatsApp
- python-dotenv — gerenciamento de variáveis de ambiente
- requests — requisições HTTP

## Estrutura do Projeto

```
b2bflow-desafio/
├── main.py
├── .env.example
├── .gitignore
└── README.md
```

## Setup da Tabela no Supabase

Acesse o SQL Editor no painel do Supabase e execute:

```sql
CREATE TABLE contatos (
  id SERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  telefone TEXT NOT NULL
);

INSERT INTO contatos (nome, telefone) VALUES
  ('Henrique', '5511966549908');
```

Em seguida, habilite a leitura pública via RLS:

```sql
ALTER TABLE contatos ENABLE ROW LEVEL SECURITY;

CREATE POLICY "permitir leitura publica" ON contatos
FOR SELECT USING (true);
```

O telefone deve estar no formato internacional sem caracteres especiais: `55` + DDD + numero (exemplo: `5511912345678`).

## Variaveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
SUPABASE_URL=https://sua-url.supabase.co
SUPABASE_KEY=sua-chave-publica

ZAPI_INSTANCE_ID=seu-instance-id
ZAPI_TOKEN=seu-token
ZAPI_CLIENT_TOKEN=seu-client-token
```

O arquivo `.env` esta listado no `.gitignore` e nao deve ser versionado.

## Instalacao

```bash
# Clone o repositorio
git clone https://github.com/Henriquesantos-git/Test-2b2flow.git
cd Test-2b2flow

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependencias
pip install supabase python-dotenv requests
```

## Como Rodar

```bash
python main.py
```

## Exemplo de Saida

```
2026-06-16 21:14:53 [INFO] Iniciando envio de mensagens...
2026-06-16 21:14:55 [INFO] 1 contato(s) encontrado(s) no banco.
2026-06-16 21:14:56 [INFO] Mensagem enviada para Henrique (5511966549908)
2026-06-16 21:14:56 [INFO] Processo finalizado.
```
