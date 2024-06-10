class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}")


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    return Aluno(nome, idade, nota)


def main():
    lista_alunos = []

    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Exibir todos os alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            aluno = cadastrar_aluno()
            lista_alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")
        elif opcao == "2":
            if not lista_alunos:
                print("Nenhum aluno cadastrado.")
            else:
                print("\n=== Alunos Cadastrados ===")
                for aluno in lista_alunos:
                    aluno.exibir_informacoes()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
