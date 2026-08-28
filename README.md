# SILAS Chatbot

## Sistema Idiota de Linguística e Análise Sintática

O SILAS é um chatbot experimental em Python para detecção de intenção em linguagem natural. O projeto foi pensado como alternativa leve e modular para conversas simples, em vez de depender de um modelo grande para tarefas básicas.

Ele combina:

- normalização e tokenização de mensagens;
- lematização e análise sintática com spaCy;
- comparação de frases por similaridade léxica e estrutural;
- arquitetura em camadas para facilitar expansão.

---

## Objetivo

O sistema busca interpretar a intenção do usuário e classificar mensagens em categorias como cumprimentos, perguntas, tarefas, lembretes e comandos. A proposta principal é manter o código simples, transparente e fácil de adaptar em projetos próprios.

---

## Estrutura do projeto

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
│       └── preprocessing/
│           └── message.py
└── .venv/
```

---

## Como o sistema trabalha

A pipeline atual do projeto é:

```text
Mensagem do usuário
   ↓
Normalização
   ↓
Tokenização + lematização
   ↓
Análise de partes do discurso e dependências
   ↓
Comparação com intenções treinadas
   ↓
Ranking dos candidatos
   ↓
Resposta ou ação
```

A detecção de intenção usa similaridade léxica e estrutural. Em outras palavras, o sistema tenta identificar a intenção comparando o texto do usuário com frases de exemplo já conhecidas no dataset.

---

## Intenções de exemplo

O arquivo `test.json` contém vários exemplos de intenções, incluindo:

- cumprimento (`greeting`)
- despedida (`goodbye`)
- agradecimento (`thanks`)
- ajuda (`help`)
- hora/data (`time_query`, `date_query`)
- clima (`weather_query`)
- tarefas e lembretes
- pesquisa, aplicativos e controle de sistema
- conversa casual e piadas
- intent desconhecida (`unknown`)

---

## Componentes principais

### `src/services/preprocessing/message.py`

Responsável por:

- limpar a mensagem;
- normalizar para minúsculas;
- tokenizar;
- extrair lemas;
- obter tags e dependências sintáticas.

### `src/services/NLU/IntentDetector.py`

Implementa a lógica de classificação. Ele calcula pontuações de:

- similaridade lexical;
- similaridade estrutural;
- ranking dos candidatos.

### `src/services/NLU/models/Intents.py`

Define as classes que representam uma intenção e um grupo de intenções, além de processamento e persistência do conjunto de intenções.

### `src/services/NLU/Context.py`

Mantém o contexto do diálogo e o histórico de estado da conversa.

---

## Requisitos

- Python 3.10+
- spaCy
- modelo `pt_core_news_sm`

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

### 4) Testar a detecção de intenção

```bash
python src/tests.py
```

---

## Status atual

O projeto está em desenvolvimento, mas já possui uma base funcional de NLU experimental.

### Funcionalidades presentes

- ✅ preprocessamento de mensagem
- ✅ tokenização e lematização
- ✅ análise de tags e dependências
- ✅ detecção de intenção por similaridade
- ✅ dataset inicial com intenções
- ✅ execução básica do chatbot em terminal

### O que ainda está sendo construido

- refinamento da detecção de intenção
- gerenciamento de diálogo mais robusto
- entidades e contexto mais avançados
- integração com respostas estruturadas
- evolução da camada CFG e análise sintática

---

## Filosofia do projeto

O SILAS foi pensado como uma opção leve e transparente para projetos próprios. Em vez de depender de um modelo gigante para algo que pode ser resolvido com regras, similaridade e análise linguística simples, o projeto busca manter o sistema compreensível e adaptável.

> Quando a tarefa é bem definida e limitada, nem sempre é necessário carregar um LLM completo para resolvê-la.

---

## Licença

A licença do projeto ainda será definida conforme sua evolução e uso.
