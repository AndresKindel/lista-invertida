class IndiceInvertido:
    def __init__(self):
        self.nome_indice = {}
        self.cidade_indice = {}
        self.time_indice = {}
        self.salario_indice = {}
        self.pessoas = {}

    def adicionar(self, p):
        self.pessoas[p.id] = p

        if p.nome not in self.nome_indice:
            self.nome_indice[p.nome] = set()
        self.nome_indice[p.nome].add(p.id)

        if p.cidade not in self.cidade_indice:
            self.cidade_indice[p.cidade] = set()
        self.cidade_indice[p.cidade].add(p.id)

        if p.time not in self.time_indice:
            self.time_indice[p.time] = set()
        self.time_indice[p.time].add(p.id)

        if p.salario not in self.salario_indice:
            self.salario_indice[p.salario] = set()
        self.salario_indice[p.salario].add(p.id)

    def remover(self, id):
        if id in self.pessoas:
            p = self.pessoas[id]
            del self.pessoas[id]
            self.nome_indice[p.nome].remove(id)
            self.cidade_indice[p.cidade].remove(id)
            self.time_indice[p.time].remove(id)
            self.salario_indice[p.salario].remove(id)

    def buscar_simples(self, campo, valor):
        if campo == 'nome':
            return self.nome_indice.get(valor, set())
        elif campo == 'cidade':
            return self.cidade_indice.get(valor, set())
        elif campo == 'time':
            return self.time_indice.get(valor, set())
        elif campo == 'salario':
            return self.salario_indice.get(valor, set())

    def buscar_composta(self, campo1, valor1, campo2, valor2):
        resultado1 = self.buscar_simples(campo1, valor1)
        resultado2 = self.buscar_simples(campo2, valor2)
        return resultado1.intersection(resultado2)
    