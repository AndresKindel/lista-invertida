### Projeto de Solução: Sistema de Indexação Complementar utilizando Lista Invertida

### Descrição do Problema

O objetivo deste projeto é implementar um esquema de indexação complementar utilizando lista invertida para resolver problemas de busca eficiente em um conjunto de dados com múltiplos critérios. O sistema deve oferecer funcionalidades como carga de dados, busca simples e composta, inclusão e remoção de elementos, e exibição de todos os dados.

#### Feito por:

- Andres Kindel Barbosa - 23100757
- Luiz Adriano Augusto dos Santos - 23102478

### Documentação

### Explicação

Optamos por utilizar uma multilista (índice invertido) para facilitar buscas eficientes por diferentes campos. Dividimos o projeto em três classes: Pessoa para representar os dados, IndiceInvertido para gerenciar os índices, e Sistema para interagir com o usuário. A modularização facilita a manutenção e a escalabilidade, permitindo a substituição ou a melhoria de partes específicas sem afetar o restante do sistema. Essas decisões foram tomadas para garantir um código organizado, de fácil compreensão e com bom desempenho.

#### Estrutura de Dados

Utilizamos uma estrutura de lista invertida para armazenar os elementos e facilitar as buscas por múltiplos critérios. A lista invertida permite consultas eficientes, especialmente em campos discretos e contínuos.

#### Modularização

- *Pessoa*: Representa cada item do conjunto de dados com seus atributos.
- *IndiceInvertido*: Gerencia a estrutura da lista invertida e as operações de busca.
- *Sistema*: Interface do sistema que gerencia a interação do usuário e operações principais.

### Funcionalidades

- *Carga de Dados*: Possibilidade de carregar um conjunto pré-definido de dados.
- *Inclusão de Novo Elemento*: Adiciona um novo elemento à estrutura de dados.
- *Remoção de Elemento Existente*: Remove um elemento existente da estrutura de dados.
- *Busca Simples*: Busca elementos com base em um critério único.
- *Busca Composta*: Busca elementos com base em dois critérios.
- *Exibir Todos os Dados*: Exibe todos os dados armazenados na estrutura.

### Execução

Para executar o programa, basta rodar o arquivo `sistema.py`. A interface de menu permitirá ao usuário realizar todas as operações mencionadas.