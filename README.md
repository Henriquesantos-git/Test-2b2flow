# b2bflow - Desafio Estágio Python

Projeto desenvolvido como parte do processo seletivo para Estágio em Desenvolvimento Python na **b2bflow**.

## 📋 Descrição

Script Python que lê contatos cadastrados no **Supabase** e envia mensagens personalizadas via **Z-API** (WhatsApp), com a mensagem:

```
Olá, <nome_contato> tudo bem com você?
```

## 🛠️ Tecnologias

- Python 3
- [Supabase](https://supabase.com/) — banco de dados
- [Z-API](https://z-api.io/) — envio de mensagens WhatsApp

## 🗄️ Setup da Tabela no Supabase

Acesse o **SQL Editor** no painel do Supabase e execute:

```sql
CREATE TABLE contatos (
  id SERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  telefone TEXT NOT NULL
);

INSERT INTO contatos (nome, telefone) VALUES
  ('Henrique', '5511966549908');
```

Depois habilite a leitura pública:

```sql
ALTER TABLE contatos ENABLE ROW LEVEL SECURITY;

CREATE POLICY "permitir leitura publica" ON contatos
FOR SELECT USING (true);
```

> O telefone deve estar no formato internacional: `55` + DDD + número (ex: `5511912345678`)

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
SUPABASE_URL=https://sua-url.supabase.co
SUPABASE_KEY=sua-chave-publica

ZAPI_INSTANCE_ID=seu-instance-id
ZAPI_TOKEN=seu-token
ZAPI_CLIENT_TOKEN=seu-client-token
```

> ⚠️ Nunca suba o `.env` para o GitHub! Ele já está no `.gitignore`.

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/b2bflow-desafio.git
cd b2bflow-desafio

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install supabase python-dotenv requests
```

## ▶️ Como rodar

```bash
python main.py
```

## 📌 Exemplo de saída

```
2026-06-16 21:14:53 [INFO] Iniciando envio de mensagens...
2026-06-16 21:14:55 [INFO] 1 contato(s) encontrado(s) no banco.
2026-06-16 21:14:56 [INFO] Mensagem enviada para Henrique (5511966549908) ✅
2026-06-16 21:14:56 [INFO] Processo finalizado.
```
