# SILAS
## Sistema Idiota de Linguística e Análise Sintática

> Chatbot experimental baseado em NLU, Gramática Livre de Contexto e Cadeias de Markov.

---

# 1. Objetivo

Construir um chatbot funcional e interessante utilizando técnicas clássicas de processamento de linguagem natural, combinando ferramentas modernas com algoritmos próprios quando fizer sentido.

O SILAS não tem como objetivo reproduzir um LLM. A proposta é construir uma arquitetura linguística capaz de:

- compreender entradas do usuário;
- identificar intenções;
- extrair informações relevantes;
- analisar estrutura sintática;
- manter contexto de conversa;
- decidir como responder;
- gerar respostas com variação probabilística;
- produzir conversas coerentes dentro das limitações do modelo.

---

# 2. Arquitetura principal

```text
                    ENTRADA
                       │
                       ▼
              ┌─────────────────┐
              │     spaCy       │
              │ NLP básica      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      NLU        │
              │                 │
              │ intenção        │
              │ entidades       │
              │ confiança       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      CFG        │
              │                 │
              │ estrutura       │
              │ sintática       │
              │ interpretação   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    DIÁLOGO      │
              │                 │
              │ contexto        │
              │ estado          │
              │ decisão         │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     MARKOV      │
              │                 │
              │ geração         │
              │ variação        │
              │ estilo          │
              └────────┬────────┘
                       │
                       ▼
                    RESPOSTA
```

### Responsabilidade de cada camada

**spaCy**

Processamento linguístico básico:

- tokenização;
- lematização;
- POS tagging;
- dependências sintáticas;
- outras informações linguísticas úteis.

**NLU**

Determina o que o usuário está tentando fazer ou perguntar.

**CFG**

Analisa e estrutura a frase de acordo com uma gramática definida pelo projeto.

**Dialogue Manager**

Mantém o estado da conversa e decide qual estratégia utilizar.

**Markov**

Gera ou varia respostas de forma probabilística utilizando corpus e modelos de transição.

---

# 3. Princípios de desenvolvimento

- [ ] Priorizar um sistema funcional em vez de implementar tudo do zero.
- [ ] Usar bibliotecas quando elas resolverem bem um problema.
- [ ] Implementar os componentes que forem importantes para o funcionamento ou para a identidade do SILAS.
- [ ] Manter os componentes desacoplados.
- [ ] Evitar abstrações desnecessárias.
- [ ] Testar cada componente isoladamente antes da integração.
- [ ] Manter um modo de debug para observar o processamento interno.
- [ ] Evoluir a arquitetura conforme o projeto crescer.

> **Não reinventar a roda é permitido. Construir rodas melhores também.**

---

# 4. Fase 1 — Preprocessamento

Objetivo: transformar texto bruto em uma representação linguística útil.

## Tarefas

- [x] Criar representação inicial de mensagem.
- [x] Preservar texto original.
- [x] Implementar normalização básica.
- [x] Implementar tokenização com spaCy.
- [x] Implementar lematização.
- [x] Obter POS tags.
- [x] Obter dependências sintáticas.
- [ ] Definir estrutura final de `Message`.
- [ ] Adicionar tratamento de erros.
- [ ] Adicionar testes básicos.

## Resultado esperado

Uma entrada como:

```text
"O gato estava correndo no telhado!"
```

deve fornecer ao restante do sistema informações como:

```text
texto original
texto normalizado
tokens
lemas
POS
dependências
```

---

# 5. Fase 2 — NLU

Objetivo: transformar informações linguísticas em uma interpretação semântica inicial.

## 5.1 Intenções

- [ ] Criar estrutura para representar uma intenção.
- [ ] Criar catálogo inicial de intenções.
- [ ] Criar exemplos para cada intenção.
- [ ] Implementar classificação inicial.
- [ ] Implementar sistema de pontuação.
- [ ] Implementar confiança.
- [ ] Criar intenção `unknown`.
- [ ] Permitir múltiplas estratégias de classificação.

### Intenções iniciais sugeridas

```text
greeting
farewell
thanks
question
request
confirmation
negation
help
unknown
```

### Futuramente

```text
get_time
get_date
weather
open_application
search
calculate
remember
forget
conversation
```

## 5.2 Entidades

- [ ] Criar estrutura de entidade.
- [ ] Identificar pessoas.
- [ ] Identificar locais.
- [ ] Identificar datas.
- [ ] Identificar horários.
- [ ] Identificar números.
- [ ] Identificar objetos.
- [ ] Identificar ações.
- [ ] Permitir múltiplas entidades.
- [ ] Associar entidades às intenções.

## 5.3 NLU baseada em biblioteca

- [ ] Avaliar recursos do spaCy.
- [ ] Avaliar NLTK quando necessário.
- [ ] Avaliar outros recursos somente quando houver necessidade.
- [ ] Comparar resultados das ferramentas com as regras próprias.

---

# 6. Fase 3 — Gramática Livre de Contexto

Objetivo: dar ao SILAS uma representação estrutural das frases.

## 6.1 Gramática

- [ ] Definir símbolos terminais.
- [ ] Definir símbolos não-terminais.
- [ ] Definir símbolo inicial.
- [ ] Definir produções.
- [ ] Criar primeira gramática em português.
- [ ] Criar regras para frases declarativas.
- [ ] Criar regras para perguntas.
- [ ] Criar regras para comandos.
- [ ] Criar regras para negação.
- [ ] Criar regras para estruturas compostas.

## 6.2 Parser

- [ ] Definir representação das regras.
- [ ] Implementar parser inicial.
- [ ] Produzir árvore sintática.
- [ ] Identificar estruturas inválidas.
- [ ] Tratar ambiguidade.
- [ ] Avaliar parsers/bibliotecas existentes.
- [ ] Comparar parser próprio com ferramentas externas.

## 6.3 Integração com NLU

- [ ] Utilizar intenção para auxiliar a interpretação.
- [ ] Utilizar estrutura sintática para auxiliar a NLU.
- [ ] Extrair relações úteis da árvore.
- [ ] Criar representação semântica intermediária.

---

# 7. Fase 4 — Modelo de diálogo

Objetivo: transformar uma análise isolada em uma conversa.

## Estado

- [ ] Criar estado da conversa.
- [ ] Armazenar histórico.
- [ ] Armazenar intenção atual.
- [ ] Armazenar entidades conhecidas.
- [ ] Armazenar assunto atual.
- [ ] Definir duração do contexto.
- [ ] Implementar limpeza/expiração de contexto.

## Comportamento

- [ ] Responder perguntas simples.
- [ ] Executar diálogos de múltiplas etapas.
- [ ] Fazer perguntas quando faltar informação.
- [ ] Processar confirmações.
- [ ] Processar negações.
- [ ] Permitir correções do usuário.
- [ ] Detectar mudança de assunto.
- [ ] Recuperar contexto anterior quando apropriado.

### Exemplo

```text
Usuário: quero saber a previsão do tempo
SILAS: Para qual cidade?
Usuário: Pelotas
SILAS: ...
```

O sistema deverá preservar:

```text
intent = weather
location = Pelotas
```

---

# 8. Fase 5 — Cadeia de Markov

Objetivo: utilizar modelagem probabilística para gerar respostas variadas e desenvolver um estilo próprio.

## Modelo

- [ ] Definir o que representa um estado.
- [ ] Construir tabela de transições.
- [ ] Contabilizar frequências.
- [ ] Calcular probabilidades.
- [ ] Implementar cadeia de primeira ordem.
- [ ] Implementar cadeia de segunda ordem.
- [ ] Experimentar ordens superiores.
- [ ] Comparar qualidade das gerações.

## Corpus

- [ ] Criar corpus inicial.
- [ ] Criar corpus conversacional.
- [ ] Criar corpus específico para respostas.
- [ ] Permitir carregar corpus externo.
- [ ] Separar corpus por estilo/persona.

## Geração

- [ ] Implementar geração probabilística.
- [ ] Definir tamanho máximo.
- [ ] Definir palavras/frases iniciais.
- [ ] Implementar seed.
- [ ] Tratar estados sem transições.
- [ ] Evitar repetições excessivas.
- [ ] Experimentar diferentes estratégias de seleção.

## Integração com respostas

- [ ] Gerar variações de respostas.
- [ ] Utilizar Markov somente quando apropriado.
- [ ] Permitir respostas determinísticas para situações críticas.
- [ ] Permitir diferentes estilos de geração.
- [ ] Avaliar coerência das respostas.

---

# 9. Fase 6 — Gerador de respostas

Objetivo: decidir **como** o SILAS deve responder.

## Estratégia

- [ ] Criar sistema de estratégias de resposta.
- [ ] Criar respostas determinísticas.
- [ ] Criar respostas parametrizadas.
- [ ] Integrar contexto.
- [ ] Integrar entidades.
- [ ] Integrar Markov.
- [ ] Criar fallback para baixa confiança.
- [ ] Criar respostas para situações desconhecidas.

## Prioridade sugerida

```text
Resposta específica
        ↓
Resposta contextual
        ↓
Resposta baseada em regra
        ↓
Resposta gerada por Markov
        ↓
Fallback
```

---

# 10. Fase 7 — Pipeline completo

Objetivo: integrar todas as partes.

- [ ] Entrada do usuário.
- [ ] Preprocessamento.
- [ ] NLU.
- [ ] CFG.
- [ ] Gerenciamento de contexto.
- [ ] Decisão de resposta.
- [ ] Geração.
- [ ] Saída.

Fluxo final esperado:

```text
"você sabe onde fica a biblioteca?"
                 │
                 ▼
              spaCy
                 │
                 ▼
               NLU
                 │
        question_location
                 │
                 ▼
                CFG
                 │
         estrutura sintática
                 │
                 ▼
          Dialogue Manager
                 │
          decisão de resposta
                 │
                 ▼
              Markov
                 │
                 ▼
              resposta
```

---

# 11. Fase 8 — Personalidade do SILAS

Objetivo: fazer o sistema ter identidade própria em vez de ser apenas um conjunto de classificadores.

- [ ] Definir personalidade.
- [ ] Definir tom de voz.
- [ ] Criar padrões de resposta.
- [ ] Criar corpus compatível com a personalidade.
- [ ] Criar estilos de resposta.
- [ ] Fazer Markov respeitar o estilo escolhido.
- [ ] Criar respostas específicas para situações recorrentes.
- [ ] Criar pequenas peculiaridades do SILAS.

---

# 12. Fase 9 — Debug e observabilidade

Objetivo: conseguir enxergar o que o SILAS está fazendo internamente.

- [ ] Criar modo debug.
- [ ] Mostrar tokens.
- [ ] Mostrar lemas.
- [ ] Mostrar POS.
- [ ] Mostrar dependências.
- [ ] Mostrar intenção.
- [ ] Mostrar confiança.
- [ ] Mostrar entidades.
- [ ] Mostrar árvore CFG.
- [ ] Mostrar estado do diálogo.
- [ ] Mostrar estratégia de resposta.
- [ ] Mostrar informações relevantes do Markov.

Exemplo:

```text
[INPUT]
"me diz que horas são"

[TOKENS]
me | diz | que | horas | são

[INTENT]
time_query

[CONFIDENCE]
0.94

[ENTITIES]
{}

[GRAMMAR]
QUESTION

[CONTEXT]
{}

[RESPONSE]
rules
```

---

# 13. Fase 10 — Testes

## NLU

- [ ] Testar intenções conhecidas.
- [ ] Testar frases equivalentes.
- [ ] Testar erros ortográficos.
- [ ] Testar frases ambíguas.
- [ ] Testar entradas desconhecidas.
- [ ] Testar múltiplas entidades.

## CFG

- [ ] Testar frases válidas.
- [ ] Testar frases inválidas.
- [ ] Testar perguntas.
- [ ] Testar comandos.
- [ ] Testar ambiguidades.

## Markov

- [ ] Testar corpus vazio.
- [ ] Testar corpus pequeno.
- [ ] Testar diferentes ordens.
- [ ] Testar seeds.
- [ ] Testar estados inexistentes.
- [ ] Testar repetições.

## Diálogo

- [ ] Conversa simples.
- [ ] Conversa com contexto.
- [ ] Perguntas de múltiplas etapas.
- [ ] Mudança de assunto.
- [ ] Correções.
- [ ] Confirmações.
- [ ] Negações.

---

# 14. Bibliotecas

Bibliotecas são permitidas e desejáveis quando agregarem valor.

## Já utilizada

- [x] **spaCy** — processamento linguístico.

## Possíveis bibliotecas

- [ ] **NLTK** — avaliar recursos clássicos de NLP e gramáticas.
- [ ] **pytest** — testes automatizados.
- [ ] **Hypothesis** — testes baseados em propriedades.
- [ ] **NumPy** — operações numéricas quando necessário.
- [ ] **Rich** — terminal e debug.
- [ ] [ ] Avaliar bibliotecas específicas de parsing se necessário.

### Regra

Antes de adicionar uma biblioteca:

```text
Qual problema ela resolve?
        ↓
É realmente necessária?
        ↓
Existe alternativa simples?
        ↓
Ela melhora o SILAS?
        ↓
Adicionar
```

Não existe obrigação de implementar tudo manualmente.

---

# 15. Métricas futuras

- [ ] Precisão da NLU.
- [ ] Precisão das entidades.
- [ ] Taxa de parsing correto.
- [ ] Cobertura da CFG.
- [ ] Taxa de fallback.
- [ ] Diversidade das respostas.
- [ ] Repetição de respostas.
- [ ] Tempo de processamento.
- [ ] Tamanho do contexto.

---

# 16. Roadmap geral

```text
PREPROCESSAMENTO
       ↓
      NLU
       ↓
      CFG
       ↓
   DIÁLOGO
       ↓
     MARKOV
       ↓
   RESPOSTAS
       ↓
   INTEGRAÇÃO
       ↓
 PERSONALIDADE
       ↓
 TESTES / MÉTRICAS
       ↓
   REFINAMENTO
```

---

# 17. Estado atual

### Concluído

- [x] Projeto SILAS definido.
- [x] Objetivo arquitetural definido.
- [x] Estrutura inicial de preprocessamento implementada.
- [x] spaCy integrado.
- [x] Tokenização funcionando.
- [x] Lematização funcionando.
- [x] POS tagging funcionando.
- [x] Dependências sintáticas funcionando.

### Próximo passo

**Implementar a primeira NLU funcional.**

Prioridade imediata:

1. Representar uma intenção.
2. Criar algumas intenções básicas.
3. Classificar mensagens.
4. Produzir confiança.
5. Integrar o resultado ao `Message`.

Depois disso, avançar para entidades e começar a construir a CFG.

> **O SILAS não precisa nascer perfeito. Precisa nascer conversando.**
