# SILAS Chatbot

## Sistema Idiota de Linguística e Análise Sintática

O SILAS é um chatbot experimental em Python focado em detecção de intenção em linguagem natural. O projeto foi pensado como uma alternativa leve, modular e transparente para aplicações de conversação simples, sem depender de um modelo grande para tarefas bem definidas.

A proposta central é combinar técnicas clássicas de NLP em uma arquitetura simples:

- normalização de texto;
- tokenização e lematização;
- análise sintática básica com spaCy;
- comparação por similaridade léxica e estrutural;
- classificação de intenções em um pipeline organizado.

---

## Visão geral

O SILAS tenta interpretar mensagens do usuário e identificar a intenção por trás delas, como:

- cumprimento;
- despedida;
- agradecimento;
- pergunta sobre hora/data;
- clima;
- lembretes;
- tarefas;
- comandos de sistema;
- conversa casual;
- intenção desconhecida.

O objetivo não é competir com LLMs em conhecimento geral, mas oferecer uma base leve e controlável para projetos próprios, automações simples e protótipos de chatbot.

---

## Arquitetura do projeto

```text
SILAS/
├── README.md
├── intent_test.py
├── test.json
├── data/
│   ├── corpus/
│   └── grammar/
├── src/
│   ├── main.py
│   ├── tests.py
│   └── services/
│       ├── CFG/
│       ├── NLU/
│       │   ├── Context.py
│       │   ├── IntentDetector.py
│       │   ├── natural_processing.py
│       │   ├── Vocabulary.py
│       │   └── models/
│       │       ├── Entitys.py
│       │       └── Intents.py
│       ├── preprocessing/
│       │   └── message.py
│       └── models/
├── .venv/
└── .gitignore
```

---

## Fluxo atual do sistema

```text
Mensagem do usuário
        ↓
Normalização
        ↓
Tokenização
        ↓
Lematização
        ↓
Extração de tags e dependências
        ↓
Comparação com intenções treinadas
        ↓
Ranking de candidatos
        ↓
Resposta / ação
```

A detecção de intenção usa principalmente:

1. similaridade léxica;
2. similaridade estrutural;
3. peso das palavras por frequência no conjunto de intenções.

---

## Componentes principais

### `src/services/preprocessing/message.py`

Responsável por transformar a mensagem em uma representação útil para processamento:

- limpeza e normalização;
- tokenização;
- lematização;
- extração de POS tags;
- extração de dependências sintáticas.

### `src/services/NLU/IntentDetector.py`

Contém a lógica para classificar a mensagem e gerar um ranking de intenções. O detector combina:

- similaridade lexical entre frase do usuário e frases de treino;
- comparação estrutural com dependências sintáticas;
- pontuação final para seleção do melhor candidato.

### `src/services/NLU/models/Intents.py`

Define a estrutura de:

- `Intent`: representação de uma intenção com frases, lemas e dependências;
- `IntentsGroup`: conjunto de intenções, processamento e persistência.

### `src/services/NLU/Context.py`

Módulo de contexto para manter estado e histórico da conversa.

---

## Dataset de intents

O arquivo `test.json` contém exemplos diversos de intenções para treinamento e teste, incluindo:

- `greeting`
- `goodbye`
- `thanks`
- `help`
- `time_query`
- `date_query`
- `weather_query`
- `create_reminder`
- `list_reminders`
- `create_task`
- `list_tasks`
- `search`
- `open_application`
- `close_application`
- `unknown`

Esse conjunto funciona como base para a detecção inicial de intenção.

---

## Requisitos

- Python 3.10+
- spaCy
- modelo do idioma `pt_core_news_sm`

---

## Como executar

### 1) Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Instalar dependências

```bash
pip install spacy
python -m spacy download pt_core_news_sm
```

### 3) Rodar o chatbot

```bash
python src/main.py
```

### 4) Rodar teste de detecção de intenção

```bash
python src/tests.py
```

### 5) Rodar teste experimental

```bash
python intent_test.py
```

---

## Status do projeto

O projeto está em desenvolvimento e já possui uma base funcional de NLU experimental.

### Funcionalidades presentes

- ✅ preprocessamento de mensagens
- ✅ tokenização e lematização
- ✅ extração de tags e dependências sintáticas
- ✅ detecção de intenção por similaridade
- ✅ dataset inicial com intenções
- ✅ execução básica do chatbot em terminal

### Em evolução

- refinamento da detecção de intenção;
- contexto e memória de diálogo;
- extração de entidades mais avançada;
- respostas estruturadas;
- camada de integração com ações reais;
- evolução para análise sintática e CFG.

---

## Filosofia do projeto

O SILAS foi criado para ser um chatbot enxuto, transparente e fácil de adaptar. Em vez de depender de um modelo grande para tarefas simples, ele busca fazer uso de regras, processamento lingüístico e comparação semântica de forma controlada e eficiente.

> Quando a tarefa é específica e bem delimitada, muitas vezes não vale a pena “carregar” um LLM inteiro para resolvê-la.

---

## Roadmap

- [ ] melhorar robustez da NLU para frases mais naturais;
- [ ] ampliar intent detection com mais casos reais;
- [ ] melhorar estado de contexto e diálogo multi-turno;
- [ ] criar regras de resposta por intenção;
- [ ] integrar entidades e parâmetros de consulta;
- [ ] explorar gramáticas CFG e análise sintática mais profunda;
- [ ] testar uso em projetos reais e automações simples.

---

## Licença

A licença do projeto ainda será definida conforme sua evolução e uso.
