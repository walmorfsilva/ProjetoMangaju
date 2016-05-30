def listar_quarto():
    print("**********************************")
    print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
    print("**********************************")
    print("***    QUARTOS CADASTRADOS     ***")
    print("**********************************")
    for i in range(len(quarto)):
        print(i+1,":"+quarto[i])

def quarto_cadastro():
    entrada = "s"
    while entrada == "s":
          print("**********************************")
          print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
          print("**********************************")
          print("***     CADASTRO DE QUARTOS    ***")
          print("**********************************")
          quarto.append(input("NUMERO DE QUARTOS:"))
          quarto.append(input("QUANTAS PESSOAS POR QUARTO:"))
          quarto.append(input("TIPO DE QUARTO:"))
          quarto.append(input("NOME DAS PESSOAS DO QUARTO:"))
          entrada = input("Continuar? [S/N]:")

def listar_equipamento():
    print("**********************************")
    print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
    print("**********************************")
    print("***  EQUIPAMENTOS CADASTRADOS  ***")
    print("**********************************")
    for i in range(len(equipamento)):
        print(i+1,":"+equipamento[i])

def equipamento_cadastro():
    entrada = "s"
    while entrada == "s":
          print("**********************************")
          print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
          print("**********************************")
          print("***  CADASTRO DE EQUIPAMENTOS  ***")
          print("**********************************")
          equipamento.append(input("NOME DO EQUIPAMENTO:"))
          equipamento.append(input("TIPO DO EQUIPAMENTO:"))
          equipamento.append(input("FUNÇÃO DO EQUIPAMENTO:"))
          equipamento.append(input("DATA DA ENTREGA DO EQUIPAMENTO:"))
          equipamento.append(input("PROPRIETÀRIO DO EQUIPAMENTO:"))
          entrada = input("Continuar? [S/N]:")

def cadastrar_equipamento():
    opcao = ""
    while opcao != "5":
         print("**********************************")
         print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
         print("**********************************")
         print("***  CADASTRO DE EQUIPAMENTOS  ***")
         print("**********************************")
         print("[1] EQUIPAMENTOS               ***")
         print("**********************************")
         print("[2] LISTAR EQUIPAMENTOS        ***")
         print("**********************************")
         print("[3] QUARTOS                    ***")
         print("**********************************")
         print("[4] LISTAR QUARTOS             ***")
         print("**********************************")
         print("[5] SAIR                       ***")
         print("**********************************")
         opcao = input("INFORME À OPÇÂO:")

         if opcao == "1":
             equipamento_cadastro()
         
         elif opcao == "2":
             listar_equipamento()
     
         elif opcao == "3":
             quarto_cadastro()

         elif opcao == "4":
             listar_quartos()

         elif opcao == "5":
             print("Obrigado até a próxima!")

         else:
             print("Opçãp Inválida!")

def listar_aluno():
    print("**********************************")
    print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
    print("**********************************")
    print("***   RESIDENTES CADASTRADOS   ***")
    print("**********************************")
    for i in range(len(nome)):
        print(i+1,":"+nome[i])

def cadastrar_aluno():
    entrada = "s"
    while entrada == "s":
          print("**********************************")
          print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
          print("**********************************")
          print("***   CADASTRO DE RESIDENTES   ***")
          print("**********************************")
          nome.append(input("NOME DO ALUNO:"))
          nome.append(input("RG:"))
          nome.append(input("CPF:"))
          nome.append(input("DATA DE NASCIMENTO:"))
          nome.append(input("SEXO:"))
          nome.append(input("CIDADE:"))
          nome.append(input("ESTADO:"))
          nome.append(input("NACIONALIDADE:"))
          nome.append(input("MATRICULA:"))
          nome.append(input("CURSO:"))
          nome.append(input("FONE:"))
          nome.append(input("EMAIL:"))
          entrada = input("Continuar? [S/N]:")

def cadastrar_residente():
    opcao = ""
    while opcao != "3":
         print("**********************************")
         print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
         print("**********************************")
         print("[1] CADASTRAR ALUNOS           ***")
         print("**********************************")
         print("[2] LISTAR ALUNOS              ***")
         print("**********************************")
         print("[3] SAIR                       ***")
         print("**********************************")
         opcao = input("INFORME À OPÇÂO:")

         if opcao == "1":
             cadastrar_aluno()
     
         elif opcao == "2":
             listar_aluno()

         elif opcao == "3":
             print("Obrigado até a próxima!")

         else:
             print("Opçãp Inválida!")


def exibir_menuprincipal():
    opcao = ""
    while opcao != "3":
         print("**********************************")
         print("*** RESIDÊNCIA MANGAJU UFPB RT ***")
         print("**********************************")
         print("****        BEM VINDO          ***")
         print("**********************************")
         print("[1] CADASTRAR RESIDENTES       ***")
         print("**********************************")
         print("[2] CADASTRAR EQUIPAMENTOS     ***")
         print("**********************************")
         print("[3] SAIR                       ***")
         print("**********************************")
         opcao = input("INFORME À OPÇÂO:")


         if opcao == "1":
             cadastrar_residente()
     
         elif opcao == "2":
             cadastrar_equipamento()


         elif opcao == "3":
             print("Obrigado até a próxima!")

         else:
             print("Opçãp Inválida!")


quarto = []
equipamento = []
nome = []
exibir_menuprincipal()
