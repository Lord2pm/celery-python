# Estudo Celery + Redis + Flask + Flower

Este repositório contém um pequeno estudo sobre **tarefas assíncronas** em Python, utilizando:

- [Celery](https://docs.celeryq.dev/en/stable/) → para processamento assíncrono/distribuído  
- [Redis](https://redis.io/) → como broker  
- [SQLite](https://www.sqlite.org/) → como backend de resultados  
- [Flask](https://flask.palletsprojects.com/) → aplicação web simples para disparar tasks  
- [Flower](https://flower.readthedocs.io/) → painel web para monitorar workers e filas  

---

## Estrutura do Projeto

```
.
├── tasks.py        # Definição das tasks do Celery
├── app.py          # Aplicação Flask que dispara tasks
├── celery.sqlite   # Backend de resultados (gerado em runtime)
└── README.md
```

---

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/celery-redis-flask-study.git
cd celery-redis-flask-study
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

No `requirements.txt` deve conter pelo menos:
```
flask
celery
redis
flower
```

---

## Executando o projeto

### 1. Inicie o Redis
Certifique-se que o **Redis** está rodando localmente (porta padrão: `6379`).

```bash
redis-server
```

### 2. Inicie o worker do Celery
Em outro terminal:

```bash
celery -A tasks worker --loglevel=info
```

### 3. Rode a aplicação Flask
```bash
python app.py
```

Aceda em: [http://localhost:5000](http://localhost:5000)  

Quando chamar `/`, o Flask dispara uma task assíncrona para o worker Celery.

### 4. (Opcional) Monitore com Flower
```bash
celery -A tasks flower
```

Painel disponível em: [http://localhost:5555](http://localhost:5555)

---

## Exemplo de Uso

Request para `/`:

```bash
curl http://localhost:5000/
```

Resposta imediata:

```json
{
  "msg": "Olá, mundo"
}
```

Enquanto isso, o **Celery Worker** processa a task em background:

```
[2025-08-29 10:00:00,000: INFO] Task tasks.hello[1234abcd] succeeded in 0.1s: 'Hello, Luís'
```

---

## Objetivo

Este repositório é apenas um **estudo prático** para compreender:

- Como configurar Celery com Redis como broker  
- Como integrar Celery em um projeto Flask  
- Como visualizar e monitorar tasks em tempo real usando Flower  

---

Feito com ☕ e estudo por **[Luís Muhele](https://github.com/lord2pm)**.
