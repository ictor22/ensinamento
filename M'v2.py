
import os
import time
import json

class Aluno:
    
    def __init__(self, idade=0, altura=0.0, peso=0.0, nome="", rgm=""):
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.nome = nome
        self.rgm = rgm

    def imc(self):
        resultado = self.peso / (self.altura * self.altura)
        if resultado >= 40.0:
            return "Obesidade classe III"
        elif resultado >= 35.0:
            return "Obesidade classe II"
        elif resultado >= 30.0:
            return "Obesidade classe I"
        elif resultado >= 25.0:
            return "Excesso de Peso"
        elif resultado >= 18.5:
            return "Peso Normal"
        if resultado < 18.5:
            return "Abaixo do peso normal"

    def serializar(self):
        dic = {
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "peso": self.peso,
            "rgm": self.rgm
        }
        texto_json = json.dumps(dic, indent=3)
        return texto_json

    def deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.idade = dic["idade"]
        self.altura = dic["altura"]
        self.peso = dic["peso"]
        self.rgm = dic["rgm"]

    
    def cadastrarAluno():
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        nome = input("Digite o nome: ")
        rgm = input("Digite o RGM: ")
        return Aluno(idade, altura, peso, nome, rgm)

    def salvarAlunos(alunos):
        lista = [aluno.serializar() for aluno in alunos]
        with open("alunos.json", 'w') as arquivo:
            json.dump(lista, arquivo)
        print("Alunos Salvos em alunos.json!!")
    
    
    def recuperarAlunos():
        alunos = []
        try:
            with open("alunos.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    aluno = Aluno()
                    aluno.deserializar(text)
                    alunos.append(aluno)
        except FileNotFoundError:
            print("Arquivo 'alunos.json' não encontrado. Criando uma nova lista de alunos.")
        return alunos

class Professor:

    def __init__(self, nome="", rgm=""):
        self.nome = nome
        self.rgm = rgm

    def serializar(self):
        dic = {
            "nome": self.nome,
            "rgm": self.rgm
        }
        texto_json = json.dumps(dic, indent=3)
        return texto_json

    def deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.rgm = dic["rgm"]

    def cadastrarProfessor():
        nome = input("Digite o nome do professor: ")
        rgm = input("Digite o RGM do professor: ")
        return Professor(nome, rgm)

    
    def salvarProfessores(professores):
        lista = [professor.serializar() for professor in professores]
        with open("professores.json", 'w') as arquivo:
            json.dump(lista, arquivo)
        print("Professores Salvos em professores.json!!")
    
    def recuperarProfessores():
        professores = []
        try:
            with open("professores.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    professor = Professor()
                    professor.deserializar(text)
                    professores.append(professor)
        except FileNotFoundError:
            print("Arquivo 'professores.json' não encontrado. Criando uma nova lista de professores.")
        return professores

class Disciplina:

    def __init__(self, nome="", sala=""):
        self.nome = nome
        self.sala = sala

    def serializar(self):
        dic = {
            "nome": self.nome,
            "sala": self.sala
        }
        texto_json = json.dumps(dic, indent=3)
        return texto_json

    def deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.sala = dic["sala"]

    def cadastrarDisciplina():
        nome = input("Digite o nome da disciplina: ")
        sala = input("Digite a sala da disciplina: ")
        return Disciplina(nome, sala)

    def salvarDisciplinas(disciplinas):
        lista = [disciplina.serializar() for disciplina in disciplinas]
        with open("disciplinas.json", 'w') as arquivo:
            json.dump(lista, arquivo)
        print("Disciplinas Salvas em disciplinas.json!!")
    
    
    def recuperarDisciplinas():
        disciplinas = []
        try:
            with open("disciplinas.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    disciplina = Disciplina()
                    disciplina.deserializar(text)
                    disciplinas.append(disciplina)
        except FileNotFoundError:
            print("Arquivo 'disciplinas.json' não encontrado. Criando uma nova lista de disciplinas.")
        return disciplinas

class ModuloAcademico:
    def __init__(self):
        self.opcao = 1
        self.listaAlunos = Aluno.recuperarAlunos()
        self.listaProfessores = Professor.recuperarProfessores()
        self.listaDisciplinas = Disciplina.recuperarDisciplinas()

    def executar(self):
        while self.opcao != 12:
            print("|############################################################|")
            print("|              OOP PYTHON              | ")
            print("|############################################################|")
            print("")
            print("")
            print("1) Cadastrar Alunos")
            print("2) Imprimir Alunos")
            print("3) Consulta Alunos > 65 Kg:")
            print("4) Cadastrar Professor")
            print("5) Listar Professores")
            print("6) Remover Professor")
            print("7) Cadastrar Disciplina")
            print("8) Listar Disciplinas")
            print("9) Salvar alunos, professores e disciplinas")
            print("10) Recuperar disciplinas")
            print("11) Recuperar professor")
            print("12) Sair!!!")

            self.opcao = int(input("Qual é a sua opção? : "))
            
            if self.opcao == 1:
                aluno = self.cadastrarAluno()
                self.listaAlunos.append(aluno)
                print("Aluno cadastrado com sucesso.")
                time.sleep(1)
            
            elif self.opcao == 2:
                self.imprimirAlunos()
                time.sleep(1)
            
            elif self.opcao == 3:
                self.consultaPeso()
                time.sleep(1)
            
            elif self.opcao == 4:
                professor = self.cadastrarProfessor()
                self.listaProfessores.append(professor)
                print("Professor cadastrado com sucesso.")
                time.sleep(1)
            
            elif self.opcao == 5:
                self.listarProfessores()
                time.sleep(1)
            
            elif self.opcao == 6:
                self.removerProfessor()
                time.sleep(1)
            
            elif self.opcao == 7:
                disciplina = self.cadastrarDisciplina()
                self.listaDisciplinas.append(disciplina)
                print("Disciplina cadastrada com sucesso.")
                time.sleep(1)
            
            elif self.opcao == 8:
                self.listarDisciplinas()
                time.sleep(1)
            
            elif self.opcao == 9:
                self.salvarDados()
                time.sleep(1)
                
            elif self.opcao == 10:
                self.recuperarDisciplinas
                time.sleep(1)

            elif self.opcao == 11:
                self.recuperarProfessores
                time.sleep(1)

            elif self.opcao == 12:
                print("Saindo...")
                time.sleep(1)

    def cadastrarAluno(self):
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        nome = input("Digite o nome: ")
        rgm = input("Digite o RGM: ")
        return Aluno(idade, altura, peso, nome, rgm)

    def imprimirAlunos(self):
        print("| Alunos:")
        print("| Nome | Altura | Idade | Peso | RGM |")
        print("-------------------------------")
        for aluno in self.listaAlunos:
            print(aluno.nome, "|", aluno.altura, "|", aluno.idade, "|", aluno.peso, "|", aluno.rgm)
        print("-------------------------------")

    def consultaPeso(self):
        contador = 0
        for aluno in self.listaAlunos:
            if aluno.peso > 65:
                contador += 1
        print("Quantidade de alunos > 65 kg é: ", contador)
        for aluno in self.listaAlunos:
            if aluno.peso > 65:
                print("O aluno", aluno.nome, "tem IMC:", aluno.imc())

    def cadastrarProfessor(self):
        nome = input("Digite o nome do professor: ")
        rgm = input("Digite o RGM do professor: ")
        return Professor(nome, rgm)

    def listarProfessores(self):
        print("| Professores:")
        print("| Nome | RGM |")
        print("-------------------------------")
        for professor in self.listaProfessores:
            print(professor.nome, "|", professor.rgm)
        print("-------------------------------")

    def removerProfessor(self):
        rgm = input("Digite o RGM do professor que deseja remover: ")
        for professor in self.listaProfessores:
            if professor.rgm == rgm:
                self.listaProfessores.remove(professor)
                print("O professor", rgm, "foi excluído com sucesso.")

    def cadastrarDisciplina(self):
        nome = input("Digite o nome da disciplina: ")
        sala = input("Digite a sala da disciplina: ")
        return Disciplina(nome, sala)

    def listarDisciplinas(self):
        print("| Disciplinas:")
        print("| Nome | Sala |")
        print("-------------------------------")
        for disciplina in self.listaDisciplinas:
            print(disciplina.nome, "|", disciplina.sala)
        print("-------------------------------")

    def salvarDados(self):
        Aluno.salvarAlunos(self.listaAlunos)
        Professor.salvarProfessores(self.listaProfessores)
        Disciplina.salvarDisciplinas(self.listaDisciplinas)
        print("Dados Salvos!")

    def recuperarDisciplinas():
        disciplinas = []
        try:
            with open("disciplinas.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    disciplina = Disciplina()
                    disciplina.deserializar(text)
                    disciplinas.append(disciplina)
        except FileNotFoundError:
            print("Arquivo 'disciplinas.json' não encontrado. Criando uma nova lista de disciplinas.")
        return disciplinas

    def recuperarProfessores():
        professores = []
        try:
            with open("professores.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                    professor = Professor()
                    professor.deserializar(text)
                    professores.append(professor)
        except FileNotFoundError:
                print("Arquivo 'professores.json' não encontrado. Criando uma nova lista de professores.")
        return professores
    
modulo_academico = ModuloAcademico()
modulo_academico.executar()
