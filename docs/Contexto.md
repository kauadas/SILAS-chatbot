
# Contexto

O módulo de contexto é responsável por conter as ferramentas relacionadas a lidar com informações de
histórico de mensagens, intenções e entidades passadas, hístorico de mensagens e etc.

# como essas informações são usadas?

- Resolução de ambiguidades, uma mesma mensagem pode ter intenções diferentes dependendo do contexto.
- Recuperar dados, certas ações podem precisar ser confirmadas ou pedir alguma informação extra e o contexto
ajuda a identificar esses retornos.

# Sobre a classe Context

A classe Context após gerada armazena:
  - Ultima intenção.
  - Ultimas entidades.
  - Ultima mensagem.
  - Estado atual: pode ser usado para certas funções.
  - Humor: algo interessante para póssiveis micro-conversações.
  - Um array com o histórico total.

A classe conta com um método:

    ```py
    def remember(self, intent, entities, message):
        self.last_intent = intent
        self.last_entities = entities
        self.last_message = message
        self.history.append((intent, entities, message))
    ```