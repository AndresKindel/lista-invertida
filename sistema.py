from pessoa import Pessoa
from indice_invertido import IndiceInvertido


class Sistema:
    def __init__(self):
        self.indice = IndiceInvertido()

    def carregar_dados(self, pessoas):
        for p in pessoas:
            self.indice.adicionar(p)

    def incluir_pessoa(self):
        id = input("ID: ")
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        curso = input("Curso: ")
        time = input("Time: ")
        salario = float(input("Salário: "))
        p = Pessoa(id, nome, cidade, curso, time, salario)
        self.indice.adicionar(p)

    def remover_pessoa(self):
        id = input("ID da pessoa a ser removida: ")
        self.indice.remover(id)

    def buscar_simples(self):
        campo = input("Campo para busca (nome/cidade/time/salario): ")
        valor = input("Valor para busca: ")
        if campo == 'salario':
            valor = float(valor)
        resultado = self.indice.buscar_simples(campo, valor)
        self.exibir_resultados(resultado)

    def buscar_composta(self):
        campo1 = input("Primeiro campo para busca (nome/cidade/time/salario): ")
        valor1 = input("Primeiro valor para busca: ")
        campo2 = input("Segundo campo para busca (nome/cidade/time/salario): ")
        valor2 = input("Segundo valor para busca: ")
        if campo1 == 'salario':
            valor1 = float(valor1)
        if campo2 == 'salario':
            valor2 = float(valor2)
        resultado = self.indice.buscar_composta(campo1, valor1, campo2, valor2)
        self.exibir_resultados(resultado)

    def exibir_todos(self):
        for id, p in self.indice.pessoas.items():
            print(f"ID: {id}, Nome: {p.nome}, Cidade: {p.cidade}, Curso: {p.curso}, Time: {p.time}, Salário: {p.salario}")

    def exibir_resultados(self, ids):
        for id in ids:
            p = self.indice.pessoas[id]
            print(f"ID: {id}, Nome: {p.nome}, Cidade: {p.cidade}, Curso: {p.curso}, Time: {p.time}, Salário: {p.salario}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Carregar dados")
            print("2. Incluir nova pessoa")
            print("3. Remover pessoa existente")
            print("4. Busca simples")
            print("5. Busca composta")
            print("6. Exibir todos os dados")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                pessoas = [
                    Pessoa("1", "João", "Criciúma", "Engenharia", "Figueirense", 5000),
                    Pessoa("2", "Maria", "Floripa", "Medicina", "Avaí", 8000),
                    Pessoa("3", "Pedro", "Criciúma", "Direito", "Figueirense", 4500)
                ]
                self.carregar_dados(pessoas)
            elif opcao == "2":
                self.incluir_pessoa()
            elif opcao == "3":
                self.remover_pessoa()
            elif opcao == "4":
                self.buscar_simples()
            elif opcao == "5":
                self.buscar_composta()
            elif opcao == "6":
                self.exibir_todos()
            elif opcao == "7":
                break
            else:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()