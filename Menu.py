
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
