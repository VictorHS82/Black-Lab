## Black Lab
Repositório criado para prática. A prática consiste em criar um bot para jogar RPG de mesa.

## Instalação
Este projeto utiliza Python e o Discord.py. Para instalar as bibliotecas necessárias, utilize "pip install -r requirements"

## Processamento de strings de dados de rolagem de dados

O bot recebe comandos de rolagem de dados como strings de texto e as processa em três etapas principais:

1. Extração de grupos de cálculo
2. Parse de cada token
3. Execução das rolagens e montagem do resultado

### 1. Extração de grupos de cálculo

O método `Diceman.breaking_it_down(message: str)` recebe a string inteira e separa em partes com base nos sinais `+` e `-`.

- A entrada é normalizada com `strip()` para remover espaços nas extremidades.
- Se a string estiver vazia, retorna uma lista vazia.
- Usa `re.findall(r"[+-]?\s*[^+-]+", message)` para capturar blocos como `2d6`, `+3`, `- 1`, `d8`, `+2d10`.
- Cada pedaço resultante é limpo com `strip()` e retornado como um token individual.

Exemplo:
- Entrada: `"2d6 + 3 - d4"`
- Saída: `['2d6', '+ 3', '- d4']`

### 2. Parse de cada token

O método `Diceman.parse_dice(token: str)` transforma cada token em uma estrutura de dados com informações semânticas.

- Remove espaços e verifica sinal inicial:
  - `-` define `sinal = -1`
  - `+` é ignorado explicitamente, mantendo `sinal = 1`
- Se o token não contiver `d`, assume-se que é um modificador numérico puro:
  - Retorna `{ 'kind': 'modifier', 'sinal': sinal, 'valor': int(token) }`
- Se o token contiver `d`, divide em quantidade e lados:
  - `quantidade` = 1 quando a parte antes do `d` estiver vazia (ex.: `d8` significa `1d8`)
  - `lados` é o valor depois do `d`
  - Retorna `{ 'kind': 'dice', 'sinal': sinal, 'quantidade': quantidade, 'lados': lados }`

Exemplos válidos:
- `"2d6"` → `dice`, quantidade 2, lados 6
- `"-d8"` → `dice`, quantidade 1, lados 8, sinal -1
- `"+3"` → `modifier`, valor 3

### 3. Execução das rolagens e montagem do resultado

O método `Diceman.roll_dice(message: str)` coordena o processamento:

- Chama `breaking_it_down` para obter os grupos.
- Para cada grupo, chama `parse_dice`.
- Ignora grupos inválidos (quando `parse_dice` retorna `None`).
- Para tokens com `kind == 'dice'`:
  - Gera `quantidade` valores aleatórios entre `1` e `lados` usando `random.randint(1, lados)`.
  - Soma os resultados e aplica o `sinal`.
  - Armazena os resultados individuais e o valor total do bloco.
- Para tokens com `kind == 'modifier'`:
  - Calcula `valor * sinal`.

No final, monta uma resposta textual com:
- os resultados de cada grupo;
- os modificadores aplicados com `+` ou `-`;
- o total final.

Exemplo de saída formatada:
- Entrada: `"2d6 + 3 - d4"`
- Saída: `[4, 2] 2d6 + 3 - [1] d4 = 8`

### Considerações técnicas

- O parser aceita expressões compostas por rolagens de dados e modificadores, como `2d6`, `d8`, `+3`, `-1`.
- A análise não valida todos os formatos possíveis; entradas com sintaxe inválida levam o token a retornar `None` e são ignoradas.
- O método `on_message` em `cogs/basemat.py` e o comando `roll` chamam `Diceman.roll_dice()` para obter a resposta pronta.

Essa documentação explica como a string de dados é transformada em grupos, como cada grupo é interpretado e como o resultado final é calculado e formatado para o usuário.
