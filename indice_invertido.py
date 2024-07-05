from collections import defaultdict


class IndiceInvertido:
    def __init__(self):
        self.indice_nome = defaultdict(set)
        self.indice_cidade = defaultdict(set)
        self.indice_time = defaultdict(set)
        self.indice_salario = defaultdict(set)
        self.elementos = {}

    def adicionar(self, elemento):
        self.elementos[elemento.id] = elemento
        self.indice_nome[elemento.nome].add(elemento.id)
        self.indice_cidade[elemento.cidade_origem].add(elemento.id)
        self.indice_time[elemento.time].add(elemento.id)
        self.indice_salario[elemento.salario].add(elemento.id)

    def remover(self, id):
        if id in self.elementos:
            elemento = self.elementos[id]
            del self.elementos[id]
            self.indice_nome[elemento.nome].remove(id)
            self.indice_cidade[elemento.cidade_origem].remove(id)
            self.indice_time[elemento.time].remove(id)
            self.indice_salario[elemento.salario].remove(id)

    def buscar_simples(self, campo, valor):
        if campo == 'nome':
            return self.indice_nome.get(valor, set())
        elif campo == 'cidade_origem':
            return self.indice_cidade.get(valor, set())
        elif campo == 'time':
            return self.indice_time.get(valor, set())
        elif campo == 'salario':
            return self.indice_salario.get(valor, set())

    def buscar_composta(self, campo1, valor1, campo2, valor2):
        resultado1 = self.buscar_simples(campo1, valor1)
        resultado2 = self.buscar_simples(campo2, valor2)
        return resultado1.intersection(resultado2)
