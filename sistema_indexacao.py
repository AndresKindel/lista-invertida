from elemento import Elemento
from indice_invertido import IndiceInvertido


class SistemaIndexacao:
    def __init__(self):
        self.indice = IndiceInvertido()

    def carregar_dados(self, elementos):
        for elemento in elementos:
            self.indice.adicionar(elemento)

    def incluir_elemento(self):
        id = input("ID: ")
        nome = input("Nome: ")
        cidade_origem = input("Cidade de Origem: ")
        curso = input("Curso: ")
        time = input("Time: ")
        salario = float(input("Salário: "))
        elemento = Elemento(id, nome, cidade_origem, curso, time, salario)
        self.indice.adicionar(elemento)

    def remover_elemento(self):
        id = input("ID do elemento a ser removido: ")
        self.indice.remover(id)

    def buscar_simples(self):
        campo = input("Campo para busca (nome/cidade_origem/time/salario): ")
        valor = input("Valor para busca: ")
        if campo == 'salario':
            valor = float(valor)
        resultado = self.indice.buscar_simples(campo, valor)
        self.exibir_resultados(resultado)

    def buscar_composta(self):
        campo1 = input("Primeiro campo para busca (nome/cidade_origem/time/salario): ")
        valor1 = input("Primeiro valor para busca: ")
        campo2 = input("Segundo campo para busca (nome/cidade_origem/time/salario): ")
        valor2 = input("Segundo valor para busca: ")
        if campo1 == 'salario':
            valor1 = float(valor1)
        if campo2 == 'salario':
            valor2 = float(valor2)
        resultado = self.indice.buscar_composta(campo1, valor1, campo2, valor2)
        self.exibir_resultados(resultado)

    def exibir_todos(self):
        for id, elemento in self.indice.elementos.items():
            print(
                f"ID: {id}, Nome: {elemento.nome}, Cidade de Origem: {elemento.cidade_origem}, Curso: {elemento.curso}, Time: {elemento.time}, Salário: {elemento.salario}")

    def exibir_resultados(self, ids):
        for id in ids:
            elemento = self.indice.elementos[id]
            print(
                f"ID: {id}, Nome: {elemento.nome}, Cidade de Origem: {elemento.cidade_origem}, Curso: {elemento.curso}, Time: {elemento.time}, Salário: {elemento.salario}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Carregar dados")
            print("2. Incluir novo elemento")
            print("3. Remover elemento existente")
            print("4. Busca simples")
            print("5. Busca composta")
            print("6. Exibir todos os dados")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                elementos = [
                    Elemento("1", "João", "Criciúma", "Engenharia", "Figueirense", 5000),
                    Elemento("2", "Maria", "Florianópolis", "Medicina", "Avaí", 8000),
                    Elemento("3", "Pedro", "Criciúma", "Direito", "Figueirense", 4500)
                ]
                self.carregar_dados(elementos)
            elif opcao == "2":
                self.incluir_elemento()
            elif opcao == "3":
                self.remover_elemento()
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
    sistema = SistemaIndexacao()
    sistema.menu()
