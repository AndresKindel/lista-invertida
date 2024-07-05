### Projeto de Solução: Sistema de Indexação Complementar utilizando Lista Invertida

### Descrição do Problema

O objetivo deste projeto é implementar um esquema de indexação complementar utilizando lista invertida para resolver problemas de busca eficiente em um conjunto de dados com múltiplos critérios. O sistema deve oferecer funcionalidades como carga de dados, busca simples e composta, inclusão e remoção de elementos, e exibição de todos os dados.

### Documentação

#### Estrutura de Dados

Utilizamos uma estrutura de lista invertida para armazenar os elementos e facilitar as buscas por múltiplos critérios. A lista invertida permite consultas eficientes, especialmente em campos discretos e contínuos.

#### Modularização

- *Elemento*: Representa cada item do conjunto de dados com seus atributos.
- *IndiceInvertido*: Gerencia a estrutura da lista invertida e as operações de busca.
- *SistemaIndexacao*: Interface do sistema que gerencia a interação do usuário e operações principais.

### Funcionalidades

- *Carga de Dados*: Possibilidade de carregar um conjunto pré-definido de dados.
- *Inclusão de Novo Elemento*: Adiciona um novo elemento à estrutura de dados.
- *Remoção de Elemento Existente*: Remove um elemento existente da estrutura de dados.
- *Busca Simples*: Busca elementos com base em um critério único.
- *Busca Composta*: Busca elementos com base em dois critérios.
- *Exibir Todos os Dados*: Exibe todos os dados armazenados na estrutura.

### Execução

Para executar o programa, basta rodar o arquivo `sistema_indexacao.py`. A interface de menu permitirá ao usuário realizar todas as operações mencionadas.