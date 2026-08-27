# SILAS Chatbot

## Sistema Idiota de Linguística e Análise Sintática

O **SILAS** é um chatbot experimental desenvolvido como uma alternativa **extremamente leve** aos modelos de linguagem de grande escala (LLMs) para aplicações de conversação em projetos próprios.

A proposta é utilizar técnicas clássicas de processamento de linguagem natural combinadas em uma arquitetura modular, evitando a necessidade de executar grandes modelos neurais para tarefas simples de conversação.

> **Leve, modular, interpretável e feito para ser incorporado em projetos próprios.**

---

## 🧠 Conceito

Em vez de depender de um grande modelo que tenta resolver toda a tarefa de linguagem de uma única vez, o SILAS divide o processamento em componentes especializados.

```text
Entrada
   │
   ▼
Preprocessamento
   │
   ▼
NLU
   │
   ▼
Análise sintática / CFG
   │
   ▼
Gerenciamento de diálogo
   │
   ▼
Geração Markov
   │
   ▼
Resposta
```

Cada componente possui uma responsabilidade específica, permitindo que o sistema seja adaptado de acordo com as necessidades do projeto onde for utilizado.

---

## 🔬 Tecnologias e conceitos

O SILAS utiliza ou pretende utilizar:

- **NLU (Natural Language Understanding)** para interpretação das entradas;
- **spaCy** para processamento linguístico;
- **Gramáticas Livres de Contexto (CFG)** para estruturação e análise sintática;
- **Cadeias de Markov** para modelagem probabilística e geração de texto;
- **Gerenciamento de contexto** para conversas de múltiplas etapas;
- **Regras e respostas determinísticas** para situações que exigem precisão.

Bibliotecas externas podem ser utilizadas quando agregarem valor ao projeto. O objetivo não é reinventar todas as ferramentas existentes, mas construir uma arquitetura simples e eficiente utilizando as melhores ferramentas disponíveis para cada problema.

---

## ⚡ Por que o SILAS?

LLMs são extremamente poderosos, mas nem todo chatbot precisa de bilhões de parâmetros para responder a comandos, interpretar intenções ou conduzir diálogos simples.

O SILAS busca atender justamente esse espaço.

### Vantagens pretendidas

- 🪶 **Baixo consumo de recursos**
- 🚀 **Execução local**
- 🔧 **Fácil integração em projetos próprios**
- 🧩 **Arquitetura modular**
- 🔍 **Comportamento interpretável**
- 📦 **Poucas dependências**
- ⚙️ **Controle sobre o funcionamento interno**
- 📴 **Possibilidade de funcionamento totalmente offline**

O SILAS não pretende competir diretamente com LLMs em conhecimento geral ou geração aberta de texto. A proposta é oferecer uma alternativa quando **simplicidade, controle, desempenho e baixo consumo de recursos** forem mais importantes.

---

## 🏗️ Arquitetura

### Preprocessamento

Responsável por transformar o texto bruto em informações linguísticas utilizáveis.

Exemplos:

- tokenização;
- normalização;
- lematização;
- POS tagging;
- dependências sintáticas.

### NLU

Responsável por determinar o que o usuário está tentando fazer.

Exemplo:

```text
"que horas são?"

intent: time_query
confidence: 0.94
```

Também deverá realizar a extração de entidades relevantes.

### CFG

A Gramática Livre de Contexto será utilizada para representar e analisar estruturas sintáticas.

Exemplo conceitual:

```text
S  → NP VP
NP → DET N
VP → V NP
```

### Dialogue Manager

Responsável por manter o estado da conversa e decidir como o sistema deve reagir ao contexto atual.

### Markov

As cadeias de Markov serão utilizadas para gerar variações probabilísticas de respostas e permitir que o SILAS desenvolva diferentes estilos de geração a partir de corpora.

Respostas que exigem precisão poderão continuar utilizando regras determinísticas.

---

## 🎯 Objetivos do projeto

- [ ] Construir uma NLU funcional.
- [ ] Implementar identificação de intenções.
- [ ] Implementar extração de entidades.
- [ ] Construir uma gramática para português.
- [ ] Implementar análise sintática baseada em CFG.
- [ ] Implementar cadeia de Markov para geração.
- [ ] Criar gerenciamento de contexto.
- [ ] Integrar todas as camadas em um pipeline único.
- [ ] Desenvolver uma personalidade própria para o SILAS.
- [ ] Criar testes e métricas de desempenho.
- [ ] Otimizar consumo de memória e processamento.
- [ ] Facilitar a integração do SILAS em outros projetos.

---

## 📁 Organização

A arquitetura do projeto será definida de forma incremental conforme os componentes forem desenvolvidos.

A prioridade é manter separadas as responsabilidades de:

```text
preprocessamento
NLU
CFG / parser
diálogo
Markov
geração
interface
```

A estrutura definitiva não é considerada fechada e poderá evoluir durante o desenvolvimento.

---

## 🧪 Status

**Em desenvolvimento.**

O preprocessamento linguístico inicial já está funcionando com spaCy, incluindo:

- tokenização;
- lematização;
- POS tagging;
- análise de dependências sintáticas.

As próximas etapas concentram-se na construção da NLU e na integração progressiva das demais camadas.

---

## 🚧 Filosofia

O SILAS foi concebido para ser uma ferramenta prática para **projetos próprios**, e não apenas uma demonstração acadêmica.

A arquitetura deverá permitir que um desenvolvedor escolha quais capacidades deseja utilizar e adapte o chatbot ao domínio específico da aplicação.

A ideia é simples:

> **Se uma tarefa simples pode ser resolvida com algumas regras, probabilidades e análise linguística, não há necessidade de colocar uma LLM inteira para fazê-la.**

---

## 📜 Licença

A licença do projeto será definida posteriormente.
