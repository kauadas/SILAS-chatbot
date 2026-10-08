# NLG — Geração de Linguagem Natural

## 1. Objetivo

O módulo de NLG (Natural Language Generation) é responsável por transformar uma representação estruturada de uma intenção em uma resposta textual.

O NLG não deve interpretar diretamente a mensagem original do usuário. Essa responsabilidade pertence ao NLU.

O fluxo geral é:

```text
Representação semântica
        ↓
     PLANNER
        ↓
Conjunto de orações
        ↓
    REALIZAÇÃO
        ↓
     MARKOV
        ↓
Orações geradas
        ↓
Concatenação
        ↓
Texto final
```

A arquitetura deve ser modular para permitir que o algoritmo de realização seja substituído futuramente sem alterar o Planner.

---

# 2. Entrada

O NLG recebe uma representação estruturada produzida pelas camadas anteriores do SILAS.

A entrada deve conter, no mínimo:

```text
intent
entities / variables
context
```

Exemplo:

```json
{
    "intent": "weather_query",
    "variables": {
        "location": "Pelotas",
        "temperature": 18,
        "humidity": 82,
        "condition": "nublado"
    },
    "context": {}
}
```

### 2.1 Intent

Representa o objetivo comunicativo da resposta.

Exemplos:

```text
greeting
goodbye
weather_query
time_query
date_query
help
thanks
```

### 2.2 Variables

Contêm os dados necessários para construir a resposta.

Exemplo:

```text
location = "Pelotas"
temperature = 18
humidity = 82
condition = "nublado"
```

As variáveis são dados semânticos. O NLG deve decidir como transformá-las em linguagem.

### 2.3 Context

Contém informações relevantes do diálogo atual.

Exemplo:

```json
{
    "previous_intent": "weather_query",
    "previous_topic": "weather",
    "conversation_turn": 4
}
```

O contexto pode ser utilizado pelo Planner e, posteriormente, pelo sistema de realização.

---

# 3. Fluxo de dados

O NLG funciona em etapas.

```text
INPUT
  │
  ▼
[ PLANNER ]
  │
  ▼
[ ORAÇÕES ]
  │
  ▼
[ MARKOV ]
  │
  ▼
[ ORAÇÕES REALIZADAS ]
  │
  ▼
[ CONCATENAÇÃO ]
  │
  ▼
OUTPUT
```

---

# 4. Planner

O Planner é responsável por decidir **o que deve ser dito**.

Ele não deve gerar diretamente o texto final.

Sua função é transformar:

```text
intent + variables + context
```

em uma estrutura contendo as orações necessárias.

### Entrada

```text
Intent:
    weather_query

Variables:
    location = Pelotas
    temperature = 18
    humidity = 82
    condition = nublado
```

### Saída

Por exemplo:

```text
[
    {
        "type": "location_condition",
        "variables": ["location", "condition"]
    },

    {
        "type": "temperature",
        "variables": ["temperature"]
    },

    {
        "type": "humidity",
        "variables": ["humidity"]
    }
]
```

O Planner, portanto, decide:

```text
1. falar sobre o local e condição
2. falar sobre temperatura
3. falar sobre umidade
```

Mas não decide necessariamente as palavras exatas.

---

# 5. Orações

Cada elemento produzido pelo Planner representa uma unidade de informação que deverá ser transformada em uma oração.

Exemplo:

```text
Oração 1:
    location + condition

Oração 2:
    temperature

Oração 3:
    humidity
```

Representação:

```text
[
    ORATION(
        type="location_condition",
        variables=[location, condition]
    ),

    ORATION(
        type="temperature",
        variables=[temperature]
    ),

    ORATION(
        type="humidity",
        variables=[humidity]
    )
]
```

Uma oração representa **uma intenção linguística local**, e não necessariamente uma frase pronta.

---

# 6. Realização das orações

Cada oração é enviada individualmente para o componente responsável pela geração linguística.

```text
Planner
   │
   ├── Oração 1 ──→ Realizador
   ├── Oração 2 ──→ Realizador
   └── Oração 3 ──→ Realizador
```

Na primeira implementação, o realizador será baseado em Markov.

---

# 7. Markov

O Markov é responsável por gerar a sequência linguística de uma oração.

Ele não deve decidir quais informações serão comunicadas.

Essa decisão pertence ao Planner.

### Exemplo

Entrada:

```text
Oração:

type = temperature

variables:
    temperature = 18
```

O Markov recebe as informações necessárias e produz uma sequência textual.

Possíveis resultados:

```text
"a temperatura é de 18 °C"
```

ou:

```text
"está fazendo 18 °C"
```

ou:

```text
"a temperatura está em 18 °C"
```

Dependendo do modelo e das probabilidades aprendidas.

---

# 8. Responsabilidade do Markov

O Markov deve responder à pergunta:

> "Como expressar esta oração?"

Ele não deve responder:

> "O que devo dizer?"

Essa segunda decisão pertence ao Planner.

Portanto:

```text
PLANNER
    ↓
O que dizer?
    ↓
MARKOV
    ↓
Como dizer?
```

Essa separação permite substituir o Markov futuramente por outro método de realização.

Por exemplo:

```text
                 ┌── Markov
                 │
Planner → Oração ├── Gramática
                 │
                 ├── Regras
                 │
                 └── Modelo estatístico
```

---

# 9. Saída do Markov

Cada execução do realizador deve produzir uma oração textual.

Exemplo:

```text
Oração 1:
"Em Pelotas, está nublado."

Oração 2:
"A temperatura é de 18 °C."

Oração 3:
"A umidade está em 82%."
```

Internamente, a saída pode conter metadados:

```json
{
    "text": "A temperatura é de 18 °C.",
    "score": 0.82,
    "tokens": [
        "a",
        "temperatura",
        "é",
        "de",
        "18",
        "°C"
    ]
}
```

O `score` permite posteriormente comparar diferentes realizações.

---

# 10. Concatenação

Depois que todas as orações forem realizadas, elas são combinadas na ordem determinada pelo Planner.

```text
[
    "Em Pelotas, está nublado.",
    "A temperatura é de 18 °C.",
    "A umidade está em 82%."
]
```

↓

```text
"Em Pelotas, está nublado. A temperatura é de 18 °C. A umidade está em 82%."
```

A concatenação não deve alterar o significado das orações.

Sua responsabilidade é apenas produzir a sequência textual final.

---

# 11. Saída final

O NLG deve retornar o texto que será apresentado ao usuário.

Exemplo:

```text
Em Pelotas, está nublado. A temperatura é de 18 °C. A umidade está em 82%.
```

A saída mínima do NLG é:

```python
str
```

Porém, internamente, é recomendado manter uma estrutura mais rica:

```json
{
    "text": "Em Pelotas, está nublado. A temperatura é de 18 °C. A umidade está em 82%.",
    "sentences": [
        "Em Pelotas, está nublado.",
        "A temperatura é de 18 °C.",
        "A umidade está em 82%."
    ]
}
```

---

# 12. Pipeline completa

A pipeline completa do NLG é:

```text
┌──────────────────────────────┐
│       REPRESENTAÇÃO          │
│ intent + variables + context │
└──────────────┬───────────────┘
               │
               ▼
        ┌─────────────┐
        │   PLANNER   │
        └──────┬──────┘
               │
               ▼
      ┌─────────────────┐
      │ CONJUNTO DE     │
      │ ORAÇÕES         │
      └────────┬────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
    Oração 1       Oração 2  ...
        │             │
        ▼             ▼
     MARKOV         MARKOV
        │             │
        ▼             ▼
   Texto 1        Texto 2   ...
        │             │
        └──────┬──────┘
               ▼
       ┌───────────────┐
       │ CONCATENAÇÃO  │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │ TEXTO FINAL   │
       └───────────────┘
```

---

# 13. Exemplo completo

## Entrada

```json
{
    "intent": "weather_query",
    "variables": {
        "location": "Pelotas",
        "temperature": 18,
        "humidity": 82,
        "condition": "nublado"
    },
    "context": {}
}
```

## Planner

Produz:

```text
[
    location_condition,
    temperature,
    humidity
]
```

## Realização

```text
location_condition
    ↓
"Em Pelotas, está nublado."

temperature
    ↓
"A temperatura é de 18 °C."

humidity
    ↓
"A umidade está em 82%."
```

## Concatenação

```text
Em Pelotas, está nublado. A temperatura é de 18 °C. A umidade está em 82%.
```

## Saída

```text
Em Pelotas, está nublado. A temperatura é de 18 °C. A umidade está em 82%.
```

---

# 14. Contrato geral

O contrato externo do NLG pode ser resumido como:

```text
INPUT

{
    intent,
    variables,
    context
}

        ↓

PLANNER

{
    sentences: [...]
}

        ↓

REALIZER

{
    text,
    metadata
}

        ↓

OUTPUT

{
    text,
    sentences
}
```

---

# 15. Princípio arquitetural

O NLG deve manter uma separação clara entre:

```text
SEMÂNTICA
    ↓
"O que dizer?"

PLANEJAMENTO
    ↓
"Quais informações serão transformadas em orações?"

REALIZAÇÃO
    ↓
"Como expressar cada oração?"

LINEARIZAÇÃO
    ↓
"Como juntar as orações?"

TEXTO
    ↓
"O que será enviado ao usuário?"
```

O sistema não deve depender de frases completas armazenadas para cada resposta.

A informação deve ser transformada progressivamente:

```text
dados
  ↓
estrutura semântica
  ↓
plano de mensagem
  ↓
orações
  ↓
realização linguística
  ↓
texto
```

Isso permite que o SILAS gere diferentes respostas a partir da mesma informação sem precisar armazenar cada resposta possível explicitamente.

---

# 16. Princípio de modularidade

O Planner e o Realizador devem ser independentes.

O Planner deve funcionar sem saber como o texto será gerado.

O Realizador deve receber uma oração estruturada e não precisar saber como ela foi escolhida.

Assim:

```text
             ┌──────────────┐
             │   PLANNER    │
             └──────┬───────┘
                    │
              ORAÇÃO ESTRUTURADA
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    MARKOV       GRAMÁTICA      REGRAS
       │            │            │
       └────────────┼────────────┘
                    ▼
               TEXTO
```

A implementação inicial utilizará Markov como realizador, mas a arquitetura não deve depender conceitualmente dele.